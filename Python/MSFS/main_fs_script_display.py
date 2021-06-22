import logging
import threading
import _thread
from threading import Lock
from queue import Queue
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

prev_time = time.time()
current_time = time.time()

lock = threading.Lock()

# Open Arduino Serial Port
serial_port =  serial.Serial('COM3', 9600, timeout=0)

display_serial_port =  serial.Serial('COM6', 9600, timeout=0)

#SimConnect link
sim_connect = SimConnect()
aircraft_requests = AircraftRequests(sim_connect, _time=0)
aircraft_events = AircraftEvents(sim_connect)

FPS = 30
AIRCRAFT_TYPE = 0 # holder for type of aircraft

DISPLAY_XPNDR = 0 # display transponder
DISPLAY_COM_ACTIVE1 = 0 # display
DISPLAY_COM_STANDBY1 = 0 # display
DISPLAY_NAV_ACTIVE1 = 0 # display
DISPLAY_NAV_STANDBY1 = 0

DISPLAY_COM_ACTIVE2 = 0 # display
DISPLAY_COM_STANDBY2 = 0 # display
DISPLAY_NAV_ACTIVE2 = 0 # display
DISPLAY_NAV_STANDBY2 = 0

COM_UPDATE = False
NAV_UPDATE = False
XPNDR_UPDATE = False

# only update the display what is needed
# causes a delay if trying to update everything at once
def update_com():
    global DISPLAY_COM_ACTIVE1
    global DISPLAY_COM_ACTIVE2
    global DISPLAY_COM_STANDBY1
    global DISPLAY_COM_STANDBY2

    if DEBUG: print("update_com()")
    DISPLAY_COM_ACTIVE1 = aircraft_requests.get('COM_ACTIVE_FREQUENCY:1')
    #DISPLAY_COM_ACTIVE2 = aircraf_requests.get('COM_ACTIVE_FREQUENCY:2')
    DISPLAY_COM_STANDBY1 = aircraft_requests.get('COM_STANDBY_FREQUENCY:1')
    #DISPLAY_COM_STANDBY2 = aircraft_requests.get('COM_STANDBY_FREQUENCY:2')

    display_serial_port.write(bytes("g" + str(DISPLAY_COM_STANDBY1) + "\n",'utf-8'))
    if DEBUG: print(bytes("g" + str(DISPLAY_COM_STANDBY1) + "\n",'utf-8'))
    display_serial_port.write(bytes("o" + str(DISPLAY_COM_ACTIVE1) + "\n",'utf-8'))
    if DEBUG: print(bytes("o" + str(DISPLAY_COM_ACTIVE1) + "\n",'utf-8'))

    '''display_serial_port.write(bytes("g" + str(DISPLAY_COM_STANDBY2) + "\n",'utf-8'))
    if DEBUG: print(bytes("g" + str(DISPLAY_COM_STANDBY2) + "\n",'utf-8'))
    display_serial_port.write(bytes("o" + str(DISPLAY_COM_ACTIVE2) + "\n",'utf-8'))
    if DEBUG: print(bytes("o" + str(DISPLAY_COM_ACTIVE2) + "\n",'utf-8'))'''

    '''if active: DISPLAY_COM_ACTIVE1 = aircraft_requests.get('COM_ACTIVE_FREQUENCY:1')
    if active: DISPLAY_COM_ACTIVE2 = aircraft_requests.get('COM_ACTIVE_FREQUENCY:2')
    if standby: DISPLAY_COM_STANDBY1 = aircraft_requests.get('COM_STANDBY_FREQUENCY:1')
    if standby: DISPLAY_COM_STANDBY2 = aircraft_requests.get('COM_STANDBY_FREQUENCY:2')

    if standby: display_serial_port.write(bytes("g" + str(DISPLAY_COM_STANDBY1) + "\n",'utf-8'))
    if DEBUG: print(bytes("g" + str(DISPLAY_COM_STANDBY1) + "\n",'utf-8'))
    if active: display_serial_port.write(bytes("o" + str(DISPLAY_COM_ACTIVE1) + "\n",'utf-8'))
    if DEBUG: print(bytes("o" + str(DISPLAY_COM_ACTIVE1) + "\n",'utf-8'))'''

def update_nav():
    pass
    DISPLAY_NAV_ACTIVE1 = aircraft_requests.get('NAV_ACTIVE_FREQUENCY:1')
    display_serial_port.write(bytes("o" + str(DISPLAY_NAV_ACTIVE1) + "\n",'utf-8'))

def update_xpndr():
    global DISPLAY_XPNDR
    DISPLAY_XPNDR = get_xpndr()
    display_serial_port.write(bytes("g" + str(DISPLAY_XPNDR) + "\n",'utf-8'))

def get_xpndr():
    # get() returns a hex version of an int
    transponder = hex(int(aircraft_requests.get('TRANSPONDER_CODE:1')))
    # removes the beginning 0x because it's a hex
    return transponder.lstrip("0x")

