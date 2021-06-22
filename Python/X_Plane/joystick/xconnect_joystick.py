import pygame
import time
import sys
import xpc
import os

sys.path.append(r"C:\Users\philip\Desktop\xplane_stuff\python\joystick")
# from cockpit_values import *

pygame.init()
j = pygame.joystick.Joystick(1)
j.init()

# cockpit_values = CockpitValues()

DEBUG = True
FPS = 30

button_dict = {
    "0": "sim/cockpit2/electrical/generator_on",
    "1": "sim/cockpit/electrical/battery_on",
    "2": "sim/cockpit2/engine/actuators/fuel_pump_on[0]",
    "3": "sim/cockpit/electrical/beacon_lights_on",
    "4": "sim/cockpit/electrical/landing_lights_on",
    "5": "sim/cockpit/electrical/taxi_light_on",
    "6": "sim/cockpit/electrical/nav_lights_on",
    "7": "sim/cockpit/electrical/strobe_lights_on",
    "8": "sim/cockpit/switches/pitot_heat_on",
    "9": "sim/test/test_float",
    "10": "simcoders/rep/cockpit2/switches/avionics_power_on",
    "11": "sim/cockpit2/electrical/cross_tie"
}


def check_dict(key):
    if key != 2:
        return True
    return False


def main():
    client = xpc.XPlaneConnect()
    # Verify connection
    try:
        # If X-Plane does not respond to the request, a timeout error
        # will be raised.
        print("Connecting")
        if DEBUG: print("Debugging")
        client.getDREF("sim/test/test_float")
        # cockpit_values.set_client(client)
    except ConnectionError:
        print("Error establishing connection to X-Plane.")
        print("Exiting...")

    try:
        jid = j.get_instance_id()
    except AttributeError:
        # get_instance_id() is an SDL2 method
        jid = j.get_id()
    print("Joystick {}".format(jid))

    try:
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    print("down")
                    if DEBUG:
                        print(event.dict, event.joy,
                              button_dict[str(event.button)], 'pressed')
                    if check_dict(str(event.button)):
                        client.sendDREF(button_dict[str(event.button)], True)
                elif event.type == pygame.JOYBUTTONUP:
                    if DEBUG:
                        print(event.dict, event.joy,
                              button_dict[str(event.button)], 'released')
                    if check_dict(str(event.button)):
                        client.sendDREF(button_dict[str(event.button)], False)

            time.sleep(1 / FPS)

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
