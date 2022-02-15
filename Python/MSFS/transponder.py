from button_bytes import *
import enum

class TransponderDial(enum.Enum):
    First = 1
    Second = 2
    Third = 3
    Fourth = 4

_transponder_dial = TransponderDial.First

def is_transponder(key):
    # return True if Transponder dial is used
    if key == "38" or key == "39" or key == "40":
        return True
    return False

def set_transponder_dial(dial):
    # return False if error
    global _transponder_dial
    _transponder_dial = dial

def get_transponder_dial():
    global _transponder_dial
    return _transponder_dial

def return_transponder_key_lookup(key):
    # returns Simconnect value for Transponder
    if is_transponder(key):
        if key == "38": # turn Rotary_H_CW
            if get_transponder_dial() == TransponderDial.First:
                return 'XPNDR_1000_INC'
            if get_transponder_dial() == TransponderDial.Second:
                return 'XPNDR_100_INC'
            if get_transponder_dial() == TransponderDial.Third:
                return 'XPNDR_10_INC'
            if get_transponder_dial() == TransponderDial.Fourth:
                return 'XPNDR_1_INC'

        if key == "39": # turn Rotary_H_CCW
            if get_transponder_dial() == TransponderDial.First:
                return 'XPNDR_1000_DEC'
            if get_transponder_dial() == TransponderDial.Second:
                return 'XPNDR_100_DEC'
            if get_transponder_dial() == TransponderDial.Third:
                return 'XPNDR_10_DEC'
            if get_transponder_dial() == TransponderDial.Fourth:
                return 'XPNDR_1_DEC'

        if key == "40": # Rotary_H_Button_Pressed
            # one button to change values, swaps between 1st, 2nd,
            # 3rd, 4th Transponder number
            if get_transponder_dial() == TransponderDial.First:
                set_transponder_dial(TransponderDial.Second)
                return
            if get_transponder_dial() == TransponderDial.Second:
                set_transponder_dial(TransponderDial.Third)
                return
            if get_transponder_dial() == TransponderDial.Third:
                set_transponder_dial(TransponderDial.Fourth)
                return
            if get_transponder_dial() == TransponderDial.Fourth:
                set_transponder_dial(TransponderDial.First)
                return
