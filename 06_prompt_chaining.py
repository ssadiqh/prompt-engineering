"""Prompt chaining with LangChain + local Qwen2.5:7b"""
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Initialize local Qwen model
llm = OllamaLLM(model="qwen2.5:7b")

# Step 1: Generate a topic idea
print("=== Step 1: Generate Topic ===\n")

step1_template = """Generate a single interesting blog post topic about {subject}.
Return only the topic, nothing else."""

step1_prompt = PromptTemplate(
    input_variables=["subject"],
    template=step1_template
)

step1_formatted = step1_prompt.format(subject="artificial intelligence")
topic = llm.invoke(step1_formatted).strip()
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
outline = llm.invoke(step2_formatted)
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
introduction = llm.invoke(step3_formatted)
print(f"Generated Introduction:\n{introduction}")