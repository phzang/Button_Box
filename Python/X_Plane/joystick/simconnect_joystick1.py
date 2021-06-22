import pygame
import time
import sys

sys.path.insert(1,'/home/joe/Desktop/xplane stuff/python/')
from cockpit_values import *

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

cockpit_values = CockpitValues()

DEBUG = True
FPS = 30

button_dict = {
    "0": "sim/electrical/cross_tie_on",
    "1": "sim/cockpit/electrical/battery_on",
    "2": "sim/cockpit/engine/fuel_pump_on",
    "3": "sim/cockpit/electrical/beacon_lights_on",
    "4": "sim/cockpit/electrical/landing_lights_on",
    "5": "sim/cockpit/electrical/taxi_light_on",
    "6": "sim/cockpit/electrical/nav_lights_on",
    "7": "sim/cockpit/electrical/strobe_lights_on",
    "8": "sim/cockpit/switches/pitot_heat_on",
    "9": "9",
    "10": "10",
    "11": "11"
}

def check_dict(key):
    if key != 2 or key != 9 or key != 10 or key != 11:
        return True
    return False

def main():
    client = xpc.XPlaneConnect()
            # Verify connection
    try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
        client.getDREF("sim/test/test_float")
        cockpit_values.set_client(client)
    except:
        print("Error establishing connection to X-Plane.")
        print("Exiting...")

    try:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if DEBUG: print(event.dict, event.joy,
                        button_dict[str(event.button)], 'pressed')
                    if check_dict(str(event.button)):
                        client.sendDREF(button_dict[str(event.button)],1)
                elif event.type == pygame.JOYBUTTONUP:
                    if DEBUG: print(event.dict, event.joy,
                        button_dict[str(event.button)], 'released')
                    if check_dict(str(event.button)):
                        client.sendDREF(button_dict[str(event.button)],0)



            time.sleep(1/FPS)

    except KeyboardInterrupt:
        print("EXITING NOW")
        j.quit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program End")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
