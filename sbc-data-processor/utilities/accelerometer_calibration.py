def calibrate_g_x_signal(analog_input):
    return ((float(analog_input) - 2.5118) / 0.3302 + 0.1)

def calibrate_g_y_signal(analog_input):
    return ((float(analog_input) - 2.5217) / 0.3446 + 0.1)

def calibrate_g_z_signal(analog_input):
    return ((float(analog_input) - 2.5014) / 0.3250 + 0.1)    
