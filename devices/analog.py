from pyCAP.core.bbox import BBox
from pyCAP.core.timing import TimeValue
from pyCAP.models.generic import BehavioralModel


class AnalogSiSo(BBox):

    def __init__(self):
        super().__init__("analogdev")
        self._add_input("Ain")
        self._add_output("Aout")

        self.continuous()


    def update(self, t : TimeValue):
        
        if t.isZero:
            self.out_Aout.value = 0.0
            return
        
        self.out_Aout.value = self._model.update(
            t,
            self.inp_Ain.value
        )

