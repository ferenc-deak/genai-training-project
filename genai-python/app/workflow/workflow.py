from app.agents.planner import PlannerAgent
from app.agents.executor import ExecutorAgent
from app.agents.external import ExternalExecutorAgent

from app.workflow.state_store import StateStore
from app.core.tracing import TraceLogger
from app.core.simple_llm import SimpleLLM


class WorkflowEngine:

    def __init__(self, use_external=False, llm=None):

        # Create a default LLM if one is not provided
        self.llm = llm or SimpleLLM()

        self.planner = PlannerAgent(self.llm)

        if use_external:
            self.executor = ExternalExecutorAgent(self.llm)
        else:
            self.executor = ExecutorAgent(self.llm)

        self.store = StateStore()
        self.tracer = TraceLogger()

    def run(self, task: str):

        # Start each workflow with a fresh state
        state = {
            "task": task,
            "plan": [],
            "status": "created",
            "retrieved_context": "",
            "results": []
        }

        self.tracer.log("workflow_start", state)

        state = self.planner.run(task, state)
        self.tracer.log("planner_completed", state)

        state = self.executor.run(state)
        self.tracer.log("executor_completed", state)

        self.store.save(state)

        self.tracer.log("workflow_finished", state)

        return state