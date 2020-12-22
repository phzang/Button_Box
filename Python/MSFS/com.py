from button_bytes import *
import enum

class CommunicationSelect(enum.Enum):
    Primary = 1
    Secondary = 2

_com_dial = CommunicationSelect.Primary

def set_com_dial(dial):
    global _com_dial
    _com_dial = dial

def get_com_dial():
    global _com_dial
    return _com_dial

# return True if com dial is used
def is_com(key):
    if int(key) >= 18 and int(key) <= 24:
        return True
    return False

def switch_com_dial():
    if get_com_dial() == CommunicationSelect.Primary:
        set_com_dial(CommunicationSelect.Secondary)
        return
    set_com_dial(CommunicationSelect.Primary)

def return_com_key_lookup(key):
    if is_com(key):
        if key == "18": # turn Rotary_C_CW
            if get_com_dial() == CommunicationSelect.Primary:
                return 'COM_RADIO_WHOLE_INC'
            if get_com_dial() == CommunicationSelect.Secondary:
                return 'COM2_RADIO_WHOLE_INC'

        if key == "19": # turn Rotary_C_CCW
            if get_com_dial() == CommunicationSelect.Primary:
                return 'COM_RADIO_WHOLE_DEC'
            if get_com_dial() == CommunicationSelect.Secondary:
                return 'COM2_RADIO_WHOLE_DEC'

        if key == "22": # turn Rotary_D_CW
            if get_com_dial() == CommunicationSelect.Primary:
                return 'COM_RADIO_FRACT_INC'
            if get_com_dial() == CommunicationSelect.Secondary:
                return 'COM2_RADIO_FRACT_INC'

        if key == "23": # turn Rotary_D_CCW
            if get_com_dial() == CommunicationSelect.Primary:
                return 'COM_RADIO_FRACT_DEC'
            if get_com_dial() == CommunicationSelect.Secondary:
                return 'COM2_RADIO_FRACT_DEC'

        if key == "24": # turn Rotary_D_Button_Pressed
            switch_com_dial()
