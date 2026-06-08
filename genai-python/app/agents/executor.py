class ExecutorAgent:

    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict):

        from app.rag.retriever import search_docs

        query = state.get("task")

        docs = search_docs(query)
        context = "\n".join([d.page_content for d in docs])

        state["retrieved_context"] = context

        results = []

        for step in state.get("plan", []):

            prompt = f"""
You are an execution agent.

Context:
{context}

Step:
{step}

Explain how you would execute this step.
"""

            try:
                result = self.llm.generate(prompt)
            except Exception as e:
                result = f"ERROR: {str(e)}"
            results.append(result)

        state["results"] = results
        state["status"] = "completed"

        return state