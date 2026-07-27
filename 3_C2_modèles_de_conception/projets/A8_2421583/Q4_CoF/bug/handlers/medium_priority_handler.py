from bug import BugPriority, BugReport
from .bug_handler import BugHandler



class MediumPriorityHandler(BugHandler):
    def can_handle(self, bug_report: BugReport) -> bool:
        return bug_report.priority == BugPriority.MEDIUM

    def process_bug(self, bug_report: BugReport):
        print(f"Processing medium priority bug: {bug_report.title} with description: {bug_report.description} and priority: {bug_report.priority.value}")