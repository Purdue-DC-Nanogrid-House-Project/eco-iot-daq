import serial
import datetime
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
        # Obtain the current timestamp
        current_datetime = datetime.datetime.now()

        # Read serial data in
        b = self.ser_client.readline()  # read a byte string
        string_n = b.decode('utf-8')  # decode byte string into Unicode
        serial_string = string_n.rstrip()  # remove \n and \r
        print(serial_string)

        # Parse received data




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



    @staticmethod
    def _parse_serial_data(serial_string):
        # Determine message type
        data_type_id = serial_string[:4]
        print(data_type_id)
        if data_type_id == defs.DataType.Analog.name:
            pass
        elif data_type_id == defs.DataType.Thermocouple.name:
            pass
        elif data_type_id == defs.DataType.AMultiplexer.name:
            pass