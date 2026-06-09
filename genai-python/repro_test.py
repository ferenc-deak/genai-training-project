from app.main import generate_agent


inputs = [
    "Login system is broken",
    "UI typo on homepage",
    "Database is down"
]


def normalize(output):
    """
    Extract comparable label from different possible formats
    """
    if isinstance(output, dict):
        output = output.get("action") or output.get("result")

    if output is None:
        return None

    return str(output).strip().lower()


def run_repro_test():
    print("\n🧪 REPRODUCIBILITY TEST START\n")

    failures = 0

    for prompt in inputs:
        print("\nINPUT:", prompt)

        outputs = []

        for run in range(3):
            result = generate_agent(prompt, mode="eval")
            norm = normalize(result)
            outputs.append(norm)

            print(f"RUN {run+1}: {norm}")

        # Check consistency
        consistent = len(set(outputs)) == 1

        print("CONSISTENT:", consistent)
        print("-" * 40)

        if not consistent:
            failures += 1

    print("\nFINAL RESULT")
    print("FAILURES:", failures)
    print("PASSED:", len(inputs) - failures)


if __name__ == "__main__":
    run_repro_test()