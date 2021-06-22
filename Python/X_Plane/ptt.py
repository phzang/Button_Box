from button_bytes_xconnect_test import *
import enum
import keyboard

DEBUG = False

_vatsim_ptt_key = "ctrl+shift+0"
_discord_ptt_key = "ctrl+shift+1"

_vatsim_ptt_pressed = False
_discord_ptt_pressed = False

def set_vatsim_ptt(pressed):
    global _vatsim_ptt_pressed
    _vatsim_ptt_pressed = pressed

def get_vatsim_ptt():
    global _vatsim_ptt_pressed
    return _vatsim_ptt_pressed


def set_discord_ptt(pressed):
    global _discord_ptt_pressed
    _discord_ptt_pressed = pressed

def get_discord_ptt():
    global _discord_ptt_pressed
    return _discord_ptt_pressed

# return True if ptt is used
def is_ptt(key):
    if int(key) >= 2 and int(key) <= 5:
        return True
    return False

def process_ptt(key):
    try:
        if key == "DISCORD_PRESSED":
            if DEBUG: print("dpress")
            keyboard.press(_discord_ptt_key)
            set_discord_ptt(True)
        elif key == "DISCORD_RELEASED":
            if DEBUG: print("drel")
            keyboard.release(_discord_ptt_key)
            set_discord_ptt(False)
        elif key == "VATSIM_PRESSED":
            if DEBUG: print("vpress")
            set_vatsim_ptt(True)
            keyboard.press(_vatsim_ptt_key)
        elif key == "VATSIM_RELEASED":
            if DEBUG: print("vrel")
            set_vatsim_ptt(False)
            keyboard.release(_vatsim_ptt_key)
        else:
            if DEBUG: print("PTT ERRRRR")

    except TypeError:
        if DEBUG: print("Oops ptt")
