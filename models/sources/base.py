from abc import ABC, abstractmethod
from pyCAP.core.timing import TimeValue


class SignalSourceBase(ABC):

    def __init__(self, name):
        self.name = name


    def __call__(self, t : TimeValue):
        return self.value(t)


    @abstractmethod
    def value(self, t : TimeValue) -> float:
        ...
