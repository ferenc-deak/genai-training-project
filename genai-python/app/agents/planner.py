import json
import re


class PlannerAgent:

    def __init__(self, llm):
        self.llm = llm

    def run(self, task: str, state: dict):

        prompt = f"""
You are a planning agent.

Return ONLY a valid JSON array of strings.

STRICT RULES:
- Output must be ONLY JSON
- No explanations
- No markdown
- No extra text

Example:
["Analyze login issue", "Check backend logs", "Fix authentication"]

Task:
{task}
"""

        response = self.llm.generate(prompt)

        # -----------------------------
        # DEBUG (IMPORTANT)
        # -----------------------------
        print("\n[PLANNER RAW RESPONSE]\n", response, "\n")

        steps = []

        # -----------------------------
        # SAFETY CLEANING
        # -----------------------------
        if response and isinstance(response, str):

            response = response.strip()

            # Try direct JSON first (BEST CASE)
            try:
                steps = json.loads(response)

            except Exception:

                # fallback: extract JSON array from text
                match = re.search(r"\[.*\]", response, re.DOTALL)

                if match:
                    try:
                        steps = json.loads(match.group())
                    except Exception:
                        steps = []
                else:
                    steps = []

        # -----------------------------
        # FINAL SAFETY CHECK
        # -----------------------------
        if not isinstance(steps, list):
            steps = []

        # -----------------------------
        # UPDATE STATE
        # -----------------------------
        state["plan"] = steps
        state["status"] = "planned"

        return state