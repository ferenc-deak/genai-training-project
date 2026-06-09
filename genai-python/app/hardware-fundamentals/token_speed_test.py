import time

context_lengths = [512, 1024, 2048, 4096, 8192]

# simulate "1 token step cost"
# (replace this later with real model forward pass)
def simulate_token_step():
    x = 0
    for _ in range(1000):
        x += _ * 2
    return x

for ctx in context_lengths:
    start = time.time()

    # simulate processing ctx tokens
    for _ in range(ctx):
        simulate_token_step()

    end = time.time()

    time_taken = end - start
    tokens_per_sec = ctx / time_taken

    print(f"Context: {ctx} -> Tokens/sec: {tokens_per_sec:.2f}")