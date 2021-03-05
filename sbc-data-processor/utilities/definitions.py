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
    OnOff = 'OnOff'

class ThermocoupleSources(Enum):
    T_r_s = 'T_r_s'
    T_r_exp_v_in = 'T_r_exp_v_in'

class PressureSources(Enum):
    OnOff = 'OnOff'
    LiquidYesNo = 'LiquidYesNo'
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
        22: DataType.Digital.value,
        23: DataType.Digital.value,
        24: DataType.Digital.value,
        25: DataType.Digital.value,
        26: DataType.Digital.value,
        27: DataType.Digital.value,
        28: DataType.Digital.value,
        29: DataType.Digital.value,
        30: DataType.Digital.value,
        31: DataType.Digital.value,
        32: DataType.Digital.value,
        33: DataType.Digital.value,
        34: DataType.Digital.value,
        35: DataType.Digital.value,
        36: DataType.Digital.value,
        37: DataType.Digital.value,
        38: DataType.Digital.value,
        39: DataType.Digital.value,
        40: DataType.Digital.value,
        41: DataType.Digital.value,
        42: DataType.Digital.value,
        43: DataType.Digital.value,
        44: DataType.Digital.value,
        45: DataType.Digital.value,
        46: DataType.Digital.value,
        47: DataType.Digital.value,
        48: DataType.Digital.value,
        49: DataType.Digital.value,
        50: DataType.Digital.value,
        51: DataType.Digital.value,
        52: DataType.Digital.value,
        53: DataType.Digital.value,
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
        0: PressureSources.OnOff.value,
        1: PressureSources.LiquidYesNo.value,
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