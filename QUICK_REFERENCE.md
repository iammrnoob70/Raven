# 🚀 RAVEN v2.0 - QUICK REFERENCE CARD

## ⚡ QUICK START (3 COMMANDS)

```bash
# 1. Install Ollama models (one-time setup)
ollama pull llama3.2 && ollama pull llama3.2-vision && ollama cp llama3.2 Raven

# 2. Install Python dependencies (one-time setup)
pip install -r raven_requirements.txt

# 3. Run Raven (every time)
ollama serve                    # Terminal 1 (keep running)
python raven_assistant.py       # Terminal 2
```

---

## 🎮 CONTROL BUTTONS

| Button | Function |
|--------|----------|
| 🎤 Voice | Toggle voice input/output |
| 👁 Vision | Auto-capture screen with every message |
| 📸 Capture | Take screenshot on demand |
| 🗑 Clear | Clear chat display |

---

## 🤖 VOICE COMMANDS

Say these naturally:

### Time & Date:
- "What time is it?"
- "What day is today?"

### Open Apps:
- "Open Chrome"
- "Open WhatsApp"
- "Open VS Code"
- "Open Notepad"

### Search:
- "Search for Python tutorials"
- "Look up AI news"

### Type Text:
- "Type this: Hello World"

### System:
- "Minimize everything"

---

## 🎨 STATE COLORS

Watch the border glow to see Raven's state:

| Color | State | Meaning |
|-------|-------|---------|
| 🟢 Green | Listening | Voice mode active |
| 🟣 Purple | Thinking | Processing your request |
| 🔵 Cyan | Talking | Delivering response |
| 🟡 Yellow | Happy | Success! |
| ⚫ Grey | Idle | Waiting for you |

---

## 📁 FILE LOCATIONS

```
D:/Raven/Memory/
  ├── history.json                    ← Conversation memory (20 messages)
  ├── chat_20250102_143015.txt        ← Session log
  └── screenshot_20250102_143015.png  ← Screen captures (last 20)
```

---

## 🎨 CHARACTER IMAGES

Place in `raven_assets/` folder:
- `raven_idle.png` - Waiting
- `raven_listening.png` - Voice active
- `raven_thinking.png` - Processing
- `raven_talking.png` - Responding
- `raven_happy.png` - Success

*Missing images? No problem - emoji fallback!*

---

## 🔧 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "Cannot connect to Ollama" | Start: `ollama serve` |
| "Model not found" | Install: `ollama pull llama3.2` |
| "Mic Unavailable" | Check Windows microphone permissions |
| No images showing | Check `raven_assets/` folder exists |
| Vision not working | Toggle "👁 Vision: ON" button |

**Pro tip**: All technical errors appear in the terminal with `[Terminal]` prefix. Chat stays clean!

---

## 📊 USAGE EXAMPLES

### Basic Chat:
```
You: Hello Raven!
Raven: Good morning! Hope your Monday is going well. How can I help?
```

### Vision Mode:
```
[Click "👁 Vision: ON"]
You: What's on my screen?
Raven: I can see you have VS Code open with Python code...
```

### Voice Mode:
```
[Click "🎤 Voice: ON"]
[Green glow appears]
You: [Speak] "Search for Python tutorials"
Raven: [Opens browser and searches]
```

### Commands:
```
You: What time is it?
Raven: The current time is 3:45 PM.

You: Open Chrome
Raven: Opening chrome...

You: Minimize everything
Raven: All windows minimized.
```

---

## 💾 MEMORY SYSTEM

Raven remembers your last 20 messages:

```
Session 1 (Monday):
You: My favorite color is purple
Raven: Got it!
[Close]

Session 2 (Tuesday):
[Raven loads memory automatically]
You: What's my favorite color?
Raven: Purple! You told me yesterday.
```

---

## 🎯 PRO TIPS

1. **Vision + Voice**: Enable both for hands-free screen help
2. **Memory**: Raven remembers across sessions
3. **Screenshots**: Auto-cleaned (keeps last 20 only)
4. **Terminal**: Watch for technical info
5. **Commands**: Speak naturally, no rigid syntax

---

## 📝 MODEL INFO

- **Text**: `Raven` (your custom llama3.2)
- **Vision**: `llama3.2-vision`
- **Memory**: `D:/Raven/Memory/history.json`

---

## 🆘 NEED HELP?

1. Check terminal for `[Terminal]` messages
2. Run: `python validate_raven.py`
3. Read: `UPGRADE_README.md` (full guide)
4. Read: `FINAL_DELIVERY.md` (technical details)

---

## 🎉 ENJOY!

**Your AI assistant is ready!**

- ✅ Modular architecture
- ✅ 20-message memory
- ✅ Time-aware greetings
- ✅ Auto vision capture
- ✅ 6 system commands
- ✅ Silent logs
- ✅ Voice stability

**v2.0 - Production Ready** 🚀

---

*Print this card for quick reference while using Raven!*
