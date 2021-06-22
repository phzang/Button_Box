import logging
import threading
import time
import sys
import traceback
import os
import serial
import pygame
from button_bytes import keypress_dictionary
from switch_dictionary import switch_dictionary
from SimConnect import *
from transponder import *
from com import *
from nav import *
from button_helpers import *

DEBUG = True

# Open Arduino Serial Port
serial_port =  serial.Serial('COM3', 9600, timeout=0)

#SimConnect link
sim_connect = SimConnect()
aircraft_requests = AircraftRequests(sim_connect, _time=200)
aircraft_events = AircraftEvents(sim_connect)

FPS = 30
AIRCRAFT_TYPE = 0 # holder for type of aircraft

# --------------------- START JOYSTICK ITEMS --------------------------------
# --------------------- END JOYSTICK ITEMS ----------------------------------

pygame.init()
pygame.joystick.init()

# finds the button box joystick from USB devices and initializes it
for x in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(x)
    joystick.init()
    if joystick.get_name() == "Generic USB Joystick":
        break

def joystick_main_thread(blank):
    convert_key = 'NONE' # byte identifier to SimConnect identifier holder
    event_function = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if DEBUG:
                    print(event.dict, event.joy,
                    switch_dictionary[str(event.button)], 'pressed')
                if check_switch_dictionary(str(event.button)):
                    convert_key = switch_dictionary[str(event.button)]
                else:
                    convert_key = 'NONE'
            elif event.type == pygame.JOYBUTTONUP:
                if DEBUG:
                    print(event.dict, event.joy,
                    switch_dictionary[str(event.button)], 'released')
                if check_switch_dictionary(str(event.button)):
                    convert_key = switch_dictionary[str(event.button)]
                else:
                    convert_key = 'NONE'

            if convert_key != 'NONE':
                try:
                    if DEBUG:
                        print("FINAL CONVERT KEY ",convert_key)
                    event_function = aircraft_events.find(convert_key)
                    event_function()
                except TypeError:
                    pass

        time.sleep(1/FPS)
# --------------------- END JOYSTICK ITEMS ----------------------------------

# --------------------- START DIAL ITEMS ------------------------------------
def arduino_main_thread(blank):
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
                    # if DEBUG: print(AIRCRAFT_TYPE)
                    if AIRCRAFT_TYPE == "MODEL_C152":
                        event_function(0)
                    elif AIRCRAFT_TYPE == "MODEL_DA40":
                        event_function(1300)
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


# --------------------- END DIAL ITEMS --------------------------------------


def thread_function(name):
    print("Thread %s: starting", name)
    time.sleep(2)
    print("Thread %s: ending", name)

if __name__ == '__main__':
    try:
        AIRCRAFT_TYPE = get_aircraft_type(aircraft_requests)
        print("Current aircraft type is", AIRCRAFT_TYPE)
        #x = threading.Thread(target=thread_function, args=(1,), daemon=True)
        joystick_thread = threading.Thread(target=joystick_main_thread, args=(1,),
            daemon=True)
        joystick_thread.start()
        joystick_thread = threading.Thread(target=arduino_main_thread, args=(1,),
            daemon=True)
        joystick_thread.start()
        while True:
            pass
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
