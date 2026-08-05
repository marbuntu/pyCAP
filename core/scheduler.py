from heapq import heappush, heappop
from itertools import count

from pyCAP.core.timing import TimeValue
from pyCAP.core.events import SimEvent


class SimScheduler:
    """
        ## Simulation Event Scheduler
    """

    def __init__(self, Tsim : TimeValue):
        """
            Create new Scheduler

            Params:
            -------
            Tsim : TimeValue
                Simulation Time
        """

        self.time = TimeValue(0.0)
        self.until = Tsim
        self._queue = []
        self._counter = count()


    def schedule_event(self, event):
        """
            Schedule an Event

            Params
            ------
            event : SimEvent
        """
        event.priority = next(self._counter)
        heappush(self._queue, event)


    def schedule(self, delay : TimeValue, callback : callable, *args, **kwargs):
        """
            Schedule a Callback with Args

            Params
            ------
            delay : TimeValue
                Callback Delay
            
            callback : callable
                Callback Function
        """
        event = SimEvent(
            time=self.time + delay,
            priority=0, #next(self._counter),
            callback=callback,
            args=args,
            kwargs=kwargs
        )

        self.schedule_event(event)

    def schedule_periodic(self, initial : TimeValue, period : TimeValue, callback, *args, **kwargs):
        """
            Schedule a periodic Callback with Args

            Params
            ------
            initial : TimeValue
                Inial Callback Delay

            period : TimeValue
                Periodic Callback Delay
            
            callback : callable
                Callback Function

        """

        event = SimEvent(
            time=self.time + initial,
            priority=0, #next(self._counter),
            callback=callback,
            args=args,
            kwargs=kwargs,
            period=period
        )

        self.schedule_event(event)


    def run(self):
        """
            Start Scheduler
        """

        while self._queue:

            event = heappop(self._queue)

            if event.time > self.until:
                break

            self.time = event.time

            event.execute(self)