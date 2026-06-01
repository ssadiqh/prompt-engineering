"""Test local Qwen2.5:7b model with LangChain"""
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize Ollama with Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

print("="*60)
print("Testing Local Qwen2.5:7b Model")
print("="*60)

# Test 1: Basic prompt
print("\n1. BASIC PROMPT TEST")
print("-" * 60)
basic_template = "What are the top 3 benefits of {technology}?"
basic_prompt = PromptTemplate(
    input_variables=["technology"],
    template=basic_template
)
formatted = basic_prompt.format(technology="Python")
response = llm.invoke(formatted)
print(f"Q: {formatted}")
print(f"A: {response}\n")

# Test 2: Few-shot example
print("2. FEW-SHOT PROMPTING TEST")
print("-" * 60)
few_shot = """Examples:
Input: sunny
Output: happy, energetic

Input: rainy
Output: calm, peaceful

Input: cloudy
Output:"""

response = llm.invoke(few_shot)
print(f"Few-shot response: {response}\n")

# Test 3: Math problem with chain-of-thought
print("3. CHAIN-OF-THOUGHT TEST")
print("-" * 60)
cot = """Solve this step by step:
If you have 5 apples and buy 3 more, then eat 2, how many apples do you have?

Step 1: Start with
Step 2: Add
Step 3: Subtract
Answer:"""

response = llm.invoke(cot)
print(f"Response:\n{response}\n")

# Test 4: Role-based
print("4. ROLE-BASED TEST")
print("-" * 60)
role = """You are a pirate. Explain what an API is in pirate speak."""
response = llm.invoke(role)
print(f"Response:\n{response}\n")

# Test 5: JSON output
print("5. STRUCTURED OUTPUT TEST")
print("-" * 60)
json_prompt = """Return this information as JSON:
Name: Alice
Age: 30
Job: Engineer

JSON:"""
response = llm.invoke(json_prompt)
print(f"Response:\n{response}")
