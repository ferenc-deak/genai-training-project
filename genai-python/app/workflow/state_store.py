import json
import os


class StateStore:

    def __init__(self, file_path="workflow_state.json"):
        self.file_path = file_path

    def load(self):

        if not os.path.exists(self.file_path):
            return {}

        with open(self.file_path, "r") as file:
            return json.load(file)

    def save(self, state: dict):

        with open(self.file_path, "w") as file:
            json.dump(state, file, indent=2)