# Read data over serial from connected SoC
import serial
import paho.mqtt.client as mqtt
from config.appconfig import config


def main():
    usb_port = "/dev/ttyACM0"
    ser = serial.Serial(usb_port, 9600)
    temp_data = []

    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(config.MQTT_SERVER_IP, int(config.MQTT_PORT), int(config.KEEPALIVE_PERIOD))

    while(1):
        # Read serial data in
        b = ser.readline()                  # read a byte string
        string_n = b.decode()               # decode byte string into Unicode
        serial_string = string_n.rstrip()   # remove \n and \r

        # Parse temperature fields
        temp_data = serial_string.split()
        print(temp_data)

        # Publish to MQTT Broker
        for tc_idx in range(8):
            topic_name = "Thermocouple_" + str(tc_idx)
            mqtt_client.publish(topic_name, str(temp_data[tc_idx]))


def on_connect():
    print()


def on_message():
    print()


if __name__ == '__main__':
    main()
