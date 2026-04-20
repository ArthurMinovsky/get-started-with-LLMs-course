# Gemini API — Getting Started Examples

## Prerequisites
- A Google account
- A free API key from [Google AI Studio](https://aistudio.google.com/apikey)
- Python 3.8+ installed

## Installation

```bash
pip install google-generativeai
```

---

## Example 1 — Basic Text Generation

```python
import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="YOUR_API_KEY")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate a response
response = model.generate_content("Explain what a Large Language Model is in simple terms.")

print(response.text)
```

---

## Example 2 — Multi-turn Conversation (Chat)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session
chat = model.start_chat(history=[])

# First message
response = chat.send_message("What are the main types of machine learning?")
print("Assistant:", response.text)

# Follow-up (model remembers previous context)
response = chat.send_message("Can you explain supervised learning with an example?")
print("Assistant:", response.text)

# View conversation history
for message in chat.history:
    print(f"{message.role}: {message.parts[0].text[:100]}...")
```

---

## Example 3 — Image Analysis (Multimodal)

```python
import google.generativeai as genai
import PIL.Image
import requests
from io import BytesIO

genai.configure(api_key="YOUR_API_KEY")

# Use gemini-1.5-pro or gemini-1.5-flash for multimodal
model = genai.GenerativeModel("gemini-1.5-flash")

# Load an image from URL
response_img = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png")
image = PIL.Image.open(BytesIO(response_img.content))

# Analyze the image
response = model.generate_content([
    "Describe what you see in this image in detail.",
    image
])

print(response.text)
```

---

## Example 4 — Document Summarization

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-pro")

# Long document text (replace with your content)
document = """
[Paste your long document here — Gemini 1.5 Pro supports up to 1 million tokens!]
"""

prompt = f"""
Please analyze this document and provide:
1. A 3-sentence executive summary
2. 5 key points in bullet form
3. Any action items or recommendations mentioned

Document:
{document}
"""

response = model.generate_content(prompt)
print(response.text)
```

---

## Example 5 — System Instructions (System Prompt)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Configure the model with a system instruction
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
    You are a professional SQL database expert.
    When asked to write queries:
    - Always use proper SQL formatting with uppercase keywords
    - Add comments explaining complex parts
    - Include example output where helpful
    - Mention potential performance considerations
    """
)

response = model.generate_content(
    "Write a query to find the top 5 customers by total order value in the last 30 days."
)

print(response.text)
```

---

## Example 6 — Structured Output with JSON

```python
import google.generativeai as genai
import json

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("""
Extract the following information from this text and return ONLY valid JSON:

Text: "John Smith joined our company on March 15, 2023. He works as a Senior Engineer
in the Engineering department and his email is john.smith@company.com. His employee
ID is EMP-4821."

Return JSON with these fields: name, join_date, job_title, department, email, employee_id
""")

# Parse the JSON response
try:
    # Remove markdown code blocks if present
    text = response.text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]

    data = json.loads(text.strip())
    print("Extracted data:")
    for key, value in data.items():
        print(f"  {key}: {value}")
except json.JSONDecodeError:
    print("Raw response:", response.text)
```

---

## Example 7 — Content Safety Settings

```python
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

# Configure safety settings (adjust thresholds as needed)
safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

response = model.generate_content(
    "Write a story about a friendly robot helping people.",
    safety_settings=safety_settings
)

print(response.text)
```

---

## Quick Reference: Gemini Models

| Model | Use Case | Speed | Context |
|-------|----------|-------|---------|
| `gemini-1.5-flash` | Fast tasks, prototyping | Fast | 1M tokens |
| `gemini-1.5-pro` | Complex tasks | Medium | 1M tokens |
| `gemini-1.0-pro` | Standard tasks | Medium | 32K tokens |

## Free Tier Limits (as of 2024)
- `gemini-1.5-flash`: 15 requests/minute, 1,500 requests/day
- `gemini-1.5-pro`: 2 requests/minute, 50 requests/day
