from .transition import Transition
from ..models.state import SchedulingState
from ..decisions.action import Action, WaitAction,DispatchAction

class EventDrivenTransition(Transition):
    def apply(self, state: SchedulingState, action: Action) -> List[Event]:
        if isinstance(action, WaitAction):
            return self.advance(state)
        elif isinstance(action, DispatchAction):
            return self.advance(state)
        else:
            raise ValueError("Unsupported action type")