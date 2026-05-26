class PlannerAgent:

    def run(self, task: str, state: dict):

        steps = [
            f"Analyze task: {task}",
            "Break task into smaller steps",
            "Prepare execution strategy"
        ]

        state["plan"] = steps
        state["status"] = "planned"

        return state