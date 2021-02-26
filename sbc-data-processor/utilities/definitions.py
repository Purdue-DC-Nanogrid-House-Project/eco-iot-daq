from enum import Enum


class DataType(Enum):
    Analog = 'ANLG'
    Thermocouple = 'TEMP'
    AMultiplexer = 'AMUX'
    Unused = 'N/A'


class DataSourceMapping:
    # Data source mapping starting from 20201103
    Analog_Map = {
        1: 'OnOff',
        2: 'LiquidYesNo',
        3: 'P_r_s',
        4: 'P_r_exp_v_in',
        5: 'N/A',
    }

    Thermocouple_Map = {
        1: 'T_r_s',
        2: 'T_r_exp_v_in',
        3: 'N/A',
        4: 'N/A',
        5: 'N/A',
        6: 'N/A',
        7: 'N/A',
    }

    AMultiplexer_Map = {
        0: 'Mux',
    }