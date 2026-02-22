from __future__ import annotations

from ..planning.planner import Planner
from ..models.task import Task
from ..models.resource import Resource
from ..models.state import SchedulingState
from ..policies.base import PlanningPolicy
class Simulator:
    """
    Responsible for :
    - initializing state
    - running rollout until finished
    """

    def __init__(self):
        self.planner = Planner()

    def initialize_state(
            self,
            tasks: list[Task],
            resources: list[Resource]
            ) -> SchedulingState:
        """
        Initialize the state of the system with the given tasks and resources.
        """
        # Implementation to initialize the state based on tasks and resources
        resource_copy = [ Resource(
            id=resource.id,
            availability_time=resource.availability_time) 
            for resource in resources]
        return SchedulingState(
            current_time=0,
            pending_tasks= list(tasks),
            completed_tasks=[],
            resources= resource_copy,
            allocations=[]
        )
    
    def run(self,
            tasks: list[Task],
            resources: list[Resource],
            policy: PlanningPolicy
            ) -> SchedulingState:
            
        state = self.initialize_state(tasks, resources)
        self.planner.run_until_finished(state, policy)
        return state