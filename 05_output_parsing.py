"""Output parsing with LangChain + local Qwen2.5:7b"""
import json
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize local Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

# Template that requests structured JSON output
template = """Extract the following information from the text and return as JSON:
- name: person's name
- age: person's age
- occupation: what they do
- skills: list of skills

Text: {text}

Return ONLY valid JSON, no other text:"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)

text = """
John Smith is a 35-year-old software engineer with expertise in Python,
JavaScript, and cloud architecture. He has been developing software for 12 years.
"""

formatted = prompt.format(text=text)
print("Parsing Prompt:")
print(formatted)
print("\n" + "="*50 + "\n")

# Call Qwen model
response = llm.invoke(formatted)
print("Raw Response:")
print(response)
print("\n" + "="*50 + "\n")

# Parse the JSON
try:
    parsed = json.loads(response)
    print("Parsed JSON:")
    print(json.dumps(parsed, indent=2))
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")