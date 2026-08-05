from pyCAP.core.bbox import BBox
from pyCAP.core.timing import TimeValue


class InstAmp(BBox):

    def __init__(self):
        super().__init__("instamp")
        self._add_input("Ainp")
        self._add_input("Ainn")
        self._add_output("Aout")
        self.A = 1.0


    def set_amplification(self, A : float):
        self.A = A
        return self
    

    def add_source(self, source : SignalSource):
        ...


    def update(self, t : TimeValue):
        self.out_Aout.value = self.A * (self.inp_Ainp.value - self.inp_Ainn.value)
