from application import BugTrackingSystem
from bug import BugReport,BugPriority
from bug.handlers import LowPriorityHandler, MediumPriorityHandler, HighPriorityHandler
def main():
    low_handler = LowPriorityHandler()
    medium_handler = MediumPriorityHandler()
    high_handler = HighPriorityHandler()

    low_handler.set_next_handler(medium_handler).set_next_handler(high_handler)
    

    bug_tracking_system = BugTrackingSystem(low_handler)

    bugs = [BugReport(title="Bug 1",
                    priority=BugPriority.LOW,
                    description="This is a low priority bug."
                    ), 
            BugReport(title="Bug 2", 
                      priority=BugPriority.MEDIUM,
                      description="This is a medium priority bug."
                      ), 
            BugReport(title="Bug 3", 
                      priority=BugPriority.HIGH,
                      description="This is a high priority bug."
                        )]

    for bug in bugs:
        bug_tracking_system.submit_bug(bug)
        print("**" * 20)

if __name__ == "__main__":
    main()