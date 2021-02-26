from enum import Enum


class DataType(Enum):
    Analog = 'ANLG'
    Thermocouple = 'TEMP'
    AMultiplexer = 'AMUX'
    Unused = 'N/A'

class AnalogSources(Enum):
    pass

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