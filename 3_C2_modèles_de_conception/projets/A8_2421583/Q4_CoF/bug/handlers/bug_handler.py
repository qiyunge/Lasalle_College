from __future__ import annotations
from abc import ABC, abstractmethod


from bug import BugReport

class BugHandler(ABC):

    def __init__(self):
        self._next_handler: BugHandler | None = None
    
    def handle_bug(self, bug_report: BugReport):
        if self.can_handle(bug_report):
            self.process_bug(bug_report)
        elif self._next_handler:
            self._next_handler.handle_bug(bug_report)
        else:
            print(f"No handler available for bug: {bug_report.title}")

    def set_next_handler(self, handler: BugHandler)-> BugHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def can_handle(self, bug_report: BugReport) -> bool:
        pass

    @abstractmethod
    def process_bug(self, bug_report: BugReport):
        pass

    