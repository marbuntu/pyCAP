import numpy as np

from pyCAP.models.generic import ModelParam
from pyCAP.models.generic import BehavioralModel
from pyCAP.core.timing import TimeValue


class ChirpSource(BehavioralModel):

    f0  = ModelParam(1.0, float, "Hz", "Start Frequency")
    f1  = ModelParam(1.0, float, "Hz", "End Frequency")
    Tpr = ModelParam(1.0, TimeValue, "time", "Time Period to increase f from f0 -> f1")
    Tpf = ModelParam(1.0, TimeValue, "time", "Time Period to decrease f from f1 -> f0")

    def __init__(self):
        super().__init__(__class__.__name__)

    def reset(self):
        ...

    def update(self, t : TimeValue) -> float:

        # self._t = t.seconds % (self.Tpr.seconds + self.Tpf.seconds)

        # if (self._t < self.Tpr.seconds):
        #     f_start = self.f0
        #     tau = self._t
        #     self._k = (self.f1 - self.f0) / self.Tpr.seconds
        # else:
        #     f_start = self.f1
        #     tau = self._t - self.Tpr.seconds
        #     self._k = (self.f0 - self.f1) / self.Tpf.seconds

        # self._p = 2 * np.pi * (f_start * tau + 0.5 * self._k * self._t**2)

        Tpr = self.Tpr.seconds
        Tpf = self.Tpf.seconds

        t = t.seconds % (Tpr + Tpf)

        if t < Tpr:

            tau = t
            k = (self.f1 - self.f0) / Tpr

            phase = 2 * np.pi * (
                self.f0 * tau +
                0.5 * k * tau**2
            )

        else:

            tau = t - Tpr
            k = (self.f0 - self.f1) / Tpf

            # Phase accumulated during rising sweep
            phase_rise = 2 * np.pi * (
                self.f0 * Tpr +
                0.5 * (self.f1 - self.f0) * Tpr
            )

            phase = phase_rise + 2 * np.pi * (
                self.f1 * tau +
                0.5 * k * tau**2
            )

        self._p = phase

        return np.sin(self._p)