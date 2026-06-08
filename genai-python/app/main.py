from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import subprocess
import sys

from app.chat import generate_agent
from app.rag.rag import ask_question
from app.workflow.workflow import WorkflowEngine
from app.mcp.server import mcp

app = FastAPI()

engine = WorkflowEngine(use_external=True)


# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- MODELS ----------------
class ChatRequest(BaseModel):
    prompt: str


class RAGRequest(BaseModel):
    question: str


# ---------------- CHAT ----------------
@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": generate_agent(req.prompt, mode="chat")
    }


# ---------------- RAG ----------------
@app.post("/ask")
def ask(req: RAGRequest):

    rag_result = ask_question(req.question)

    rag_answer = rag_result.get("answer", "")
    rag_score = rag_result.get("score", 0)

    ai_answer = generate_agent(req.question, mode="chat")
    ai_score = len(ai_answer) / 1000

    if rag_score > ai_score and rag_answer.strip():
        return {
            "answer": rag_answer,
            "source": "rag",
            "score": rag_score
        }

    return {
        "answer": ai_answer,
        "source": "ai",
        "score": ai_score
    }


# ---------------- WORKFLOW ----------------
@app.post("/workflow")
def run_workflow(req: ChatRequest):
    return engine.run(req.prompt)


# ---------------- HARDWARE TESTS ----------------
BASE = "app/hardware-fundamentals"

def run_hardware_tests():
    subprocess.run([sys.executable, f"{BASE}/latency_test.py"])
    subprocess.run([sys.executable, f"{BASE}/token_speed_test.py"])
    subprocess.run([sys.executable, f"{BASE}/throughput_test.py"])
    subprocess.run([sys.executable, f"{BASE}/report.py"])


@app.post("/run-hardware-tests")
def run_hardware(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_hardware_tests)
    return {
        "status": "started",
        "message": "Hardware benchmarks running in background"
    }


# ---------------- MCP ----------------
if __name__ == "__main__":
    mcp.run()