# 🎭 RAVEN ASSISTANT - DOWNLOAD & INSTALLATION GUIDE

## 📦 Complete Package Ready!

Your Raven Desktop Assistant is complete with custom pixel art character animations!

---

## 🎨 Your Custom Raven Character

I've downloaded and organized your beautiful pixel art Raven character with all 5 expressions:

✅ **raven_idle.png** - Peaceful blinking state (95KB)
✅ **raven_blinking.png** - Eye blink animation (91KB)  
✅ **raven_thinking.png** - Processing/analyzing (81KB)
✅ **raven_talking.png** - Speaking/responding (80KB)
✅ **raven_happy.png** - Success/joy (90KB)

All images are properly sized and ready to use!

---

## 📥 HOW TO DOWNLOAD AND RUN

### Method 1: Download All Files (Recommended)

**Step 1: Download the Complete Package**

Download these files to a folder on your Windows PC:

**Core Application:**
1. `raven_assistant.py` - Main application script
2. `raven_requirements.txt` - Python dependencies
3. `check_setup.py` - System verification tool

**Documentation:**
4. `MAIN_README.md` - Overview and quick start
5. `RAVEN_README.md` - Complete user manual
6. `SETUP_GUIDE.md` - Installation & troubleshooting
7. `ASSET_GUIDE.md` - Image specifications

**Windows Scripts:**
8. `setup_raven.bat` - Automated installer
9. `start_raven.bat` - Quick launcher

**Character Assets Folder:**
10. Create folder: `raven_assets/`
11. Download all 5 images to this folder:
    - `raven_idle.png`
    - `raven_blinking.png`
    - `raven_thinking.png`
    - `raven_talking.png`
    - `raven_happy.png`

**Your folder structure should look like:**
```
RavenAssistant/
├── raven_assistant.py
├── raven_requirements.txt
├── check_setup.py
├── MAIN_README.md
├── RAVEN_README.md
├── SETUP_GUIDE.md
├── ASSET_GUIDE.md
├── setup_raven.bat
├── start_raven.bat
└── raven_assets/
    ├── raven_idle.png
    ├── raven_blinking.png
    ├── raven_thinking.png
    ├── raven_talking.png
    └── raven_happy.png
```

---

## 🚀 INSTALLATION STEPS

### Step 1: Install Ollama

1. Download Ollama from: **https://ollama.ai/download**
2. Install it on your Windows PC
3. Open Command Prompt and verify: `ollama --version`

### Step 2: Download AI Models

Open Command Prompt and run:
```bash
ollama pull llama2
ollama pull llama3.2-vision
```

**Note**: If you want to use the 'raven' model specifically:
```bash
ollama pull raven
```

If 'raven' model doesn't exist, the app will use 'llama2' by default.

### Step 3: Install Python Dependencies

**Option A - Automated (Recommended):**
```bash
cd path\to\RavenAssistant
setup_raven.bat
```

**Option B - Manual:**
```bash
cd path\to\RavenAssistant
pip install -r raven_requirements.txt
```

### Step 4: Verify Setup

```bash
python check_setup.py
```

This will check:
- ✓ Python version
- ✓ All dependencies installed
- ✓ Ollama running
- ✓ Models available
- ✓ Assets folder and images
- ✓ Memory folder

### Step 5: Launch Raven!

**Terminal 1** (keep running):
```bash
ollama serve
```

**Terminal 2**:
```bash
cd path\to\RavenAssistant
python raven_assistant.py
```

Or simply double-click: **`start_raven.bat`**

---

## 🎯 FIRST RUN CHECKLIST

- [ ] Ollama installed and running (`ollama serve`)
- [ ] AI models downloaded (`ollama list` to verify)
- [ ] Python 3.8+ installed (`python --version`)
- [ ] Dependencies installed (`pip list | findstr customtkinter`)
- [ ] All files downloaded to same folder
- [ ] `raven_assets` folder created with 5 images
- [ ] `check_setup.py` shows all green checkmarks
- [ ] Ready to launch!

---

## 🎨 ABOUT YOUR RAVEN CHARACTER

Your custom pixel art character is absolutely beautiful! The purple and blue color scheme with the cute anime style is perfect for a desktop assistant. Each expression is well-designed:

- **Idle**: Peaceful, with eyes closed - perfect for waiting state
- **Blinking**: Sweet with big sparkly eyes - great for attention
- **Thinking**: Thoughtful with hands together - shows processing
- **Talking**: Excited with open mouth - indicates speaking
- **Happy**: Delighted with finger to chin - celebrates success

The consistent style and color palette make the animations flow smoothly!

---

## 🔧 QUICK TROUBLESHOOTING

### "Cannot connect to Ollama"
```bash
# Ensure Ollama is running:
ollama serve
```

### "Model not found"
```bash
# Download the models:
ollama pull llama2
ollama pull llama3.2-vision
```

