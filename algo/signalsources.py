
from abc import ABC, abstractmethod
import numpy as np

from pyCAP.core.timing import TimeValue


class SignalSource(ABC):

    def __call__(self, t : TimeValue):
        return self.value(t)

    @abstractmethod
    def value(self, t : TimeValue) -> float:
        ...



class SineSource(SignalSource):

    def __init__(self, amplitide : float, f_hz : float, phase_rad : float = 0.0):
        self.A = amplitide
        self.f = f_hz
        self.phase = phase_rad


    def value(self, t : TimeValue):

        return self.A * np.sin((2.0 * np.pi * self.f * t.seconds) + self.phase)

        # print(self._inner)