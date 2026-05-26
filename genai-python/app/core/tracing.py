import json
import time


class TraceLogger:

    def __init__(self, file_path="workflow_traces.log"):
        self.file_path = file_path

    def log(self, event: str, data: dict):

        trace = {
            "event": event,
            "timestamp": time.time(),
            "data": data
        }

        with open(self.file_path, "a") as file:
            file.write(json.dumps(trace) + "\n")