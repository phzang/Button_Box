from button_bytes import keypress_dictionary
from switch_dictionary import switch_dictionary

DEBUG = False

def get_aircraft_type(aircraft_requests):
    # ATC_MODEL returns a string similar to
    # TT:ATCCOM.AC_MODEL_TBM9.0.text
    # Remove spaces from text replacing with underscore
    # Remove beginning and trailing excess text to return
    # Type of aircraft
    request_aircraft_type = aircraft_requests.get('ATC_MODEL')
    if DEBUG: print(request_aircraft_type)
    aircraft_type = request_aircraft_type.decode('utf8').replace(" ", "_")
    aircraft_type = aircraft_type[13:] # removes TT:ATCCOM.AC_ from text
    aircraft_type = aircraft_type[:len(aircraft_type)-7] # removes .0.text
    return aircraft_type

def print_keyboard_lookup(key):
    # keyboardpress_dictionary in button_bytes.py
    print(key)
    print(keypress_dictionary[key])


# return dial/button that was pressed
def get_dial_input(key):
    return keypress_dictionary[key]

# return NONE if no key set
def convert_keyboard_input(key):
    return keypress_dictionary[key]

def check_switch_dictionary(key):
    if switch_dictionary[key] == 'NONE':
        return False
    return True
