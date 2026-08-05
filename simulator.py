from heapq import heappush, heappop
from itertools import count

from adc import ADC
from timing import TimeValue
from signals import Signal
from generator import SignalGenerator
from events import SimEvent


class Scheduler:

    def __init__(self, Tsim : TimeValue):
        self.time = TimeValue(0.0)
        self.until = Tsim
        self._queue = []
        self._counter = count()

    # def schedule(self, delay : TimeValue, callback, *args, **kwargs):
    #     event_time = self.time + delay
    #     heappush(
    #         self._queue,
    #         (event_time, next(self._counter), callback, args, kwargs)
    #     )


    # def schedule_at(self, event_time : TimeValue, callback, *args, **kwargs):
    #     heappush(
    #         self._queue,
    #         (event_time, next(self._counter), callback, args, kwargs)
    #     )


    # def schedule_periodic(self, event_time : TimeValue, period : TimeValue, callback, *args, **kwargs):
    #     heappush(
    #         self._queue,
    #         (event_time, next(self._counter), self.self.call_periodic, callback, args, kwargs)
    #     )


    # def call_periodic(self, period, callback, *args, **kwargs):
    #     print("call")

    def schedule_event(self, event):
        event.priority = next(self._counter)
        heappush(self._queue, event)

    def schedule(self, delay : TimeValue, callback, *args, **kwargs):

        event = SimEvent(
            time=self.time + delay,
            priority=next(self._counter),
            callback=callback,
            args=args,
            kwargs=kwargs
        )

        self.schedule_event(event)

    def schedule_periodic(self, period : TimeValue, callback, *args, **kwargs):

        event = SimEvent(
            time=self.time + period,
            priority=next(self._counter),
            callback=callback,
            args=args,
            kwargs=kwargs,
            period=period
        )

        self.schedule_event(event)

    # def run(self):
    #     while self._queue:
    #         event_time, _, callback, args, kwargs = heappop(self._queue)

    #         if event_time > self.until:
    #             break

    #         self.time = event_time
    #         callback(*args, **kwargs)

    def run(self):

        while self._queue:

            event = heappop(self._queue)

            if event.time > self.until:
                break

            self.time = event.time

            event.execute(self)


class Simulator:


    def __init__(self, Tsim : TimeValue, dTsim : TimeValue, f_update : callable, *args, **kwargs):
        self.Tsim = Tsim
        self.dT = dTsim
        self._func = f_update
        self._args = args
        self._kwargs = kwargs

        self.scheduler = Scheduler(Tsim)
        self.scheduler.schedule(self.dT, self.update)


    def add_periodic(self, initial_delay : TimeValue, period : TimeValue, callback, *args, **kwargs):
        self.scheduler.schedule(period, callback, *args, **kwargs)


    def update(self) -> None:
        self._func(*self._args, **self._kwargs)
        self.scheduler.schedule(self.dT, self.update)


    def run(self) -> None:
        self.scheduler.run()



if __name__ == "__main__":

    def update(*arg, **kwargs):
        ...


    gen = SignalGenerator()
    adc = ADC(2.4, True, 8)
    adc.sig_in = gen.sig_out

    Tsim = TimeValue.fromSeconds(1.0)
    dTsim = TimeValue.fromSeconds(0.1)

    sig = Signal("raw", 0.0)

    sim = Simulator(Tsim, dTsim, update)
    sim.add_periodic(TimeValue.fromSeconds(0.0), TimeValue.fromSeconds(0.2), adc.update)
    sim.add_periodic(TimeValue.fromSeconds(0.01), TimeValue.fromSeconds(0.1), gen.update)

    # sim.schedule(10e-6, adc.convert, 2.0)
    sim.run()
