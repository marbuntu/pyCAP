from pyCAP.core.bbox import BBox
from pyCAP.core.timing import TimeValue


class UserDspBlock(BBox):

    def __init__(self, update_clbk : callable, *args, **kwargs):
        super().__init__("user-dsp")

        if update_clbk is None:
            raise ValueError(
                "Callback cannot be None!"
            )

        self.clbk = update_clbk
        self.args = args
        self.kwargs = kwargs


    def add_input(self, name : str):
        self._add_input(name)
        return self


    def add_output(self, name : str):
        self._add_output(name)
        return self
    

    def add_debug(self, name : str):
        self._add_debug(name)
        return self


    def update(self, t : TimeValue):
        self.clbk(self, t, *self.args, **self.kwargs)