print("""
GENAI PERFORMANCE REPORT

1. Latency increases with batch size because more requests are processed together.

2. Tokens/sec decreases as context length increases due to higher attention cost.

3. Throughput increases with batch size because GPU utilization improves.

4. TTFT increases with batch size because the system waits longer before first output.

TRADE-OFFS:
- Bigger batch = higher throughput but slower response
- Longer context = better understanding but slower generation
- Hardware limits (GPU memory + compute) affect everything
""")