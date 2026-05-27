from app.rag.retriever import search_docs

class ExecutorAgent:

    def run(self, state: dict):

        query = state.get("task")

        # 🔥 RAG STEP
        docs = search_docs(query)

        context = [doc.page_content for doc in docs]
        state["retrieved_context"] = context

        results = []

        for step in state.get("plan", []):
            results.append(f"Executed: {step}")

        state["results"] = results
        state["status"] = "completed"

        return state