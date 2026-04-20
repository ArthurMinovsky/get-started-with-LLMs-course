# n8n Workflow Examples

Ready-to-understand workflow blueprints for common AI automation use cases.
These examples describe the logic and node configuration for each workflow.

---

## Workflow 1 — AI Email Classifier and Auto-Responder

### Purpose
Automatically classify incoming emails and draft AI-powered responses.

### Flow
```
[Gmail Trigger] → [OpenAI: Classify] → [IF: Urgent?] → [OpenAI: Draft Reply] → [Gmail: Send]
                                                      ↘ [Slack: Alert Team]
```

### Node Configuration

#### Node 1: Gmail Trigger
- **Trigger**: "New Email" event
- **Filters**: Unread emails in Inbox

#### Node 2: OpenAI — Classify Email
- **Model**: gpt-4o-mini
- **Prompt**:
```
Classify this email into one of these categories:
- URGENT: Requires response within 1 hour
- STANDARD: Requires response within 24 hours
- NEWSLETTER: Marketing/newsletter, no response needed
- SPAM: Unwanted email

Email Subject: {{ $json.subject }}
Email Body: {{ $json.snippet }}

Respond with ONLY the category name.
```

#### Node 3: IF — Check if Urgent
- **Condition**: `{{ $json.message.content }}` equals `URGENT`

#### Node 4: OpenAI — Draft Reply (runs if URGENT)
- **Model**: gpt-4o
- **Prompt**:
```
Draft a professional email reply to this message.
Be helpful, concise, and ask for any needed clarification.

Original email:
Subject: {{ $('Gmail Trigger').item.json.subject }}
Body: {{ $('Gmail Trigger').item.json.snippet }}
```

#### Node 5: Gmail — Send Reply
- **To**: `{{ $('Gmail Trigger').item.json.from.email }}`
- **Subject**: `Re: {{ $('Gmail Trigger').item.json.subject }}`
- **Body**: `{{ $json.message.content }}`

---

## Workflow 2 — Document Summarizer to Slack

### Purpose
When a new PDF is added to Google Drive, summarize it with AI and post to Slack.

### Flow
```
[Google Drive Trigger] → [Google Drive: Download] → [Extract Text] → [Claude: Summarize] → [Slack: Post]
```

### Node Configuration

#### Node 1: Google Drive Trigger
- **Event**: File created
- **Folder**: /Team Documents/Incoming

#### Node 2: Google Drive — Download File
- **File ID**: `{{ $json.id }}`

#### Node 3: Extract Text from PDF
- Use the **PDF Extract** node or HTTP request to a PDF parsing service

#### Node 4: Anthropic Claude — Summarize
- **Model**: claude-3-5-sonnet-20241022
- **System**: "You are an expert document summarizer."
- **Prompt**:
```
Please summarize this document with:
1. A 2-sentence overview
2. 5 key bullet points
3. Any action items or deadlines mentioned

Document content:
{{ $json.text }}
```

#### Node 5: Slack — Post Message
- **Channel**: #document-summaries
- **Message**:
```
📄 *New Document Summary*
*File*: {{ $('Google Drive Trigger').item.json.name }}
*Added by*: {{ $('Google Drive Trigger').item.json.owners[0].displayName }}

{{ $json.content[0].text }}
```

---

## Workflow 3 — AI Customer Support Agent

### Purpose
Answer customer support questions using a knowledge base, create tickets for complex issues.

### Flow
```
[Webhook] → [AI Agent] → [Tools: Search KB / Create Ticket] → [Respond]
```

### Node Configuration

#### Node 1: Webhook
- **Method**: POST
- **Path**: /support
- **Response Mode**: Last node

