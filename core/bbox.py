from abc import ABC

from pyCAP.core.signals import Signal, InputPort, OutputPort, DebugPort
from pyCAP.core.timing import TimeValue
from pyCAP.core.events import SimEvent


class BBox(ABC):
    """
        ## BBox Abstract Base Class (ABC)

        Represents an arbitray "Black-Box" model.
        The BBox base class offers generic functions to set Event timing and Signals
    """

    def __init__(self, module_name : str):

        # self.sig_in = Signal(f"{module_name}.in", 0.0)
        # self.sig_out = Signal(f"{module_name}.out", 0.0)

        self._inputs : dict[str, InputPort] = {}
        self._outputs : dict[str, OutputPort] = {}
        self._debugps : dict[str, DebugPort] = {}

        self.events = []

    def __getattr__(self, name):

        try:
            prefix, port_name = name.split("_", 1)
        except:
            raise AttributeError(name)

        if prefix == "inp":
            if port_name in self._inputs:
                return self._inputs[port_name]
            
        elif prefix == "out":
            if port_name in self._outputs:
                return self._outputs[port_name]

        elif prefix == "dbg":
            if port_name in self._debugps:
                return self._debugps[port_name]

        raise AttributeError(
            f"{type(self).__name__} has no attribute '{name}'"
        )

    def _add_input(self, name: str) -> InputPort:

        if name in self._inputs:
            raise ValueError(
                f"Input '{name}' already exists."
            )

        port = InputPort(name)
        self._inputs[name] = port
        return port


    def _add_output(self, name: str, initial=0.0) -> OutputPort:

        if name in self._outputs:
            raise ValueError(
                f"Output '{name}' already exists."
            )

        port = OutputPort(name, initial)
        self._outputs[name] = port
        return port


    def _add_debug(self, name : str, initial=0.0) -> DebugPort:

        if name in self._debugps:
            raise ValueError(
                f"Output '{name}' already exists."
            )

        port = DebugPort(name, initial)
        self._debugps[name] = port
        return port


    def ports(self):
        """
            Get Module Ports
        """
        return {
            "inp": self._inputs,
            "out": self._outputs,
            "dbg": self._debugps
        }


    # def signals(self):
    #     """
    #         Get Signal Ports
    #     """
    #     return {
    #         "input": self.sig_in,
    #         "output": self.sig_out,

    #     }


    def every(self, period : TimeValue, initial_delay : TimeValue = TimeValue(0.0)):
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



    # def connectInput(self, port : str, input : Signal):
    #     """
    #         Connect Input Signal Port to Signal
    #     """
    #     self.sig_in = input
    #     return self

