import sys
import datetime
from _csv import writer
import paho.mqtt.client as mqtt
from config.appconfig import config


class MQTTProcessor:
    def __init__(self):
        self.mqtt_client = []
        self.is_mqtt_connected = False

    def initialize_mqtt_connection(self):
        self.mqtt_client = mqtt.Client(clean_session=True)
        self.mqtt_client.on_connect = self._on_connect
        self.mqtt_client.on_message = self._on_message
        self.mqtt_client.on_log = self._on_log
        self.mqtt_client.connect(config.MQTT_SERVER_IP, int(config.MQTT_PORT), int(config.KEEPALIVE_PERIOD))
        self.mqtt_client.subscribe(config.MQTT_USER_INPUT_TOPIC_NAME)

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.is_connected = True

    @staticmethod
    def _on_message(client, userdata, message):
        # Obtain the current timestamp
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S.%f")

    @staticmethod
    def _on_log(client, userdata, level, buf):
        # Turn this on to enable debug logging
        # print("log: ", buf)
        pass

    def process_mqtt_data(self, proc_message):
        try:
            # Loop through the MQTT client
            self.mqtt_client.loop(timeout=float(config.SERIAL_TIMEOUT))

            # Transmit processed message data to local broker
            self.mqtt_client.user_data_set(proc_message)
            self.mqtt_client.publish(proc_message.topic_name, proc_message.message_data_value)

        except KeyboardInterrupt:
            # Allows termination of the program at the terminal by entering "CTRL+C"
            sys.exit("KeyboardInterrupt")

        except ValueError:
            print()