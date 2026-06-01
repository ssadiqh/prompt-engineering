"""Prompt chaining - using output from one prompt as input to another - Using Qwen2.5:7b"""
import requests

def call_qwen(prompt):
    """Helper function to call Qwen model"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:7b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

# Step 1: Generate a topic idea
print("=== Step 1: Generate Topic ===\n")

step1_template = """Generate a single interesting blog post topic about {subject}.
Return only the topic, nothing else."""

step1_prompt = step1_template.format(subject="artificial intelligence")
print(step1_prompt)
topic = call_qwen(step1_prompt)
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

step2_prompt = step2_template.format(topic=topic)
print(step2_prompt)
outline = call_qwen(step2_prompt)
print(f"Generated Outline:\n{outline}\n")

# Step 3: Write the introduction
print("="*50)
print("=== Step 3: Write Introduction ===\n")

step3_template = """Write a compelling 2-3 sentence introduction for a blog post with this topic: {topic}

Outline:
{outline}

Make it engaging and set up the main points."""

step3_prompt = step3_template.format(topic=topic, outline=outline)
print(step3_prompt)
introduction = call_qwen(step3_prompt)
print(f"Generated Introduction:\n{introduction}")