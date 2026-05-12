1. How to run API
   uvicorn app.main:app --reload
2. How to run evaluation
   python evaluate.py
3. How to test reproducibility
   python repro_steps.py

Baseline Engineering Setup

1. I did a Deterministic LLM classifier:
   response = client.chat.completions.create(
   model="meta-llama/Llama-3.1-8B-Instruct",
   messages=[{"role": "user", "content": structured_prompt}],
   max_tokens=300,
   temperature=0
   )
   a. temperature=0 → no randomness
   b. same prompt → same output
   c. same model → same behavior
   structured_prompt = f"""
   You are a strict classification system...
   """ – forces the model to bahave like a classifier
2. Evaluation pipeline:
   with open("eval_dataset.jsonl", "r") as f:
   for line in f:
   sample = json.loads(line)

output = generate_agent(sample["input"])

3. I created a file called repro_test.py and it:
   Demonstrated reproducibility of results
   it was demonstrated by:
   a. repeating the same request
   b. showing identical outputs
   c. proving deterministic behavior
