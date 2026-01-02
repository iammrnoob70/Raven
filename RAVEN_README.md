# Raven Desktop Assistant

A powerful AI-powered desktop assistant with vision, voice, and system automation capabilities.

## Features

- **CustomTkinter GUI**: Modern, semi-transparent overlay interface
- **State-Based Animations**: Visual feedback with Idle, Blinking, Thinking, Talking, and Happy states
- **Voice Interaction**: Speech recognition input and text-to-speech output
- **Vision Capabilities**: 
  - Screenshot analysis using Ollama's llama3.2-vision
  - Live Vision mode (continuous screen monitoring)
- **System Automation**: 
  - PyAutoGUI for mouse and keyboard control
  - WhatsApp messaging automation
  - Browser control
- **Web Search**: Integrated DuckDuckGo search
- **Memory System**: JSON-based conversation history and preferences
- **Chat History**: All conversations saved to timestamped .txt files

## Prerequisites

### 1. Install Ollama
Download and install Ollama from: https://ollama.ai

### 2. Pull Required Models
```bash
# Pull the Raven model (or use an alternative like llama2)
ollama pull raven

# Pull the vision model
ollama pull llama3.2-vision

# If 'raven' model is not available, you can use:
# ollama pull llama2
# Then change self.text_model = "llama2" in the code
```

### 3. Start Ollama Server
```bash
ollama serve
```

## Installation

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Assets Folder
Create a folder named `raven_assets` in the same directory as the script, and place your 5 state images:

```
raven_assets/
├── raven_idle.png
├── raven_blinking.png
├── raven_thinking.png
├── raven_talking.png
└── raven_happy.png
```

**Note**: If images are not provided, the app will use emoji placeholders.

### 3. Configure Memory Path (Optional)
By default, memory is saved to `D:/Raven/Memory`. To change this, edit line 33 in `raven_assistant.py`:
```python
self.memory_path = "D:/Raven/Memory"  # Change to your preferred path
```

## Usage

### Running the Assistant
```bash
python raven_assistant.py
```

### Basic Chat
- Type your message in the input box and press Enter or click Send
- Raven will respond using the Ollama AI model
- All conversations are automatically saved

### Voice Mode
1. Click the "🎤 Voice Mode" button to enable
2. Speak your question/command
3. Raven will respond with both text and speech

### Vision Features

**Take Screenshot:**
- Click the "📸 Screenshot" button
- Or type "take a screenshot" or "what do you see"
- Raven will analyze and describe what's on your screen

**Live Vision Mode:**
1. Click "📹 Live Vision" to enable
2. Raven will take screenshots every 5 seconds
3. Use this for real-time guidance: "Watch my screen and help me..."

### System Automation

**WhatsApp Messaging:**
```
You: "Send a WhatsApp message saying Hello"
```
- Raven will open WhatsApp Web
- You have 5 seconds to select the contact
- Raven will type and send the message

**Open Websites:**
```
You: "Open YouTube"
You: "Open Google"
You: "Open gmail"
```

**Web Search:**
```
You: "Search for Python tutorials"
You: "Look up weather in New York"
```

## GUI Controls

- **Voice Mode Toggle**: Enable/disable voice input and output
- **Vision Mode Toggle**: Enable vision-enhanced responses
- **Live Vision Toggle**: Continuous screen monitoring (5-second intervals)
- **Screenshot Button**: Instant screen capture and analysis

## State Animations

Raven's visual state changes based on activity:
- **Idle/Blinking**: Waiting for input (cycles automatically)
- **Thinking**: Processing your request
- **Talking**: Delivering a response
- **Happy**: Successful completion or positive sentiment

## File Structure

```
project/
├── raven_assistant.py          # Main application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── raven_assets/              # State images (user-provided)
│   ├── raven_idle.png
│   ├── raven_blinking.png
│   ├── raven_thinking.png
│   ├── raven_talking.png
│   └── raven_happy.png
└── D:/Raven/Memory/           # Memory and chat logs
    ├── memory.json
    ├── chat_YYYYMMDD_HHMMSS.txt
    └── screenshot_*.png
```

## Memory System

**Location**: `D:/Raven/Memory/`

- **memory.json**: Stores last 100 messages and preferences
- **chat_*.txt**: Timestamped chat logs for each session
- **screenshot_*.png**: Saved screenshots with timestamps

Memory is automatically loaded on startup and saved on exit.

## Customization

### Change AI Models
Edit lines 38-39 in `raven_assistant.py`:
```python
self.text_model = "raven"  # Change to "llama2", "mistral", etc.
self.vision_model = "llama3.2-vision"  # Change to "llava", "bakllava"
```

### Adjust TTS Settings
Edit lines 45-46:
```python
self.tts_engine.setProperty('rate', 150)    # Speech speed
self.tts_engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
```

### Modify Window Appearance
Edit lines 18-22:
```python
self.root.geometry("800x900")                # Window size
self.root.attributes('-alpha', 0.95)        # Transparency (0.0 to 1.0)
self.root.attributes('-topmost', True)      # Always on top
```

## Troubleshooting

### "Cannot connect to Ollama"
- Ensure Ollama is installed and running: `ollama serve`
- Check that required models are pulled: `ollama list`

### "Model not found"
- Pull the required model: `ollama pull raven` or `ollama pull llama2`
- Update the model name in code if using alternative models

### Voice Recognition Not Working
- Check microphone permissions
- Ensure internet connection (Google Speech Recognition requires it)
- Adjust ambient noise: The app auto-adjusts, but very noisy environments may cause issues

### Screenshots Not Working
- Ensure PyAutoGUI has necessary permissions
- On some systems, you may need to run as administrator

### WhatsApp Automation Issues
- Ensure WhatsApp Web is accessible
- Give enough time for the page to load
- Manually select the contact when prompted

## Security & Privacy

- **Local Processing**: All AI processing happens locally via Ollama
- **No Cloud**: Conversations stay on your machine
- **Memory Control**: You can delete memory files anytime from `D:/Raven/Memory/`
- **Screenshot Privacy**: Screenshots are saved locally and never uploaded

## Advanced Features

### Custom Commands
You can extend the `process_message` method to add custom commands:

```python
if "custom_command" in user_input.lower():
    self.handle_custom_command(user_input)
    return
```

### Integration with Other Apps
The PyAutoGUI automation can be extended to control any application on your system.

## Known Limitations

- WhatsApp automation requires manual contact selection
- Voice recognition requires internet connection (uses Google API)
- Live Vision mode can be resource-intensive
- Some antivirus software may flag PyAutoGUI automation

## Credits

Created using:
- CustomTkinter for modern GUI
- Ollama for local AI processing
- PyAutoGUI for system automation
- SpeechRecognition & pyttsx3 for voice features

## License

Free to use and modify for personal projects.

---

**Need Help?**
- Check Ollama documentation: https://ollama.ai/docs
- Verify all dependencies are installed: `pip list`
- Ensure Ollama server is running: `ollama serve`
