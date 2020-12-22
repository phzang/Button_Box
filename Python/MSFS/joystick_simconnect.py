# Switches use a generic USB Encoder instead of Arduino
# They are recognized as game input joystick

import pygame
import time
import sys, traceback, os
import serial
from SimConnect import *


pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

DEBUG = False
FPS = 30

# Hex : Button Press
# ------ Lookup Table Buttons -------
switch_dictionary = {
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

DEBUG = True

#SimConnect link
sim_connect = SimConnect()
aircraft_requests = AircraftRequests(sim_connect, _time=200)
aircraft_events = AircraftEvents(sim_connect)
event_funtion = 0
convert_key = 'NONE' # byte identifier to SimConnect identifier holder

# return NONE if no key set
def convert_switch_input(key):
    return switch_dictiionary[key]

def check_dict(key):
    if switch_dictionary[key] == 'NONE':
        return False
    return True

def main():
    global convert_key # byte identifier to SimConnect identifier holder
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if DEBUG:
                    print(event.dict, event.joy,
                    switch_dictionary[str(event.button)], 'pressed')
                if check_dict(str(event.button)):
                    convert_key = switch_dictionary[str(event.button)]
                else:
                    convert_key = 'NONE'
            elif event.type == pygame.JOYBUTTONUP:
                if DEBUG:
                    print(event.dict, event.joy,
                    switch_dictionary[str(event.button)], 'released')
                if check_dict(str(event.button)):
                    convert_key = switch_dictionary[str(event.button)]
                else:
                    convert_key = 'NONE'

            if convert_key != 'NONE':
                try:
                    if DEBUG: print("FINAL CONVERT KEY ",convert_key)
                    event_function = aircraft_events.find(convert_key)
                    event_function()
                except TypeError:
                    pass

        time.sleep(1/FPS)


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
