from button_bytes_keyboard import *
import enum

class TransponderDial(enum.Enum):
    First = 1
    Second = 2
    Third = 3
    Fourth = 4

_transponder_dial = TransponderDial.First

# return True if Transponder dial is used
def is_transponder(key):
    #print("transponder key: ", key)
    if key == "38" or key == "39" or key == "40":
        return True
    return False

# return False if error
def set_transponder_dial(dial):
    global _transponder_dial
    _transponder_dial = dial

def get_transponder_dial():
    global _transponder_dial
    return _transponder_dial

def return_transponder_key_lookup(key):
    if is_transponder(key):
        if key == "38": # turn Rotary_H_CW
            if get_transponder_dial() == TransponderDial.First:
                return 'shift+4'
            if get_transponder_dial() == TransponderDial.Second:
                return 'shift+3'
            if get_transponder_dial() == TransponderDial.Third:
                return 'shift+2'
            if get_transponder_dial() == TransponderDial.Fourth:
                return 'shift+1'

        if key == "39": # turn Rotary_H_CCW
            if get_transponder_dial() == TransponderDial.First:
                return 'ctrl+shift+4'
            if get_transponder_dial() == TransponderDial.Second:
                return 'ctrl+shift+3'
            if get_transponder_dial() == TransponderDial.Third:
                return 'ctrl+shift+2'
            if get_transponder_dial() == TransponderDial.Fourth:
                return 'ctrl+shift+1'

        if key == "40": # Rotary_H_Button_Pressed
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
