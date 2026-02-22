from __future__ import annotations
from dataclasses import dataclass

from .base import Policy
from ..decisions.observation import Observation
from ..decisions.action import Action, WaitAction,DispatchAction
from ..models.state import SchedulingState
from .spt import SPTPolicy


class EDDPolicy(Policy):
    '''
    Earliest Due Date policy.
    '''
    def __init__(self, state:SchedulingState):
        self._state = state

    def decide(self, obs: Observation) -> Action:
        if not obs.ready_tasks or not obs.idle_machines:
            return WaitAction()
        
        def due(tid):
            spec = self._state.task_specs[tid]
            return spec.deadline
        
        dues = [due(tid) for tid in obs.ready_tasks]
        if any(d is None for d in dues):
            # if any task has no deadline, fall back to SPT
            spt_policy = SPTPolicy(self._state)
            return spt_policy.decide(obs)
        else:
            tid = min(obs.ready_tasks, key=due)
            mid = sorted(obs.idle_machines)[0]  # pick the first idle machine
            return DispatchAction(task_id=tid, machine_id=mid)
        