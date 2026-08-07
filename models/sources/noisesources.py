import numpy as np

from pyCAP.models.sources.base import SignalSourceBase
from pyCAP.core.timing import TimeValue


class AWGNSource(SignalSourceBase):

    def __init__(self, sigma, mean : float = 0.0):
        super().__init__(__class__.__name__)
        self.sigma = sigma
        self.mean = mean

    def value(self, t : TimeValue) -> float:
        return np.random.normal(
            loc=self.mean,
            scale=self.sigma
        )