# --------------------- START JOYSTICK ITEMS --------------------------------

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
    global prev_time
    global current_time
    global COM_UPDATE
    global NAV_UPDATE
    global XPNDR_UPDATE
    set_cache_values()
    while True:
        current_time = time.time()
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
                    XPNDR_UPDATE = True
                # if communication dials pressed
                elif (int(ser.hex()) >= 18 and int(ser.hex()) <= 24):
                    convert_key = return_com_key_lookup(ser.hex())
                    lock.acquire()
                    COM_UPDATE = True
                    lock.release()
                    if DEBUG: print("COM_UPDATE ", COM_UPDATE)
                # if navigation dials pressed
                elif (int(ser.hex()) >= 42 and int(ser.hex()) <= 48):
                    convert_key = return_nav_key_lookup(ser.hex())
                    lock.acquire()
                    NAV_UPDATE = True
                    lock.release()
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

                        if ser.hex() == "06":
                            lock.acquire()
                            COM_UPDATE = True
                            lock.release()
                        if COM_UPDATE:
                            prev_time = time.time()
                        elif NAV_UPDATE:
                            pass
                            #update_nav()
                        elif XPNDR_UPDATE:
                            pass
                            #update_xpndr()

                    except TypeError:
                        pass

            time.sleep(0.01)
            ser = 0 # Reset serial data
            lock.acquire()
            COM_UPDATE = False
            NAV_UPDATE = False
            XPNDR_UPDATE = False
            lock.release()
        except serial.SerialTimeoutException:
            print('Data could not be read')
            time.sleep(0.01)

        # this keeps the display update thread going for 2 seconds after
        # a dial was moved, otherwise there will be missed inputs
        '''if (COM_UPDATE and (current_time - prev_time) > 2):
            print("False")
            lock.acquire()
            COM_UPDATE = False
            NAV_UPDATE = False
            XPNDR_UPDATE = False
            lock.release()
            prev_time = time.time()'''



# --------------------- END DIAL ITEMS --------------------------------------


def thread_function(name):
    print("Thread %s: starting", name)
    time.sleep(2)
    print("Thread %s: ending", name)

def print_display():
    global AIRCRAFT_TYPE
    global DISPLAY_XPNDR
    global DISPLAY_COM_ACTIVE1
    global DISPLAY_COM_ACTIVE2
    global DISPLAY_COM_STANDBY1
    global DISPLAY_COM_STANDBY2

    global DISPLAY_NAV_ACTIVE1
    global DISPLAY_NAV_ACTIVE2
    global DISPLAY_NAV_STANDBY1
    global DISPLAY_NAV_STANDBY2

    AIRCRAFT_TYPE = get_aircraft_type(aircraft_requests)
    print("Current aircraft type is", AIRCRAFT_TYPE)

    DISPLAY_XPNDR = get_xpndr()
    print("Transponder: ", DISPLAY_XPNDR)
    DISPLAY_COM_ACTIVE1 = aircraft_requests.get('COM_ACTIVE_FREQUENCY:1')
    DISPLAY_COM_ACTIVE2 = aircraft_requests.get('COM_ACTIVE_FREQUENCY:2')
    DISPLAY_COM_STANDBY1 = aircraft_requests.get('COM_STANDBY_FREQUENCY:1')
    DISPLAY_COM_STANDBY2 = aircraft_requests.get('COM_STANDBY_FREQUENCY:2')

    #display_serial_port.write(bytes("g" + str(DISPLAY_COM_STANDBY1) + "\n",'utf-8'))
    #display_serial_port.write(bytes("o" + str(DISPLAY_COM_ACTIVE1) + "\n",'utf-8'))


    print("COM ACTIVE1: ", format(DISPLAY_COM_ACTIVE1, '.3f'))
    print("COM STANDBY1: ", format(DISPLAY_COM_STANDBY1, '.3f'))
    print("COM ACTIVE2: ", format(DISPLAY_COM_ACTIVE2, '.3f'))
    print("COM STANDBY2: ", format(DISPLAY_COM_STANDBY2, '.3f'))

    DISPLAY_NAV_ACTIVE1 = aircraft_requests.get('NAV_ACTIVE_FREQUENCY:1')
    DISPLAY_NAV_ACTIVE2 = aircraft_requests.get('NAV_ACTIVE_FREQUENCY:2')
    DISPLAY_NAV_STANDBY1 = aircraft_requests.get('NAV_STANDBY_FREQUENCY:1')
    DISPLAY_NAV_STANDBY2 = aircraft_requests.get('NAV_STANDBY_FREQUENCY:2')

    print("NAV ACTIVE1: ", format(DISPLAY_NAV_ACTIVE1, '.3f'))
    print("NAV STANDBY1: ", format(DISPLAY_NAV_STANDBY1, '.3f'))
    print("NAV ACTIVE2: ", format(DISPLAY_NAV_ACTIVE2, '.3f'))
    print("NAV STANDBY2: ", format(DISPLAY_NAV_STANDBY2, '.3f'))

def update_display_thread(input):
    while True:
        global COM_UPDATE
        global NAV_UPDATE
        global XPNDR_UPDATE

        if(COM_UPDATE): update_com()
        if(XPNDR_UPDATE): update_xpndr()
        time.sleep(0.001)

def set_cache_values():
    frequency = aircraft_requests.find('COM_ACTIVE_FREQUENCY:1')
    frequency.time = 0
    frequency = aircraft_requests.find('COM_ACTIVE_FREQUENCY:2')
    frequency.time = 0
    frequency = aircraft_requests.find('COM_STANDBY_FREQUENCY:1')
    frequency.time = 0
    frequency = aircraft_requests.find('COM_STANDBY_FREQUENCY:2')
    frequency.time = 0


if __name__ == '__main__':
    #update_com() # won't work without moving a button, why?
    print_display()

    try:
        #x = threading.Thread(target=thread_function, args=(1,), daemon=True)
        joystick_thread = threading.Thread(target=joystick_main_thread, args=(1,),
            daemon=True)
        joystick_thread.start()
        arduino_thread = threading.Thread(target=arduino_main_thread, args=(1,),
            daemon=True)
        arduino_thread.start()
        display_thread = threading.Thread(target=update_display_thread, args=(1,),
            daemon=True)
        display_thread.start()
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
