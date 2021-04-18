def calibrate_liquidlevel_signal(analog_input):
    return (float(analog_input) * -89.568 + 399.61)
    