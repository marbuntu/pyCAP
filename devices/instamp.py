from pyCAP.core.bbox import BBox
from pyCAP.core.timing import TimeValue
from pyCAP.models.generic import BehavioralModel

class InstAmp(BBox):

    def __init__(self):
        super().__init__("instamp")
        self._add_input("Ainp")
        self._add_input("Ainn")
        self._add_output("Aout")
        self._model : BehavioralModel | None = None


    def set_model(self, model : BehavioralModel) -> BehavioralModel:
        if not isinstance(model, BehavioralModel):
            raise TypeError(model)

        self._model = model

        return self
    

    def update(self, t : TimeValue):

        self.out_Aout.value = self._model.update(
            t, 
            self.inp_Ainp.value, 
            self.inp_Ainn.value
        )

