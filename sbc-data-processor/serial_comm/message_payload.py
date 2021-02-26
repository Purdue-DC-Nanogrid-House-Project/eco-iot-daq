class MessagePayload:
    def __init__(self):
        self.topic_name = []
        self.message_data_value = []
        self.message_data_units = []
        self.message_date = []
        self.message_timestamp = []

    def set_topic_name(self, topic_name):
        self.topic_name = topic_name
        return self

    def set_message_data_value(self, message_data_value):
        self.message_data_value = message_data_value
        return self

    def set_message_data_units(self, message_data_units):
        self.message_data_units = message_data_units
        return self

    def set_message_date(self, message_date):
        self.message_date = message_date
        return self

    def set_message_timestamp(self, message_timestamp):
        self.message_timestamp = message_timestamp
        return self