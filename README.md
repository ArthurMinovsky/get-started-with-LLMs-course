---
marp: true
theme: default
paginate: true
header: 'Get Started with LLMs'
footer: '© LLMs Course'
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;500;600;700&family=Sarabun:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
  section {
    font-family: 'Noto Sans Thai', 'Sarabun', 'Sukhumvit Set', 'Thonburi', sans-serif;
    font-size: 24px;
    line-height: 1.6;
    letter-spacing: 0.01em;
  }
  h1, h2, h3, h4 {
    font-family: 'Noto Sans Thai', 'Sarabun', 'Sukhumvit Set', 'Thonburi', sans-serif;
    font-weight: 600;
    line-height: 1.35;
  }
  h1 {
    color: #2563eb;
    font-size: 1.8em;
  }
  h2 {
    color: #1e40af;
    border-bottom: 2px solid #93c5fd;
    padding-bottom: 6px;
    font-size: 1.4em;
  }
  h3 {
    color: #334155;
    font-size: 1.1em;
  }
  table {
    font-size: 18px;
    line-height: 1.45;
  }
  th {
    background: #eff6ff;
  }
  code {
    font-family: 'JetBrains Mono', 'Menlo', 'Consolas', monospace;
    background: #f1f5f9;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.92em;
  }
  pre {
    font-family: 'JetBrains Mono', 'Menlo', 'Consolas', monospace;
    font-size: 15px;
    line-height: 1.5;
  }
  pre code {
    background: transparent;
    padding: 0;
  }
  blockquote {
    border-left: 4px solid #93c5fd;
    color: #475569;
    font-style: normal;
  }
  strong {
    color: #1e40af;
    font-weight: 600;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->


# Get Started with LLMs Course

Welcome to the **Get Started with LLMs** course.  By Jillaphat Jaroenkantasima

\
A practical, beginner-friendly tour of today's most useful large language model tools.





\
github:  https://github.com/ArthurMinovsky/get-started-with-LLMs-course/blob/main/README.md

---

## Table of Contents

| # | Chapter | Key Topics |
|---|---------|------------|
| 1 | [Introduction to LLMs](#1-introduction-to-llms) | LLM basics · System Prompts · Agents · Context Files · Documentation |
| 2 | [LLMs model and Prompt engineering](#2-llms-model-and-prompt-engineering) | Prompt engineering · Model comparison |
| 2.1 | [ChatGPT](#21-chatgpt) | Prompt engineering · Best practices |
| 2.2 | [Claude](#22-claude) | Long context · Project workflow |
| 2.3 | [Gemini](#23-gemini) | Multimodal AI · Google ecosystem |
| 2.5 | [Prompt & Context engineering](#25-prompt--context-engineering) | Prompt design · Context files · Agent setup |
| 3 | [NotebookLM](#3-notebooklm) | Source-grounded research · Studio |
| 4 | [LM Studio](#6-lm-studio-) | Local models · curl · Python API |
| 5 | [n8n](#7-n8n) | Workflow automation · Google Cloud API |

---

## Prerequisites & How to Use

### Prerequisites
- A computer with internet access
- Basic familiarity with web browsers
- No prior programming experience required

### How to Use This Repository
- Read all chapter learning material in this root `README.md`
- Open chapter-specific sample files inside each `examples/` folder
- Folders `01-07` are used to store chapter examples only

---

# 1. Introduction to LLMs

### What is an LLM?
A **Large Language Model** is an AI model trained on very large text datasets to generate, summarize, translate, and analyze language — typically using a Transformer-based architecture.

 
\
\
see more:
[llm-glossary.md](01-introduction/examples/llm-glossary.md)

---

## 1. Introduction — Key Concepts

- **Prompt / Response**
- **Token / Context Window**
- **Temperature**
- **System Prompt**
- **Hallucination**
- **Fine-tuning / RAG**


---

# 1.1 หลักการทำงานของ LLM

![bg right:38% w:90%](https://commons.wikimedia.org/wiki/Special:FilePath/Transformer,_full_architecture.png)

LLM = โมเดลทำนาย **token ถัดไป** จากบริบทที่ได้รับ

ขั้นตอนการทำงานคร่าวๆ:
1. **Tokenization** — แปลงข้อความเป็นหน่วยย่อย (tokens)
2. **Embedding** — แปลง token เป็น vector ตัวเลข
3. **Transformer + Attention** — ประมวลผลความสัมพันธ์ของ token
4. **Next-token prediction** — ทำนาย token ถัดไปทีละตัว
5. **Sampling** — สุ่มตามความน่าจะเป็น (ควบคุมด้วย temperature)

Tip: แนะนำให้ prompt เป็นภาษาอังกฤษ​ เพราะจะได้รีดความสามารถของ AI และประหยัดต้นทุนกว่าภาษาไทย

---

## 1.1 วงจรการสอนโมเดลและใช้งานของ LLM (LLMs cycle)

| ขั้นตอน | สิ่งที่เกิดขึ้น |
|---------|----------------|
| **Pre-training** | เรียนรู้ภาษาจากข้อมูลขนาดใหญ่ (เว็บ, หนังสือ, โค้ด) |
| **Fine-tuning** | ปรับให้ทำตามคำสั่งเฉพาะทาง |
| **RLHF** | ใช้ feedback จากมนุษย์ปรับพฤติกรรม |
| **Inference** | ตอนที่เราเรียกใช้งานจริง (chat, API) |

> LLM **ไม่ได้ "คิด" หรือ "เข้าใจ"** — มันทำนายคำถัดไปจากรูปแบบที่เคยเห็น

---

# 2. LLMs model and Prompt engineering

---

# 2.1 ChatGPT

![bg right:35% w:70%](https://commons.wikimedia.org/wiki/Special:FilePath/ChatGPT-Logo.svg)

### Highlights

- เริ่มต้นใช้งานผ่านเว็บได้ทันที
- เป็นต้นกำเนิดของ chatbot, image generation, AI API, etc.
- คุณภาพผลลัพธ์ขึ้นกับคุณภาพของ prompt
- สามารถต่อกับ plugin ส่วนเสริมต่างๆ และสร้าง agent เฉพาะของเราเองได้

---

## 2.1 ChatGPT — Best Practices

- ระบุเป้าหมายให้ชัดเจน
- กำหนดรูปแบบคำตอบ
- iterative prompting (ถามต่อเนื่องเพื่อปรับผลลัพธ์)
- ChatGPT มีปัญหาเรื่อง Hallucination ต้องตรวจสอบข้อเท็จจริงที่สำคัญเสมอ

Example file: [prompt-examples.md](02-chatgpt/examples/prompt-examples.md)

---

# 2.2 Claude

![bg right:38% w:90%](https://commons.wikimedia.org/wiki/Special:FilePath/Claude_AI_logo.svg)

### Highlights
- เก่งด้านงานเฉพาะด้าน
- รองรับบริบทขนาดใหญ่ (long context)
- เหมาะกับงานวิเคราะห์เอกสาร, code review, งานประมวลผล, งานที่เน้นเฉพาะด้่านเช่น claudecode, cowork, claude-design
- claude มักคิดเยอะ และใช้ภาษาอังกฤษสละสลวยจนเข้าใจยาก และชอบติด rate limit บ่อย

---

## 2.2 Claude — Best Practices

- ใช้ **Projects** สำหรับงานที่ทำซ้ำ
- พยายามใส่ context ที่เพียงพอ ไม่มากไม่น้อยเกินไป
- อัปโหลดเอกสารจริงเพื่อให้ตอบแบบ grounded
- ขอหลายแนวทางเพื่อเปรียบเทียบก่อนตัดสินใจ

Example file: [system-prompt-templates.md](03-claude/examples/system-prompt-templates.md)

---

# 2.3 Gemini

![bg right:35% w:70%](https://commons.wikimedia.org/wiki/Special:FilePath/Google_Gemini_icon_2025.svg)

### Highlights
- โมเดล **multimodal** (ข้อความ / ภาพ / เสียง / วิดีโอ)
- รับ context ได้มากที่สุด (~2M tokens)
- ผสานกับ Google ecosystem (Search, Workspace, Sheet, Stinch, NotebookLM)
- ใช้งานผ่าน Gemini UI, API ใน Google AI Studio หรือใน gemini-cli

---

## 2.3 Gemini — Best Practices

- เหมาะสำหรับ deep research และข้อมูลที่ต้องแนบ reference เพื่อตรวจสอบ
- เหมาะนำไปใช้เป็น application เฉพาะ เช่น nanobanana, stitch, canvas
- เชื่อมต่อ ecosystem เช่น google sheet, google drive, google doc, google slide

Example file: [gemini-api-examples.py](04-gemini/examples/gemini-api-examples.py)

---

# 2.4 ตารางเปรียบเทียบ ChatGPT, Claude, Gemini

| | **ChatGPT** | **Claude** | **Gemini** |
|--|-------------|------------|------------|
| **จุดแข็ง** | สนทนาทั่วไป, image gen, ecosystem ใหญ่ | วิเคราะห์เอกสารยาว, coding, reasoning | Multimodal, context 2M, Google ecosystem |
| **เหมาะกับ** | งานเขียน, ไอเดีย, image | งานวิเคราะห์เชิงลึก, dev work | Research, multimedia, integrate Google |
| **ข้อควรระวัง** | hallucinate ตัวเลข, ข้อมูลสด | บางครั้งระมัดระวังเกินไป, ใช้คำฟุ่มเฟือย | การทำตามคำสั่งยังไม่ดีพอเท่า 2 โมเดลก่อนหน้า |
| **ราคา** | Free / Plus $20 | Free / Pro $20 | Free / Advanced $20 |

> เลือกตามงาน — ไม่มีค่ายไหนชนะทุกด้าน

---


# 2.5 Prompt & Context engineering

### by Claude Opus 4.7 System Prompt use case
\
**System prompt** = คือคำสั่งซ่อนที่กำหนดบุคลิกและกฎของโมเดล

แหล่งที่เปิดเผยอย่างเป็นทางการ:
- **Anthropic** เผยแพร่ system prompt ของ Claude ที่
  `docs.anthropic.com/en/release-notes/system-prompts`


---

## 2.5.1 ตัวอย่าง: NVIDIA Nemotron (โครงสร้างจาก model card)

```text
You are a helpful, respectful and honest assistant.
Always answer as helpfully as possible, while being safe.

If a question does not make any sense, or is not factually
coherent, explain why instead of answering something not
correct. If you don't know the answer, please don't share
false information.
```

จุดสังเกต: เน้น **"helpful, harmless, honest"** (HHH)
+ instruction ป้องกัน hallucination ตรงๆ

---

# 2.5.2 Logic ของ LLM ที่เรียนรู้จาก system prompt

จาก system prompt เราจะเห็นว่า LLM:

1. **ทำตามคำสั่งตามลำดับ** — instruction ก่อน มีน้ำหนักกว่า
2. **ต้องการ context ชัดเจน** — บอกบทบาท, วันเวลา, knowledge cutoff
3. **ตอบดีขึ้นเมื่อมี structure** — markdown, ขั้นตอน, ตัวอย่าง
4. **ปฏิบัติตามขอบเขตที่ตั้งไว้** — "do this" / "don't do that"
5. **ไม่รู้สิ่งที่ไม่ได้บอก** — ถ้าไม่ใส่บริบท จะเดา

---

## 2.5.3 โครงสร้าง prompt ที่ดี (RICCE)

| ส่วน | ตัวอย่าง |
|------|----------|
| **R**ole — บทบาทที่ต้องการให้แสดงออกมา | "คุณเป็น product manager มือใหม่..." |
| **I**nstruction — คำสั่งที่เนื้อความครบถ้วน | "สรุปฟีเจอร์ใหม่ใน 3 ข้อ" |
| **C**ontext — บริบทหรือข้อมูลแวดล้อมรอบตัว | "ผลิตภัณฑ์เป็น mobile app สำหรับนักเรียน" |
| **C**onstraint — ขอบเขต | "ไม่เกิน 200 คำ ใช้ภาษาไทย" |
| **E**xample — ตัวอย่าง | "เช่น: '🎯 ฟีเจอร์ X ช่วย...'" |

Ref: https://www.supplychaintoday.com/chatgpt-prompt-cheat-sheet/

---

# 2.5.4 เปรียบเทียบ prompt ที่ดี vs กำกวม

| ❌ กำกวม | ✅ ดี |
|----------|--------|
| "เขียนอีเมลให้หน่อย" | "เขียนอีเมลขอเลื่อนนัด เหตุผลคือป่วย ภาษาทางการ ไม่เกิน 4 บรรทัด" |
| "ช่วยอธิบาย AI" | "อธิบาย AI ให้นักเรียน ม.4 ฟัง ใช้คำง่าย พร้อมตัวอย่าง 1 ข้อ" |
| "สรุปเอกสารนี้" | "สรุปเอกสารนี้เป็น 5 bullet points เน้นข้อสรุปและตัวเลขสำคัญ" |
| "เขียนโค้ดเรียง" | "เขียน Python function `sort_by_date(items)` รับ list ของ dict ที่มี key `date` (ISO string) คืน list ที่เรียงจากเก่าไปใหม่" |

![bg right:45% w:90%](https://scontent.fbkk22-1.fna.fbcdn.net/v/t39.30808-6/672683461_122100991352735490_1150064677866112344_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=e06c5d&_nc_ohc=MVNXHfTSVuMQ7kNvwF2Lx4R&_nc_oc=Ado1cnXViNaT9kLGkOPf8kURiO7j0wRYhAcB8eXADsS4tk9Pc1XHv2LWx4GqjVKRS8Q&_nc_zt=23&_nc_ht=scontent.fbkk22-1.fna&_nc_gid=coat6cwiD7gRYeXXa4iimA&_nc_ss=7a3a8&oh=00_Af1SM7a-Z6S6OJmBuZ1aiNfeN7HG4XPYdnNZ1bfG-DxP8Q&oe=69EC2A0C)

---

## 2.5.5 ทำไม prompt กำกวมถึงผลลัพธ์แย่

LLM จะ **เดา** ส่วนที่เราไม่ได้บอก → ผลคือ:

- 🎲 ผลลัพธ์ไม่สม่ำเสมอ (ครั้งละแบบ)
- 📏 ความยาวไม่ตรงต้องการ
- 🌐 ภาษา/โทนไม่เหมาะกับผู้ฟัง
- ❓ ไม่ได้ตอบคำถามจริงๆ

> **เคล็ดลับ** ถ้ามนุษย์ด้วยกันเองยังถามกลับ — LLM ก็จะเดาสุ่ม


---
# 2.5.6 Context engineering ทำไม Documentation ถึงสำคัญในยุค AI
ในยุคก่อน AI:

เอกสารคือคู่มือสำหรับ มนุษย์ อ่าน ไม่มีก็ "อ่านโค้ดเอา"

ในยุค AI:

เอกสารคือ input ให้ AI ทำงาน AI ดีเท่ากับเอกสารที่คุณให้

No docs = AI hallucinates
Good docs = AI ทำงานเหมือนเพื่อนร่วมทีม
💡 Documentation = เครื่องมือเพิ่ม productivity x10 ในยุค AI

---
 # 2.5.7 Context File คืออะไร

**Context file** = ไฟล์ที่โหลดเข้า LLMs เพื่อให้ LLMs อ่านประกอบคำสั่งนั้น

หน้าที่:
- บอกข้อมูลเบื้องต้นเกี่ยวกับงานที่ต้องการให้ทำ
- ให้รายละเอียดเพิ่มเติมจากสิ่งที่คำสั่ง (propmt) ตกหล่น
- กำหนดขอบเขตการทำงานและแสดงตัวอย่างของผลลัพธ์
- ลด **hallucination** เพราะ AI มีข้อมูลจริงอ้างอิง

---

## 2.5.7.1 ตัวอย่าง Context File 

README.md — overview, quickstart
examples/ — ตัวอย่างจริง
API docs (OpenAPI, JSDoc, etc.)
.docx, .pdf, .txt, .csv, .xlsx - ไฟล์ที่เกี่ยวข้อง
เขียนเอกสารดี = ลงทุนให้ตัวเอง + AI + ทีมในอนาคต

---

# 2.5.8 System Prompt และหลักการสร้าง Agent

Agent = LLM + บทบาท + เครื่องมือ + เป้าหมาย

## หลักการออกแบบ system prompt สำหรับ agent:

กำหนดบทบาท ชัดเจน (You are a...)
ระบุความสามารถ (You can do X, Y, Z)
ระบุข้อจำกัด (You cannot do A, B, C)
กำหนดรูปแบบ output (เช่น JSON, markdown)
ระบุพฤติกรรมเมื่อไม่แน่ใจ (ถามกลับ / บอกว่าไม่ทราบ)

---

# 2.5.9 ตัวอย่าง Agent System Prompt

คุณคือ "น้องช่วย" ผู้ช่วยตอบลูกค้าของร้านกาแฟ ABC

✅ ทำได้:
- ตอบเมนู ราคา และเวลาเปิด-ปิด
- แนะนำเครื่องดื่มตามรสชาติที่ลูกค้าชอบ
- รับ feedback และส่งต่อให้ทีม

❌ ทำไม่ได้:
- ยืนยันการสั่งซื้อ (ต้องผ่าน LINE OA)
- คืนเงิน หรือส่วนลดพิเศษ

หากไม่แน่ใจ ให้ตอบว่า "ขออนุญาตส่งต่อให้พี่ทีมงานนะคะ"

---

# 3. NotebookLM

![bg right:38% w:90%](https://commons.wikimedia.org/wiki/Special:FilePath/NotebookLM_logo.svg)

### Highlights
- เน้นถามตอบจาก **แหล่งข้อมูลที่ผู้ใช้ให้** เป็นหลัก
- มี **citation** ช่วยตรวจสอบที่มาของคำตอบ
- เหมาะกับงาน research, study, synthesis เอกสารหลายแหล่ง

---

## 3.1 แนะนำ NotebookLM เบื้องต้น

**NotebookLM** = AI research assistant ของ Google
ที่ทำงานบน **source ที่คุณให้เท่านั้น**

ขั้นตอนใช้งาน:
1. เข้า `notebooklm.google.com` (login Google account)
2. สร้าง **New notebook**
3. เพิ่ม **Sources** (สูงสุด 50 sources / 500K คำ ต่อ source)
4. ถามคำถามใน chat — AI จะตอบพร้อม **citation**
5. ใช้เครื่องมือ Studio เพื่อแปลง source เป็น media

---

## 3.2 ประเภท Source ที่รองรับ

| ประเภท | ตัวอย่าง |
|--------|----------|
| **เอกสาร** | PDF, Google Docs, Word, txt, markdown |
| **เว็บ** | URL ของบทความ, blog, Wikipedia |
| **วิดีโอ** | YouTube link (ถอดเสียงอัตโนมัติ) |
| **เสียง** | mp3, m4a (ถอดเสียงอัตโนมัติ) |
| **ที่วาง** | Paste text ตรงๆ |


> Tip: ผสมหลายประเภทใน notebook เดียวเพื่อ cross-reference

---

## 3.3 การหา Source คุณภาพ

- **Google Scholar** — งานวิจัย peer-reviewed
- **arXiv** — preprint สาย CS / ML / Physics
- **Wikipedia** — ภาพรวม + reference list
- **YouTube** — lecture, podcast, conference talks
- **GitHub** — README, docs ของ project
- **เอกสารทางการ** — government, NGO, official reports

> ตรวจ **author, date, source** ทุกครั้งก่อน import

---

## 3.4 แปลง Source เป็น Media (Studio)

NotebookLM Studio สร้าง media จาก source ได้:

| Output | คำอธิบาย |
|--------|----------|
| 🎙️ **Audio Overview** | Podcast 2 host คุยกันเป็นภาษาธรรมชาติ |
| 🧠 **Mind Map** | แผนผังความคิดเชื่อมโยงหัวข้อ |
| 📝 **Briefing Doc** | สรุปสำหรับผู้บริหาร |
| ❓ **FAQ** | คำถาม-คำตอบที่พบบ่อย |
| 📚 **Study Guide** | คู่มือพร้อมคำถามทบทวน |
| ⏱️ **Timeline** | ลำดับเหตุการณ์ |
| 🎬 **Video Overview** | สไลด์พร้อม narration |

---

## 3.5 Best Practices

- เริ่มจากภาพรวม (guide / summary)
- ถามแบบเจาะจงและตรวจ citation ทุกครั้ง
- ใช้การเทียบข้ามเอกสารเพื่อหาจุดร่วม / จุดต่าง

Example file: [use-case-scenarios.md](05-notebooklm/examples/use-case-scenarios.md)

---

## 3.6 ⚠️ ข้อควรระวังของ NotebookLM

| ข้อจำกัด | ผลกระทบ |
|---------|---------|
| ตอบจาก source **เท่านั้น** | ไม่รู้ข้อมูลนอก source ที่ใส่ |
| คุณภาพ output = คุณภาพ source | source ผิด → คำตอบผิด |
| ไม่เหมาะกับ creative writing | มันคือ research tool ไม่ใช่ writer |
| Citation ไม่ใช่ "ความถูกต้อง" | citation บอกที่มา ไม่ได้ verify ข้อเท็จจริง |
| ข้อมูลถูกใช้ฝึกโมเดลได้ | อย่าใส่ข้อมูลลับ / ส่วนตัว |
| ภาษาไทย: คุณภาพต่ำกว่า EN | บางครั้งสรุปไม่ครบ / แปลผิด |

> 💡 ใช้คู่กับ **Claude / ChatGPT** สำหรับงานต่อยอด

---

# 4. LM Studio 💻

### Highlights
- รัน open-source LLM บนเครื่องตนเอง (offline ได้)
- เหมาะกับงานที่ต้องการความเป็นส่วนตัว
- รองรับ local **OpenAI-compatible API**

---

## 4.1 แนะนำการใช้งาน LM Studio

ขั้นตอนเริ่มต้น:
1. ดาวน์โหลด LM Studio จาก `lmstudio.ai`
2. เปิดแอป → tab **Discover** → ค้นหาโมเดล
   เช่น `Llama 3.1 8B`, `Qwen 2.5 7B`, `Gemma 2 9B`
3. กด **Download** (เลือก quantization เช่น `Q4_K_M`)
4. ไปที่ tab **Chat** → โหลดโมเดล → เริ่มคุย
5. เปิด local server ที่ tab **Developer**
   → จะได้ endpoint `http://localhost:1234/v1`

---

## 4.2 เลือกโมเดลตามทรัพยากร

| RAM / VRAM | ขนาดโมเดลที่เหมาะ |
|------------|---------------------|
| 8 GB | 3B - 7B (Q4) |
| 16 GB | 7B - 13B (Q4-Q5) |
| 24 GB | 13B - 32B (Q4) |
| 32 GB+ | 32B - 70B (Q4) |

> Q4_K_M = สมดุลระหว่างคุณภาพและขนาด (แนะนำสำหรับมือใหม่)

---

## 4.3 เรียกใช้ด้วย curl

LM Studio ใช้ API format เดียวกับ OpenAI

```bash
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "local-model",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "อธิบาย LLM ใน 3 ประโยค"}
    ],
    "temperature": 0.7
  }'
```

---

## 4.4 เรียกใช้ด้วย Python (openai library)

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # ใส่อะไรก็ได้ ไม่ตรวจ
)

response = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "ตอบเป็นภาษาไทย"},
        {"role": "user", "content": "LLM คืออะไร?"}
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)
```

---

## 4.5 Best Practices

- เริ่มจากโมเดลขนาดเล็กและ quantization สมดุล (เช่น `Q4_K_M`)
- เลือกโมเดลตามทรัพยากรเครื่อง (RAM / GPU)
- ปรับ temperature / context ให้เหมาะกับประเภทงาน

Example file: [model-selection-guide.md](06-lm-studio/examples/model-selection-guide.md)

---

# 5. n8n

![bg right:38% w:90%](https://commons.wikimedia.org/wiki/Special:FilePath/N8n-logo-new.svg)

### Highlights
- สร้าง **workflow automation** แบบ visual
- ผสาน LLM กับระบบจริง (email, docs, APIs, DB)
- เหมาะกับงาน **agentic workflow** และงานที่ทำซ้ำ

---

## 5.1 แนะนำการใช้งาน n8n

n8n = visual workflow automation (open-source, self-host ได้)

ขั้นตอนเริ่มต้น:
1. ติดตั้งแบบ Cloud (`n8n.io/cloud`) หรือ self-host (Docker)
2. สร้าง **New Workflow**
3. เลือก **Trigger node** (เริ่มเมื่อไร?)
   - Manual, Schedule, Webhook, Email, etc.
4. เพิ่ม **Action nodes** (ทำอะไรต่อ?)
   - HTTP Request, Google Sheets, OpenAI, etc.
5. เชื่อม node ด้วยลากเส้น → กด **Execute Workflow**

Ref: https://www.thepexcel.com/n8n-ep01/

---

## 5.2 ตัวอย่าง Workflow เบื้องต้น

```
[Schedule Trigger] (ทุก 9 โมง)
        ↓
[Google Sheets] (อ่านรายชื่อลูกค้า)
        ↓
[OpenAI / Claude] (สร้างข้อความ personalized)
        ↓
[Gmail] (ส่งอีเมล)
        ↓
[Google Sheets] (บันทึก log)
```

> Tip: ทดสอบทีละ node ด้วย **Execute step** ก่อนรันทั้ง workflow

---

## 5.3 ดึง Google Cloud API มาใช้กับ n8n

ขั้นตอนสร้าง Google credential:

1. เข้า `console.cloud.google.com` → สร้าง **Project**
2. **APIs & Services** → **Library** → เปิด API ที่ต้องการ
   (เช่น Google Sheets API, Gmail API, Drive API)
3. **Credentials** → **Create Credentials** → **OAuth client ID**
   - Application type: **Web application**
   - Authorized redirect URIs: copy จาก n8n credential page
4. ดาวน์โหลด `Client ID` + `Client Secret`
5. เพิ่มตัวเองใน **OAuth consent screen** → Test users

Ref: https://www.youtube.com/watch?v=FBGtpWMTppw&t=184s

---

## 5.4 ตั้งค่า Credential ใน n8n

1. ใน n8n → **Credentials** → **New** → ค้นหา **Google**
2. เลือกประเภท เช่น **Google Sheets OAuth2 API**
3. ใส่ **Client ID** และ **Client Secret**
4. กด **Sign in with Google** → อนุญาต permissions
5. เก็บ credential นี้ไว้ใช้ในทุก Google node

> ⚠️ Self-host: ต้องตั้ง `WEBHOOK_URL` env เป็น public URL
> เพื่อให้ Google redirect กลับได้

---

## 5.5 Service Account (สำหรับ server-to-server)

ทางเลือกแทน OAuth (ไม่ต้อง login ผู้ใช้):

1. **Credentials** → **Create Credentials** → **Service Account**
2. ดาวน์โหลด JSON key
3. ใน Google Sheets / Drive: **Share** ไฟล์ให้ service account email
   (อยู่ในไฟล์ JSON: `client_email`)
4. ใน n8n: เลือก credential type **Service Account**
   → paste JSON key ทั้งไฟล์

> ใช้กับ workflow ที่รัน **อัตโนมัติ** ไม่มีคน login

---

## 5.6 Best Practices

- เริ่มจาก workflow เล็ก ๆ และทดสอบทีละ node
- ตั้ง error handling และ monitoring
- จัดการ credentials และ API limits อย่างรัดกุม

Example file: [workflow-examples.md](07-n8n/examples/workflow-examples.md)

---

# AI Challenge

- หลังจากนี้​ "ความเข้าใจ"​ จะเป็นกุญแจสำคัญมากขึ้น
- ความรู้พื้นฐานจะเป็นตัวกำหนดขอบเขตการสร้างสรรค์สิ่งต่างๆ ของมนุษย์หลังจากนี้
- AI ควรทำให้มนุษย์ฉลาดขึ้น ไม่ใช่โง่ลง

---

## References

- [OpenAI ChatGPT](https://chat.openai.com)
- [Anthropic Claude](https://claude.ai) — [System Prompts](https://docs.anthropic.com/en/release-notes/system-prompts)
- [Google Gemini](https://gemini.google.com) — [AI Studio](https://aistudio.google.com)
- [Google NotebookLM](https://notebooklm.google.com)
- [LM Studio](https://lmstudio.ai)
- [n8n](https://n8n.io) — [Docs](https://docs.n8n.io)
- [คู่มือการเขียน prompt อย่างมีประสิทธิภาพ](https://www.facebook.com/AiLife5.0/posts/pfbid02Axbo2UnSGd7Vbu2FGj3cineoBfwiur96pvwfVncydqModmyGxR3d3irz3AWnRVvPl?__cft__[0]=AZbBUIKrCwnSlGiPPzRIsYWerxRpjrtsrM4XB6r6HfQNTZ3t2x_k8F3-_KsqYsqnssnN2O496lcYnZa3mBW8F65YQhPFGRjMZgARlaymubBPaQQtzJRPCEndEyAfPegwh9rfcDgQRFInh66tCqAllipM3nmdruH2-ILTOs2QV77vP91wFfhokQTYNaRZqXL3LsI&__tn__=%2CO%2CP-R)
- [การใช้งาน n8n เบื้องต้น](https://www.thepexcel.com/n8n-ep01/)
- [NVIDIA Nemotron (HuggingFace)](https://huggingface.co/nvidia)

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# Thank You

Happy learning with LLMs! 🚀
