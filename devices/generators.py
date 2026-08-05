
from pyCAP.core.bbox import BBox
from pyCAP.core.timing import TimeValue
from pyCAP.algo.signalsources import SignalSource


class SignalGenerator(BBox):

    def __init__(self):
        super().__init__("generator")
        self.sources = []

    def add_source(self, source : SignalSource):
        if source is None:
            raise ValueError(
                f"Source Obect is 'None'"
            )

        if not isinstance(source, SignalSource):
            raise ValueError(
                f"Source Obect is not Instance of 'SignalSource'"
            )

        self.sources.append(source)

        return self
        


    def update(self, t : TimeValue):
        tmp = 0.0
        for src in self.sources:
            tmp += src(t)

        self.sig_out.value = tmp



