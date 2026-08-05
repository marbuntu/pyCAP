from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class TimeValue:
    ns: int

    def __add__(self, other):
        return TimeValue(self.ns + other.ns)


    def __sub__(self, other):
        return TimeValue(self.ns - other.ns)

    @property
    def seconds(self) -> float:
        """
            Get Value in Seconds
        """
        return self.ns * 1e-9

    @property
    def millis(self) -> float:
        """
            Get Value in Milliseconds
        """
        return self.ns * 1e-6
    
    @property
    def micros(self) -> float:
        """
            Get Value in Microseconds
        """
        return self.ns * 1e-3


    @classmethod
    def fromSeconds(cls, seconds : float) -> object:
        """
            Get Time Object from Seconds
        """
        return cls(int(seconds*1e9))
    

    @classmethod
    def fromMillis(cls, millis : float) -> object:
        """
            Get Time Object from Milliseconds
        """
        return cls(int(millis*1e6))


    @classmethod
    def fromMicros(cls, micros : float) -> object:
        """
            Get Time Object from Microseconds
        """
        return cls(int(micros*1e3))



def TSeconds(seconds : float) -> TimeValue:
    """
        Get Time Object from Seconds
    """
    return TimeValue.fromSeconds(seconds)


def TMillis(millis : float) -> TimeValue:
    """
        Get Time Object from Milliseconds
    """
    return TimeValue.fromMillis(millis)


def TMicros(micros : float) -> TimeValue:
    """
        Get Time Object from Microseconds
    """
    return TimeValue.fromMicros(micros)