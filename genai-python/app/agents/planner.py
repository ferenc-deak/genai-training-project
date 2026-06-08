class PlannerAgent:

    def __init__(self, llm):
        self.llm = llm

    def run(self, task: str, state: dict):

        prompt = f"""
You are a planning agent.

Break this task into steps:
{task}

Return a JSON list of steps.
"""

        response = self.llm.generate(prompt)

        import json
        steps = json.loads(response)

        state["plan"] = steps
        state["status"] = "planned"

        return state