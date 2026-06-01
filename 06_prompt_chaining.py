"""Prompt chaining - using output from one prompt as input to another"""
from langchain.prompts import PromptTemplate
from langchain_anthropic import Anthropic

client = Anthropic()

# Step 1: Generate a topic idea
print("=== Step 1: Generate Topic ===\n")

step1_template = """Generate a single interesting blog post topic about {subject}.
Return only the topic, nothing else."""

step1_prompt = PromptTemplate(
    input_variables=["subject"],
    template=step1_template
)

step1_formatted = step1_prompt.format(subject="artificial intelligence")
response1 = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=100,
    messages=[{"role": "user", "content": step1_formatted}]
)
topic = response1.content[0].text.strip()
print(f"Generated Topic: {topic}\n")

# Step 2: Create an outline based on the topic
print("="*50)
print("=== Step 2: Create Outline ===\n")

step2_template = """Create a detailed outline for a blog post with this topic: {topic}

Include:
1. Introduction point
2. Three main sections
3. Conclusion point

Format as a numbered list."""

step2_prompt = PromptTemplate(
    input_variables=["topic"],
    template=step2_template
)

step2_formatted = step2_prompt.format(topic=topic)
response2 = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=200,
    messages=[{"role": "user", "content": step2_formatted}]
)
outline = response2.content[0].text
print(f"Generated Outline:\n{outline}\n")

# Step 3: Write the introduction
print("="*50)
print("=== Step 3: Write Introduction ===\n")

step3_template = """Write a compelling 2-3 sentence introduction for a blog post with this topic: {topic}

Outline:
{outline}

Make it engaging and set up the main points."""

step3_prompt = PromptTemplate(
    input_variables=["topic", "outline"],
    template=step3_template
)

step3_formatted = step3_prompt.format(topic=topic, outline=outline)
response3 = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=150,
    messages=[{"role": "user", "content": step3_formatted}]
)
introduction = response3.content[0].text
print(f"Generated Introduction:\n{introduction}")
