import json
from app.main import generate_agent

def evaluate():

    correct = 0
    total = 0

    with open("eval_dataset.jsonl", "r") as f:

        for line in f:
            sample = json.loads(line)

            output = generate_agent(sample["input"], mode="eval")

            # 🔥 FIX: ensure dict format
            if isinstance(output, str):
                try:
                    output = json.loads(output)
                except:
                    output = {"action": None}

            predicted = output.get("action")
            expected = sample["expected"]

            is_correct = predicted == expected

            print("INPUT:", sample["input"])
            print("EXPECTED:", expected)
            print("PREDICTED:", predicted)
            print("CORRECT:", is_correct)
            print("-" * 40)

            total += 1
            if is_correct:
                correct += 1

    print("\nFINAL ACCURACY:", correct / total if total > 0 else 0)


if __name__ == "__main__":
    evaluate()