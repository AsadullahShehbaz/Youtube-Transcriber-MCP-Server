# 🎬 YouTube Transcriber MCP Server

A powerful Model Context Protocol (MCP) server that fetches transcripts from YouTube videos. Perfect for students, researchers, and content creators who need quick access to video transcripts!

## ✨ Features

- 📝 Extract transcripts from any YouTube video with captions
- 🌍 Supports multiple languages (English, German, Hindi, Urdu)
- 🔄 Automatic fallback method if primary extraction fails
- 🧹 Clean formatting with timestamp removal
- ☁️ Hosted on FastMCP Cloud - no setup required!

## 🚀 Quick Start (3 Easy Steps!)

### Step 1: Install Claude Desktop

If you haven't already, download and install Claude Desktop from [claude.ai](https://claude.ai/download)

### Step 2: Configure the MCP Server

1. **Find your Claude configuration file:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Open the file** in any text editor (Notepad, TextEdit, VS Code, etc.)

3. **Add this configuration:**

```json
{
  "mcpServers": {
    "youtube-transcriber": {
      "url": "https://youtubetranscriber.fastmcp.app/mcp"
    }
  }
}
```

**Note**: If you already have other MCP servers configured, just add the `"youtube-transcriber"` section inside the existing `"mcpServers"` object.

### Step 3: Restart Claude Desktop

Close Claude Desktop completely and reopen it. You're done! 🎉

## 🎯 How to Use

Once configured, simply chat with Claude and ask it to transcribe YouTube videos. Here are some examples:

### Example 1: Get a Transcript
```
Can you get the transcript of this YouTube video?
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Example 2: Summarize a Video
```
Please transcribe this video and give me a summary:
https://www.youtube.com/watch?v=VIDEO_ID
```

### Example 3: Extract Key Points
```
Get the transcript from this tutorial and list the main steps:
https://www.youtube.com/watch?v=VIDEO_ID
```

### Example 4: Clean Transcript
```
Fetch the transcript and remove all timestamps:
https://www.youtube.com/watch?v=VIDEO_ID
```

## 🛠️ Available Tools

The server provides three powerful tools that Claude can use automatically:

### 1. `get_api_transcript`
- **Primary method** for fetching transcripts
- Fast and reliable
- Works with videos that have official captions

### 2. `get_tactiq_transcript`
- **Fallback method** when the API fails
- Scrapes transcript from Tactiq.io
- Slower but more comprehensive

### 3. `clean_transcript`
- Removes timestamps from raw transcript text
- Makes the output cleaner and easier to read

## 📋 Requirements

**For Users**: 
- Claude Desktop app (that's it!)

**For Developers** (if running locally):
- Python 3.8+
- Dependencies: `fastmcp`, `selenium`, `youtube-transcript-api`, `beautifulsoup4`, `webdriver-manager`

## ❓ Troubleshooting

### Server Not Working?

1. **Check Configuration**: Make sure your `claude_desktop_config.json` is properly formatted (valid JSON)
2. **Restart Claude**: Always restart Claude Desktop after making config changes
3. **Test with a Popular Video**: Try a well-known video with confirmed captions first
4. **Check Video Has Captions**: Not all videos have transcripts available

### Common Issues

**"No captions available"**
- The video doesn't have captions enabled
- Try another video or ask the creator to enable captions

**Server appears disconnected**
- Check your internet connection
- Verify the URL is exactly: `https://youtubetranscriber.fastmcp.app/mcp`
- Restart Claude Desktop

**Transcript looks messy**
- Ask Claude to "clean the transcript and remove timestamps"
- The `clean_transcript` tool will format it nicely

## 🎓 Use Cases

Perfect for:
- 📚 **Students**: Transcribe lectures and study videos
- 🔬 **Researchers**: Extract information from video content
- ✍️ **Content Creators**: Get transcripts for subtitles or blog posts
- 🌐 **Translators**: Work with video content in multiple languages
- ♿ **Accessibility**: Make video content available as text

## 🔒 Privacy & Limits

- This server doesn't store any transcripts
- All processing happens in real-time
- Respects YouTube's terms of service
- Only works with publicly available videos that have captions

## 💡 Pro Tips

1. **Be Specific**: Tell Claude exactly what you want (summary, key points, full transcript, etc.)
2. **Multiple Languages**: The server supports English, German, Hindi, and Urdu - just ask!
3. **Combine with Analysis**: After getting a transcript, ask Claude to analyze, summarize, or answer questions about it
4. **Batch Processing**: You can ask Claude to transcribe multiple videos in one conversation

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to open an issue on the repository!

## 📄 License

This project is provided as-is for educational and personal use.

## 🌟 Support

If you find this useful, give it a star ⭐ and share it with others who might benefit!

---

**Happy Transcribing! 🎉**

Need help? Just ask Claude - it knows how to use this server!