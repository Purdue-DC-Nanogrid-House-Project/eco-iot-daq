import datetime
from _csv import writer
import serial
import paho.mqtt.client as mqtt
from utilities.definitions import *
from config.appconfig import config


class MQTTProcessor:
    def __init__(self):
        self.mqtt_client = []
        self.ser_client = []
        self.is_mqtt_connected = False
        self.is_serial_connected = False

    def initialize_serial_connection(self):
        self.ser_client = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE)
        self.is_serial_connected = not self.ser_client.closed
        print()

    def initialize_mqtt_connection(self):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client.connect(config.MQTT_SERVER_IP, int(config.MQTT_PORT), int(config.KEEPALIVE_PERIOD))

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.is_connected = True

    @staticmethod
    def _on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        msg_data = str(msg.payload).replace("b'", "").replace("'", "")

        current_date = str(datetime.datetime.date(datetime.datetime.now()))
        file_path = config.DATA_FILE_DIRECTORY + current_date + '_' + config.DATA_FILENAME + '.csv'
        with open(file_path, 'a+', newline='') as \
                write_obj:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")

            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([
                current_time,
                msg.topic,
                msg_data])

    def process_serial_data_forever(self):
        while True:
            # Loop through the MQTT client
            self.mqtt_client.loop()

            # Read serial data in
            b = self.ser_client.readline()  # read a byte string
            string_n = b.decode()  # decode byte string into Unicode
            serial_string = string_n.rstrip()  # remove \n and \r

            # Parse received serial data
            data = serial_string.split()
            print(data)

            if data[0] == DataType.Analog.value:

                a_idx = 1
                while a_idx <= len(data) / 2:
                    topic_name = "AnalogIn_" + str(a_idx - 1)
                    # Subscribe to the topic in advance to save message data
                    self.mqtt_client.subscribe(topic_name)
                    # Publish to MQTT Broker
                    self.mqtt_client.publish(topic_name, str(data[2 * a_idx - 1]))
                    print(topic_name, str(data[2 * a_idx - 1]))
                    a_idx = a_idx + 1

            elif data[0] == DataType.Thermocouple.value:
                tc_idx = 1
                while tc_idx < len(data) / 2:
                    topic_name = "Thermocouple_" + str(tc_idx - 1)
                    # Subscribe to the topic in advance to save message data
                    self.mqtt_client.subscribe(topic_name)
                    # Publish to MQTT Broker
                    self.mqtt_client.publish(topic_name, str(data[2 * tc_idx - 1]))
                    print(topic_name, str(data[2 * tc_idx - 1]))
                    tc_idx = tc_idx + 1

            self.mqtt_client.publish('T_sat_low', 20.0)
