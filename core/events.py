from dataclasses import dataclass, field
from typing import Callable, Optional
from itertools import count

from pyCAP.core.timing import TimeValue


@dataclass(order=True)
class SimEvent:
    time: TimeValue
    priority: int = field(compare=True)

    callback: Callable = field(compare=False)
    args: tuple = field(default_factory=tuple, compare=False)
    kwargs: dict = field(default_factory=dict, compare=False)

    period: Optional[TimeValue] = field(default=None, compare=False)

    cancelled: bool = field(default=False, compare=False)

    def execute(self, scheduler):

        if self.cancelled:
            return

        self.callback(self.time, *self.args, **self.kwargs)

        if self.period is not None:
            self.time += self.period
            scheduler.schedule_event(self)