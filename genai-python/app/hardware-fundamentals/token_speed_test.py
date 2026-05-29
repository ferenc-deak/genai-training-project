context_lengths = [512, 1024, 2048, 4096, 8192]

for ctx in context_lengths:
    time_taken = ctx / 600  # simulated compute time
    tokens_per_sec = ctx / time_taken

    print(f"Context: {ctx} -> Tokens/sec: {tokens_per_sec:.2f}")