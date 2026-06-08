import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.workflow.workflow import WorkflowEngine
from app.core.simple_llm import SimpleLLM

llm = SimpleLLM()
engine = WorkflowEngine(use_external=True, llm=llm)

result = engine.run("Login system is broken")

print(result)