batch_sizes = [1, 2, 4, 8, 16]

for batch in batch_sizes:
    throughput = batch * 120
    ttft = 100 + batch * 60

    print(f"Batch: {batch} -> Throughput: {throughput}, TTFT: {ttft}ms")