# 🔐 OpenWebUI + Lorica.ai Integration

> 💬 **TL;DR:** Run your own ChatGPT-style interface connected to **Lorica.ai’s encrypted inference API** —  
> all your prompts and responses stay **private**, even from the service provider.

A privacy-first integration that connects **OpenWebUI** with **Lorica.ai** using **Oblivious HTTP (OHTTP)** and **Confidential Computing** — ensuring that even the server cannot see or log your data.

---

## 🔒 Security Features

- **End-to-End Encryption (via OHTTP)** — prompts are encrypted *before* leaving your environment  
- **Confidential Computing** — data is processed inside hardware-secured enclaves (Azure + NVIDIA H100)  
- **Transport Security** — HTTPS + OHTTP with replay protection  
- **Encrypted Storage** — data remains encrypted at rest within Lorica infrastructure  

---

## 🚀 Quick Start

### Prerequisites

- Python **3.12** (required for OpenWebUI compatibility)
- Lorica.ai API credentials (`LORICA_API_BASE_URL`, `LORICA_API_KEY`, `MODEL_ID`)

> **Compatibility:** This project is compatible with Unix-based systems (macOS and Linux).  
> It has not been tested on Windows Subsystem for Linux (WSL) or Docker on Windows.

---

### Installation

```bash
git clone https://github.com/alhassankhedr/encrypted_chat.git
cd encrypted_chat
bash setup.sh
```

Activate the environment:

```bash
source venv/bin/activate
```

Then start OpenWebUI:

```bash
open-webui serve
```

---

## 🧪 Try the Public Demo

You can test Lorica.ai's confidential inference endpoint for a limited time using these credentials:

```bash
LORICA_API_BASE_URL=https://e4d9a526.dep.lorica.ai
LORICA_API_KEY=w98Ahk2n.KvOwfLuFYodGkmsZJ5PoKy7tCm8Rqp7S
MODEL_ID=cortecs/Llama-3.3-70B-Instruct-FP8-Dynamic
```

> 🧩 This runs on **Azure Confidential Computing** with **NVIDIA H100 GPUs** —  
> all prompts and responses are processed inside secure enclaves.

---

## ⚙️ Configuration Steps

### 1️⃣ Add the Lorica Function

1. Open OpenWebUI in your browser (default: `http://localhost:8080`)
2. Create an admin account (if not already)
3. Click your user icon → **Admin Panel**
4. Navigate to **Functions → Add New Function**
5. Click **New Function**
6. Copy and paste the contents of `open_webui.py` into the code editor
7. Fill in:
   - **Function Name:** `Lorica Encrypted Inference`
   - **Function ID:** `lorica-ohttp`
   - **Description:** `Secure integration with Lorica.ai using OHTTP and Confidential Computing`
8. Click **Save**

---

### 2️⃣ Configure API Credentials

1. In the **Functions** list, click the ⚙️ gear icon beside your function  
2. Set the following environment variables:

```bash
LORICA_API_BASE_URL=https://your-endpoint.dep.lorica.ai
LORICA_API_KEY=your-api-key
MODEL_ID=org/model-name
```

3. Enable the function (toggle to green ✅)

---

### 3️⃣ Verify Model Availability

- Go to **Settings → Models**
- Confirm your function appears as an available model

---

### 4️⃣ Start Chatting Securely

- Click **New Chat**
- Select your configured model
- Start chatting — all data stays encrypted end-to-end 🔐

---

## 🧠 How It Works

1. **Local Encryption** — Prompts are encrypted with Lorica’s OHTTP client before leaving your device  
2. **Oblivious Routing** — Requests pass through a proxy that hides your identity and destination  
3. **Secure Execution** — Model inference runs inside a **Confidential VM (H100 enclave)**  
4. **Encrypted Response** — Results are encrypted back to your client for decryption  

```
🧑‍💻 OpenWebUI  
   ↓ (OHTTP Encryption)
🌐 Lorica Gateway
   ↓ (Secure Channel)
🖥️ Enclave Runtime (Confidential Compute)
   ↓  
🔒 Encrypted Response → User
```

---

## 🧰 Project Structure

```
encrypted_chat/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── setup.sh               # Automated setup script
├── open_webui.py          # Lorica OHTTP integration
├── examples/              # Example code
│   └── lorica_ohttp_example.py  # Direct API usage example
├── LICENSE                # MIT License
├── .gitignore             # Ignored files
├── CONTRIBUTING.md        # Contribution guidelines
```

---

## 🧑‍💻 Development

**Requirements:** Python 3.12, OpenWebUI, Lorica Python SDK

Local workflow:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then modify `open_webui.py` as needed and test your integration.

---

## 📝 Examples

For a direct API usage example (without OpenWebUI), see `examples/lorica_ohttp_example.py`.  
This demonstrates how to use the `lorica` OHTTP library directly to make encrypted API calls.

```bash
python examples/lorica_ohttp_example.py
```

---

## 💡 Why Lorica?

Lorica.ai enables **confidential AI inference** on Nvidia GPU enclaves using **Confidential Computing** and **Oblivious HTTP**.  
This architecture ensures full data privacy — no plaintext ever leaves your environment, and not even Lorica can decrypt your prompts or results.

---

## 🤝 Contributing

We welcome contributions!  
Please fork the repo, create a branch, and open a PR.

---

## 📄 License

MIT License — see `LICENSE` for details.

---

## 🆘 Support

- Issues: [https://github.com/alhassankhedr/encrypted_chat/issues](https://github.com/alhassankhedr/encrypted_chat/issues)  
- Docs: [https://docs.lorica.ai](https://docs.lorica.ai)  
- OpenWebUI: [https://docs.openwebui.com](https://docs.openwebui.com)

---

## 🙏 Acknowledgments

- [Open-WebUI](https://github.com/open-webui/open-webui)  
- [Lorica.ai](https://lorica.ai)  
- The open-source community 💜
