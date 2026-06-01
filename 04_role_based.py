"""Role-based prompting with LangChain + local Qwen2.5:7b"""
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize local Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

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

response = llm.invoke(ds_prompt)
print("Response:")
print(response)
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

response = llm.invoke(devops_prompt)
print("Response:")
print(response)