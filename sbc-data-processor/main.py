import mqtt.processor as processor


def main():
    p = processor.MQTTProcessor()
    p.initialize_serial_connection()
    p.initialize_mqtt_connection()
    p.process_serial_data_forever()


if __name__ == '__main__':
    main()
