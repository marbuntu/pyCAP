from pyCAP.core.bbox import BBox
from pyCAP.core.signals import Signal
from pyCAP.core.timing import TimeValue
from pyCAP.algo.signalsources import SignalSource


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


    def addPort(self, name : str):
        

        return self


    def update(self, t : TimeValue):
        self.sig_out.value = self.clbk(t, self.sig_in, *self.args, **self.kwargs)