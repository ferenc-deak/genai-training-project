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
def generate_text(prompt: str):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    return response.choices[0].message.content


# API endpoint
@app.post("/chat")
def chat(req: PromptRequest):
    result = generate_text(req.prompt)
    return {"response": result}