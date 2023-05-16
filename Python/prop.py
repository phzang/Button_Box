import enum
from arduino_dictionary import arduino_dictionary
from SimConnect import *
from globals import DEBUG

# min propeller = -16383, max propeller = 16383
AXIS_PROPELLER = -16383
AXIS_PROPELLER_CONV = 32766
AXIS_PROPELLER_PERCENT = 0 # 0 - 100

def __check_prop_range():
    global AXIS_PROPELLER
    global AXIS_PROPELLER_PERCENT
    if AXIS_PROPELLER < -16383:
        AXIS_PROPELLER = -16383
        AXIS_PROPELLER_PERCENT = 0
    if AXIS_PROPELLER > 16383:
        AXIS_PROPELLER = 16383
        AXIS_PROPELLER_PERCENT = 100


def increase_prop_position():
    global AXIS_PROPELLER
    global AXIS_PROPELLER_PERCENT
    global DEBUG
    AXIS_PROPELLER_PERCENT = AXIS_PROPELLER_PERCENT + 5
    if DEBUG:
        print(AXIS_PROPELLER_PERCENT)
    if DEBUG:
        print(AXIS_PROPELLER)
    set_axis_prop_position()
    __check_prop_range()

def decrease_prop_position():
    global AXIS_PROPELLER
    global AXIS_PROPELLER_PERCENT
    AXIS_PROPELLER_PERCENT = AXIS_PROPELLER_PERCENT - 5
    print(AXIS_PROPELLER_PERCENT)
    print(AXIS_PROPELLER)
    set_axis_prop_position()
    __check_prop_range()

def get_axis_prop_position():
    global AXIS_PROPELLER
    return AXIS_PROPELLER

def get_axis_prop_percent():
    global AXIS_PROPELLER
    return int(((AXIS_PROPELLER + 16383) / 32766) * 100)

def set_axis_prop_position():
    global AXIS_PROPELLER
    global AXIS_PROPELLER_PERCENT
    AXIS_PROPELLER = int((AXIS_PROPELLER_PERCENT / 100 * 32766) - 16383)

