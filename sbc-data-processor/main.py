import utilities.io as io
import mqtt_comm.mqtt_processor as mprocessor
import serial_comm.serial_processor as sprocessor

def main():
    # Instantiate class objects
    sp = sprocessor.SerialProcessor()   
    mp = mprocessor.MQTTProcessor()

    # Initialize connections
    sp.initialize_serial_connection()
    mp.initialize_mqtt_connection()

    # Begin data processing loop
    while True:
        proc_message = sp.process_serial_data()

        # If a valid message was received, save locally and transmit the data over MQTT 
        if proc_message:
            io.IO_Operations.save_processed_data(proc_message)
            mp.process_mqtt_data(proc_message)


if __name__ == '__main__':
    main()
