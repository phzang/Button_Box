class ComMixin:
    def get_com1(self):
        self.com1 = self.client.getDREF("sim/cockpit2/radios/actuators/com1_frequency_hz_833")[0]
        print(self.com1)
        self.com1_stdby = self.client.getDREF("sim/cockpit2/radios/actuators/com1_standby_frequency_hz_833")[0]
        # print(self.com1_stdby)

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
        self.move_com_dial(1,"WHOLE", "UP")

    def com1_whole_down(self):
        self.move_com_dial(1,"WHOLE", "DOWN")

    def com1_decimal_up(self):
        self.move_com_dial(1,"DECIMAL", "UP")

    def com1_decimal_down(self):
        self.move_com_dial(1, "DECIMAL", "DOWN")

    def move_com_dial(self, com, number, direction):
        # com: com1 = 1, com2 = 2
        # number: WHOLE, DECIMAL
        # direction: UP, DOWN
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
