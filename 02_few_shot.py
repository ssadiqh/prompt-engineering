"""Few-shot prompting with LangChain + local Qwen2.5:7b"""
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize local Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

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

# Call Qwen model
response = llm.invoke(formatted_prompt)
print("Response:")
print(response)