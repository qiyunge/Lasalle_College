from __future__ import annotations

from dataclasses import dataclass
from .ids import ResourceId,MachineId

@dataclass
class Resource:
    id:ResourceId
    availability_time:int = 0

    def __post_init__(self):
        if self.availability_time < 0:
            raise ValueError("Availability time must be a non-negative integer.")   
        

@dataclass
class MachineSpec:
    id:MachineId
    availability_time:int = 0

    def __post_init__(self):
        if self.availability_time < 0:
            raise ValueError("Availability time must be a non-negative integer.")   