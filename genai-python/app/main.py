from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.mcp.server import mcp

from app.chat import generate_agent
from app.rag.rag import ask_question   # ONLY this
from app.workflow.workflow import WorkflowEngine

app = FastAPI()

engine = WorkflowEngine(use_external=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- CHAT ----------------
class ChatRequest(BaseModel):
    prompt: str


@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": generate_agent(req.prompt)}


# ---------------- RAG ----------------
class RAGRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(req: RAGRequest):
    question = req.question

    # 1. Get RAG result
    rag_result = ask_question(question)

    # make sure you return structured data from RAG
    rag_answer = rag_result.get("answer", "")
    rag_score = rag_result.get("score", 0)

    # 2. Get AI answer
    ai_answer = generate_agent(question)

    # optional: simple AI scoring heuristic
    ai_score = len(ai_answer) / 1000  # VERY simple baseline

    # 3. Decision logic
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

if __name__ == "__main__":
    mcp.run()

@app.post("/workflow")
def run_workflow(req: ChatRequest):
    result = engine.run(req.prompt)
    return result
