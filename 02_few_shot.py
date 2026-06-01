"""Few-shot prompting example - Using local Qwen2.5:7b"""
import requests

# Few-shot examples
examples = """Examples:
Text: The movie was absolutely terrible and boring.
Sentiment: Negative

Text: I loved it! Best film I've seen all year.
Sentiment: Positive

Text: It was okay, nothing special.
Sentiment: Neutral"""

# Create prompt with examples
prompt = f"""{examples}

Text: This product exceeded my expectations!
Sentiment:"""

print("Few-Shot Prompt:")
print(prompt)
print("\n" + "="*50 + "\n")

# Call Qwen model
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()
print("Response:")
print(result["response"])