# Convert Byte data from Arduino Mega to Keypresses

import serial
import time
import sys, traceback, os
from button_bytes import *
from SimConnect import *
from transponder import *
from com import *
from nav import *


DEBUG = False

# Open Arduino Serial Port
serial_port =  serial.Serial('COM4', 9600, timeout=0)

#SimConnect link
sim_connect = SimConnect()
aircraft_requests = AircraftRequests(sim_connect, _time=200)
aircraft_events = AircraftEvents(sim_connect)
event_funtion = 0
convert_key = 'NONE' # byte identifier to SimConnect identifier holder


def print_keyboard_lookup(key):
    # keyboardpress_dictionary in button_bytes.py
    print(key)
    print(keypress_dictionary[key])


# return dial/button that was pressed
def get_input(key):
    return keypress_dictionary[key]

# return NONE if no key set
def convert_input(key):
    return keypress_dictionary[key]


def read_ardiuno():
    while True:
        try:
            ser = serial_port.read()
            if (ser):
                #altitude = aircraft_requests.get("PLANE_ALTITUDE")
                #print(altitude)

                if DEBUG: print_keyboard_lookup(ser.hex())
                if DEBUG: print(is_transponder(ser.hex()))

                convert_key = convert_input(ser.hex())

                # if transponder dials pressed
                if ser.hex() == "38" or ser.hex() == "39" or ser.hex() == "40":
                    convert_key = return_transponder_key_lookup(ser.hex())
                # if communication dials pressed
                elif (int(ser.hex()) >= 18 and int(ser.hex()) <= 24):
                    convert_key = return_com_key_lookup(ser.hex())
                # if navigation dials pressed
                elif (int(ser.hex()) >= 42 and int(ser.hex()) <= 48):
                    convert_key = return_nav_key_lookup(ser.hex())

                if convert_key != 'NONE':
                    try:
                        if DEBUG: print("FINAL CONVERT KEY ",convert_key)
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
    print("Working...")
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
