# Claude — Getting Started

## What is Claude?

**Claude** is an AI assistant developed by **Anthropic**, an AI safety company founded in 2021 by former OpenAI researchers. Claude is designed with a strong emphasis on being **helpful, harmless, and honest**.

Claude is known for its exceptional ability to handle very long documents, nuanced reasoning, and careful, thoughtful responses.

## Available Models

| Model | Context Window | Key Strengths |
|-------|---------------|---------------|
| **Claude 3 Haiku** | 200K tokens | Fast, lightweight tasks |
| **Claude 3 Sonnet** | 200K tokens | Balanced performance |
| **Claude 3.5 Sonnet** | 200K tokens | Best coding & reasoning |
| **Claude 3 Opus** | 200K tokens | Most capable, complex tasks |

> **200K token context window** = roughly 150,000 words — enough to analyze an entire book in one session!

## Available Plans

| Plan | Access | Features |
|------|--------|----------|
| **Free** | claude.ai | Limited daily messages |
| **Pro** ($20/month) | claude.ai | 5× more usage, priority access |
| **Team** ($25/user/month) | claude.ai | Collaboration features |
| **API** | api.anthropic.com | Programmatic access |

## Getting Started

### Step 1 — Access Claude
1. Go to [https://claude.ai](https://claude.ai)
2. Sign up with your email or Google account
3. Start chatting immediately on the free tier

### Step 2 — Start a Conversation
1. Type your message in the chat box
2. Attach files (PDFs, Word docs, images, code files) if needed
3. Claude responds with thoughtful, detailed answers

### Step 3 — Explore Projects
**Projects** (Pro feature) let you:
- Give Claude a persistent **system prompt** for a specific purpose
- Upload reference documents that Claude keeps in context
- Maintain ongoing work across multiple conversations

## Key Features

### Long Document Analysis
Claude's 200K token context window lets you:
- Upload an entire research paper and ask detailed questions
- Analyze long contracts or legal documents
- Summarize and compare multiple documents at once

**Example**: Upload a 100-page PDF and ask:
> "What are the three most important findings in this research paper? List any limitations the authors mention."

### Code Generation and Review
Claude excels at software development tasks:
- Writing code in Python, JavaScript, TypeScript, Go, and more
- Reviewing code for bugs and security issues
- Explaining complex codebases
- Converting code between programming languages

### Writing and Editing
- Drafting professional documents, essays, and reports
- Editing for clarity, tone, and grammar
- Matching specific writing styles

### Artifacts
Claude can create **Artifacts** — interactive content displayed alongside the conversation:
- Rendered HTML/CSS/JavaScript code
- SVG diagrams
- Markdown documents
- Spreadsheet-like tables

## Anthropic's Safety Approach

Anthropic uses a technique called **Constitutional AI (CAI)** to train Claude:
1. Claude is given a set of principles (a "constitution")
2. Claude learns to evaluate and revise its own responses based on these principles
3. This makes Claude less likely to produce harmful content

Claude is also trained to **express uncertainty** rather than confidently stating incorrect information.

## Common Use Cases

| Use Case | Example Prompt |
|----------|---------------|
| Document Analysis | "Here is a research paper [paste text]. Summarize it and identify the key claims." |
| Coding | "Review this Python code for bugs and suggest improvements: [code]" |
| Long-form Writing | "Write a 1,500-word blog post about the benefits of remote work" |
| Data Extraction | "Extract all dates, names, and amounts from this contract: [text]" |
| Learning | "Explain transformer architecture from first principles" |
| Debate Prep | "Give me the strongest arguments for and against universal basic income" |

## Tips and Best Practices

1. **Use Projects** — Set up a system prompt to define Claude's role for recurring tasks
2. **Upload documents directly** — Claude handles PDFs, Word docs, and code files natively
3. **Ask for reasoning** — "Think step by step before answering"
4. **Request multiple options** — "Give me three different approaches to this problem"
5. **Be explicit about length** — "Answer in one paragraph" or "Give a detailed explanation"

## Limitations

- **No real-time internet access** by default (Claude.ai has some web search capability)
- **Knowledge cutoff**: Training data has a cutoff date
- **No image generation**: Claude can analyze images but cannot create them
- **Hallucination**: Like all LLMs, Claude can occasionally generate incorrect information

## References

- [Claude Official Site](https://claude.ai)
- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude Model Overview](https://docs.anthropic.com/en/docs/about-claude/models)
- [Constitutional AI Paper](https://arxiv.org/abs/2212.08073)
- [Anthropic's Claude Usage Policy](https://www.anthropic.com/legal/usage-policy)
