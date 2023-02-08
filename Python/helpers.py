from arduino_dictionary import arduino_dictionary
from toggle_switch_dictionary import toggle_switch_dictionary


from globals import DEBUG
from globals import SUPPORTED_AIRCRAFT

def get_aircraft_type(aircraft_requests):
    # ATC_MODEL returns a string similar to
    # TT:ATCCOM.AC_MODEL_TBM9.0.text
    # Remove spaces from text replacing with underscore
    # Remove beginning and trailing excess text to return
    # Type of aircraft
    request_aircraft_type = aircraft_requests.get('ATC_MODEL')
    if DEBUG:
        print("DEBUG request_aircraft_type ", request_aircraft_type)
    aircraft_type = request_aircraft_type.decode('utf8').replace(" ", "_")

    # standard aircraft start with TT:ATCCOM.AC_
    # search standard first then trim text
    # otherwise custom aircraft, ex. b'Optica', doesn't need formatting
    if "TT:ATCCOM.AC_" in aircraft_type:
        aircraft_type = aircraft_type[13:] # removes TT:ATCCOM.AC_ from text
        aircraft_type = aircraft_type[:len(aircraft_type)-7] # removes .0.text

    if aircraft_type in SUPPORTED_AIRCRAFT:
        return aircraft_type

    return "DEFAULT"

def print_arduino_lookup(key):
    # arduino_dictionary in button_bytes.py
    print(key)
    print(arduino_dictionary[key])


# return dial/button that was pressed
def get_dial_input(key):
    return arduino_dictionary[key]

# return NONE if no key set
def convert_arduino_input(key):
    return arduino_dictionary[key]

def verify_toggle_switch_dictionary(key, aircraft_type):
    if toggle_switch_dictionary[aircraft_type][key] == 'NONE':
        return False
    return True
