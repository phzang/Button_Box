import random
import unittest
import importlib
import time
import xpc

#from importlib.machinery import SourceFileLoader
#xpc = SourceFileLoader('xpc', '../XPlaneConnect-master/Python/src/xpc.py').load_module()

def tryagain():
    print("X-Plane Connect example script")
    print("Setting up simulation")
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return

        client.sendDREF("sim/cockpit/electrical/beacon_lights_on",0)

tryagain()