#### Node 2: AI Agent
- **Model**: OpenAI GPT-4o
- **System Message**:
```
You are a helpful customer support agent for TechCorp.

You have access to these tools:
- search_knowledge_base: Search product documentation
- create_support_ticket: Create a ticket for complex issues

Always:
1. Try to answer from the knowledge base first
2. If the issue is complex or requires human intervention, create a ticket
3. Be empathetic and professional
4. Confirm the customer's issue is resolved before ending
```
- **Tools**: Knowledge Base Search, Create Ticket
- **Input**: `{{ $json.body.message }}`

#### Node 3: Respond to Webhook
- **Response**: `{{ $json.output }}`

---

## Workflow 4 — Daily News Summary

### Purpose
Every morning, fetch top news, summarize with AI, and send via email.

### Flow
```
[Schedule Trigger] → [HTTP: Fetch News API] → [OpenAI: Summarize] → [Gmail: Send Email]
```

### Node Configuration

#### Node 1: Schedule Trigger
- **Trigger at**: 7:00 AM every weekday

#### Node 2: HTTP Request — News API
- **URL**: `https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY`
- **Method**: GET

#### Node 3: Code Node — Format Articles
```javascript
const articles = $input.item.json.articles.slice(0, 10);
const formatted = articles.map(a => 
  `Title: ${a.title}\nSource: ${a.source.name}\nDescription: ${a.description}`
).join('\n\n---\n\n');

return { articles: formatted, count: articles.length };
```

#### Node 4: OpenAI — Generate Summary
- **Prompt**:
```
Here are today's top {{ $json.count }} news stories. 
Please create a concise morning briefing with:
- 3-sentence overview of the biggest story
- Brief bullets for the other stories
- Any notable trends across stories

News articles:
{{ $json.articles }}
```

#### Node 5: Gmail — Send Morning Briefing
- **To**: your-email@example.com
- **Subject**: `🗞️ Your AI Morning Briefing — {{ $today }}`
- **Body**: HTML formatted version of the summary

---

## Workflow 5 — Social Media Content Generator

### Purpose
Generate and schedule social media posts automatically on a schedule.

### Flow
```
[Schedule] → [Airtable: Get Topic] → [OpenAI: Generate Post] → [Buffer: Schedule Post]
```

### Node Configuration

#### Node 1: Schedule Trigger
- **Trigger at**: 9:00 AM daily

#### Node 2: Airtable — Get Today's Topic
- **Table**: Content Calendar
- **Filter**: Status = "Ready to Publish" AND Scheduled Date = Today

#### Node 3: OpenAI — Generate Social Post
- **Prompt**:
```
Write a LinkedIn post about the following topic. 

Requirements:
- Length: 150-200 words
- Tone: Professional but conversational
- Include 3-5 relevant hashtags at the end
- End with a question to encourage engagement
- Do NOT use emojis in the main text

Topic: {{ $json.fields.Topic }}
Key points to include: {{ $json.fields.KeyPoints }}
Target audience: {{ $json.fields.Audience }}
```

#### Node 4: Buffer — Create Post
- **Profile**: LinkedIn
- **Text**: `{{ $json.choices[0].message.content }}`
- **Scheduled at**: `{{ $('Airtable').item.json.fields.ScheduledDate }}T10:00:00`

---

## n8n Expressions Quick Reference

| Expression | Output |
|-----------|--------|
| `{{ $json.fieldName }}` | Value of a field from current node |
| `{{ $('Node Name').item.json.field }}` | Value from a specific previous node |
| `{{ $now }}` | Current timestamp |
| `{{ $today }}` | Today's date |
| `{{ $runIndex }}` | Current run index in a loop |
| `{{ $input.all() }}` | All items from the input |
| `{{ $json.array.length }}` | Length of an array |
| `{{ $json.text.toUpperCase() }}` | Uppercase string |
| `{{ $json.number + 10 }}` | Math operation |

---

## Exporting and Importing Workflows

Workflows can be exported as JSON and version-controlled in git:

1. Open a workflow in n8n
2. Click the **three dots (...)** menu → **Download**
3. Save the `.json` file to your project folder
4. To import: Go to **Workflows** → **Add Workflow** → **Import from File**
