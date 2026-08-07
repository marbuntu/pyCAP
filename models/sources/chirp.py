import numpy as np

from pyCAP.models.generic import ModelParam
from pyCAP.models.sources.base import SignalSourceBase
from pyCAP.core.timing import TimeValue


class ChirpSource(SignalSourceBase):

    f0  = ModelParam(1.0, float, "Hz", "Start Frequency")

    def __init__(self):
        super().__init__(__class__.__name__)


    def value(self, t : TimeValue) -> float:
        ...