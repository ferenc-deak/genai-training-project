from app.workflow.workflow import WorkflowEngine

if __name__ == "__main__":

    engine = WorkflowEngine(use_external=True)

    result = engine.run(
        "Build a RAG system for document QA"
    )

    print("\n===== WORKFLOW RESULT =====\n")
    print(result)