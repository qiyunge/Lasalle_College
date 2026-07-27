from bug import BugPriority, BugReport
from .bug_handler import BugHandler



class LowPriorityHandler(BugHandler):
    def can_handle(self, bug_report: BugReport) -> bool:
        return bug_report.priority == BugPriority.LOW

    def process_bug(self, bug_report: BugReport):
        print(f"Processing low priority bug: {bug_report.title} with description: {bug_report.description} and priority: {bug_report.priority.value}")