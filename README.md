# Get Started with LLMs Course

Welcome to the **Get Started with LLMs** course.  
เนื้อหาทุกบทถูกรวมไว้ในไฟล์นี้ และแต่ละโฟลเดอร์ใช้เก็บไฟล์ตัวอย่างใน `examples/` เท่านั้น

## Course Overview

| # | Topic | Learning focus | Example file |
|---|-------|----------------|--------------|
| 1 | [Introduction](#1-introduction-to-llms) | พื้นฐาน LLM, คำศัพท์สำคัญ, การใช้งานเบื้องต้น | [`01-introduction/examples/llm-glossary.md`](./01-introduction/examples/llm-glossary.md) |
| 2 | [ChatGPT](#2-chatgpt) | การเริ่มใช้งาน, prompt engineering, ข้อจำกัด | [`02-chatgpt/examples/prompt-examples.md`](./02-chatgpt/examples/prompt-examples.md) |
| 3 | [Claude](#3-claude) | long-context, project workflow, use cases | [`03-claude/examples/system-prompt-templates.md`](./03-claude/examples/system-prompt-templates.md) |
| 4 | [Gemini](#4-gemini) | multimodal AI, Google ecosystem, API | [`04-gemini/examples/gemini-api-examples.py`](./04-gemini/examples/gemini-api-examples.py) |
| 5 | [NotebookLM](#5-notebooklm) | research workflow แบบอ้างอิงแหล่งข้อมูล | [`05-notebooklm/examples/use-case-scenarios.md`](./05-notebooklm/examples/use-case-scenarios.md) |
| 6 | [LM Studio](#6-lm-studio) | รันโมเดล local, เลือกโมเดล, ตั้งค่า inference | [`06-lm-studio/examples/model-selection-guide.md`](./06-lm-studio/examples/model-selection-guide.md) |
| 7 | [n8n](#7-n8n) | automation + AI agent workflow | [`07-n8n/examples/workflow-examples.md`](./07-n8n/examples/workflow-examples.md) |

## Prerequisites

- A computer with internet access
- Basic familiarity with web browsers
- No prior programming experience required

## How to Use This Repository

- Read all chapter learning material in this root `README.md`.
- Open chapter-specific sample files inside each `examples/` folder.
- Folders `01-07` are used to store chapter examples only.
- (TH) เนื้อหาหลักอยู่ใน `README.md` นี้ และโฟลเดอร์ `01-07` ใช้เก็บไฟล์ตัวอย่างของแต่ละบทเท่านั้น

---

## 1) Introduction to LLMs

### What is an LLM?
Large Language Model (LLM) คือโมเดล AI ที่ฝึกจากข้อมูลข้อความจำนวนมาก เพื่อสร้าง สรุป แปล และวิเคราะห์ข้อความได้อย่างมีประสิทธิภาพ โดยมีสถาปัตยกรรมหลักคือ Transformer

### Key concepts
- Prompt / Response
- Token / Context Window
- Temperature
- System Prompt
- Hallucination
- Fine-tuning / RAG

### Categories of LLM tools
- Cloud-based: ChatGPT, Claude, Gemini
- Local/on-device: LM Studio + open-source models
- Workflow automation: n8n

ตัวอย่างไฟล์: [`01-introduction/examples/llm-glossary.md`](./01-introduction/examples/llm-glossary.md)

## 2) ChatGPT

### Highlights
- เริ่มต้นใช้งานผ่านเว็บได้ทันที
- เหมาะกับงานสนทนา เขียน สรุป และช่วยเขียนโค้ด
- คุณภาพผลลัพธ์ขึ้นกับคุณภาพของ prompt

### Best practices
- ระบุเป้าหมายให้ชัดเจน
- กำหนดรูปแบบคำตอบ
- iterative prompting (ถามต่อเนื่องเพื่อปรับผลลัพธ์)
- ตรวจสอบข้อเท็จจริงที่สำคัญเสมอ

ตัวอย่างไฟล์: [`02-chatgpt/examples/prompt-examples.md`](./02-chatgpt/examples/prompt-examples.md)

## 3) Claude

### Highlights
- เด่นด้านการวิเคราะห์เอกสารยาวและการให้เหตุผล
- รองรับบริบทขนาดใหญ่ (long context)
- เหมาะกับงานวิเคราะห์เอกสาร, code review, งานเขียนเชิงลึก

### Best practices
- ใช้ Projects สำหรับงานที่ทำซ้ำ
- อัปโหลดเอกสารจริงเพื่อให้ตอบแบบ grounded
- ขอหลายแนวทางเพื่อเปรียบเทียบก่อนตัดสินใจ

ตัวอย่างไฟล์: [`03-claude/examples/system-prompt-templates.md`](./03-claude/examples/system-prompt-templates.md)

## 4) Gemini

### Highlights
- โมเดล multimodal (ข้อความ/ภาพ/เสียง/วิดีโอ)
- ผสานกับ Google ecosystem (Search, Workspace)
- ใช้งานผ่าน Gemini UI หรือ API ใน Google AI Studio

### Best practices
- ใช้ extension/เครื่องมือที่เกี่ยวข้องกับงาน
- รวมหลายชนิดข้อมูลใน prompt เดียว
- แยกทดลอง prompt ใน AI Studio ก่อนนำไปใช้จริง

ตัวอย่างไฟล์: [`04-gemini/examples/gemini-api-examples.py`](./04-gemini/examples/gemini-api-examples.py)

## 5) NotebookLM

### Highlights
- เน้นถามตอบจาก “แหล่งข้อมูลที่ผู้ใช้ให้” เป็นหลัก
- มี citation ช่วยตรวจสอบที่มาของคำตอบ
- เหมาะกับงาน research, study, synthesis เอกสารหลายแหล่ง

### Best practices
- เริ่มจากภาพรวม (guide/summary)
- ถามแบบเจาะจงและตรวจ citation ทุกครั้ง
- ใช้การเทียบข้ามเอกสารเพื่อหาจุดร่วม/จุดต่าง

ตัวอย่างไฟล์: [`05-notebooklm/examples/use-case-scenarios.md`](./05-notebooklm/examples/use-case-scenarios.md)

## 6) LM Studio

### Highlights
- รัน open-source LLM บนเครื่องตนเอง (offline ได้)
- เหมาะกับงานที่ต้องการความเป็นส่วนตัว
- รองรับ local OpenAI-compatible API

### Best practices
- เริ่มจากโมเดลขนาดเล็กและ quantization ระดับสมดุล (เช่น Q4_K_M)
- เลือกโมเดลตามทรัพยากรเครื่อง (RAM/GPU)
- ปรับ temperature/context ให้เหมาะกับประเภทงาน

ตัวอย่างไฟล์: [`06-lm-studio/examples/model-selection-guide.md`](./06-lm-studio/examples/model-selection-guide.md)

## 7) n8n

### Highlights
- สร้าง workflow automation แบบ visual
- ผสาน LLM กับระบบจริง (email, docs, APIs, DB)
- เหมาะกับงาน agentic workflow และงานที่ทำซ้ำ

### Best practices
- เริ่มจาก workflow เล็ก ๆ และทดสอบทีละ node
- ตั้ง error handling และ monitoring
- จัดการ credentials และ API limits อย่างรัดกุม

ตัวอย่างไฟล์: [`07-n8n/examples/workflow-examples.md`](./07-n8n/examples/workflow-examples.md)

---

## References

- [OpenAI ChatGPT](https://chat.openai.com)
- [Anthropic Claude](https://claude.ai)
- [Google Gemini](https://gemini.google.com)
- [Google NotebookLM](https://notebooklm.google.com)
- [LM Studio](https://lmstudio.ai)
- [n8n](https://n8n.io)
