# Convert Byte data from Arduino Mega to Keypresses

import serial
import time
import sys, traceback, os
import keyboard
from button_bytes_keyboard import *
from com import *
from nav import *
from transponder import *
from ptt import *

DEBUG = False

# Open Arduino Serial Port
serial_port =  serial.Serial('/dev/ttyACM0', 9600, timeout=0)

def keyboard_press(keypress):
    keyboard.press(keypress)
    time.sleep(0.01)
    keyboard.release(keypress)

'''def keyboard_lookup(key):
    # keyboardpress_dictionary in button_bytes.py
    keyboard.press(keypress_dictionary[key])
    time.sleep(0.0001)
    keyboard.release(keypress_dictionary[key])
    print(keypress_dictionary[key])'''

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
                convert_key = convert_input(ser.hex())

                # if transponder dials pressed
                if (int(ser.hex())== 38 or int(ser.hex()) == 39 or int(ser.hex()) == 40):
                    convert_key = return_transponder_key_lookup(ser.hex())
                # if communication dials pressed
                elif (int(ser.hex()) >= 18 and int(ser.hex()) <= 24):
                    convert_key = return_com_key_lookup(ser.hex())
                # if navigation dials pressed
                elif (int(ser.hex()) >= 42 and int(ser.hex()) <= 48):
                    convert_key = return_nav_key_lookup(ser.hex())

                if DEBUG: print("convert key: ", convert_key)

                if convert_key != 'NONE':
                        try:
                            if DEBUG: print("FINAL CONVERT KEY ",convert_key)
                            # check for PTT keys first
                            if is_ptt(int(ser.hex())):
                                process_ptt(convert_key)
                            else:
                                keyboard_press(convert_key)

                        except TypeError:
                            print("oops")
                            pass

                time.sleep(0.001)
                ser = 0 # Reset serial data
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
            os._exit(0)
