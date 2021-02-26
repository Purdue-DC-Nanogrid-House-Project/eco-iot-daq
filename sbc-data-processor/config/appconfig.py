from configparser import ConfigParser
import os


class Config:
    def __init__(self, config_file_name):
        parser = ConfigParser()
        parser.optionxform = str
        found = parser.read(os.path.join(os.path.dirname(__file__), config_file_name))
        if not found:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))


# Specify your config file name and extension here
config = Config('appconfig.ini')