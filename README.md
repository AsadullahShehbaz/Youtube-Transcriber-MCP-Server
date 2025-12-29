
# 🎥 YouTube Transcript MCP Server

A **beginner-friendly** Model Context Protocol (MCP) server that extracts **YouTube video transcripts** using multiple methods. Perfect for AI/ML students building RAG systems, LLM agents, or transcript analysis projects.

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-ready-green.svg)](https://github.com/jlowin/fastmcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Primary Method**: Fast YouTube Transcript API (supports English, German, Hindi, Urdu)
- **Fallback Method**: Selenium scraping via Tactiq.io (works when API fails)
- **Text Cleaning**: Automatically removes timestamps
- **Production Ready**: Headless Chrome with optimized options
- **Easy MCP Integration**: Connects to any LLM agent or AI application

## 🛠️ Quick Start (2 Minutes)

### 1. Clone & Install
```
git clone <your-repo-url>
cd youtube-transcript-mcp
pip install -r requirements.txt
```

### 2. Run Server
```
python main.py
```
Server starts at `http://127.0.0.1:8000`

### 3. Test in Browser
Visit `http://127.0.0.1:8000` to see available tools!

## 🔗 Available Tools

| Tool | Description | Input | Output |
|------|-------------|-------|--------|
| `get_api_transcript` | Fast API method (primary) | YouTube URL | `{"transcript": "text"}` or `{"error": "message"}` |
| `get_tactiq_transcript` | Selenium fallback | YouTube URL | Raw transcript text |
| `clean_transcript` | Remove timestamps | Raw transcript | Clean text |

## 💻 Example Usage

### With Claude Desktop / Cursor
1. Add to your MCP config:
```
http://127.0.0.1:8000
```

2. Ask your AI:
```
"Get the transcript for this video and summarize it: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Python Client Example
```
from mcp.client import MCPClient

client = MCPClient("http://127.0.0.1:8000")
result = client.call_tool("get_api_transcript", {"url": "https://youtube.com/watch?v=VIDEO_ID"})
print(result["transcript"])
```

## 📦 Installation

### Local Development
```
# Clone repo
git clone <repo-url>
cd youtube-transcript-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Production (Docker) - Coming Soon!

## 🗄️ Requirements File
```
fastmcp>=0.1.0
selenium>=4.15.0
webdriver-manager>=4.0.0
youtube-transcript-api>=0.6.1
beautifulsoup4>=4.12.0
requests>=2.31.0
```

**Note**: Chrome browser auto-installs via `webdriver-manager`

## ⚙️ Configuration

### Environment Variables
```
# Optional: Custom host/port
MCP_HOST=0.0.0.0
MCP_PORT=8001

# Run with custom config
MCP_HOST=0.0.0.0 MCP_PORT=8001 python main.py
```

### Chrome Options (Already Optimized)
- ✅ Headless mode
- ✅ No sandbox (Docker-friendly)
- ✅ Anti-detection user agent
- ✅ Muted audio
- ✅ Optimized memory/performance

## 🧪 Testing Your Server

### 1. Health Check
```
curl http://127.0.0.1:8000/health
```

### 2. List Tools
```
curl http://127.0.0.1:8000/tools
```

### 3. Test Transcript
```
curl -X POST http://127.0.0.1:8000/call \
  -H "Content-Type: application/json" \
  -d '{"tool": "get_api_transcript", "arguments": {"url": "https://youtube.com/watch?v=dQw4w9WgXcQ"}}'
```

## 🎯 Use Cases for CS Students

1. **RAG Pipeline**: Feed transcripts to your LangChain/VectorDB
2. **Video Summarization**: LLM + Transcript = Instant summaries
3. **Multilingual Analysis**: Supports 4+ languages
4. **Portfolio Project**: Production-grade MCP server
5. **Agentic Workflow**: Multi-tool transcript pipeline

## 🚀 Example Workflow

```
YouTube URL → get_api_transcript() → [Success?] → clean_transcript()
                        ↓ No
                 get_tactiq_transcript() → clean_transcript()
                        ↓
                   ✅ Clean Transcript Ready!
```

## 🔍 Troubleshooting

| Issue | Solution |
|-------|----------|
| `Chrome not found` | `webdriver-manager` auto-downloads |
| `Port 8000 busy` | `MCP_PORT=8001 python main.py` |
| `No captions` | Falls back to Tactiq automatically |
| `Selenium timeout` | Video might need manual captions enabled |
| `Permission denied` | Add `--no-sandbox` (already included) |

## 📱 Deploy Anywhere

### Railway/Render
```
# Just set PORT env var
PORT=10000 python main.py
```

### Google Colab
```
!pip install -r requirements.txt
!python main.py &
# Access via ngrok
```

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License
MIT License - Use freely in your projects!

## 👨‍💻 Author
**Asadullah Shehbaz** - CS Student | AI/ML Enthusiast | 8th Semester BSCS

## 🌟 Star & Share
Help other students! ⭐ **Star this repo** and share with your batchmates.

---

**Built with ❤️ for CS students building their first production MCP server**

