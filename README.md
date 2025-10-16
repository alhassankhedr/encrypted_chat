# OpenWebUI + Lorica.ai Integration

A secure integration that enables OpenWebUI to use Lorica.ai's encrypted inference service with end-to-end encryption and confidential computing protection.

## 🔒 Security Features

- **End-to-End Encryption**: Prompts are encrypted locally using Lorica OHTTP before transmission
- **Confidential Computing**: Data is processed inside secure enclaves, preventing exposure during execution
- **Transport Security**: HTTPS + OHTTP encryption for all communications
- **Encrypted Storage**: Data remains encrypted within Lorica infrastructure

## 🚀 Quick Start

### Prerequisites

- Python 3.12 (required for OpenWebUI compatibility)
- Lorica.ai API credentials (API URL, API Key, and Model ID)

### Installation

1. Clone repo and setup
   ```bash
   git clone https://github.com/alhassankhedr/encrypted_chat.git && cd encrypted_chat && bash setup.sh
   ```

2. Activate virtual environment
   ```bash
   source venv/bin/activate
   ```

3. Start OpenWebUI
   ```bash
   open-webui serve
   ```

## 📋 Configuration Steps

### 1) Add the Lorica Function

1. Open OpenWebUI in your browser (usually `http://localhost:8080`)
2. Click the user icon (top right or bottom left)
3. Go to Admin Panel
4. Click the Functions tab
5. Click Add New Function (right side)
6. Click New Function
7. Copy and paste the contents of `open_webui.py` into the code space
8. Fill in the function details:
   - Function Name: `Lorica Encrypted Inference`
   - Function ID: `lorica-ohttp`
   - Function Description: `Secure integration with Lorica.ai using OHTTP encryption and confidential computing`
9. Click Save

### 2) Configure API Credentials

1. Go back to the Functions menu
2. Find your function and click the gear icon
3. Configure:
   - LORICA_API_BASE_URL: e.g., `https://xxxxxxxx.dep.lorica.ai`
   - LORICA_API_KEY: your Lorica API key
   - MODEL_ID: the model identifier from Lorica (e.g., `org/model-name`)
4. Enable the function by toggling it on (green)

### 3) Verify Model Availability

1. Go to Settings (top)
2. Click Models
3. You should see your function name listed as an available model

### 4) Start Chatting Securely

1. Click New Chat (top left)
2. Select your configured model from the dropdown
3. Start chatting with complete privacy

## 🔧 Technical Details

### How It Works

1. Local Encryption: Prompts are encrypted using Lorica OHTTP before leaving your environment
2. Secure Transport: Data is transmitted over HTTPS + OHTTP with replay protection
3. Confidential Computing: Processing happens inside secure enclaves
4. Encrypted Storage: All data remains encrypted within Lorica infrastructure

### Architecture

```
OpenWebUI → OHTTP Encryption → Lorica.ai → Confidential Compute → Encrypted Response
```

### Security Lifecycle

- Transport Protection: HTTPS + OHTTP encryption
- Compute Protection: Confidential computing enclaves
- Replay Protection: Built into OHTTP protocol

## 📁 Project Structure

```
openwebui-lorica/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── setup.sh               # Automated setup script
├── open_webui.py          # Lorica OHTTP pipe implementation
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
├── CONTRIBUTING.md        # Contribution guidelines
```

## 🛠️ Development

Requirements: Python 3.12+, OpenWebUI, Lorica Python SDK

Local steps:
- Create virtual environment
- `pip install -r requirements.txt`
- Edit `open_webui.py`
- Test with OpenWebUI

## 🤝 Contributing

We welcome contributions. Please fork, branch, and open a PR.

## 📄 License

MIT License. See `LICENSE`.

## 🆘 Support

- Issues: https://github.com/alhassankhedr/encrypted_chat/issues
- Lorica Docs: https://docs.lorica.ai
- OpenWebUI Docs: https://docs.openwebui.com

## 🙏 Acknowledgments

- Open-WebUI
- Lorica.ai
- The open source community