### "No module named 'customtkinter'"
```bash
# Install dependencies:
pip install -r raven_requirements.txt
```

### Images not showing
1. Verify `raven_assets` folder exists in same directory as script
2. Check all 5 PNG files are present
3. Ensure filenames are exact (lowercase, underscores)

### For detailed help, see:
- **SETUP_GUIDE.md** - Comprehensive troubleshooting
- **MAIN_README.md** - Overview and features
- **RAVEN_README.md** - Complete documentation

---

## ✨ FEATURES TO TRY FIRST

### Basic Chat
```
You: Hello Raven, who are you?
You: Tell me a joke
You: What's 2+2?
```

### Screenshot Analysis
```
Click the 📸 Screenshot button
Or type: "Take a screenshot and tell me what you see"
```

### Voice Mode
```
1. Click "🎤 Voice Mode: OFF" to enable
2. Speak: "Hello Raven"
3. She'll respond with voice!
```

### Web Search
```
You: Search for Python tutorials
You: Look up today's weather
```

### Browser Control
```
You: Open YouTube
You: Open Google
```

### WhatsApp Automation
```
You: Send a WhatsApp message saying "Hello friend"
(App will open WhatsApp - you select contact, she types)
```

### Live Vision Mode
```
1. Click "📹 Live Vision: OFF" to enable
2. Say: "Watch my screen and guide me through this task"
3. Raven takes screenshots every 5 seconds and can guide you
```

---

## 💾 WHERE YOUR DATA IS STORED

**Memory Folder**: `D:\Raven\Memory\`

Contains:
- `memory.json` - Conversation history and preferences
- `chat_YYYYMMDD_HHMMSS.txt` - Timestamped chat logs
- `screenshot_*.png` - Saved screenshots

You can change this location in the code (line 33 of `raven_assistant.py`)

---

## 🎓 LEARNING RESOURCES

**Included Documentation:**
1. **MAIN_README.md** - Start here for overview
2. **SETUP_GUIDE.md** - Detailed installation
3. **RAVEN_README.md** - Full feature documentation
4. **ASSET_GUIDE.md** - Character customization

**External Resources:**
- Ollama: https://ollama.ai/docs
- CustomTkinter: https://customtkinter.tomschimansky.com
- PyAutoGUI: https://pyautogui.readthedocs.io

---

## 🌟 WHAT MAKES YOUR RAVEN SPECIAL

✨ **100% Local & Private** - All AI runs on your PC (Ollama)
✨ **Custom Character** - Your unique pixel art design
✨ **Voice Enabled** - Talk to Raven hands-free
✨ **Vision Capable** - Can see and understand your screen
✨ **System Control** - Automates tasks for you
✨ **Smart Memory** - Remembers your conversations
✨ **Always Learning** - Web search for current info
✨ **State Animations** - Reacts visually to conversations

---

## 🔒 PRIVACY NOTES

**100% Private:**
- AI processing (all local via Ollama)
- Screenshots (saved to your disk only)
- Chat history (local files)
- Memory/preferences (local JSON)

**Requires Internet:**
- Voice recognition (Google Speech API)
- Web search (DuckDuckGo)
- WhatsApp Web (browser-based)

**You Control Your Data:**
- Delete `D:\Raven\Memory\` anytime to clear history
- No accounts or cloud sync required
- No telemetry or tracking

---

## 🎉 YOU'RE ALL SET!

Your Raven Desktop Assistant is ready to go! Just:

1. ✅ Download all files to one folder
2. ✅ Place the 5 character images in `raven_assets/` folder
3. ✅ Run `setup_raven.bat`
4. ✅ Start Ollama: `ollama serve`
5. ✅ Launch: `python raven_assistant.py`

**Quick Launch:**
```bash
start_raven.bat
```

---

## 🆘 NEED HELP?

**Run Diagnostics:**
```bash
python check_setup.py
```

**Check Documentation:**
- Installation issues → SETUP_GUIDE.md
- Feature questions → RAVEN_README.md
- General overview → MAIN_README.md

**Verify Everything:**
```bash
# Python
python --version

# Ollama
ollama --version
ollama list

# Dependencies
pip list | findstr "customtkinter pyautogui"

# Test Ollama
curl http://localhost:11434/api/tags
```

---

## 📞 SUPPORT

If you encounter any issues:

1. Run `python check_setup.py` and fix any red X's
2. Read the TROUBLESHOOTING section in SETUP_GUIDE.md
3. Check that Ollama is running: `ollama serve`
4. Verify models are installed: `ollama list`
5. Ensure all files are in the same folder

---

## 🎊 ENJOY YOUR RAVEN ASSISTANT!

Your custom AI assistant is now ready to:
- Chat intelligently
- Understand your screen
- Respond with voice
- Automate tasks
- Remember your preferences
- And express emotions with your beautiful pixel art!

**Start chatting with Raven today!** 🎭✨

---

*Built with ❤️ using Ollama, CustomTkinter, and your amazing character art*
