class Television:
    # Class constants, otherwise representative of the limits of the TV
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method for initializing a new TV object with default values:
        TV is off -- Unmuted -- Volume set at MIN_VOLUME -- Channel set at MIN_CHANNEL
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to toggle the power status of the TV.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method for muting the TV when on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method for increasing the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method for increasing the volume of the TV by 1.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method for decreasing the volume of the TV by 1.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status (power, channel, and volume).
        """
        volume = Television.MIN_VOLUME if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'