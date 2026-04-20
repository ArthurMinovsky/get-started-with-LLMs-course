# n8n — Getting Started with AI Automation

## What is n8n?

**n8n** (pronounced "n-eight-n" or "nodemation") is an open-source **workflow automation platform** that allows you to connect apps, services, and AI models to automate tasks without extensive coding.

n8n is particularly powerful for building **AI-powered workflows** — connecting LLMs like ChatGPT, Claude, and Gemini to real-world data sources, APIs, and services to create intelligent automation pipelines.

## n8n vs Other Automation Tools

| Feature | n8n | Zapier | Make (Integromat) |
|---------|-----|--------|-------------------|
| **Open Source** | ✅ | ❌ | ❌ |
| **Self-Hosted** | ✅ | ❌ | ❌ |
| **AI/LLM Integration** | ✅ Built-in | Limited | Limited |
| **Code Execution** | ✅ (JS/Python) | ❌ | Limited |
| **Free Tier** | ✅ Self-host | Limited | Limited |
| **Visual Builder** | ✅ | ✅ | ✅ |

## Access Options

| Option | Description | Best For |
|--------|-------------|----------|
| **n8n Cloud** | Hosted by n8n, free trial available | Getting started quickly |
| **Self-Hosted (Docker)** | Run on your own server | Full control, no usage limits |
| **Self-Hosted (npm)** | Install via Node.js | Development/testing |
| **Desktop App** | Local installation | Local development |

## Getting Started

### Option A — n8n Cloud (Quickest Start)
1. Go to [https://n8n.io](https://n8n.io)
2. Click **"Get started for free"**
3. Create an account
4. You'll get a free trial with full features

### Option B — Self-Hosted with Docker
```bash
# Pull and run n8n with Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```
Then open `http://localhost:5678` in your browser.

### Option C — Install with npm
```bash
npm install n8n -g
n8n start
```

## The n8n Interface

### Workflow Canvas
- **Nodes**: Individual building blocks that perform specific actions
- **Connections**: Arrows connecting nodes to define data flow
- **Trigger Node**: Every workflow starts with a trigger (e.g., a webhook, schedule, or form)

### Building Your First Workflow

1. Click **"New Workflow"**
2. Click the **"+"** button to add a trigger node (e.g., "Manual Trigger" for testing)
3. Connect action nodes by clicking the **"+"** on a node's right side
4. Configure each node with credentials and settings
5. Click **"Execute Workflow"** to test
6. Click **"Save"** and **"Activate"** to run automatically

## AI Nodes in n8n

### AI Agent Node
The most powerful AI feature — create autonomous AI agents that can:
- Reason about tasks
- Use tools (web search, databases, APIs)
- Make decisions and loop until a goal is achieved

### LLM Integration Nodes
| Node | Service | Capability |
|------|---------|------------|
| **OpenAI** | ChatGPT/GPT-4 | Text generation, embeddings |
| **Anthropic** | Claude | Text generation, analysis |
| **Google Gemini** | Gemini models | Multimodal AI |
| **Ollama** | Local models | Self-hosted AI (privacy) |
| **Hugging Face** | Open models | Various AI tasks |

### AI Tool Nodes
These give AI agents the ability to take actions:
- **Calculator**: Math operations
- **Wikipedia**: Knowledge lookup
- **SerpAPI**: Google Search
- **HTTP Request**: Call any API
- **Code**: Run custom JavaScript or Python

## Common n8n + AI Workflow Patterns

### Pattern 1 — AI Email Responder
```
Gmail Trigger → OpenAI (classify/respond) → Gmail (send reply)
```
Automatically classify incoming emails and draft AI-generated responses.

### Pattern 2 — Document Summarizer
```
Google Drive (new file) → Extract Text → Claude → Slack (send summary)
```
When a new document is added to Drive, summarize it and post to Slack.

### Pattern 3 — Customer Support Bot
```
Webhook → AI Agent → [Search Knowledge Base, Create Ticket] → Respond
```
Build a support bot that searches your documentation and creates tickets automatically.

### Pattern 4 — Social Media Content Generator
```
Schedule (daily) → OpenAI (generate post) → Buffer/Twitter (publish)
```
Automatically generate and publish social media content on a schedule.

### Pattern 5 — Data Enrichment Pipeline
```
CRM Trigger → Clearbit (enrich) → Claude (analyze) → CRM (update)
```
Enrich CRM data with AI-powered analysis.

## Building an AI Agent in n8n

An **AI Agent** in n8n is a workflow where an LLM can:
1. Receive a task
2. Decide which tools to use
3. Execute tools
4. Evaluate results
5. Repeat until the task is complete

### Step-by-Step: Simple Research Agent

1. Add an **AI Agent** node
2. Set the **Model**: Choose OpenAI GPT-4 or Claude
3. Add **Tools**:
   - Wikipedia Tool (for general knowledge)
   - HTTP Request Tool (for web data)
4. Write a **System Message**: "You are a research assistant. Use available tools to answer questions thoroughly."
5. Add an input (Manual Trigger or Webhook)
6. Test by asking: "What were the major AI developments in 2024?"

## Credentials Setup

Most nodes require credentials/API keys:

| Service | Where to Get Key |
|---------|-----------------|
| **OpenAI** | platform.openai.com/api-keys |
| **Anthropic** | console.anthropic.com |
| **Google Gemini** | aistudio.google.com/apikey |
| **Slack** | api.slack.com |
| **Gmail** | OAuth via Google Cloud Console |

### Adding Credentials in n8n
1. Click on a node
2. Click **"Create new credential"**
3. Enter your API key or follow the OAuth flow
4. Credentials are stored securely and reused across workflows

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Node** | A single step in a workflow (e.g., Send Email, Call API) |
| **Workflow** | A series of connected nodes |
| **Trigger** | The event that starts a workflow |
| **Execution** | One run of a workflow |
| **Expression** | Dynamic values using `{{ }}` syntax |
| **Memory** | Store conversation history for AI agents |
| **Vector Store** | Database for semantic search (RAG) |

## Example: Prompting n8n's AI Agent

```
System Message:
You are a helpful customer service agent for TechCorp.
You have access to these tools:
- search_knowledge_base: Search our product documentation
- create_ticket: Create a support ticket
- check_order_status: Look up order status

Always be polite and professional. If you cannot resolve an issue,
create a support ticket.
```

## Tips and Best Practices

1. **Start simple** — Build with Manual Trigger first, add automation later
2. **Use Error Workflows** — Set up error handling to catch failures
3. **Test incrementally** — Test each node before connecting the full chain
4. **Use expressions** — Reference data from previous nodes with `{{ $json.fieldName }}`
5. **Version control** — Export workflows as JSON and save in git
6. **Monitor executions** — Check the Executions log regularly
7. **Rate limiting** — Be mindful of API rate limits when processing many items

## References

- [n8n Official Site](https://n8n.io)
- [n8n Documentation](https://docs.n8n.io)
- [n8n Community Forum](https://community.n8n.io)
- [n8n GitHub Repository](https://github.com/n8n-io/n8n)
- [n8n AI Documentation](https://docs.n8n.io/advanced-ai/)
- [n8n Workflow Templates](https://n8n.io/workflows/)
