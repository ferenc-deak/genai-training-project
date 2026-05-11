import json
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
You are a strict incident severity classifier.

You MUST choose ONLY ONE label:

- high = system is broken, downtime, data loss, production outage
- medium = partial functionality broken, degraded performance
- low = cosmetic issues, typos, minor UI issues

Return ONLY valid JSON:

{{
  "action": "high | medium | low",
  "summary": "short explanation"
}}

CRITICAL RULES:
- DO NOT default to low
- You MUST choose based on severity rules above
- If system is down or broken → high
- If functionality partially broken → medium
- If cosmetic issue → low


Task:
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
    result = generate_agent(req.prompt)
    return {"response": result}
