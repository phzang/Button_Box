# Keyboard Press lookups
# Hex : Button Press

# ------ Lookup Table Buttons -------
switch_dictionary = {
    'MODEL_C152': {
        "0": 'TOGGLE_MASTER_ALTERNATOR',
        "1": 'TOGGLE_MASTER_BATTERY',
        "2": 'NONE',
        "3": 'PITOT_HEAT_TOGGLE',
        "4": 'TOGGLE_NAV_LIGHTS',
        "5": 'STROBES_TOGGLE',
        "6": 'TOGGLE_BEACON_LIGHTS',
        "7": 'TOGGLE_TAXI_LIGHTS',
        "8": 'LANDING_LIGHTS_TOGGLE',
        "9": 'NONE', # Need Glare Shield lookup
        "10": 'NONE',
        "11": 'NONE',  # Second Avionics Button
    },
    'MODEL_C172': {
        "0": 'TOGGLE_MASTER_ALTERNATOR',
        "1": 'TOGGLE_MASTER_BATTERY',
        "2": 'FUEL_PUMP',
        "3": 'TOGGLE_BEACON_LIGHTS',
        "4": 'LANDING_LIGHTS_TOGGLE',
        "5": 'TOGGLE_TAXI_LIGHTS',
        "6": 'TOGGLE_NAV_LIGHTS',
        "7": 'STROBES_TOGGLE',
        "8": 'PITOT_HEAT_TOGGLE',
        "9": 'NONE', # Need Glare Shield lookup
        "10": 'TOGGLE_AVIONICS_MASTER',
        "11": 'NONE',  # Second Avionics Button
    },
    'MODEL_DA40': {
        "0": 'ENGINE_MASTER', # Uses keyboard hotkey because simconnect doesn't have an ENGINE_MASTER command
        "1": 'TOGGLE_MASTER_BATTERY',
        "2": 'PITOT_HEAT_TOGGLE',
        "3": 'LANDING_LIGHTS_TOGGLE',
        "4": 'TOGGLE_TAXI_LIGHTS',
        "5": 'TOGGLE_NAV_LIGHTS',
        "6": 'STROBES_TOGGLE',
        "7": 'NONE',
        "8": 'TOGGLE_AVIONICS_MASTER',
        "9": 'FUEL_SELECTED_TRANSFER_MODE:3', # Need Fuel Transfer lookup
        "10": 'NONE',
        "11": 'NONE',  # Second Avionics Button
    },
    'RANDOM': {
        "0": 'TOGGLE_MASTER_ALTERNATOR',
        "1": 'TOGGLE_MASTER_BATTERY',
        "2": 'FUEL_PUMP',
        "3": 'TOGGLE_BEACON_LIGHTS',
        "4": 'LANDING_LIGHTS_TOGGLE',
        "5": 'TOGGLE_TAXI_LIGHTS',
        "6": 'TOGGLE_NAV_LIGHTS',
        "7": 'STROBES_TOGGLE',
        "8": 'PITOT_HEAT_TOGGLE',
        "9": 'NONE', # Need Glare Shield lookup
        "10": 'TOGGLE_AVIONICS_MASTER',
        "11": 'NONE',  # Second Avionics Button
    }
}
