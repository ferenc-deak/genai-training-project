import json
from app.main import generate_agent


def normalize_label(value):
    """
    Converts model output into one of: low / medium / high / None
    """
    if value is None:
        return None

    text = str(value).strip().lower()

    if "low" in text:
        return "low"
    if "medium" in text:
        return "medium"
    if "high" in text:
        return "high"

    return None


def parse_output(output):
    """
    Safely converts model output into a dict-like structure.
    Handles:
    - dict output
    - JSON string output
    - plain text output
    """
    if isinstance(output, dict):
        return output

    if isinstance(output, str):
        try:
            return json.loads(output)
        except Exception:
            return {"action": output}

    return {"action": None}


def evaluate():
    correct = 0
    total = 0

    with open("eval_dataset.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            sample = json.loads(line)

            output = generate_agent(sample["input"], mode="eval")

            output = parse_output(output)

            raw_pred = (
                output.get("action")
                or output.get("result")
                or output.get("label")
            )

            predicted = normalize_label(raw_pred)
            expected = sample["expected"]

            is_correct = predicted == expected

            print("INPUT:", sample["input"])
            print("EXPECTED:", expected)
            print("PREDICTED:", predicted)
            print("RAW:", output)
            print("CORRECT:", is_correct)
            print("-" * 40)

            total += 1
            if is_correct:
                correct += 1

    accuracy = correct / total if total > 0 else 0
    print("\nFINAL ACCURACY:", accuracy)


if __name__ == "__main__":
    evaluate()