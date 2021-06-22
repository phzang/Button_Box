class NavMixin():
    def get_nav1(self):
        self.nav1 = self.client.getDREF("sim/cockpit2/radios/actuators/nav1_left_frequency_hz")[0]
        # print(self.nav1)
        self.nav1_stdby = self.client.getDREF("sim/cockpit2/radios/actuators/nav1_right_frequency_hz")[0]
        # print(self.nav1_stdby)

    def set_nav1(self):
        self.client.sendDREF("sim/cockpit2/radios/actuators/nav1_left_frequency_hz", self.nav1)
        self.client.sendDREF("sim/cockpit2/radios/actuators/nav1_right_frequency_hz", self.nav1_stdby)

    def swap_nav1(self):
        self.get_nav1()
        tmp_nav = self.nav1
        self.nav1 = self.nav1_stdby
        self.nav1_stdby = tmp_nav
        self.set_nav1()

    def nav1_whole_up(self):
        self.move_nav1_dial(1,"WHOLE","UP")

    def nav1_whole_down(self):
        self.move_nav1_dial(1,"WHOLE","DOWN")

    def nav1_decimal_up(self):
        self.move_nav1_dial(1,"DECIMAL","UP")

    def nav1_decimal_down(self):
        self.move_nav1_dial(1,"DECIMAL","DOWN")

    def move_nav1_dial(self, nav1, number, direction):
        # nav1: nav1 = 1, nav12 = 2
        # number: WHOLE, DECIMAL
        # direction: UP, DOWN
        if nav1 == 1:
            if number == "WHOLE":
                if direction == "UP":
                    self.nav1 += 100
                if direction == "DOWN":
                    self.nav1 -= 100
            if number == "DECIMAL":
                if direction == "UP":
                    self.nav1 += 5
                if direction == "DOWN":
                    self.nav1 -= 5
            if self.nav1 > 11800:
                self.nav1 = 11800
            if self.nav1 < 10800:
                self.nav1 = 10800

            self.client.sendDREF("sim/cockpit2/radios/actuators/nav1_left_frequency_hz", self.nav1)
        elif nav1 == 2:
            pass
        return False
