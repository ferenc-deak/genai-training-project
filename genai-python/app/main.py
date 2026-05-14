from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.chat import generate_agent
from app.rag.rag import ask_question

app = FastAPI()

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
    return ask_question(req.question)