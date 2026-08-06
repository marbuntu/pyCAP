import numpy as np

from pyCAP.models.generic import BehavioralModel, ModelParam
from pyCAP.core.timing import TimeValue


class InstAmpModel(BehavioralModel):

    gain    = ModelParam(100.0, float, "V/V")
    supply  = ModelParam((-5, +5), tuple,  "V", "Supply Voltages as tuple (VCC, VEE)")
    clip    = ModelParam(False, bool, "", "Clip Inputs and Outpus exceeding the Supply Voltage")


    def __init__(self):
        super().__init__(self.__class__.__name__)


    def clip_signal(self, x : float):
        return np.clip(x, self.supply[0], self.supply[1])

    def update(self, t : TimeValue, inp : float, inn : float) -> float:

        # Clip Inputs to Supply
        if self.clip:
            inp = self.clip_signal(inp)
            inn = self.clip_signal(inn)

        res = (inp - inn) * self.gain

        # Clip Output to Supply
        if self.clip:
            res = self.clip_signal(res)

        return res


    @classmethod    
    def make_ideal(cls, gain : float) -> object:
        """
            Model Preset for Ideal InstAmp

            ouput = (inp - inn) * A
        """

        mod = cls()
        mod.gain = gain
        mod.clip = False

        return mod

    @classmethod
    def make_basic(cls, gain : float, supply : tuple) -> object:
        """
            Model Preset for a Basic InstAmp

            introduces In- and Output Clipping
        """
        mod = cls()
        mod.gain = gain
        mod.supply = supply
        mod.clip = True

        return mod