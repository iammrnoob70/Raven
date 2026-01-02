# RAVEN ASSISTANT - QUICK SETUP GUIDE

## 📋 What You'll Need

1. **Windows PC** (Windows 10/11)
2. **Python 3.8+** installed
3. **Ollama** installed locally
4. **5 State Images** (your Raven character PNGs)
5. **Microphone** (optional, for voice mode)

---

## 🚀 QUICK START (5 Steps)

### Step 1: Install Ollama
1. Download Ollama: https://ollama.ai/download
2. Run the installer
3. Open Command Prompt and verify: `ollama --version`

### Step 2: Download AI Models
Open Command Prompt and run:
```bash
ollama pull raven
ollama pull llama3.2-vision
```

**Note**: If 'raven' model doesn't exist, use an alternative:
```bash
ollama pull llama2
```
Then edit line 38 in `raven_assistant.py` to say `self.text_model = "llama2"`

### Step 3: Install Python Dependencies
Run the setup script:
```bash
setup_raven.bat
```

Or manually:
```bash
pip install -r raven_requirements.txt
```

### Step 4: Add Your Raven Images
1. Create a folder called `raven_assets` in the same location as `raven_assistant.py`
2. Place these 5 PNG files inside:
   - `raven_idle.png` - Default resting state
   - `raven_blinking.png` - Blink animation
   - `raven_thinking.png` - Processing/thinking
   - `raven_talking.png` - Speaking/responding
   - `raven_happy.png` - Success/positive emotion

**Example structure:**
```
your_folder/
├── raven_assistant.py
├── raven_requirements.txt
├── RAVEN_README.md
├── setup_raven.bat
├── start_raven.bat
└── raven_assets/
    ├── raven_idle.png
    ├── raven_blinking.png
    ├── raven_thinking.png
    ├── raven_talking.png
    └── raven_happy.png
```

### Step 5: Start Ollama and Run Raven

**Terminal 1** (keep this running):
```bash
ollama serve
```

**Terminal 2**:
```bash
python raven_assistant.py
```

Or simply double-click: `start_raven.bat`

---

## 🎯 FIRST TIME USAGE

### Testing Basic Chat
1. Type in the input box: "Hello Raven"
2. Press Enter
3. Wait for response (watch the thinking animation!)

### Testing Screenshot Feature
1. Click the "📸 Screenshot" button
2. Raven will capture and analyze your screen
3. Response appears in chat

### Testing Voice Mode
1. Click "🎤 Voice Mode: OFF" to turn it ON
2. Speak clearly into your microphone
3. Raven will transcribe and respond with voice

### Testing WhatsApp Automation
1. Type: "Send a WhatsApp message saying Hello friend"
2. WhatsApp Web will open
3. Select the contact within 5 seconds
4. Raven will type and send the message

---

## ⚙️ CONFIGURATION

### Change Memory Location
Edit line 33 in `raven_assistant.py`:
```python
self.memory_path = "D:/Raven/Memory"  # Change to your preferred path
```

### Use Different AI Models
Edit lines 38-39:
```python
self.text_model = "llama2"           # Try: llama2, mistral, gemma
self.vision_model = "llava"          # Try: llava, bakllava
```

### Adjust Window Size
Edit line 18:
```python
self.root.geometry("800x900")  # Width x Height
```

### Adjust Transparency
Edit line 21:
```python
self.root.attributes('-alpha', 0.95)  # 0.0 (invisible) to 1.0 (opaque)
```

---

## 🔧 TROUBLESHOOTING

### Issue: "Cannot connect to Ollama"
**Solution:**
1. Ensure Ollama is installed: `ollama --version`
2. Start the server: `ollama serve`
3. Test connection: `curl http://localhost:11434/api/tags`

### Issue: "Model 'raven' not found"
**Solution:**
1. Check available models: `ollama list`
2. If 'raven' is missing, pull an alternative: `ollama pull llama2`
3. Update the code (line 38) to use the model you pulled

### Issue: "No module named 'customtkinter'"
**Solution:**
```bash
pip install customtkinter
```

Or install all dependencies:
```bash
pip install -r raven_requirements.txt
```

### Issue: Voice mode not working
**Solution:**
1. Check microphone permissions in Windows Settings
2. Ensure internet connection (Google Speech Recognition needs it)
3. Try speaking louder or closer to the microphone
4. Check Windows microphone settings (not muted)

### Issue: Screenshot shows black screen
**Solution:**
1. Run the script as Administrator
2. Check Windows Privacy settings → Allow apps to take screenshots
3. Some games/protected content may block screenshots

### Issue: Images not showing (only emojis)
**Solution:**
1. Verify images are in `raven_assets/` folder
2. Check filenames exactly match:
   - `raven_idle.png`
   - `raven_blinking.png`
   - `raven_thinking.png`
   - `raven_talking.png`
   - `raven_happy.png`
