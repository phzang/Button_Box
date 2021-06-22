import pygame

# Button #, STATE
# STATE = 0 pressed
# STATE = 1 released
joystick_status = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}

temp_joystick_status = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}

def joystick_change_status(input_dict):
    if input_dict == joystick_status:
        return False
    return True
