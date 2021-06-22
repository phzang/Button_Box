import time


class MagMixin:

    # mag positions: 50/51 = Both, 51 = Off, 52 = Start

    '''def __init__(self):
        self.fifty = False
        self.fifty_one = False
        self.fifty_two = False'''

    # 50, 51, 52
    # _last_mag_pos = {False, False, False}
    # _new_mag_pos = {False, False, False}

    # 50 = False, 51 = False
    # both_dial = {self._fifty, self._fifty_one}
    # 52 = False, Temp = False
    # start_dial = {self._fifty_two, False}

    def _reset_mag(self):
        self.fifty = False
        self.fifty_one = False
        self.fifty_two = False

    def _set_mag_pos(self, a, b, c):
        self.fifty = a
        self.fifty_one = b
        self.fifty_two = c

    # return True if under X seconds
    def _check_time_diff(self):
        if time.time() - self.mag_time < 0.5:
            print("under")
            return True
        self.mag_time = time.time()

    # arg = hex input
    def run_mag(self, arg):
        # self._reset_mag()

        '''if arg == 50:
            self.fifty = True
        if arg == 51:
            self.fifty_one = True
        if arg == 52:
            self.fifty_two = True

        if self._check_time_diff():
            # mag on both position
            if self.fifty:
                self.mag_move_both()
                self._reset_mag()
            # mag on off position
            elif self.fifty_one:
                self.mag_move_off()
            # mag on start position
            elif self.fifty_two:
                self.mag_move_start()
                self._reset_mag()'''
        print(arg)
        if arg == 53:
            self.mag_move_both()
        elif arg == 52:
            self.mag_move_start()

    def mag_move_both(self):
        print("mag both")
        self.client.sendDREF("sim/cockpit2/engine/actuators/ignition_key", 3)

    def mag_move_off(self):
        print("mag off")
        self.client.sendDREF("sim/cockpit2/engine/actuators/ignition_key", 0)

    def mag_move_start(self):
        print("mag start")
        self.client.sendDREF("sim/cockpit2/engine/actuators/ignition_on", 4)
        time.sleep(3)
        self.client.sendDREF("sim/cockpit2/engine/actuators/ignition_on", 3)


