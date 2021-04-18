def calibrate_prs_signal(analog_input):
    return (float(analog_input) * 437.48 - 181.59)
    
def calibrate_prexpvin_signal(analog_input):
    return (float(analog_input) * 349.42 + 57.499)

def calibrate_prexpvout_signal(analog_input):
    return (float(analog_input) * 435.19 - 176.47)