import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

context_lengths = [512, 1024, 2048, 4096, 8192]

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

print("Device:", device)

context_lengths = [512, 1024, 2048]

def generate_prompt(n_tokens):
    return "hello " * n_tokens

for ctx in context_lengths:
    prompt = generate_prompt(ctx)

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=ctx
    ).to(device)

    start = time.time()

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=50
        )

    end = time.time()

    generated_tokens = output.shape[1] - inputs["input_ids"].shape[1]
    tokens_per_sec = generated_tokens / (end - start)

    print(f"Context: {ctx} -> Tokens/sec: {tokens_per_sec:.2f}")