3. Ensure files are PNG format
4. Check file permissions (read access)

### Issue: WhatsApp automation not working
**Solution:**
1. Ensure you have WhatsApp Web access
2. Wait for page to fully load (default is 5 seconds)
3. Have your browser open and ready
4. Select the contact quickly when prompted

### Issue: High CPU usage in Live Vision mode
**Solution:**
Live Vision mode takes screenshots every 5 seconds, which is intensive.
- Use it sparingly
- Turn it off when not needed
- Increase interval by editing the code (line 410): `time.sleep(5)` → `time.sleep(10)`

---

## 🎨 IMAGE SPECIFICATIONS

### Recommended Image Settings
- **Format**: PNG with transparency
- **Dimensions**: 300x300 to 500x500 pixels (will auto-resize)
- **Style**: Pixel art, anime, cartoon, or realistic
- **Background**: Transparent or solid color

### Creating State Images
If you don't have state images yet:
1. Use AI image generators (DALL-E, Midjourney, Stable Diffusion)
2. Commission an artist
3. Create pixel art using tools like Aseprite or Piskel
4. Use the placeholder emojis (app works without images)

**Prompt example for AI generation:**
```
"Pixel art character named Raven, [state description], transparent background, 
cute anime style, purple and black colors, side view"
```

States to generate:
- **Idle**: Calm, neutral expression
- **Blinking**: Eyes closed or half-closed
- **Thinking**: Thought bubble or thinking pose
- **Talking**: Mouth open, cheerful expression
- **Happy**: Big smile, excited expression

---

## 🎮 USAGE EXAMPLES

### Example Conversations

**General Chat:**
```
You: What's the weather like today?
Raven: [Searches web and provides weather info]

You: Tell me a joke
Raven: [Generates a joke using AI]
```

**Vision Commands:**
```
You: Take a screenshot and tell me what you see
Raven: [Captures screen and describes it]

You: Watch my screen and help me with this task
Raven: [Enables Live Vision mode]
```

**Automation:**
```
You: Open YouTube
Raven: [Opens YouTube in browser]

You: Search for Python tutorials
Raven: [Performs web search and shows results]

You: Send a WhatsApp message saying "Meeting at 3pm"
Raven: [Opens WhatsApp and types the message]
```

**Voice Interaction:**
```
[Enable Voice Mode]
You: "Hello Raven, how are you?"
Raven: "I'm doing well! How can I help you today?" [speaks response]
```

---

## 📊 PERFORMANCE TIPS

### Optimize Response Speed
1. Use smaller AI models (llama2 is faster than larger models)
2. Close other heavy applications
3. Disable Live Vision when not needed
4. Reduce screenshot quality if needed

### Reduce Memory Usage
1. Close voice mode when not using it
2. Restart the app periodically (memory auto-saves)
3. Clear old screenshots from `D:/Raven/Memory/`

### Battery Saving (Laptops)
1. Use text mode instead of voice
2. Disable Live Vision
3. Reduce AI model size
4. Lower transparency (less GPU usage)

---

## 🔒 PRIVACY & SECURITY

✅ **What stays private:**
- All AI processing (Ollama is local)
- Screenshots (saved locally only)
- Chat history (stored on your disk)
- Memory/preferences (JSON file on your PC)

⚠️ **What needs internet:**
- Voice recognition (Google Speech API)
- Web search (DuckDuckGo)
- WhatsApp Web automation
- Opening web links

🛡️ **Security notes:**
- No data sent to external servers (except voice recognition and web search)
- You can run Raven completely offline (disable voice mode)
- All files accessible only to you
- Delete `D:/Raven/Memory/` anytime to clear history

---

## 🆘 STILL NEED HELP?

### Check These Files
1. **RAVEN_README.md** - Full documentation
2. **raven_assistant.py** - Main code (readable and commented)
3. **Ollama documentation** - https://ollama.ai/docs

### Verify Installation
Run this diagnostic:
```bash
# Check Python
python --version

# Check Ollama
ollama --version
ollama list

# Check dependencies
pip list | findstr "customtkinter pyautogui requests"

# Test Ollama
curl http://localhost:11434/api/tags
```

### Common Fixes Checklist
- [ ] Ollama is installed
- [ ] Ollama server is running (`ollama serve`)
- [ ] Models are downloaded (`ollama list`)
- [ ] Python dependencies installed (`pip install -r raven_requirements.txt`)
- [ ] Images placed in `raven_assets/` folder
- [ ] Memory folder exists (`D:/Raven/Memory/`)

---

## 🎉 YOU'RE ALL SET!

Start Raven and enjoy your AI assistant! Remember:
1. Keep Ollama running in the background
2. Place your state images in the assets folder
3. Speak clearly in voice mode
4. Have fun automating tasks!

**Quick launch command:**
```bash
start_raven.bat
```

Happy chatting with Raven! 🎭
