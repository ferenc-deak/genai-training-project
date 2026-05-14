from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import ask_question

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(req: QuestionRequest):
    return ask_question(req.question)