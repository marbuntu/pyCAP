from dataclasses import dataclass
from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass(eq=False)
class Signal(Generic[T]):

    def __init__(self, name : str, value : T, unit : str = ""):
        self.name = name
        self.unit = unit
        self._value = value


    @property
    def value(self) -> T:
        return self._value


    @value.setter
    def value(self, value  : T) -> None:
        self._value = value



class SignalPort(Generic[T], ABC):

    def __init__(self, name : str):
        self.name = name


class OutputPort(SignalPort[T]):

    def __init__(self, name: str, initial: T):
        super().__init__(name)
        self._signal = Signal(name, initial)

    @property
    def signal(self) -> Signal[T]:
        return self._signal

    @property
    def value(self) -> T:
        return self._signal.value

    @value.setter
    def value(self, value: T):
        self._signal.value = value


class DebugPort(SignalPort[T]):

    def __init__(self, name : str, initial: T):
        super().__init__(name)
        self._signal = Signal(name, initial)


    @property
    def value(self) -> T:
        return self._signal.value


class InputPort(SignalPort[T]):

    def __init__(self, name : str):
        super().__init__(name)
        self._signal : Signal[T] | None = None


    @property
    def signal(self) -> Signal[T]:
        if self._signal is None:
            raise RuntimeError(
                f"Input '{self.name}' is not connected."
            )
        return self._signal


    @property
    def value(self) -> T:
        return self.signal.value


    def connect(self, signal: OutputPort[T]) -> None:
        if not isinstance(signal, OutputPort):
            raise TypeError(
                "Input can only be connected to Type 'OutputPort'"
            )
        
        self._signal = signal



