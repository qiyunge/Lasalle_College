
from __future__ import annotations  
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> None:
        pass

    @abstractmethod
    def bake(self) -> None:
        pass

    