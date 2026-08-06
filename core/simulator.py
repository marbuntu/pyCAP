from dataclasses import dataclass

from pyCAP.core.timing import TimeValue
from pyCAP.core.signals import Signal
from pyCAP.core.bbox import BBox

from pyCAP.core.scheduler import SimScheduler
from pyCAP.core.registry import SimRegistry
from pyCAP.core.tracing import SimTracer



@dataclass
class SimContext:
    scheduler : SimScheduler
    registry : SimRegistry
    tracer : SimTracer



class Simulator:
    """
        ## Simulation Handler
    """


    def __init__(self, Tsim : TimeValue, dTsim : TimeValue,*args, **kwargs):
        self.Tsim = Tsim
        self.dT = dTsim
        self._args = args
        self._kwargs = kwargs

        self.scheduler = SimScheduler(Tsim, dTsim)
        self.registry = SimRegistry()
        self.tracer = SimTracer(self.registry)

        self.ctx = SimContext(
            scheduler=self.scheduler,
            registry=self.registry,
            tracer=self.tracer
        )

        self.scheduler.schedule(self.dT, self.update)


    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_value, traceback):
        pass


    def add_periodic(self, initial_delay : TimeValue, period : TimeValue, callback, *args, **kwargs):
        """
        
        """
        self.scheduler.schedule_periodic(initial_delay, period, callback, *args, **kwargs)


    def add(self, module : BBox):

        self.registry.register(module)

        for evt in module.events:
            # Event Period equal zero is not supported (but used for analog devices)
            # Change it here to the smallest allowed time increment

            if evt.period == 0:
                print(evt, "is analog")
                evt.period = self.dT

            self.scheduler.schedule_event(evt)
        

    def update(self, t : TimeValue) -> None:
        # self._func(*self._args, **self._kwargs)
        self.tracer.sample(
            self.scheduler.time
        )

        self.scheduler.schedule(self.dT, self.update)


    def run(self) -> None:
        self.scheduler.run()


    def get_context(self) -> SimContext:
        self.ctx

