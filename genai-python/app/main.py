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
ROLE:
You are a STRICT routing classifier for a support system.

You MUST decide exactly ONE category:

-------------------------
CATEGORIES
-------------------------

1. INCIDENT
Definition:
A system failure, bug, outage, error, or performance degradation.

Examples:
- API is down
- login not working
- server returns 500
- database is slow
- app crashed

2. QUESTION
Definition:
A request for information, explanation, or learning.

Examples:
- What is REST API?
- How does caching work?
- Explain React hooks

-------------------------
DECISION RULES (VERY IMPORTANT)
-------------------------

- If the user reports a problem → INCIDENT
- If the user asks "what / how / why" → QUESTION
- If both appear → INCIDENT has HIGHER priority

- If user says "hello", greet them politely.
- If user reports a system problem, classify it as INCIDENT.
- Otherwise answer normally.

-------------------------
OUTPUT RULES (CRITICAL)
-------------------------

- Output ONLY valid JSON
- NO markdown
- NO backticks
- NO extra keys
- Detailed summary is REQUIRED for INCIDENT
- Detailed explanation is REQUIRED for QUESTION
- MUST be parseable by json.loads()

-------------------------
OUTPUT SCHEMAS
-------------------------

If INCIDENT:
{{
  "type": "incident",
  "action": "high | medium | low",
  "summary": "short incident description"
}}

If QUESTION:
{{
  "type": "question",
  "answer": "clear and concise explanation"
}}

-------------------------
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

    result = generate_agent(req.prompt)

    parsed = json.loads(result)

    message = (
        parsed.get("message")
        or parsed.get("summary")
        or parsed.get("answer")
    )

    return {
        "response": message
    }