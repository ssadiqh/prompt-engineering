"""Basic prompt template example with LangChain"""
from langchain.prompts import PromptTemplate
from langchain_anthropic import Anthropic

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

# Use with Claude
client = Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=100,
    messages=[{"role": "user", "content": formatted_prompt}]
)
print("Response:")
print(response.content[0].text)
