# Convert Byte data from Arduino Mega to Keypresses

import serial
import time
import sys, traceback, os
import keyboard
from button_bytes_keyboard import *

# Open Arduino Serial Port
serial_port =  serial.Serial('/dev/ttyACM0', 9600, timeout=0)

def keyboard_lookup(key):
    # keyboardpress_dictionary in button_bytes.py
    #keyboard.press_and_release(keypress_dictionary[key])
    keyboard.press(keypress_dictionary[key])
    time.sleep(0.0001)
    keyboard.release(keypress_dictionary[key])
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
                print()
                keyboard_lookup(ser.hex())
                time.sleep(0.01)
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
