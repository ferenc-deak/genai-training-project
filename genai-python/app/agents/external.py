from app.rag.retriever import search_docs

class ExternalExecutorAgent:

    def run(self, state: dict):

        query = state.get("task")

        docs = search_docs(query)

        context = [doc.page_content for doc in docs]
        state["retrieved_context"] = context

        results = []

        for step in state.get("plan", []):
            results.append(f"[A2A External] {step}")

        state["results"] = results
        state["status"] = "completed_external"

        return state