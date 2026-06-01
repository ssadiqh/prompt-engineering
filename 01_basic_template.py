"""Basic prompt template example with LangChain + local Qwen2.5:7b"""
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize local Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

# Create a simple prompt template
template = """You are a helpful assistant that translates English to {language}.

English: {english_text}
{language}:"""

prompt = PromptTemplate(
    input_variables=["language", "english_text"],
    template=template
)

# Format the prompt
formatted_prompt = prompt.format(language="Spanish", english_text="Hello, how are you?")
print("Formatted Prompt:")
print(formatted_prompt)
print("\n" + "="*50 + "\n")

# Use with local Qwen model
response = llm.invoke(formatted_prompt)
print("Response from Qwen2.5:7b:")
print(response)