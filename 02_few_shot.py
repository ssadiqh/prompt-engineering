"""Few-shot prompting example with LangChain"""
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_anthropic import Anthropic

# Define examples
examples = [
    {
        "input": "The movie was absolutely terrible and boring.",
        "output": "Negative"
    },
    {
        "input": "I loved it! Best film I've seen all year.",
        "output": "Positive"
    },
    {
        "input": "It was okay, nothing special.",
        "output": "Neutral"
    },
]

# Create the example prompt
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Text: {input}\nSentiment: {output}"
)

# Create few-shot prompt template
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Text: {text}\nSentiment:",
    input_variables=["text"]
)

# Format with new input
test_text = "This product exceeded my expectations!"
formatted_prompt = prompt.format(text=test_text)
print("Few-Shot Prompt:")
print(formatted_prompt)
print("\n" + "="*50 + "\n")

# Call Claude
client = Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=10,
    messages=[{"role": "user", "content": formatted_prompt}]
)
print("Response:")
print(response.content[0].text)
