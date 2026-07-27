from dataclasses import dataclass

from enum import Enum


class BugPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class BugReport:
    title: str
    description: str
    priority: BugPriority
    