import time

batch_sizes = [1, 2, 4, 8, 16]

for batch in batch_sizes:
    start = time.time()
    time.sleep(0.1 * batch)  # simulated workload
    latency = time.time() - start

    print(f"Batch size: {batch} -> Latency: {latency:.3f}s")