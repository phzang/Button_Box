#!/usr/bin/env python

# import random
# import unittest
# import importlib
# import time
import xpc
# import sys

import serial
import time
import sys
# import os
# import keyboard
from ptt import *
from cockpitvalues import CockpitValues

DEBUG = False

new_key = False
convert_key = "YO"
magneto_pressed = False

cockpit_values = CockpitValues()

# Open Arduino Serial Port
serial_port = serial.Serial('COM3', 9600, timeout=0)

client = xpc.XPlaneConnect()
# Verify connection
try:
    # If X-Plane does not respond to the request, a timeout error
    # will be raised.
    client.getDREF("sim/test/test_float")
    cockpit_values.set_client(client)
except ConnectionError:
    print("Error establishing connection to X-Plane.")
    print("Exiting...")

cockpit_values.get_starting_values()


def keyboard_press(keypress):
    keyboard.press(keypress)
    time.sleep(0.01)
    keyboard.release(keypress)


# return dial/button that was pressed
'''def get_input(key):
    return keypress_dictionary[key]

# return NONE if no key set
def convert_input(key):
    return keypress_dictionary[key]'''


def read_ardiuno():
    global new_key
    global magneto_pressed

    while True:
        try:
            ser = serial_port.read()
            if ser:
                print("ser hex", ser.hex())
                # convert_key = convert_input(ser.hex())

                # if magneto pressed
                if 50 <= int(ser.hex()) <= 53:
                    # convert_key = return_transponder_key_lookup(ser.hex())
                    magneto_pressed = True
                    new_key = True

                # if transponder dials pressed
                if int(ser.hex()) == 38 or int(ser.hex()) == 39\
                        or int(ser.hex()) == 40:
                    # convert_key = return_transponder_key_lookup(ser.hex())
                    new_key = False
                # if communication dials pressed
                elif 18 <= int(ser.hex()) <= 24:
                    # convert_key = return_com_key_lookup(ser.hex())
                    new_key = True
                # if navigation dials pressed
                elif 42 <= int(ser.hex()) <= 48:
                    # convert_key = return_nav_key_lookup(ser.hex())
                    new_key = True

                elif int(ser.hex()) == 6 or int(ser.hex()) == 8 or \
                        int(ser.hex()) == 18 or int(ser.hex()) == 19:
                    new_key = True
                    print("new key", new_key)

                if DEBUG:
                    print("convert key: ", convert_key)

                if convert_key != 'NONE':
                    try:
                        if DEBUG:
                            print("FINAL CONVERT KEY ", convert_key)
                            # check for PTT keys first
                        if is_ptt(int(ser.hex())):
                            process_ptt(convert_key)
                        else:
                            if not new_key:
                                keyboard_press(convert_key)
                            else:
                                # new_press(convert_key)
                                # print("new_press")
                                if magneto_pressed:
                                    print("mag pressed")
                                    magneto_pressed = False
                                    new_key = False
                                    cockpit_values.run_mag(int(ser.hex()))
                                else:
                                    cockpit_values.run_input(ser.hex())
                                    new_key = False
                                # print(client.getDREF("sim/cockpit/radios/com1_stdby_freq_hz"))
                                    '''print(cockpit_values.nav1,
                                        cockpit_values.nav1_stdby)
                                    cockpit_values.swap_nav1()
                                    print(cockpit_values.nav1,
                                        cockpit_values.nav1_stdby) 
                                    '''

                    except TypeError:
                        print("TypeError")
                        pass

                time.sleep(0.001)
            # ser = 0  # Reset serial data
        except serial.SerialTimeoutException:
            print('Data could not be read')
            time.sleep(0.01)
        except ValueError:
            pass


def main():
    read_ardiuno()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program End")
        try:
            sys.exit(0)
        except SystemExit:
            # os._exit(0)
            pass
