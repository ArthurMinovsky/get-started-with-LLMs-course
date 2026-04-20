# n8n — เริ่มต้นทำระบบอัตโนมัติด้วย AI

## n8n คืออะไร?

**n8n** คือแพลตฟอร์มโอเพนซอร์สสำหรับทำ **workflow automation** ที่เชื่อมแอป บริการ และโมเดล AI เข้าด้วยกัน เพื่อลดงานซ้ำและสร้างกระบวนการอัตโนมัติ

n8n เหมาะมากกับงาน **AI workflow** เช่น เชื่อม ChatGPT/Claude/Gemini เข้ากับ API, ฐานข้อมูล, อีเมล หรือระบบภายในองค์กร

## ตัวเลือกการใช้งาน

| ตัวเลือก | คำอธิบาย | เหมาะกับ |
|--------|-------------|----------|
| **n8n Cloud** | ใช้งานแบบโฮสต์โดย n8n | เริ่มต้นเร็ว |
| **Self-Hosted (Docker)** | รันบนเซิร์ฟเวอร์ของตัวเอง | ควบคุมเต็มรูปแบบ |
| **Self-Hosted (npm)** | ติดตั้งผ่าน Node.js | พัฒนา/ทดสอบ |
| **Desktop App** | ติดตั้งบนเครื่อง | พัฒนาแบบโลคัล |

## เริ่มต้นใช้งาน

### แบบเร็วสุด: n8n Cloud
1. เข้า [https://n8n.io](https://n8n.io)
2. กด **Get started for free**
3. สมัครและเริ่มสร้างเวิร์กโฟลว์

### Self-hosted ด้วย Docker
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```
จากนั้นเปิด `http://localhost:5678`

## องค์ประกอบหลัก

- **Node**: ขั้นตอนย่อยของงาน
- **Connection**: เส้นทางข้อมูลระหว่าง node
- **Trigger**: จุดเริ่มต้นของ workflow
- **Execution**: การรันแต่ละครั้ง

## AI ใน n8n

### AI Agent Node
ให้ LLM ตัดสินใจเลือกเครื่องมือและวนลูปทำงานจนบรรลุเป้าหมาย

### โหนดเชื่อม LLM
| Node | บริการ | ความสามารถ |
|------|---------|------------|
| **OpenAI** | ChatGPT/GPT-4 | สร้างข้อความ, embeddings |
| **Anthropic** | Claude | วิเคราะห์และสร้างข้อความ |
| **Google Gemini** | Gemini | AI แบบหลายสื่อ |
| **Ollama** | โมเดลโลคัล | เน้นความเป็นส่วนตัว |

### AI Tool Nodes
ตัวอย่างเครื่องมือ: Calculator, Wikipedia, SerpAPI, HTTP Request, Code

## รูปแบบเวิร์กโฟลว์ยอดนิยม

1. Email classifier + auto reply
2. สรุปเอกสารจาก Drive แล้วส่ง Slack
3. Customer support bot
4. สรุปข่าวรายวันส่งอีเมล
5. สร้างโพสต์โซเชียลอัตโนมัติ

## การตั้งค่า Credentials

บริการส่วนใหญ่ต้องใช้ API key/OAuth เช่น OpenAI, Anthropic, Gemini, Slack, Gmail

## เคล็ดลับ

1. เริ่มด้วย workflow ง่ายก่อน
2. ทดสอบทีละ node
3. ตั้ง error workflow จัดการความล้มเหลว
4. ใช้ expressions (`{{ }}`) ให้คล่อง
5. export workflow เป็น JSON แล้วเก็บใน git

## แหล่งอ้างอิง

- [n8n Official Site](https://n8n.io)
- [n8n Documentation](https://docs.n8n.io)
- [n8n Community Forum](https://community.n8n.io)
- [n8n GitHub Repository](https://github.com/n8n-io/n8n)
- [n8n AI Documentation](https://docs.n8n.io/advanced-ai/)
- [n8n Workflow Templates](https://n8n.io/workflows/)
