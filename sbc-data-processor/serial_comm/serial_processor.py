import sys
import serial
import datetime
import itertools
import utilities.definitions as defs
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
            # Obtain the current timestamp
            current_datetime = datetime.datetime.now()

            # Read serial data in
            b = self.ser_client.readline()  # read a byte string
            string_n = b.decode('utf-8')  # decode byte string into Unicode
            serial_string = string_n.rstrip()  # remove \n and \r

            # Parse received data if data is valid
            if SerialProcessor._perform_serial_data_validation(serial_string):
                SerialProcessor._parse_serial_data(serial_string)



            # # Parse received serial data and publish to broker
            # data = serial_string.split()
            # serial_idx = 1

            # if data[0] == DataType.Analog.value:
            #     while serial_idx <= len(data) / 2:
            #         topic_name = DataSourceMapping.analog_dict[serial_idx]
            #         topic_name = DataSourceMapping.analog_dict[serial_idx]
            #         msg_data = str(data[2 * serial_idx - 1])
            #         self._record_and_publish_message_data(topic_name, msg_data, current_datetime)
            #         serial_idx += 1

            # elif data[0] == DataType.Thermocouple.value:
            #     while serial_idx < len(data) / 2:
            #         topic_name = DataSourceMapping.thermocouple_dict[serial_idx]
            #         # topic_name = "Thermocouple_" + str(serial_idx - 1)
            #         topic_name = DataSourceMapping.thermocouple_dict[serial_idx]
            #         msg_data = str(data[2 * serial_idx - 1])
            #         self._record_and_publish_message_data(topic_name, msg_data, current_datetime)
            #         serial_idx += 1

            # # Publish other data to broker
            # topic_name = 'T_sat_low'
            # msg_data = 20.0
            # self._record_and_publish_message_data(topic_name, msg_data, current_datetime)

        except KeyboardInterrupt:
            # Allows termination of the program at the terminal by entering "CTRL+C"
            sys.exit("KeyboardInterrupt")


    @staticmethod
    def _perform_serial_data_validation(serial_string):
        is_data_type_present = False
        is_data_id_present = False
        is_data_value_present = True    # TBD: Need to design an appropriate verification for this
        is_data_units_present = False    
        is_single_delimiter_present = False

        # Check if data type is present
        for data_type in defs.DataType:
            if data_type.value in serial_string:
                is_data_type_present = True

        # Check if data ID is present
        for data_id in itertools.chain(
            defs.DataSourceMapping.Analog_Map, 
            defs.DataSourceMapping.Thermocouple_Map,
            defs.DataSourceMapping.AMultiplexer_Map):
            if str(data_id) in serial_string:
                is_data_id_present = True

        # Check if data units is present
        if (config.DATA_UNIT_DELIMITER in serial_string 
            and config.DATA_END_DELIMITER in serial_string):
            is_data_units_present = True

        # Checkif multiple delimiters are present
        if (serial_string.count(config.DATA_VALUE_DELIMITER) == 1
            or serial_string.count(config.DATA_UNIT_DELIMITER) == 1
            or serial_string.count(config.DATA_END_DELIMITER) == 1):
            is_single_delimiter_present = True


        return (is_data_type_present 
                and is_data_id_present 
                and is_data_value_present 
                and is_data_units_present)

    @staticmethod
    def _parse_serial_data(serial_string):
        try:
            # Determine message type 
            data_type_id = serial_string[:int(config.DATA_TYPE_CHAR_LEN)]
            data_type_index = int(serial_string[int(config.DATA_TYPE_CHAR_LEN)])
            data_source_name = []

            # Extract data value
            data_value_start_index = serial_string.index(config.DATA_VALUE_DELIMITER)
            data_value_end_index = serial_string.index(config.DATA_UNIT_DELIMITER)
            data_value = serial_string[data_value_start_index+2:data_value_end_index-1]
            
            # Extract data units
            data_unit_end_index = serial_string.index(config.DATA_END_DELIMITER)
            data_units = serial_string[data_value_end_index+1:data_unit_end_index]

            # Determine data source
            if data_type_id == defs.DataType.Analog.value:
                data_source_name = defs.DataSourceMapping.Analog_Map[data_type_index] 
                
            elif data_type_id == defs.DataType.Thermocouple.value:
                data_source_name = defs.DataSourceMapping.Thermocouple_Map[data_type_index]
                
            elif data_type_id == defs.DataType.AMultiplexer.value:
                data_source_name = defs.DataSourceMapping.AMultiplexer_Map[data_type_index]
                
        except:
            # Malformed serial data received
            pass

    def construct_formatted_message(self):
        pass