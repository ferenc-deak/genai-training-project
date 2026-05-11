from app.main import generate_agent

inputs = [
    "Login system is broken",
    "UI typo on homepage",
    "Database is down"
]

for i, prompt in enumerate(inputs):
    print(f"\nINPUT: {prompt}")

    for run in range(3):
        print(f"RUN {run+1}")
        print(generate_agent(prompt))