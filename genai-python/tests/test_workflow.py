import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.workflow.workflow import WorkflowEngine
from app.core.simple_llm import SimpleLLM


def test_workflow_execution():
    llm = SimpleLLM()

    engine = WorkflowEngine(
        use_external=True,
        llm=llm
    )

    state = engine.run("Login system is broken")

    assert state is not None
    assert state["task"] == "Login system is broken"
    assert isinstance(state["plan"], list)
    assert isinstance(state["results"], list)
    assert state["status"] != "created"