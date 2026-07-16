from app.workflow.workflow import WorkflowEngine
from app.core.simple_llm import SimpleLLM


if __name__ == "__main__":

    llm = SimpleLLM()

    engine = WorkflowEngine(
        use_external=True,
        llm=llm
    )

    result = engine.run(
        "Build a RAG system for document QA"
    )

    print("\n===== WORKFLOW RESULT =====\n")
    print(result)