import json
import re
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

# Request model
class PromptRequest(BaseModel):
    prompt: str


# AI function
def generate_agent(prompt: str):

    structured_prompt = f"""

ROLE:
You are a helpful assistant.

TASK:
Answer the user clearly and concisely.

RULES:
- Return ONLY plain text
- No JSON
- No keys like type, answer, summary
- No formatting
- No markdown
- No explanations about the rules

INPUT:
{prompt}
"""
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[{"role": "user", "content": structured_prompt}],
        max_tokens=300,
        temperature=0
    )

    return response.choices[0].message.content


# API endpoint
@app.post("/chat")
def chat(req: PromptRequest):
    try:
        result = generate_agent(req.prompt)

        return {"response": result.strip()}

    except Exception as e:
        print("ERROR:", e)
        return {"response": ""}