import sys
import datetime
from _csv import writer
import paho.mqtt.client as mqtt
import mqtt_comm.mqtt_message as mqm
from utilities.definitions import *
from config.appconfig import config


class MQTTProcessor:
    def __init__(self):
        self.mqtt_client = []
        self.is_mqtt_connected = False

    def initialize_mqtt_connection(self):
        self.mqtt_client = mqtt.Client(clean_session=True)
        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_publish = self._on_publish
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client.on_log = self._on_log
        self.mqtt_client.connect(config.MQTT_SERVER_IP, int(config.MQTT_PORT), int(config.KEEPALIVE_PERIOD))
        self.mqtt_client.subscribe(config.MQTT_USER_INPUT_TOPIC_NAME)

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.is_connected = True

    @staticmethod
    def _on_publish(client, userdata, mid):
        MQTTProcessor._save_csv_data(userdata)

    @staticmethod
    def _on_message(client, userdata, message):
        # Obtain the current timestamp
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S.%f")

        # Extract the received message data and save to the csv file
        try:
            msg = (mqm.Message()
                   .set_topic_name(message.topic)
                   .set_message_data(message.payload.decode("utf-8"))
                   .set_message_date(current_date)
                   .set_message_timestamp(current_time))
            MQTTProcessor._save_csv_data(msg)
        except UnicodeDecodeError:
            # Malformed data received
            pass

    @staticmethod
    def _on_log(client, userdata, level, buf):
        # Turn this on to enable debug logging
        # print("log: ", buf)
        pass

    def process_mqtt_data(self):
        try:
            # Loop through the MQTT client
            self.mqtt_client.loop(timeout=float(config.SERIAL_TIMEOUT))

        except KeyboardInterrupt:
            # Allows termination of the program at the terminal by entering "CTRL+C"
            sys.exit("KeyboardInterrupt")

    @staticmethod
    def _save_csv_data(message):
        file_path = config.DATA_FILE_DIRECTORY + message.message_date + '_' + config.DATA_FILENAME + '.csv'
        with open(file_path, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)

            # Add contents of list as last row in the csv file
            csv_writer.writerow([
                message.message_timestamp,
                message.topic_name,
                message.message_data])

    def _record_and_publish_message_data(self, topic_name, message_data, current_datetime):
        # Obtain current timestamps
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S.%f")

        # form the message and publish to the broker
        message = (mqm.Message()
                   .set_topic_name(topic_name)
                   .set_message_data(message_data)
                   .set_message_date(current_date)
                   .set_message_timestamp(current_time))
        self.mqtt_client.user_data_set(message)
        self.mqtt_client.publish(topic_name, message_data)
