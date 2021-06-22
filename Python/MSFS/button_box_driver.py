# Convert Byte data from Arduino Mega to Keypresses

import time
import sys
import traceback
import os
import serial
import keyboard
#from yaspin import yaspin
#from yaspin.spinners import Spinners
from button_bytes import *


# Open Arduino Serial Port
serial_port =  serial.Serial('COM3', 9600, timeout=0)

def keyboard_lookup(key):
    # keyboardpress_dictionary in button_bytes.py
    print(key)
    print(keypress_dictionary[key])
    keyboard.press_and_release('f')



#@yaspin(text="Loading...")
def read_ardiuno():
    while True:
        try:
            ser = serial_port.read()
            if ser:
                keyboard_lookup(ser.hex())
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
