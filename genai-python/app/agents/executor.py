class ExecutorAgent:

    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict):

        from app.rag.retriever import search_docs

        
        # 1. GET TASK
        
        task = state.get("task", "")

        
        # 2. BUILD SEARCH QUERY (IMPORTANT FIX)
        
        query = f"""
backend login authentication debugging issue:
{task}
"""

        
        # 3. RETRIEVE DOCS (RAG)
        
        docs = search_docs(query)

        context = "\n\n".join([f"- {d}" for d in docs])

        state["retrieved_context"] = context

        
        # 4. EXECUTION LOOP
        
        results = []

        for step in state.get("plan", []):

            prompt = f"""
You are an execution engine.

Rules:
- Use ONLY context
- Be factual
- No hallucinations
- Max 8 lines

Context:
{context}

Step:
{step}

Return:
- action
- system component
- short technical description
"""

            try:
                result = self.llm.generate(prompt).strip()
            except Exception as e:
                result = f"ERROR: {str(e)}"

            results.append(result)

        
        # 5. UPDATE STATE
        
        state["results"] = results
        state["status"] = "completed"

        return state