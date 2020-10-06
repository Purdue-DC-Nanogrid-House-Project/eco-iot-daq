# Read data over serial from connected SoC
import serial
import paho.mqtt.client as mqtt
from utilities.definitions import *
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

        # Parse received serial data
        data = serial_string.split()
        print(data)

        if data[0] == DataType.Analog.value:
            # Publish to MQTT Broker
            # for a_idx in range(len(data)-1):
            #     topic_name = "AnalogIn_" + str(a_idx)
            #     mqtt_client.publish(topic_name, str(data[a_idx+
            a_idx = 1
            while a_idx <= len(data)/2:
                topic_name = "AnalogIn_" + str(a_idx-1)
                mqtt_client.publish(topic_name, str(data[2*a_idx-1]))
                print(topic_name, str(data[2*a_idx-1]))
                a_idx = a_idx + 1

        elif data[0] == DataType.Thermocouple.value:
            # Publish to MQTT Broker
            # for tc_idx in range(len(data)-1):
            tc_idx = 1
            while tc_idx < len(data)/2:
                topic_name = "Thermocouple_" + str(tc_idx-1)
                mqtt_client.publish(topic_name, str(data[2*tc_idx-1]))
                print(topic_name, str(data[2*tc_idx-1]))
                tc_idx = tc_idx + 1

        mqtt_client.publish('T_sat_low', 20.0)

def on_connect():
    print()


def on_message():
    print()


if __name__ == '__main__':
    main()
