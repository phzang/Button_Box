import xpc
import os
import time
from com_func import ComMixin
from nav_func import NavMixin
from mag_func import MagMixin


class CockpitValues(ComMixin, NavMixin, MagMixin):

    # client = xpc.XPlaneConnect() # xplaneconnect client
    def __init__(self):
        self.barometric_pressure = 29.92
        self.heading = 0
        self.com1 = 120
        self.com1_stdby = 15
        self.com2 = 0
        self.com2_stdby = 0
        self.nav1 = 0
        self.nav1_stdby = 0
        self.nav2 = 0
        self.nav2_stdby = 0
        self.transponder = 0
        self.mixture = 0
        self.fuel_pump = 0
        self.beacon_light = 0
        self.land_light = 0
        self.taxi_light = 0
        self.nav_light = 0
        self.strobe_light = 0
        self.pitot_heat = 0
        self.client = 0

        self.fifty = False
        self.fifty_one = False
        self.fifty_two = False
        self.mag_time = time.time()

        # method list of inputs to execute to xplane
        self._functions = {
            "06": self.swap_com1,
            "08": self.swap_nav1,
            "18": self.com1_whole_up,
            "19": self.com1_whole_down,
            "22": self.com1_decimal_up,
            "23": self.com1_decimal_down,
            "42": self.nav1_whole_up,
            "43": self.nav1_whole_down,
            "46": self.nav1_decimal_up,
            "47": self.nav1_decimal_down,
        }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CockpitValues, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def check_switch_value(self, value): # so we don't have to error check
        if value < 0 or value > 1:     # for every switch
            value = 0
        return value

    def set_client(self, client):
        self.client = client

    def get_starting_values(self):
        self.com1 = self.client.getDREF("sim/cockpit2/radios/actuators/com1_frequency_hz_833")[0]
        self.com1_stdby = self.client.getDREF("sim/cockpit2/radios/actuators/com1_standby_frequency_hz_833")[0]
        self.nav1 = self.client.getDREF("sim/cockpit2/radios/actuators/nav1_left_frequency_hz")[0]
        self.nav1_stdby = self.client.getDREF("sim/cockpit2/radios/actuators/nav1_right_frequency_hz")[0]

    def run_input(self, arg):
        return self._functions[arg]()



