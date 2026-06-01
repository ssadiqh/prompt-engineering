"""Chain-of-thought prompting with LangChain + local Qwen2.5:7b"""
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize local Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

# Chain-of-thought template
template = """Solve this math problem step by step. Show your reasoning for each step.

Problem: {problem}

Let's break it down:
Step 1: Identify what we know
Step 2: Determine what we need to find
Step 3: Work through the solution
Step 4: Verify the answer

Solution:"""

prompt = PromptTemplate(
    input_variables=["problem"],
    template=template
)

# Example problem
problem = "If a train travels 120 miles at 60 mph, how long does the journey take?"
formatted = prompt.format(problem=problem)

print("Chain-of-Thought Prompt:")
print(formatted)
print("\n" + "="*50 + "\n")

# Call Qwen model
response = llm.invoke(formatted)
print("Response:")
print(response)