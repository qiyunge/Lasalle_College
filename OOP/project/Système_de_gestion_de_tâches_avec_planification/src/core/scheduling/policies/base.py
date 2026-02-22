from __future__ import annotations

from dataclasses import dataclass
from abc import ABC, abstractmethod



from ..decisions.observation import Observation
from ..decisions.action import Action

class Policy(ABC):
    """
    Decision rule pi(Observation) -> Action
    Policy is a stateless function that maps the current observation to a decision (task selection).
    """
    @abstractmethod
    def decide(self, obs:Observation) -> Action:
        raise NotImplementedError("decide method must be implemented by subclasses.")