from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, Any

class BehavioralModel(ABC):

    def __init__(self, name):
        self.name = f"{name}_behav"
        self._params : dict[ModelParam] = {}


    @abstractmethod
    def reset(self):
        ...

    @abstractmethod
    def update(self, *args, **kwargs):
        ...




class ModelParam:

    def __init__(self, default : Any, type : Type, unit="", desc=""):
        self.default = default
        self.unit = unit
        self.desc = desc
        self.dtype : Type = type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self      # access to metadata
        return instance._params.get(self.name, self.default)

    def __set__(self, instance, value):
        instance._params[self.name] = value