class ExecutorAgent:

    def run(self, state: dict):

        results = []

        for step in state.get("plan", []):
            results.append(f"Executed: {step}")

        state["results"] = results
        state["status"] = "completed"

        return state