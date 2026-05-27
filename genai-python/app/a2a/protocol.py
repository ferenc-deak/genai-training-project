from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class A2AMessage:
    sender: str
    receiver: str
    task: str
    context: Dict[str, Any]
    state: Dict[str, Any]