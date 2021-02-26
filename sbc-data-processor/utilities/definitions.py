from enum import Enum


class DataType(Enum):
    Analog = 'ANLG'
    Thermocouple = 'TEMP'
    AMultiplexer = 'AMUX'


class DataSourceMapping:
    # Dictionaries starting from 20201103
    analog_dict = {
        1: 'OnOff',
        2: 'LiquidYesNo',
        3: 'P_r_s',
        4: 'P_r_exp_v_in',
        5: 'N/A'
    }

    thermocouple_dict = {
        1: 'T_r_s',
        2: 'T_r_exp_v_in',
        3: 'N/A3',
        4: 'N/A4',
        5: 'N/A5',
        6: 'N/A6',
        7: 'N/A7',
    }