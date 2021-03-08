from enum import Enum


class DataType(Enum):
    Analog = 'ANLG'
    Digital = 'DIGL'
    Thermocouple = 'TEMP'
    AMultiplexer = 'AMUX'
    Unused = 'N/A'

class AnalogSources(Enum):
    pass

class DigitalSources(Enum):
    LiquidYesNo = 'LiquidYesNo'
    OnOff = 'OnOff'

class ThermocoupleSources(Enum):
    T_r_s = 'T_r_s'
    T_r_exp_v_in = 'T_r_exp_v_in'

class PressureSources(Enum):
    P_r_s = 'P_r_s'
    P_r_exp_v_in = 'P_r_exp_v_in'


# Data source mapping starting from 2021/02/26
class DataSourceMapping:
    Analog_Map = {
        1: DataType.Unused.value,
        2: DataType.Unused.value,
        3: DataType.Unused.value,
        4: DataType.Unused.value,
        5: DataType.Unused.value,
        6: DataType.Unused.value,
        7: DataType.Unused.value,
        8: DataType.Unused.value,
        9: DataType.Unused.value,
        10: DataType.Unused.value,
        11: DataType.Unused.value,
        12: DataType.Unused.value,
        13: DataType.Unused.value,
        14: DataType.Unused.value,
        15: DataType.Unused.value,
    }

    Digital_Map = {
        22: DataType.Unused.value,
        23: DataType.Unused.value,
        24: DataType.Unused.value,
        25: DataType.Unused.value,
        26: DataType.Unused.value,
        27: DataType.Unused.value,
        28: DataType.Unused.value,
        29: DataType.Unused.value,
        30: DigitalSources.LiquidYesNo.value,
        31: DigitalSources.OnOff.value,
        32: DataType.Unused.value,
        33: DataType.Unused.value,
        34: DataType.Unused.value,
        35: DataType.Unused.value,
        36: DataType.Unused.value,
        37: DataType.Unused.value,
        38: DataType.Unused.value,
        39: DataType.Unused.value,
        40: DataType.Unused.value,
        41: DataType.Unused.value,
        42: DataType.Unused.value,
        43: DataType.Unused.value,
        44: DataType.Unused.value,
        45: DataType.Unused.value,
        46: DataType.Unused.value,
        47: DataType.Unused.value,
        48: DataType.Unused.value,
        49: DataType.Unused.value,
        50: DataType.Unused.value,
        51: DataType.Unused.value,
        52: DataType.Unused.value,
        53: DataType.Unused.value,
    }

    Thermocouple_Map = {
        1: ThermocoupleSources.T_r_s.value,
        2: ThermocoupleSources.T_r_exp_v_in.value,
        3: DataType.Unused.value,
        4: DataType.Unused.value,
        5: DataType.Unused.value,
        6: DataType.Unused.value,
        7: DataType.Unused.value,
        8: DataType.Unused.value,
    }

    AMultiplexer_Map = {
        0: DataType.Unused.value,
        1: DataType.Unused.value,
        2: PressureSources.P_r_s.value,
        3: PressureSources.P_r_exp_v_in.value,
        4: DataType.Unused.value,
        5: DataType.Unused.value,
        6: DataType.Unused.value,
        7: DataType.Unused.value,
        8: DataType.Unused.value,
        9: DataType.Unused.value,
        10: DataType.Unused.value,
        11: DataType.Unused.value,
        12: DataType.Unused.value,
        13: DataType.Unused.value,
        14: DataType.Unused.value,
        15: DataType.Unused.value,
    }