
from bug.handlers import BugHandler
from bug import BugReport, BugPriority

class BugTrackingSystem:
    def __init__(self, first_handler: BugHandler):
        self._first_handlerfirst_handler = first_handler
       

    def submit_bug(self, bug_report: BugReport):
        print(
            f"Submitting bug: '{bug_report.title}' "
            f"[priority: {bug_report.priority.value}]"
        )

        
        self._first_handlerfirst_handler.process_bug(bug_report)

    