import pytest
from television import *

class Test:
    def setup_method(self):
        self.tvl = Television()

    def teardown_method(self):
        del self.tvl

    def test_init(self):
        # Test default initialization
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        # Toggles the power on
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Toggles the power off
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        # Turns volume up then mutes
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Toggles mute again and checks volume
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # Toggles the power and performs same checks
        self.tvl.power()
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'

        # Again asserts that turning the TV off should have no effect on the volume
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # Channel down 1 -> Channel = 3
        self.tvl.power()
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 3, Volume = 0'

        # Channel down 1 -> Channel = 2
        self.tvl.channel_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 2, Volume = 0'

    def test_volume_up(self):
        # TV is off -- volume up should do nothing
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # TV is on -- volume increases
        self.tvl.power()
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # TV is on and muted -- volume up should unmute and increase the volume
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 2'

        # TV is on and user attempts to increase volume past max
        self.tvl.volume_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # TV is off -- volume down does nothing
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # TV is on -- increase volume first then decrease
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # TV is on and muted -- volume down should unmute and lower volume
        self.tvl.mute()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Attempts to decrease the volume below the minimum
        self.tvl.volume_down()
        self.tvl.volume_down()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'