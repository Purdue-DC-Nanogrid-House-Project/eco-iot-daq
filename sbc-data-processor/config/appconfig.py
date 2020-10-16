from configparser import ConfigParser

section_names = 'CONNECTION_PARMS', 'DATA_PARAMS',


class Config(object):
    def __init__(self, *file_names):
        parser = ConfigParser()
        parser.optionxform = str
        print(file_names)
        found = parser.read(file_names)
        if not found:
            raise ValueError('No config file found!')
        for name in section_names:
            self.__dict__.update(parser.items(name))


config = Config(r'/home/eco_iot_daq/Projects/sbc-data-processor/config/appconfig.ini')
