import numpy as np

from pyCAP.models.sources.genericsource import SignalSource
from pyCAP.core.timing import TimeValue




class SineSource(SignalSource):

    def __init__(self, amplitide : float, f_hz : float, phase_rad : float = 0.0):
        self.A = amplitide
        self.f = f_hz
        self.phase = phase_rad


    def value(self, t : TimeValue):
        return self.A * np.sin((2.0 * np.pi * self.f * t.seconds) + self.phase)