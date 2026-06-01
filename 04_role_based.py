"""Role-based prompting example"""
from langchain.prompts import PromptTemplate
from langchain_anthropic import Anthropic

# Role-based template
template = """You are {role}. Your expertise is in {expertise}.

User question: {question}

Respond in a professional manner appropriate for a {role}."""

prompt = PromptTemplate(
    input_variables=["role", "expertise", "question"],
    template=template
)

# Example 1: Data Scientist
print("=== Data Scientist Response ===")
ds_prompt = prompt.format(
    role="Data Scientist",
    expertise="machine learning and statistical analysis",
    question="How would you approach predicting customer churn?"
)
print(ds_prompt)
print("\n")

client = Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=200,
    messages=[{"role": "user", "content": ds_prompt}]
)
print("Response:")
print(response.content[0].text)
print("\n" + "="*50 + "\n")

# Example 2: DevOps Engineer
print("=== DevOps Engineer Response ===")
devops_prompt = prompt.format(
    role="DevOps Engineer",
    expertise="cloud infrastructure and containerization",
    question="How would you approach predicting customer churn?"
)
print(devops_prompt)
print("\n")

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=200,
    messages=[{"role": "user", "content": devops_prompt}]
)
print("Response:")
print(response.content[0].text)
