def calibrate_prs_signal(analog_input):
    return (float(analog_input) * 27.402 - 43.672 + 14.7) * 6.89476
    
def calibrate_prexpvin_signal(analog_input):
    return (float(analog_input) * 48.285 - 6.665 + 14.7) * 6.89476