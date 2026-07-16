from pathlib import Path

print("=" * 60)
print("GENAI PERFORMANCE REPORT")
print("=" * 60)

reports = [
    ("Latency vs Batch Size", "latency_results.txt"),
    ("Throughput vs TTFT", "throughput_results.txt"),
    ("Tokens/sec vs Context Length", "token_speed_results.txt"),
]

for title, filename in reports:

    print(f"\n{title}")
    print("-" * len(title))

    path = Path(filename)

    if path.exists():
        print(path.read_text())
    else:
        print(f"{filename} not found. Run the benchmark first.")

print("\nPerformance Analysis")
print("--------------------")
print("- Larger batch sizes generally increase latency.")
print("- Larger batches improve throughput by utilizing the hardware more efficiently.")
print("- Longer context lengths reduce token generation speed because the model processes more input tokens.")
print("- GPU compute power and memory directly influence all benchmark results.")
print("- There is a trade-off between latency, throughput, and context size depending on the deployment scenario.")