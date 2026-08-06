from abc import ABC, abstractmethod
from pyCAP.core.timing import TimeValue


class SignalSource(ABC):

    def __call__(self, t : TimeValue):
        return self.value(t)

    @abstractmethod
    def value(self, t : TimeValue) -> float:
        ...
