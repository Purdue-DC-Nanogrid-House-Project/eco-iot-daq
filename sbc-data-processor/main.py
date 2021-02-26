import serial_comm.serial_processor as sprocessor
import mqtt_comm.mqtt_processor as mprocessor


def main():
    # Instantiate class objects
    sp = sprocessor.SerialProcessor()
    mp = mprocessor.MQTTProcessor()

    # Initialize connections
    sp.initialize_serial_connection()
    mp.initialize_mqtt_connection()

    # Begin data processing loop
    while True:
        sp.process_serial_data()
        mp.process_mqtt_data()


if __name__ == '__main__':
    main()
