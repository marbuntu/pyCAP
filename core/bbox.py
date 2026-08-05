from abc import ABC

from pyCAP.core.signals import Signal
from pyCAP.core.timing import TimeValue
from pyCAP.core.events import SimEvent


class BBox(ABC):
    """
        ## BBox Abstract Base Class (ABC)

        Represents an arbitray "Black-Box" model.
        The BBox base class offers generic functions to set Event timing and Signals
    """

    def __init__(self, module_name : str):

        self.sig_in = Signal(f"{module_name}.in", 0.0)
        self.sig_out = Signal(f"{module_name}.out", 0.0)

        self.events = []


    def signals(self):
        """
            Get Signal Ports
        """
        return {
            "input": self.sig_in,
            "output": self.sig_out
        }


    def setupSim(self, period : TimeValue, initial_delay : TimeValue = TimeValue(0.0)):
        """
            Set Simulation Event Timing
        """
        self.events = [
            SimEvent(
                time=initial_delay,
                callback=self.update,
                period=period,
                priority=0
            )
        ]

        return self
    

    def connectInput(self, input : Signal):
        """
            Connect Input Signal Port to Signal
        """
        self.sig_in = input
        return self

