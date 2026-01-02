# 🦅 Raven Assistant - Quick Start Guide

## Launch Application
```bash
cd /app
python raven_assistant.py
```

## Voice Commands to Test

### Language Switching
- **"English"** → Switches to 100% English mode
- **Speak any Bengali** → Automatically switches back to Banglish mode
- Language preference is saved and restored on restart

### WhatsApp Commands
- **"Open WhatsApp"** → Opens WhatsApp Web directly (no number needed)
- **"Send message to mom"** → Opens chat with saved contact + auto-sends in 2 seconds
- **"Send message to [unknown name]"** → Helpful guidance message

### System Commands
- **"What time is it?"** → Current time
- **"What's the date?"** → Current date
- **"Search for [topic]"** → Google search
- **"Open Chrome/VS Code/Calculator"** → Opens application
- **"Minimize everything"** → Show desktop

### Vision Commands
- **Click "📸 Capture"** → Screenshot analysis
- **Enable "👁 Vision"** → Automatic screen context in every response

### Voice Mode
1. **Click "🎤 Voice: OFF"** → Turns ON continuous listening
2. Speak naturally - Raven will:
   - Listen continuously
   - Process your command
   - Respond with voice
   - Automatically return to listening (no need to click again!)
3. After 30 seconds of silence (Banglish mode only):
   - Raven sends witty messages like "Sir, চুপ করে আছেন কেন?"
4. **Click "🎤 Voice: ON"** → Stops voice mode

## UI Features

### Window Controls
- **Drag:** Click and drag the title bar to move window
- **Always on Top:** Window stays visible over other apps
- **Close:** Click ✕ button (saves memory automatically)

### Button Layout
```
🎤 Voice: OFF    👁 Vision: OFF    📸 Capture    🗑 Clear
```

## Personalization

Edit `/app/raven_core.py`:

```python
# Line 31 - Set your name
USER_NAME = "Sir"  # Change this!

# Lines 34-40 - Add WhatsApp contacts
CONTACTS = {
    "mom": "+8801234567890",
    "dad": "+8801234567891",
    "brother": "+8801234567892",
}
```

## Testing Checklist

### ✅ Basic Functionality
- [ ] App launches without errors
- [ ] Window is draggable
- [ ] Window stays on top of other apps
- [ ] Greeting appears in chat

### ✅ Language Mode
- [ ] Say "English" → Response is pure English
- [ ] Speak Bengali → Switches to Banglish
- [ ] Close and reopen → Language mode is remembered
- [ ] System commands (time, date) match language mode

### ✅ Voice Mode
- [ ] Turn ON voice toggle
- [ ] Speak a command → Raven responds with voice
- [ ] Verify it keeps listening (no need to click again)
- [ ] Wait 30 seconds → Witty message appears (Banglish only)
- [ ] Turn OFF voice toggle → Listening stops

### ✅ WhatsApp
- [ ] Say "Open WhatsApp" → Opens web.whatsapp.com
- [ ] Say "Send message to [saved contact]" → Opens chat
- [ ] Verify message auto-sends after 2 seconds

### ✅ Computer Control
- [ ] "Open Chrome" → Chrome launches
- [ ] "Open WhatsApp" (app) → WhatsApp desktop/web opens
- [ ] "Search for Python tutorials" → Google search opens
- [ ] "Minimize everything" → Desktop shows

### ✅ Vision Features
- [ ] Click "📸 Capture" → Screenshot analysis appears
- [ ] Enable "👁 Vision" → Screen context in responses
- [ ] Disable "👁 Vision" → Normal chat without screen

## Memory System

All conversations are saved in:
```
D:/Raven/Memory/history.json
```

Includes:
- Last 20 chat messages
- Language mode preference (English/Banglish)
- Timestamp of last update

## Troubleshooting

### Voice not working?
- Check if microphone is connected
- Button will show "🎤 Mic Unavailable" if no mic detected

### WhatsApp not sending?
- Ensure you're logged into WhatsApp Web in your browser
- Check internet connection
- 2-second delay gives page time to load

### Bengali voice not playing?
- Verify `edge-tts` is installed: `pip install edge-tts`
- Check pygame mixer initialization in terminal logs

### Window disappeared?
- It's always on top, might be outside screen
- Close and relaunch application

## Advanced Usage

### Multiple Commands in Sequence (Voice Mode)
1. Turn ON voice mode
2. Say: "What time is it?"
3. Wait for response
4. Immediately say: "Open Chrome"
5. Wait for response
6. Say: "Search for AI news"
7. Continue as needed...

No clicking needed between commands!

### Mixed Language Conversation
```
You: "English"
Raven: "Switching to English mode, Sir..."

You: "What time is it?"
Raven: "The time is 3:45 PM, Sir!"

You: "এখন কি করছ?" (What are you doing now?)
Raven: "ঠিক আছে Sir! Banglish mode এ switch করছি..."
```

### Smart WhatsApp Workflow
```
You: "Open WhatsApp"
→ WhatsApp Web opens
→ You click contact manually
→ Type and send

OR

You: "Send message to mom: I'll be home late"
→ WhatsApp Web opens with pre-filled message
→ Auto-sends after 2 seconds
```

## Tips for Best Experience

1. **Speak clearly** - Wait 1 second between sentences
2. **Use Bengali Unicode** - Type Bengali in proper script, not romanized
3. **Save contacts** - Add frequently messaged people to CONTACTS dict
4. **Keep window visible** - Stays on top automatically
5. **Let her speak** - In voice mode, wait for response before next command

---

**Enjoy your enhanced Raven Assistant!** 🦅✨

For detailed technical documentation, see: `/app/RAVEN_IMPROVEMENTS.md`
