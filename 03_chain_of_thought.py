"""Chain-of-thought prompting example - Using local Qwen2.5:7b"""
import requests

# Chain-of-thought template
template = """Solve this math problem step by step. Show your reasoning for each step.

Problem: {problem}

Let's break it down:
Step 1: Identify what we know
Step 2: Determine what we need to find
Step 3: Work through the solution
Step 4: Verify the answer

Solution:"""

# Example problem
problem = "If a train travels 120 miles at 60 mph, how long does the journey take?"
formatted = template.format(problem=problem)

print("Chain-of-Thought Prompt:")
print(formatted)
print("\n" + "="*50 + "\n")

# Call Qwen model
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:7b",
        "prompt": formatted,
        "stream": False
    }
)

result = response.json()
print("Response:")
print(result["response"])