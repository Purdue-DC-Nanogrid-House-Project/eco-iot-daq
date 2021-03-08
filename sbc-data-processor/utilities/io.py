from _csv import writer
from config.appconfig import config


class IO_Operations():
    @staticmethod
    def save_processed_data(message):
        file_path = config.DATA_FILE_DIRECTORY + message.message_date + '_' + config.DATA_FILENAME + '.csv'
        with open(file_path, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)

            # Add contents of list as last row in the csv file
            csv_writer.writerow([
                message.message_timestamp,
                message.topic_name,
                message.message_data_value,
                message.message_data_units])