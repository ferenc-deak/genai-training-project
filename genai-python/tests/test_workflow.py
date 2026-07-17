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
    assert state["status"] != "created"
    assert isinstance(state["plan"], list)
    assert len(state["plan"]) > 0
    assert isinstance(state["results"], list)