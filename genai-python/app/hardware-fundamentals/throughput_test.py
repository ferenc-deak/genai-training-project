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
        outputs = model.generate(
            **inputs,
            max_new_tokens=30
        )

    end = time.time()

    elapsed = end - start

    generated_tokens = outputs.shape[1] - inputs["input_ids"].shape[1]

    throughput = (generated_tokens * batch) / elapsed
    ttft = elapsed * 1000

    line = (
        f"Batch: {batch} -> "
        f"Throughput: {throughput:.2f} tokens/sec, "
        f"TTFT: {ttft:.2f} ms"
    )

    print(line)
    results.append(line)

with open("throughput_results.txt", "w") as file:
    file.write("\n".join(results))