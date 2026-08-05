import numpy as np

from pyCAP.algo.signalsources import SignalSource
from pyCAP.core.timing import TimeValue


class AWGNSource(SignalSource):

    def __init__(self, sigma, mean : float = 0.0):
        self.sigma = sigma
        self.mean = mean

    def value(self, t : TimeValue) -> float:
        return np.random.normal(
            loc=self.mean,
            scale=self.sigma
        )