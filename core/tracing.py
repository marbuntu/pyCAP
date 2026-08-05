from dataclasses import dataclass, field

from pyCAP.core.registry import SimRegistry
from pyCAP.core.signals import SignalPort

@dataclass
class TraceChannel:

    name: str
    signal: object

    ltime : list = field(default_factory=list)
    lvalues : list = field(default_factory=list)

    def sample(self, t):
        # print(self.name, t, self.signal.value)
        self.ltime.append(t.millis)
        self.lvalues.append(self.signal.value)



class SimTracer:

    def __init__(self, registry : SimRegistry):
        self.channels = {}
        self._registry = registry


    def add(self, path):
        signals = self._registry.match(path)

        if signals is None:
            print(f"Tracer Error - Could not find Object at {path}")
            return 

        if signals == {}:
            print(f"Tracer Error - Could not find Object at {path}")
            return 


        for key, sig in signals.items():
            if not isinstance(sig, SignalPort):
                continue

            if key in self.channels:
                raise ValueError(
                    f"Trace '{key}' already exists"
                )


            self.channels[key] = TraceChannel(
                key,
                sig
            )

    def add_obj(self, obj : object, pattern : str = "*"):
        pat = self._registry.name_of(obj)
        self.add(f"{pat}{pattern}")


    def sample(self, t):
        for channel in self.channels.values():
            channel.sample(t)