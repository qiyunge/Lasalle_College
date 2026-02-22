from __future__ import annotations

from .base import Policy
from ..decisions.observation import Observation
from ..decisions.action import Action, DispatchAction, WaitAction

class FIFOPolicy(Policy):
    '''
    First-In-First-Out policy.
    '''
    def decide(self, obs: Observation) -> Action:
        if not obs.ready_tasks or not obs.idle_machines:
            return WaitAction()
        
        tid = sorted(obs.ready_tasks)[0]  # pick the first ready task
        mid = sorted(obs.idle_machines)[0]  # pick the first idle machine
        return DispatchAction( machine_id=mid, task_id=tid)