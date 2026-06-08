import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def generate_agent(prompt: str, mode: str = "chat"):
    """
    mode:
    - chat → free text response
    - eval → strict JSON output
    - agent → structured reasoning JSON
    """

    if mode == "eval":
        structured_prompt = f"""
You are a strict classification system.

Return ONLY valid JSON:
{{"action": "low|medium|high"}}

Rules:
- no explanation
- no markdown
- no extra text

Input:
{prompt}
"""

    elif mode == "agent":
        structured_prompt = f"""
You are an AI agent.

Return ONLY valid JSON:
{{
  "action": "analyze|execute|plan",
  "result": "short output"
}}

Input:
{prompt}
"""

    else:
        structured_prompt = f"""
You are a helpful assistant.

Be concise and clear.
No markdown.

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