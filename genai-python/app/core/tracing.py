import json
import time

class TraceLogger:

    def __init__(self, file_path="workflow_traces.log"):
        self.file_path = file_path

    def log(self, event: str, data: dict, duration=None):

        trace = {
            "event": event,
            "timestamp": time.time(),
            "duration_ms": duration,
            "data": data
        }

        with open(self.file_path, "a") as file:
            file.write(json.dumps(trace) + "\n")