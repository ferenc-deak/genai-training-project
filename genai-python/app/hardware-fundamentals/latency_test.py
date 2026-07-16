import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

print("Device:", device)

batch_sizes = [1, 2, 4, 8]

results = []

for batch in batch_sizes:

    prompts = ["Explain FastAPI."] * batch

    inputs = tokenizer(
        prompts,
        return_tensors="pt",
        padding=True,
        truncation=True
    ).to(device)

    start = time.time()

    with torch.no_grad():
        model.generate(
            **inputs,
            max_new_tokens=30
        )

    latency = time.time() - start

    line = f"Batch size: {batch} -> Latency: {latency:.3f}s"

    print(line)
    results.append(line)

with open("latency_results.txt", "w") as file:
    file.write("\n".join(results))