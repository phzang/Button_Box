# Convert Byte data from Arduino Mega to Keypresses

import sys
import traceback
import os
import time
import serial
from button_bytes import keypress_dictionary
from SimConnect import *
from transponder import *
from com import *
from nav import *


DEBUG = False

# Open Arduino Serial Port
serial_port =  serial.Serial('COM3', 9600, timeout=0)

#SimConnect link
sim_connect = SimConnect()
aircraft_requests = AircraftRequests(sim_connect, _time=200)
aircraft_events = AircraftEvents(sim_connect)
# event_function = 0
# convert_key = 'NONE' # byte identifier to SimConnect identifier holder

aircraft_name = 0 # holder for name of aircraft

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


def read_ardiuno():
    convert_key = 'NONE'
    event_function = 0
    while True:
        try:
            ser = serial_port.read()
            if ser:
                #altitude = aircraft_requests.get("PLANE_ALTITUDE")
                #print(altitude)

                if DEBUG:
                    print_keyboard_lookup(ser.hex())
                if DEBUG:
                    print(is_transponder(ser.hex()))

                convert_key = convert_keyboard_input(ser.hex())

                # if transponder dials pressed
                if ser.hex() == "38" or ser.hex() == "39" or ser.hex() == "40":
                    convert_key = return_transponder_key_lookup(ser.hex())
                # if communication dials pressed
                elif (int(ser.hex()) >= 18 and int(ser.hex()) <= 24):
                    convert_key = return_com_key_lookup(ser.hex())
                # if navigation dials pressed
                elif (int(ser.hex()) >= 42 and int(ser.hex()) <= 48):
                    convert_key = return_nav_key_lookup(ser.hex())

                # sets trim for different aircraft types
                elif int(ser.hex()) == 28:
                    event_function = aircraft_events.find('AXIS_ELEV_TRIM_SET')
                    if DEBUG: print(aircraft_name)
                    if aircraft_name == "MODEL_C152": event_function(0)
                    elif aircraft_name == "MODEL_DA40": event_function(1300)
                    else: event_function(0)

                if convert_key != 'NONE':
                    try:
                        if DEBUG:
                            print("FINAL CONVERT KEY ",convert_key)
                        event_function = aircraft_events.find(convert_key)
                        event_function()
                    except TypeError:
                        pass

                time.sleep(0.01)
                ser = 0 # Reset serial data
        except serial.SerialTimeoutException:
            print('Data could not be read')
            time.sleep(0.01)


def main():
    global aircraft_name # sets global name of aircraft
    print("Working...")
    aircraft_name = get_aircraft_type(aircraft_requests)
    print("Current aircraft is", aircraft_name)
    read_ardiuno()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program End")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except ConnectionError:
        print("Cannot connect to SimConnect")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
