from __future__ import annotations
from dataclasses import dataclass

from .base import Policy
from ..models.state import SchedulingState   
from ..decisions.observation import Observation
from ..decisions.action import Action, WaitAction,DispatchAction

class SPTPolicy(Policy):
    '''
    Shortest Processing Time policy.
    '''
    def __init__(self, state:SchedulingState):
        self._state = state

    def decide(self, obs: Observation) -> Action:
        if not obs.ready_tasks or not obs.idle_machines:
            return WaitAction()
        
        def duration(tid):
            spec = self._state.task_specs[tid]
            return spec.duration
        
        tid = min(obs.ready_tasks, key=duration)
        mid = sorted(obs.idle_machines)[0]  # pick the first idle machine
        return DispatchAction( machine_id=mid,task_id=tid)