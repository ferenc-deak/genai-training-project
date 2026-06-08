from app.agents.planner import PlannerAgent
from app.agents.executor import ExecutorAgent
from app.agents.external import ExternalExecutorAgent

from app.workflow.state_store import StateStore
from app.core.tracing import TraceLogger


class WorkflowEngine:

    def __init__(self, use_external=False, llm=None):

        # 🔥 inject LLM into planner
        self.planner = PlannerAgent(llm)

        # A2A boundary (inject same LLM)
        if use_external:
            self.executor = ExternalExecutorAgent(llm)
        else:
            self.executor = ExecutorAgent(llm)

        self.store = StateStore()
        self.tracer = TraceLogger()

    def run(self, task: str):

        state = self.store.load()
        state["task"] = task

        self.tracer.log("workflow_start", state)

        state = self.planner.run(task, state)
        self.tracer.log("planner_completed", state)

        state = self.executor.run(state)
        self.tracer.log("executor_completed", state)

        self.store.save(state)

        self.tracer.log("workflow_finished", state)

        return state