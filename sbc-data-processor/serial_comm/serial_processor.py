import sys
import serial
import datetime
import itertools
import serial_comm.message_payload as mp
import utilities.definitions as defs
import utilities.pressure_calibration as cal_p
import utilities.accelerometer_calibration as cal_a
import utilities.liquid_level_calibration as cal_l
from config.appconfig import config


class SerialProcessor:
    def __init__(self):
        self.ser_client = []
        self.is_serial_connected = False

    def initialize_serial_connection(self):
        self.ser_client = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE)
        self.is_serial_connected = not self.ser_client.closed
        self.ser_client.timeout = float(config.SERIAL_TIMEOUT)

    def process_serial_data(self):
        try:
            proc_message = []

            # Obtain the current timestamp
            current_datetime = datetime.datetime.now()
            current_date = current_datetime.strftime("%Y-%m-%d")
            current_timestamp = current_datetime.strftime("%H:%M:%S.%f")

            # Read serial data in
            b = self.ser_client.readline()  # read a byte string
            string_n = b.decode('utf-8')  # decode byte string into Unicode
            serial_string = string_n.rstrip()  # remove \n and \r

            # Parse received data if data is valid
            if SerialProcessor._perform_serial_data_validation(serial_string):
                proc_message = SerialProcessor._parse_serial_data_into_message(serial_string, current_date, current_timestamp)

            return proc_message

        except KeyboardInterrupt:
            # Allows termination of the program at the terminal by entering "CTRL+C"
            sys.exit("KeyboardInterrupt")

        except UnicodeDecodeError:
            # Invalid serial data was received
            print('UNICODE DECODE ERROR')
            print(b)

    @staticmethod
    def _perform_serial_data_validation(serial_string):
        is_data_type_present = False
        is_data_id_present = False
        is_message_format_valid = False    

        # Check if data type is present
        for data_type in defs.DataType:
            if data_type.value in serial_string:
                is_data_type_present = True

        # Check if data ID is present
        for data_id in itertools.chain(
            defs.DataSourceMapping.Analog_Map, 
            defs.DataSourceMapping.Digital_Map,
            defs.DataSourceMapping.Thermocouple_Map,
            defs.DataSourceMapping.AMultiplexer_Map):
            if str(data_id) in serial_string:
                is_data_id_present = True

        # Check if correct number of delimiters are present
        number_of_delimiters = len([i for i, letter in enumerate(serial_string) if letter == config.DATA_VALUE_DELIMITER])
        if (int(config.NUMBER_OF_DATA_FIELDS) == (number_of_delimiters + 1)):
            is_message_format_valid = True

        return (is_data_type_present 
                and is_data_id_present 
                and is_message_format_valid)

    @staticmethod
    def _parse_serial_data_into_message(serial_string, current_date, current_timestamp):
        # Determine delimiter locations
        delimiter_indices = [i for i, letter in enumerate(serial_string) if letter == config.DATA_VALUE_DELIMITER]

        # Extract data information
        try:
            data_type_id  = serial_string[:delimiter_indices[0]]
            data_type_index = int(serial_string[delimiter_indices[0]+1:delimiter_indices[1]])
            data_value = float(serial_string[delimiter_indices[1]+1:delimiter_indices[2]])
            data_units = serial_string[delimiter_indices[2]+1:]
            data_source_name = []   
        except ValueError:
            print('VALUE ERROR')
            print(serial_string)

        try:       
            # Determine data source name from mapping
            if data_type_id == defs.DataType.Analog.value:
                data_source_name = defs.DataSourceMapping.Analog_Map[data_type_index] 

            elif data_type_id == defs.DataType.Digital.value:
                data_source_name = defs.DataSourceMapping.Digital_Map[data_type_index] 
                
            elif data_type_id == defs.DataType.Thermocouple.value:
                data_source_name = defs.DataSourceMapping.Thermocouple_Map[data_type_index]
                
            elif data_type_id == defs.DataType.AMultiplexer.value:
                data_source_name = defs.DataSourceMapping.AMultiplexer_Map[data_type_index]

            # If data source is unconfigured, return empty payload
            if data_source_name == defs.DataType.Unused.value:
                return None
        except:
            # Malformed serial data received
            pass

        # Calibration of pressure signals
        if data_source_name == defs.PressureSources.P_r_s.value:
            data_value = cal_p.calibrate_prs_signal(data_value)
        elif data_source_name == defs.PressureSources.P_r_exp_v_in.value:
            data_value = cal_p.calibrate_prexpvin_signal(data_value)
        elif data_source_name == defs.PressureSources.P_r_exp_v_out.value:
            data_value = cal_p.calibrate_prexpvout_signal(data_value)

        # Calibration of accelerometer signals
        elif data_source_name == defs.AnalogSources.g_x.value:
            data_value = cal_a.calibrate_g_x_signal(data_value)
        elif data_source_name == defs.AnalogSources.g_y.value:
            data_value = cal_a.calibrate_g_y_signal(data_value)
        elif data_source_name == defs.AnalogSources.g_z.value:
            data_value = cal_a.calibrate_g_z_signal(data_value)

        # Calibration of liquid level signals
        elif data_source_name == defs.AnalogSources.liquid_level.value:
            data_value = cal_l.calibrate_liquidlevel_signal(data_value)
        
        # Build message payload
        proc_message = (mp.MessagePayload()
            .set_topic_name(data_source_name)
            .set_message_data_value(data_value)
            .set_message_data_units(data_units)
            .set_message_date(current_date)
            .set_message_timestamp(current_timestamp))
        return proc_message

    def construct_formatted_message(self):
        pass