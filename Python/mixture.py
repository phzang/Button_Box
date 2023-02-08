import enum
from arduino_dictionary import arduino_dictionary
from globals import DEBUG
from SimConnect import *

# min = -16383, max = 16383
AXIS_MIXTURE = -16383
AXIS_MIXTURE_CONV = 32766
AXIS_MIXTURE_PERCENT = 0 # 0 - 100

def __check_mixture_range():
    global AXIS_MIXTURE
    global AXIS_MIXTURE_PERCENT
    if AXIS_MIXTURE < -16383:
        AXIS_MIXTURE = -16383
        AXIS_MIXTURE_PERCENT = 0
    if AXIS_MIXTURE > 16383:
        AXIS_MIXTURE = 16383
        AXIS_MIXTURE_PERCENT = 100


def increase_mixture_position():
    global AXIS_MIXTURE
    global AXIS_MIXTURE_PERCENT
    global DEBUG
    AXIS_MIXTURE_PERCENT = AXIS_MIXTURE_PERCENT + 5
    if DEBUG:
        print(AXIS_MIXTURE_PERCENT)
    if DEBUG:
        print(AXIS_MIXTURE)
    set_axis_mixture_position()
    __check_mixture_range()

def decrease_mixture_position():
    global AXIS_MIXTURE
    global AXIS_MIXTURE_PERCENT
    AXIS_MIXTURE_PERCENT = AXIS_MIXTURE_PERCENT - 5
    if DEBUG:
        print(AXIS_MIXTURE_PERCENT)
    if DEBUG:
        print(AXIS_MIXTURE)
    set_axis_mixture_position()
    __check_mixture_range()

def get_axis_mixture_position():
    global AXIS_MIXTURE
    return AXIS_MIXTURE

def get_axis_mixture_percent():
    global AXIS_MIXTURE
    return int(((AXIS_MIXTURE + 16383) / 32766) * 100)

def set_axis_mixture_position():
    global AXIS_MIXTURE
    global AXIS_MIXTURE_PERCENT
    AXIS_MIXTURE = int((AXIS_MIXTURE_PERCENT / 100 * 32766) - 16383)