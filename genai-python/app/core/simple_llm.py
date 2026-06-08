import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from app.core.llm import LLM

load_dotenv()


class SimpleLLM(LLM):

    def __init__(self):
        self.client = InferenceClient(
            api_key=os.getenv("HF_TOKEN")
        )

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.2
        )

        return response.choices[0].message.content.strip()