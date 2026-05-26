class ExternalExecutorAgent:

    def run(self, state: dict):

        results = []

        for step in state.get("plan", []):
            results.append(f"[A2A] External agent executed: {step}")

        state["results"] = results
        state["status"] = "completed_external"

        return state