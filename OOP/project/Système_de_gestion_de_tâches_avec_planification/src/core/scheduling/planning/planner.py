from __future__ import annotations

from ..models.resource import Resource

from ..models.state import SchedulingState
from ..models.task import Task
from ..policies.base import PlanningPolicy

class Planner:
    """
    Transition operator T.
    - Does not own state
    - Applies valid transitions via schedulingstate
    """
    def step(self, state: SchedulingState, policy: PlanningPolicy)->None:
        """
        Single transition:
        - if no ready task, advance time
        - else :select task via policy,choose resource, apply allocation
        Apply the transition operator to the given state using the provided policy.
        """
        # Get the next task to schedule from the policy
        if state.is_finished():
            return 
        ready_tasks = state.ready_tasks()
        if not ready_tasks:
            # No ready tasks, advance time
            state.advance_time()
            return
        
        task = policy.select_task(state)
        resource = self._select_resource_for_task(task, state)

        start = max(state.current_time, task.release_time,resource.availability_time)
        end = start + task.duration

        state.apply_allocation(task, resource, start, end)

    def run_until_finished(self, state: SchedulingState, policy: PlanningPolicy,*,validate_each_step:bool=False) -> SchedulingState:
        """
        Run the planner until all tasks are completed.
        """
        while not state.is_finished():
            self.step(state, policy)
            if validate_each_step:
                state.validate()
        return state
    
    def _select_resource_for_task(self, task: Task, state: SchedulingState)->Resource:
        """
        Select a resource for the given task based on the current state.
        This is a placeholder implementation and should be replaced with actual resource selection logic.
        """
        return min(state.resources, 
                   key=lambda r: max(r.availability_time,task.release_time,state.current_time))