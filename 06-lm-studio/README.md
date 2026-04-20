# LM Studio — Getting Started

## What is LM Studio?

**LM Studio** is a desktop application that allows you to **download and run open-source Large Language Models locally on your own computer** — completely offline and for free. No data is sent to external servers, making it ideal for privacy-sensitive use cases.

With LM Studio, you can run powerful models like **Meta's Llama**, **Mistral**, **Google's Gemma**, and hundreds of other community models from [Hugging Face](https://huggingface.co).

## Why Run LLMs Locally?

| Advantage | Description |
|-----------|-------------|
| **Privacy** | Your data never leaves your machine |
| **Cost** | No API fees or subscription costs |
| **Offline** | Works without an internet connection |
| **Customization** | Fine-tune models or use any open-source model |
| **Unlimited Usage** | No rate limits or usage quotas |

## System Requirements

### Minimum Requirements
| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10/11, macOS 12+, Ubuntu 22.04+ |
| **RAM** | 8 GB (for small 7B models) |
| **Storage** | 10–50 GB free (models are large files) |
| **CPU** | Modern multi-core processor |

### Recommended Requirements
| Component | Recommendation |
|-----------|----------------|
| **RAM** | 16–32 GB for better performance |
| **GPU (NVIDIA)** | CUDA-capable GPU (RTX 3060 or better) |
| **GPU (Apple)** | Apple Silicon (M1/M2/M3) — excellent performance! |
| **Storage** | SSD with 50+ GB free |

> **Apple Silicon Note**: MacBooks and Mac desktops with M1/M2/M3 chips run local LLMs extremely well due to their unified memory architecture.

## Installation

### Step 1 — Download LM Studio
1. Go to [https://lmstudio.ai](https://lmstudio.ai)
2. Download the installer for your operating system (Windows, macOS, Linux)
3. Run the installer and follow the setup wizard

### Step 2 — Search and Download a Model
1. Open LM Studio
2. Click the **Search** tab (magnifying glass icon)
3. Search for a model, e.g., `llama`, `mistral`, or `gemma`
4. Select a model size appropriate for your hardware:
   - **4B–7B models**: Good for 8GB RAM
   - **13B models**: Better quality, needs 16GB RAM
   - **70B+ models**: Excellent quality, needs 32GB+ RAM or strong GPU
5. Click **Download** — models are stored in GGUF format

### Step 3 — Start a Chat
1. Click the **Chat** tab
2. Select your downloaded model from the dropdown
3. Wait for the model to load (first load may take 30–60 seconds)
4. Type your message and press Enter

## Understanding Model Names

Model filenames contain important information:

```
Meta-Llama-3-8B-Instruct-Q4_K_M.gguf
│              │          │ 
│              │          └── Quantization level
│              └───────────── Parameter count (8 Billion)
└──────────────────────────── Model name and version
```

### Quantization Guide

Quantization reduces model file size and memory requirements with some quality trade-off:

| Quantization | File Size | Quality | Use When |
|-------------|-----------|---------|----------|
| **Q2_K** | Smallest | Lower | Very limited RAM |
| **Q4_K_M** | Medium | Good | Best balance (recommended) |
| **Q5_K_M** | Larger | Better | More RAM available |
| **Q8_0** | Large | High | High RAM, best quality |
| **F16** | Largest | Highest | Maximum quality (needs lots of RAM) |

> **Recommendation**: Start with **Q4_K_M** quantization for the best balance of quality and performance.

## Key Features

### Chat Interface
- Multi-turn conversations with context memory
- System prompt configuration
- Adjustable parameters (temperature, context length, etc.)
- Conversation history saved locally

### Local Server (API Compatibility)
LM Studio can run a **local OpenAI-compatible API server**:
1. Click the **Local Server** tab
2. Select your model and click **Start Server**
3. Default URL: `http://localhost:1234/v1`

This lets you use local models with apps that support the OpenAI API format!

```python
# Example: Connect to LM Studio from Python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Any string works
)

response = client.chat.completions.create(
    model="local-model",  # Model name from LM Studio
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(response.choices[0].message.content)
```

### Model Management
- Browse and discover models from Hugging Face
- Manage downloaded models (view size, delete)
- Switch between models easily

## Popular Open-Source Models

| Model | Developer | Best For | Minimum RAM |
|-------|-----------|----------|-------------|
| **Llama 3** | Meta | General purpose, coding | 8 GB (8B) |
| **Mistral 7B** | Mistral AI | Fast, efficient responses | 8 GB |
| **Gemma 2** | Google | Balanced quality | 8 GB (9B) |
| **Phi-3** | Microsoft | Small but capable | 4 GB (3.8B) |
| **Qwen 2.5** | Alibaba | Multilingual, coding | 8 GB (7B) |
| **DeepSeek R1** | DeepSeek | Advanced reasoning | 16 GB (14B) |
| **Code Llama** | Meta | Code generation | 8 GB (7B) |

## Configuration Tips

### System Prompt
Set a system prompt to define the model's behavior:
```
You are a helpful AI assistant. Be concise and accurate. 
If you don't know something, say so rather than making something up.
```

### Key Parameters
| Parameter | Description | Recommended Value |
|-----------|-------------|------------------|
| **Temperature** | Randomness (0=deterministic, 1=creative) | 0.7 for chat, 0.2 for code |
| **Context Length** | How much text the model remembers | 4096–8192 tokens |
| **Max Tokens** | Maximum response length | 1024–2048 |
| **Top P** | Probability sampling | 0.9 |

## Use Cases

| Use Case | Recommended Model | Notes |
|----------|------------------|-------|
| General Chat | Llama 3 8B / Mistral 7B | Fast, good quality |
| Coding Assistant | Code Llama / Qwen 2.5 Coder | Specialized for code |
| Document Analysis | Llama 3 70B (if hardware allows) | Better reasoning |
| Privacy-Sensitive Work | Any local model | Data never leaves device |
| Offline Usage | Any local model | Works without internet |

## Limitations

- **Hardware dependent**: Larger, better models require more RAM/GPU
- **Slower than cloud**: Local inference is generally slower than cloud APIs
- **No internet access**: Models cannot browse the web
- **Setup required**: More technical setup than web-based tools
- **Model updates**: You must manually download updated model versions

## References

- [LM Studio Official Site](https://lmstudio.ai)
- [LM Studio Documentation](https://lmstudio.ai/docs)
- [Hugging Face Model Hub](https://huggingface.co/models)
- [GGUF Format Explained](https://huggingface.co/docs/hub/gguf)
- [Llama Models — Meta](https://llama.meta.com)
- [Mistral AI Models](https://mistral.ai/technology/)
