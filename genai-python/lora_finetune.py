import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, TaskType

model_name = "microsoft/phi-3-mini-4k-instruct"
dataset_path = "dataset.jsonl"

print("CUDA available:", torch.cuda.is_available())

dataset = load_dataset(
    "json",
    data_files=dataset_path,
    split="train"
)

print("COLUMNS:", dataset.column_names)
print("SAMPLE:", dataset[0])

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

def tokenize(example):
    # format instruction + answer
    text = f"Instruction: {example['instruction']}\nAnswer: {example['output']}"

    tokens = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128
    )

    tokens["labels"] = tokens["input_ids"].copy()
    return tokens


tokenized_dataset = dataset.map(tokenize)

tokenized_dataset = tokenized_dataset.remove_columns(
    ["instruction", "output"]
)


model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True
)

# ----------------------------
# 6. LoRA config (Phi-3 compatible)
# ----------------------------
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,

    target_modules=["o_proj"]
)

model = get_peft_model(model, lora_config)

print("Trainable parameters enabled (LoRA applied)")


training_args = TrainingArguments(
    output_dir="./lora-output",
    per_device_train_batch_size=1,
    num_train_epochs=1,
    logging_steps=10,
    save_steps=50,
    save_total_limit=2,
    report_to="none",

    fp16=False,          # CPU-safe
    bf16=False           # extra safety for older versions
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=data_collator
)


if __name__ == "__main__":
    print("🚀 Starting LoRA training...")
    trainer.train()

    print("💾 Saving model...")
    model.save_pretrained("./lora-model")
    tokenizer.save_pretrained("./lora-model")

    print("✅ Done")