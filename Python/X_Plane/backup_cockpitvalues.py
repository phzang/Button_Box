import xpc

class CockpitValues(object):

    #client = xpc.XPlaneConnect() # xplaneconnect client
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

        # method list of inputs to execute to xplane
        self._functions = {
            "06": self.swap_com1,
            "08": self.swap_nav1,
            "18": self.com1_whole_up,
            "19": self.com1_whole_down,
            "22": self.com1_decimal_up,
            "23": self.com1_decimal_down
        }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CockpitValues, cls).__new__(cls)
        return cls.instance

    def check_switch_value(self, value): # so we don't have to error check
        if (value < 0 or value > 1):     # for every switch
            value = 0
        return value

    def set_client(self, client):
        self.client = client

    def get_starting_values(self):
        self.com1 = self.client.getDREF("sim/cockpit2/radios/actuators/com1_frequency_hz_833")[0]
        self.com1_stdby = self.client.getDREF("sim/cockpit2/radios/actuators/com1_standby_frequency_hz_833")[0]
        print(self.com1_stdby)

    def run_input(self, arg):
        return self._functions[arg]()

    def get_com1(self):
        self.com1 = self.client.getDREF("sim/cockpit2/radios/actuators/com1_frequency_hz_833")[0]
        print(self.com1)
        self.com1_stdby = self.client.getDREF("sim/cockpit2/radios/actuators/com1_standby_frequency_hz_833")[0]
        #print(self.com1_stdby)


    def set_com1(self):
        self.client.sendDREF("sim/cockpit2/radios/actuators/com1_frequency_hz_833", self.com1)
        self.client.sendDREF("sim/cockpit2/radios/actuators/com1_standby_frequency_hz_833", self.com1_stdby)

    def swap_com1(self):
        self.get_com1()
        tmp_com = self.com1
        self.com1 = self.com1_stdby
        self.com1_stdby = tmp_com
        self.set_com1()


    def com1_whole_up(self):
        self.move_com_dial(1,"WHOLE","UP")

    def com1_whole_down(self):
        self.move_com_dial(1,"WHOLE","DOWN")

    def com1_decimal_up(self):
        self.move_com_dial(1,"DECIMAL","UP")

    def com1_decimal_down(self):
        self.move_com_dial(1,"DECIMAL","DOWN")

    def move_com_dial(self, com, number, direction):
        #print(com,number,direction)
        # com: com1 = 1, com2 = 2
        # direction: UP, DOWN
        # number: WHOLE, DECIMAL
        if com == 1:
            if number == "WHOLE":
                if direction == "UP":
                    self.com1 += 1000
                if direction == "DOWN":
                    self.com1 -= 1000
            if number == "DECIMAL":
                if direction == "UP":
                    self.com1 += 5
                if direction == "DOWN":
                    self.com1 -= 5
            if self.com1 > 136990:
                self.com1 = 136990
            if self.com1 < 118000:
                self.com1 = 118000

            self.client.sendDREF("sim/cockpit2/radios/actuators/com1_frequency_hz_833", self.com1)
        elif com == 2:
            pass
        return False


    def get_nav1(self):
        self.nav1 = self.client.getDREF("sim/cockpit/radios/nav1_freq_hz")[0]
        #print(self.nav1)
        self.nav1_stdby = self.client.getDREF("sim/cockpit/radios/nav1_stdby_freq_hz")[0]
        #print(self.nav1_stdby)

    def set_nav1(self):
        self.client.sendDREF("sim/cockpit/radios/nav1_freq_hz", self.nav1)
        self.client.sendDREF("sim/cockpit/radios/nav1_stdby_freq_hz", self.nav1_stdby)

    def swap_nav1(self):
        self.get_nav1()
        tmp_nav = self.nav1
        self.nav1 = self.nav1_stdby
        self.nav1_stdby = tmp_nav
        self.set_nav1()


    def set_fuel_pump(self, value):
        self.client.sendDREF("sim/cockpit/engine/fuel_pump_on",
                                self.check_switch_value(value))
        self.fuel_pump = value

    def set_beacon_light(self, value):
        self.client.sendDREF("sim/cockpit/electrical/beacon_lights_on",
                                self.check_switch_value(value))
        self.beacon_light = value

    def set_land_light(self, value):
        self.client.sendDREF("sim/cockpit/electrical/landing_lights_on",
                                self.check_switch_value(value))
        self.land_light = value

    def set_taxi_light(self, value):
        self.client.sendDREF("sim/cockpit/electrical/taxi_light_on",
                                self.check_switch_value(value))
        self.taxi_light = value

    def set_nav_light(self, value):
        self.client.sendDREF("sim/cockpit/electrical/nav_lights_on",
                                self.check_switch_value(value))
        self.nav_light = value

    def set_strobe_light(self, value):
        self.client.sendDREF("sim/cockpit/electrical/strobe_lights_on",
                                self.check_switch_value(value))
        self.strobe_light = value

    def set_pitot_heat(self, value):
        self.client.sendDREF("sim/cockpit/switches/pitot_heat_on",
                                self.check_switch_value(value))
        self.pitot_heat = value
