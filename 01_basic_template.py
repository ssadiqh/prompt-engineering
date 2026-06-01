"""Basic prompt template example - Using local Qwen2.5:7b"""
import requests

# Template
template = """You are a helpful assistant that translates English to {language}.

English: {english_text}
{language}:"""

# Format the template
language = "Spanish"
english_text = "Hello, how are you?"
formatted_prompt = template.format(language=language, english_text=english_text)

print("Formatted Prompt:")
print(formatted_prompt)
print("\n" + "="*50 + "\n")

# Call local Qwen model
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:7b",
        "prompt": formatted_prompt,
        "stream": False
    }
)

result = response.json()
print("Response from Qwen2.5:7b:")
print(result["response"])