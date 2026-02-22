from core.scheduling.models.task import TaskSpec
from core.scheduling.models.resource import MachineSpec
# from core.scheduling.models.state import SchedulingState
# from core.scheduling.models.allocation import Allocation
from .app.use_cases.run_simulation import run_simulation
from shared.utils.gantt import save_gantt
from core.scheduling.metrics.metrics import Metrics   

from core.scheduling.policies.fifo import FIFOPolicy
from core.scheduling.policies.spt  import SPTPolicy
from core.scheduling.policies.edd import EDDPolicy

def demo_tasks():
    return{
        1: TaskSpec(id=1, duration=3, release_time=0, deadline=6),
        2: TaskSpec(id=2, duration=2, release_time=1, deadline=5),
        3: TaskSpec(id=3, duration=4, release_time=2, deadline=10),
        4: TaskSpec(id=4, duration=1, release_time=0, deadline=3),
        5: TaskSpec(id=5, duration=2, release_time=4, deadline=8),     
    }

def demo_resources():
    return {
        1: MachineSpec(id=1, availability_time = 0),
        2: MachineSpec(id=2, availability_time = 0),
    }

def run(policy):
    tasks = demo_tasks()
    resources = demo_resources()

    
    
    final_state = run_simulation(tasks, resources, policy)

  #  metrics = Metrics.evaluate(final_state)

    print(f"\n====={policy}=====")
    # for k,v in metrics.items():
    #     print(f"{k}: {v}")

    #save_gantt(final_state, f"{policy}_gantt.png", title=f"Gantt Chart - {policy}")

if __name__ == "__main__":
    print("Starting FIFO demo...")
    run("FIFO")
    print("finished FIFO")
    run("SPT")
    print("finished SPT")
    run("EDD")
    print("finished EDD")