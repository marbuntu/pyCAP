from pyCAP.models.generic import BehavioralModel, ModelParam
from pyCAP.core.timing import TimeValue

class ClassName(BehavioralModel):

    # Parameter Definition
    param = ModelParam(0.0, float, "unit", "Template Parameter")

    # Model Init
    def __init__(self):
        super().__init__(self.__class__.__name__)


    # Inherited from Base Class 
    # Add List of Inputs
    def update(self, t : TimeValue, *args) -> float:
        ...