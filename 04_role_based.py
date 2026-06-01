"""Role-based prompting example - Using local Qwen2.5:7b"""
import requests

# Role-based template
template = """You are {role}. Your expertise is in {expertise}.

User question: {question}

Respond in a professional manner appropriate for a {role}."""

# Example 1: Data Scientist
print("=== Data Scientist Response ===")
ds_prompt = template.format(
    role="Data Scientist",
    expertise="machine learning and statistical analysis",
    question="How would you approach predicting customer churn?"
)
print(ds_prompt)
print("\n")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:7b",
        "prompt": ds_prompt,
        "stream": False
    }
)

result = response.json()
print("Response:")
print(result["response"])
print("\n" + "="*50 + "\n")

# Example 2: DevOps Engineer
print("=== DevOps Engineer Response ===")
devops_prompt = template.format(
    role="DevOps Engineer",
    expertise="cloud infrastructure and containerization",
    question="How would you approach predicting customer churn?"
)
print(devops_prompt)
print("\n")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:7b",
        "prompt": devops_prompt,
        "stream": False
    }
)

result = response.json()
print("Response:")
print(result["response"])