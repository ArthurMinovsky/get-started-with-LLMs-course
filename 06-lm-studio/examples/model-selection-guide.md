# LM Studio — Model Selection Guide

A practical guide to help you choose the right model for your hardware and use case.

---

## How to Read Model Names

Understanding model filenames helps you make informed choices.

### Example Filename
```
Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
│    │          │  │          │
│    │          │  │          └── Quantization: Q4_K_M
│    │          │  └───────────── Type: Instruct (chat-tuned)
│    │          └──────────────── Size: 8 Billion parameters
│    └─────────────────────────── Version: 3.1
└──────────────────────────────── Developer: Meta
```

### Model Types
| Suffix | Meaning | Use For |
|--------|---------|---------|
| **Instruct** or **Chat** | Fine-tuned for conversation | Chat, Q&A, tasks |
| **Base** | Raw pre-trained model | Advanced use, fine-tuning |
| **Code** | Fine-tuned for coding | Programming tasks |
| **GGUF** | Quantized format for local use | All LM Studio models |

---

## Quantization Cheat Sheet

| Quantization | File Size (7B model) | RAM Needed | Quality |
|-------------|---------------------|------------|---------|
| Q2_K | ~2.8 GB | ~4 GB | ⭐⭐ |
| Q3_K_M | ~3.3 GB | ~5 GB | ⭐⭐⭐ |
| Q4_K_M | ~4.1 GB | ~6 GB | ⭐⭐⭐⭐ ← Recommended |
| Q5_K_M | ~4.8 GB | ~7 GB | ⭐⭐⭐⭐ |
| Q6_K | ~5.5 GB | ~8 GB | ⭐⭐⭐⭐⭐ |
| Q8_0 | ~7.2 GB | ~10 GB | ⭐⭐⭐⭐⭐ |

**Rule of thumb**: Use Q4_K_M for the best balance of quality and performance.

---

## Hardware-Based Recommendations

### 8 GB RAM (Entry Level)

| Model | Size | Notes |
|-------|------|-------|
| Llama 3.2 3B Instruct Q8_0 | ~3.2 GB | Fast, capable for 3B |
| Mistral 7B Instruct Q4_K_M | ~4.1 GB | Excellent for general use |
| Phi-3 Mini 3.8B Q6_K | ~3.5 GB | Very capable small model |
| Gemma 2 2B Instruct Q8_0 | ~2.8 GB | Google's compact model |

### 16 GB RAM (Mid-Range)

| Model | Size | Notes |
|-------|------|-------|
| Llama 3.1 8B Instruct Q4_K_M | ~4.9 GB | Great all-rounder |
| Mistral 7B Instruct Q8_0 | ~7.2 GB | High quality 7B |
| Gemma 2 9B Instruct Q4_K_M | ~5.4 GB | Strong reasoning |
| Qwen 2.5 7B Instruct Q4_K_M | ~4.5 GB | Good multilingual support |
| Code Llama 13B Q4_K_M | ~7.9 GB | Excellent for coding |

### 32 GB RAM (High-End)

| Model | Size | Notes |
|-------|------|-------|
| Llama 3.1 70B Q2_K | ~26 GB | Excellent quality |
| Mistral Large Q3_K_M | ~28 GB | High capability |
| Qwen 2.5 14B Instruct Q8_0 | ~15 GB | Balanced performance |
| DeepSeek R1 14B Q4_K_M | ~9.3 GB | Strong reasoning |

### Apple Silicon (M1/M2/M3)

Apple Silicon Macs are excellent for local LLMs due to unified memory.

| Device | Recommended Model | Why |
|--------|------------------|-----|
| MacBook Air M1 8GB | Llama 3.2 3B Q8_0 | Fits comfortably in memory |
| MacBook Pro M1/M2 16GB | Llama 3.1 8B Q4_K_M | Great performance |
| MacBook Pro M2/M3 32GB+ | Llama 3.1 70B Q4_K_M | Near-GPT-4 quality |
| Mac Studio M2 Ultra | 70B+ models at full quality | Professional use |

---

## Use Case Recommendations

### General Chatbot / Q&A
```
Primary:   Llama 3.1 8B Instruct Q4_K_M
Backup:    Mistral 7B Instruct Q4_K_M
If 32GB+:  Llama 3.1 70B Instruct Q4_K_M
```

### Code Generation & Debugging
```
Primary:   Qwen 2.5 Coder 7B Instruct Q4_K_M
Backup:    Code Llama 7B Instruct Q4_K_M
Large:     DeepSeek Coder V2 16B Q4_K_M
```

### Document Analysis & Summarization
```
Primary:   Llama 3.1 8B Instruct Q6_K (needs longer context)
Large:     Llama 3.1 70B Instruct Q4_K_M
```

### Creative Writing
```
Primary:   Mistral 7B Instruct Q4_K_M (creative, fluent)
Backup:    Llama 3.1 8B Instruct Q4_K_M
```

### Multilingual Tasks
```
Primary:   Qwen 2.5 7B Instruct Q4_K_M (strong Asian language support)
Backup:    Mistral 7B Instruct Q4_K_M
```

### Advanced Reasoning / Math
```
Primary:   DeepSeek R1 Distill 8B Q4_K_M
Large:     DeepSeek R1 14B Q4_K_M
```

---

## LM Studio Settings Guide

### Chat Parameters (Recommended Starting Points)

```json
{
  "temperature": 0.7,
  "top_p": 0.9,
  "top_k": 40,
  "repeat_penalty": 1.1,
  "context_length": 4096,
  "max_tokens": 1024
}
```

### For Coding Tasks
```json
{
  "temperature": 0.2,
  "top_p": 0.95,
  "repeat_penalty": 1.0,
  "context_length": 8192,
  "max_tokens": 2048
}
```

### For Creative Writing
```json
{
  "temperature": 0.9,
  "top_p": 0.95,
  "repeat_penalty": 1.15,
  "context_length": 4096,
  "max_tokens": 2048
}
```

---

## Where to Find Models

1. **LM Studio Search Tab** — Built-in model browser (searches Hugging Face)
2. **Hugging Face** — [huggingface.co/models](https://huggingface.co/models) (filter by GGUF format)
3. **TheBloke** — Popular model uploader: `huggingface.co/TheBloke`
4. **bartowski** — Another popular quantizer: `huggingface.co/bartowski`

---

## Troubleshooting Common Issues

| Problem | Possible Solution |
|---------|-----------------|
| Model loads but crashes | Not enough RAM — try a smaller quantization |
| Very slow responses | Enable GPU offloading in LM Studio settings |
| Repetitive outputs | Increase `repeat_penalty` (try 1.1–1.3) |
| Incoherent responses | Lower `temperature` (try 0.5) |
| Responses cut off | Increase `max_tokens` |
| Old context forgotten | Increase `context_length` |
| GPU not detected | Update GPU drivers and LM Studio |
