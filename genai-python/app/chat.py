import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

def generate_agent(prompt: str):
    structured_prompt = f"""
You are a helpful assistant.

Rules:
- Return only plain text
- Be concise
- No markdown

User input:
{prompt}
"""

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[{"role": "user", "content": structured_prompt}],
        max_tokens=300,
        temperature=0.2
    )

    return response.choices[0].message.content.strip()