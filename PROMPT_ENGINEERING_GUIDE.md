# LangChain Prompt Engineering Examples

This guide covers practical prompt engineering techniques using LangChain with Claude.

## Setup

```bash
pip install -r requirements.txt
```

Set your API key:
```bash
$env:ANTHROPIC_API_KEY = "your-api-key"
```

## Examples Overview

### 1. **Basic Template** (`01_basic_template.py`)
Simple prompt template with variable substitution.

**Key Concepts:**
- `PromptTemplate`: Create reusable prompts with variables
- `input_variables`: Define placeholders in your template
- Format and pass to Claude

**Use Case:** Translation, simple text transformation, templated responses

---

### 2. **Few-Shot Prompting** (`02_few_shot.py`)
Provide examples to guide model behavior.

**Key Concepts:**
- `FewShotPromptTemplate`: Include example input/output pairs
- Models learn from examples to follow patterns
- Better consistency and accuracy

**Use Case:** Sentiment analysis, classification tasks, formatting

---

### 3. **Chain-of-Thought** (`03_chain_of_thought.py`)
Ask the model to show reasoning step-by-step.

**Key Concepts:**
- Explicit step-by-step breakdown
- Improves accuracy on complex reasoning
- Model shows work, not just answers

**Use Case:** Math problems, analysis, debugging, complex logic

---

### 4. **Role-Based Prompting** (`04_role_based.py`)
Assign roles and expertise to customize responses.

**Key Concepts:**
- Set context with `role` and `expertise`
- Same question, different perspectives
- Tailor tone and depth

**Use Case:** Getting expert opinions, domain-specific advice, content for different audiences

---

### 5. **Output Parsing** (`05_output_parsing.py`)
Request structured output (JSON) for programmatic use.

**Key Concepts:**
- Instruct model to return valid JSON
- Parse response for downstream processing
- Structured data for automation

**Use Case:** Data extraction, form filling, API responses

---

### 6. **Prompt Chaining** (`06_prompt_chaining.py`)
Use output from one prompt as input to another.

**Key Concepts:**
- Multi-step workflows
- Each step refines the result
- Build complex tasks from simple prompts

**Use Case:** Blog writing, creative projects, content generation workflows

---

## Running Examples

```bash
python 01_basic_template.py
python 02_few_shot.py
python 03_chain_of_thought.py
python 04_role_based.py
python 05_output_parsing.py
python 06_prompt_chaining.py
```

## Key Prompt Engineering Principles

1. **Be Specific**: Clear, detailed instructions produce better results
2. **Show Examples**: Few-shot prompting improves consistency
3. **Break It Down**: Chain-of-thought for complex reasoning
4. **Set Context**: Roles and expertise guide the tone and depth
5. **Structure Output**: Request JSON/specific formats for automation
6. **Iterate**: Test and refine based on results

## Tips for Better Prompts

- **Start with role/context**: "You are a..." sets expectations
- **Use delimiters**: Use `---` or `###` to separate prompt sections
- **Be explicit about format**: "Return as JSON", "Use bullet points"
- **Provide constraints**: "In under 100 words", "Using simple language"
- **Chain prompts**: Break complex tasks into steps
- **Test variations**: Small wording changes can significantly impact results

## Further Reading

- [LangChain Documentation](https://python.langchain.com/)
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/en/introduction-to-prompt-engineering)
- [Few-Shot Prompting](https://python.langchain.com/docs/modules/model_io/prompts/examples/few_shot_examples)
