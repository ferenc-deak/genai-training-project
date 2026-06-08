from app.core.llm import LLM

class SimpleLLM(LLM):

    def generate(self, prompt: str) -> str:
        # replace this with YOUR actual LLM call (Ollama, HF, etc.)
        return "mock response"