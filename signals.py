from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass
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

