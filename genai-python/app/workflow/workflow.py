from app.agents.planner import PlannerAgent
from app.agents.executor import ExecutorAgent
from app.agents.external import ExternalExecutorAgent

from app.workflow.state_store import StateStore
from app.core.tracing import TraceLogger


class WorkflowEngine:

    def __init__(self, use_external=False):

        self.planner = PlannerAgent()

        # A2A boundary
        if use_external:
            self.executor = ExternalExecutorAgent()
        else:
            self.executor = ExecutorAgent()

        self.store = StateStore()
        self.tracer = TraceLogger()

    def run(self, task: str):

        # Load persisted state
        state = self.store.load()

        state["task"] = task

        self.tracer.log("workflow_start", state)

        # Agent 1: planner
        state = self.planner.run(task, state)

        self.tracer.log("planner_completed", state)

        # Agent 2: executor
        state = self.executor.run(state)

        self.tracer.log("executor_completed", state)

        # Persist state
        self.store.save(state)

        self.tracer.log("workflow_finished", state)

        return state