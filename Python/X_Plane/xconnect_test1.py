import random
import unittest
import importlib
import time
import xpc
from cockpit_values import *

#from importlib.machinery import SourceFileLoader
#xpc = SourceFileLoader('xpc', '../XPlaneConnect-master/Python/src/xpc.py').load_module()
cockpit_values = CockpitValues()

def tryagain():
    print("X-Plane Connect example script")
    print("Setting up simulation")
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
            cockpit_values.set_client(client)
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return

        client.sendDREF("sim/cockpit/electrical/beacon_lights_on",0)
        cockpit_values.set_default_values()
        cockpit_values.set_fuel_pump(0)
        cockpit_values.set_beacon_light(0)
        cockpit_values.set_land_light(0)
        cockpit_values.set_taxi_light(0)
        cockpit_values.set_nav_light(0)
        cockpit_values.set_strobe_light(0)
        cockpit_values.set_pitot_heat(0)


tryagain()
