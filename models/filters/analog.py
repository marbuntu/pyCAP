import math

from pyCAP.models.generic import BehavioralModel, ModelParam
from pyCAP.core.timing import TimeValue, TSeconds


class AnalogLowPass(BehavioralModel):

    # Parameter Definition
    fc = ModelParam(10.0, float, "Hz", "Cut-Off Frequency")

    # Model Init
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self._y = 0.0
        self._lt = TSeconds(0.0)


    def reset(self):
        self._y = 0.0
        self._lt = TSeconds(0.0)


    # Inherited from Base Class 
    # Add List of Inputs
    def update(self, t : TimeValue, x : float) -> float:

        # Get Time since last Update
        dt = t.seconds - self._lt.seconds

        tau = 1.0 / (2.0 * math.pi * self.fc)
        alpha = 1.0 - math.exp(-dt / tau)

        # update state
        self._lt = t

        # update output
        self._y += alpha * (x - self._y)

        #print(x, dt, tau, alpha, self._y)

        return self._y