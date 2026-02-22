from __future__ import annotations

from dataclasses import dataclass, field
from .task import TaskSpec,TaskRuntime, TaskStatus
from .ids import TaskId, MachineId 
from .resource import MachineSpec
from .events import Event, TimeAdvanceEvent, TaskCompletedEvent, TaskStartedEvent

from ..invariants.exceptions import SchedulingException

@dataclass
class SchedulingState:
    '''
    Aggregate root of the scheduling system.
    Represents the entire runtime state of the system.
    Priciple of encapsulation: state update = state constraint validation + state mutation.
    '''
    # ---theta(immutable scenario)---
    task_specs: dict[TaskId, TaskSpec] = field(default_factory=dict) # theta, immutable information
    machine_specs:dict[MachineId,MachineSpec] = field(default_factory=dict) # immutable information
    # ---runtime---
    current_time :int = 0
    ## task state
    task_runtimes: dict[TaskId, TaskRuntime] = field(default_factory=dict) #state mutable information
    # machine -> current running task
    allocations: dict[MachineId,TaskId] = field(default_factory=dict) 
    busy_until: dict[MachineId,int] = field(default_factory=dict) # machine -> busy until when (timestamp)

    # --- derived state ---
    @property
    def total_tasks(self) -> int:
        return len(self.task_specs)
    
    @property
    def idle_machine_ids(self) -> set[MachineId]:
        return {machine_id for machine_id in self.machine_specs.keys() if machine_id not in self.allocations}
    
    @property
    def pending_task_ids(self) -> set[TaskId]:
        return {task_id for task_id, runtime in self.task_runtimes.items() if runtime.status == TaskStatus.PENDING}
    
    @property
    def completed_task_ids(self) -> set[TaskId]:
        return {task_id for task_id, runtime in self.task_runtimes.items() if runtime.status == TaskStatus.COMPLETED}
    
    @property
    def ready_task_ids(self) -> set[TaskId]:
        return {task_id for task_id in self.pending_task_ids if self.is_task_ready(task_id)}
    ## resource state
   
    #-------------------
    # Queries
    #-------------------

    def get_task(self, task_id: TaskId) -> tuple[TaskSpec,TaskRuntime]:
        return self.task_specs[task_id], self.task_runtimes[task_id]
    
    def is_task_ready(self, task_id: TaskId) -> bool:
        spec, rt = self.get_task(task_id)
        return rt.status == TaskStatus.PENDING and spec.release_time <= self.current_time

    def is_finished(self) -> bool:
        for rt in self.task_runtimes.values():
            if rt.status != TaskStatus.COMPLETED:
                return False
        return True
        # todo: optimize by maintaining a completed_count variable that increments whenever a task is completed, 
        # and compare it with total task count.
    
    #-------------------
    # S mutation(atomic) + local invariant checking(I)
    #-------------------
    def dispatch(self, *, machine_id: MachineId, task_id: TaskId) -> list[Event]:
        '''
        Dispatch a task to a machine, which involves state mutation.
        '''
        self._assert_can_dispatch( machine_id, task_id)
        spec,rt = self.get_task(task_id)

        rt.status = TaskStatus.RUNNING
        rt.machine_id = machine_id
        rt.start_time = self.current_time
    

        self.allocations[machine_id] = task_id
        self.busy_until[machine_id] = self.current_time + spec.duration

        return [TaskStartedEvent(task_id=task_id, machine_id=machine_id, time=self.current_time)]

       

    def _assert_can_dispatch(self,  machine_id: MachineId, task_id: TaskId)->None:
        if machine_id in self.allocations:
            raise SchedulingException(f"Machine {machine_id} is already allocated to task {self.allocations[machine_id]}.")
        # task must exist
        if task_id not in self.task_runtimes or task_id not in self.task_specs:
            raise SchedulingException(f"Unknown task {task_id}.")
        # task must be READY (derived): PENDING + released
        if not self.is_task_ready(task_id):
            raise SchedulingException(f"Task {task_id} is not ready to be dispatched.")

        # consistency check: allocations <-> busy_until
        if machine_id not in self.machine_specs:
            raise SchedulingException(f"Unknown machine {machine_id}.")
        if machine_id in self.busy_until:   
            raise SchedulingException(f"Inconsistent state: machine {machine_id} has busy_until but no allocation.")
        
    def advance_to_next_completion(self) -> list[Event]:
        """
        Event-driven time advance:
        - jump 'now' to the earliest busy_until among running machines
        - mark any tasks finishing at that time as COMPLETED, free those machines
        """
        
        if not self.busy_until:
            return []
        
        events = []
        t0 = self.current_time
        t1 = min(self.busy_until.values())

        self.current_time = t1
        events.append(TimeAdvanceEvent(from_time=t0, to_time=t1))

        finished_machines = [machine_id for machine_id, busy_until in self.busy_until.items() if busy_until == t1]
        for machine_id in finished_machines:
            tid = self.allocations[machine_id]
            _, rt = self.get_task(tid)

            rt.status = TaskStatus.COMPLETED
            rt.finish_time = t1
            rt.machine_id = machine_id

            del self.allocations[machine_id]
            del self.busy_until[machine_id] 

            events.append(TaskCompletedEvent(task_id=tid, machine_id=machine_id, time=t1))
            return events
    def audit(self) -> None:
        '''
        Check internal consistency of the state. Raise exception if any invariant is violated.
        '''
        # 1. allocations <-> busy_until consistency
        for machine_id in self.allocations.keys():
            if machine_id not in self.busy_until:
                raise SchedulingException(f"Inconsistent state: machine {machine_id} has allocation but no busy_until.")
        for machine_id in self.busy_until.keys():
            if machine_id not in self.allocations:
                raise SchedulingException(f"Inconsistent state: machine {machine_id} has busy_until but no allocation.")
        
        # 2. task status consistency with allocations
        for machine_id, task_id in self.allocations.items():
            rt = self.task_runtimes[task_id]
            if rt.status != TaskStatus.RUNNING:
                raise SchedulingException(f"Inconsistent state: task {task_id} allocated to machine {machine_id} but status is {rt.status}.")
        
        # 3. time consistency: current_time should be non-negative
        if self.current_time < 0:
            raise SchedulingException(f"Inconsistent state: current_time {self.current_time} is negative.")    
   
   
    # def advance_to_next_release_if_idle(self) -> list[Event]:
    #         '''
    #         If there is no running task, we can jump to the next release time of pending tasks.
    #         '''
    #         if self.busy_until or self.is_finished():
    #             return []
            
    #         future_releases = []
    #         for tid,spec in self.task_specs.items():
    #             rt = self.task_runtimes[tid]
    #             if rt.status == TaskStatus.PENDING and spec.release_time > self.current_time:
    #                 future_releases.append(spec.release_time)

    #         if not future_releases:
    #             return []
            
    #         t0 = self.current_time
    #         t1 = min(future_releases)

    #         self.current_time = t1
    #         return [TimeAdvanceEvent(from_time=t0, to_time=t1)  ]
           
    #-------------------
    # State mutation + constraint validation(invariant checking)
    #-------------------

def initialize_state(task_specs: dict[TaskId, TaskSpec], machine_specs:dict[MachineId,MachineSpec],now:int) -> SchedulingState:
    '''
    Factory method to create initial state from scenario specifications.
    '''
    state = SchedulingState(task_specs=task_specs, machine_specs=machine_specs, current_time=now)
    for task_id in task_specs.keys():
        state.task_runtimes[task_id] = TaskRuntime(id=task_id, status=TaskStatus.PENDING)
    
    
    state.audit()
    return state