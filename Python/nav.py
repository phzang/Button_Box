import enum
from arduino_dictionary import arduino_dictionary

class NavigationSelect(enum.Enum):
    PRIMARY = 1
    SECONDARY = 2

NAV_DIAL = NavigationSelect.PRIMARY

def set_nav_dial(dial):
    global NAV_DIAL
    NAV_DIAL = dial

def get_nav_dial():
    global NAV_DIAL
    return NAV_DIAL

def is_nav(key):
    # return True if navigation dial is used
    if int(key) >= 42 and int(key) <= 48:
        return True
    return False

def switch_nav_dial():
    if get_nav_dial() == NavigationSelect.PRIMARY:
        set_nav_dial(NavigationSelect.SECONDARY)
        return
    set_nav_dial(NavigationSelect.PRIMARY)

def return_nav_arduino_lookup(key):
    # returns navigation SimConnect lookup
    if is_nav(key):
        if key == "42": # turn Rotary_I_CW
            if get_nav_dial() == NavigationSelect.PRIMARY:
                return 'NAV1_RADIO_WHOLE_INC'
            if get_nav_dial() == NavigationSelect.SECONDARY:
                return 'NAV2_RADIO_WHOLE_INC'

        if key == "43": # turn Rotary_I_CCW
            if get_nav_dial() == NavigationSelect.PRIMARY:
                return 'NAV1_RADIO_WHOLE_DEC'
            if get_nav_dial() == NavigationSelect.SECONDARY:
                return 'NAV2_RADIO_WHOLE_DEC'

        if key == "46": # turn Rotary_J_CW
            if get_nav_dial() == NavigationSelect.PRIMARY:
                return 'NAV1_RADIO_FRACT_INC'
            if get_nav_dial() == NavigationSelect.SECONDARY:
                return 'NAV2_RADIO_FRACT_INC'

        if key == "47": # Rotary_J_CCW
            if get_nav_dial() == NavigationSelect.PRIMARY:
                return 'NAV1_RADIO_FRACT_DEC'
            if get_nav_dial() == NavigationSelect.SECONDARY:
                return 'NAV2_RADIO_FRACT_DEC'

        if key == "48": # Rotary_J_Button_Pressed
            switch_nav_dial()
