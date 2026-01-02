# 🦅 RAVEN ELITE - Complete Transformation Guide

## Overview
Raven has been upgraded to her **ELITE** version with three major pillars of enhancement:

1. **Elite Dark UI (Glassmorphism)** - Nova-inspired visual design
2. **Emotionally Human Logic** - Mood detection and adaptive responses
3. **Universal File Opener** - Automatic file handling utility

---

## 🎨 PILLAR 1: Elite Dark UI (Glassmorphism)

### Visual Design
- **Background**: Deep Charcoal (`#0a0a0a`) with 0.85 opacity for glassmorphism effect
- **Borders**: Neon Blue (`#00f2ff`) for futuristic, high-tech appearance
- **Title**: "🦅 RAVEN ELITE" in neon blue

### Mood-Based Glow Colors
Raven's avatar border changes color based on her state and your mood:

| State/Mood | Color | Hex Code | Visual Effect |
|------------|-------|----------|---------------|
| **Listening** | Emerald Green | `#50fa7b` | Pulsing glow |
| **Thinking** | Electric Violet | `#bd93f9` | Pulsing glow |
| **Stressed** | Deep Crimson | `#dc143c` | Alert mode |
| **Talking** | Cyan | `#8be9fd` | Active bounce |
| **Happy** | Yellow | `#f1fa8c` | Bright glow |
| **Idle** | Soft Blue | `#60a5fa` | Gentle pulse |

### Avatar Animations
- **Bouncing Effect**: Avatar bounces/vibrates (±5 pixels) when talking or thinking
- **Pulsing Glow**: Border brightness pulses continuously based on state
- **Smooth Transitions**: All animations run in separate threads for UI responsiveness

### System Integration
- ✅ **Always on Top**: Window stays visible above all other applications
- ✅ **Draggable**: Click and drag title bar to move window anywhere
- ✅ **Glassmorphism**: Semi-transparent background (85% opacity)

---

## 🧠 PILLAR 2: Emotionally Human Logic

### Mood Detection System

Raven automatically detects your emotional state from keywords:

#### **Stressed/Angry Mood**
**Keywords**: `stressed`, `angry`, `frustrated`, `রাগ`, `irritated`, `annoyed`, `problem`

**Raven's Response Style**:
```
"Sir, ektu relax koren, ami achi to. Tea break niben?"
"Don't worry, Sir. Let me handle this for you."
```

**Visual**: Deep Crimson glow (#dc143c) on avatar border

---

#### **Sad Mood**
**Keywords**: `sad`, `upset`, `মন খারাপ`, `down`, `depressed`, `unhappy`, `lonely`

**Raven's Response Style**:
```
"কি হয়েছে, Sir? Share করতে পারো, I'm here for you."
"Don't worry, everything will be okay. আমি আছি তো!"
```

**Visual**: Thinking state with empathetic tone

---

#### **Tired Mood**
**Keywords**: `tired`, `thaka`, `ক্লান্ত`, `exhausted`, `sleepy`, `fatigue`

**Raven's Response Style**:
```
"Rest nao, Sir. I'll handle things!"
"একটু ঘুমিয়ে নাও, তুমি tired লাগছো।"
```

**Visual**: Soft encouragement to take a break

---

#### **Happy Mood**
**Keywords**: `happy`, `great`, `excellent`, `খুশি`, `awesome`, `wonderful`, `amazing`

**Raven's Response Style**:
```
"Haha, khushi dekhe bhalo lagche! Keep it up, Sir!"
"Great to see you happy! কি ব্যাপার, কি good news?"
```

**Visual**: Yellow glow with witty, playful responses

---

### Mood Memory System
- **Tracking**: Last 5 moods stored with timestamps
- **Context**: AI uses mood history to provide contextually aware responses
- **Persistence**: Moods saved in `D:/Raven/Memory/history.json`
- **Adaptive**: Responses become more personalized over time

### Mood Indicator
- **Location**: Title bar (right side)
- **Format**: Emoji + Mood name
  - 😌 Neutral
  - 😊 Happy
  - 😔 Sad
  - 😤 Stressed
  - 😴 Tired
- **Color**: Neon blue when mood is active, gray when neutral

---

## 📁 PILLAR 3: Universal File Opener

### Automatic File Detection
Raven automatically detects file paths in your messages using intelligent pattern matching:

```
You: "Raven, open D:/Documents/report.pdf"
Raven: "Opening document: report.pdf, Sir!"
```

### Supported File Types

#### Documents & PDFs
**Extensions**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
**Opens With**: System default viewer (Adobe Reader, Microsoft Office, etc.)

**Example**:
```
"Open D:/Projects/presentation.pptx"
"Read this file C:/Users/Documents/invoice.pdf"
```

---

#### Images
**Extensions**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp`, `.svg`
**Opens With**: Default Photos app / Image viewer

**Example**:
```
"Show me D:/Photos/vacation.jpg"
"Open this image C:/Pictures/screenshot.png"
```

---

#### Code Files
**Extensions**: `.py`, `.js`, `.html`, `.css`, `.json`, `.txt`, `.md`, `.java`, `.cpp`, `.c`, `.ts`, `.jsx`, `.tsx`
**Opens With**: VS Code (if available), otherwise default text editor

**Example**:
```
"Open D:/Projects/app.py"
"Read this code C:/Dev/script.js"
```

---

#### Videos
**Extensions**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`
**Opens With**: Default video player

**Example**:
```
"Play D:/Videos/tutorial.mp4"
```

---

#### Audio
**Extensions**: `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`
**Opens With**: Default music player

**Example**:
```
"Play this song D:/Music/favorite.mp3"
```

---

### Usage Patterns

#### Direct Command
```
You: "Raven, open D:/Documents/report.pdf"
Raven: "Opening document: report.pdf, Sir!"
```

#### Conversational
```
You: "Can you read D:/Notes/todo.txt for me?"
Raven: "Opening code file in VS Code: todo.txt, Sir!"
```

#### Automatic Detection
```
You: "I need to check D:/Work/budget.xlsx"
Raven: "Opening document: budget.xlsx, Sir!"
```

---

## 🚀 Getting Started

### 1. Launch Raven Elite
```bash
python raven_assistant.py
```

### 2. Test Mood Detection
Try saying or typing:
- "I'm stressed about this project" → Deep Crimson glow
- "I'm so happy today!" → Yellow glow + witty response
- "I'm tired" → Gentle suggestion to rest

### 3. Test File Opener
Try:
- "Raven, open D:/Documents/file.pdf"
- "Read this code C:/Projects/app.py"
- Just mention a file path in conversation

### 4. Observe UI Changes
- Watch the **bouncing avatar** when she talks
- See the **pulsing glow** change colors
- Check the **mood indicator** in title bar

---

## 🎯 Key Features Summary

| Feature | Description | Status |
|---------|-------------|--------|
| Glassmorphism UI | Deep charcoal (#0a0a0a) with 0.85 opacity | ✅ |
| Neon Blue Borders | Futuristic #00f2ff borders | ✅ |
| Mood Detection | Detects stressed, sad, tired, happy | ✅ |
| Adaptive Responses | Banglish responses based on mood | ✅ |
| Mood Memory | Tracks last 5 moods with timestamps | ✅ |
| Deep Crimson Glow | Alert mode for stressed/angry users | ✅ |
| Bouncing Avatar | Vibrates during talking/thinking | ✅ |
| Pulsing Glow | Continuous border brightness animation | ✅ |
| Universal File Opener | Auto-opens PDFs, images, code, videos | ✅ |
| VS Code Integration | Opens code files in VS Code | ✅ |
| Always on Top | Window stays above all apps | ✅ |
| Draggable Window | Move by dragging title bar | ✅ |
| Bengali Voice | edge-tts with bn-BD-NabanitaNeural | ✅ |

---

## 📝 Configuration

### Personalization (raven_core.py)
```python
# Line 31: Set your name
USER_NAME = "Sir"  # Change to your name

# Lines 34-40: Add WhatsApp contacts
CONTACTS = {
    "mom": "+8801234567890",
    "dad": "+8801234567891",
    # Add more contacts here
}
```

### Memory Location
All data is stored in: `D:/Raven/Memory/`
- `history.json` - Chat history, language mode, mood history
- `chat_YYYYMMDD_HHMMSS.txt` - Daily chat logs
- `screenshot_*.png` - Screenshots (last 20 kept)

---

## 🔧 Technical Details

### Threading Architecture
- **Main Thread**: GUI rendering (customtkinter)
- **Voice Thread**: Continuous listening loop
- **Processing Thread**: Message processing and AI calls
- **Animation Threads**: 
  - Pulsing glow animation
  - Bouncing avatar animation
  - Idle blinking animation

### Mood Detection Algorithm
1. Text preprocessing (lowercase, strip)
2. Keyword matching across 5 mood categories
3. Priority order: stressed > sad > tired > happy > neutral
4. Update mood_history with timestamp
5. Pass mood context to AI prompt

### File Path Detection
Uses regex patterns to detect:
- Windows absolute paths: `D:/path/file.ext`, `C:\path\file.ext`
- Unix paths: `/path/to/file.ext`
- Relative filenames: `filename.ext`

Then checks:
1. File existence with `os.path.exists()`
2. Extension mapping to appropriate application
3. Platform-specific opening command

---

## 🐛 Troubleshooting

### Issue: Mood not detecting
**Solution**: Use exact keywords like "stressed", "sad", "tired", "happy", or Bengali equivalents

### Issue: File not opening
**Solution**: 
- Ensure full file path is provided
- Check file actually exists
- For code files, install VS Code or use default editor

### Issue: Avatar not bouncing
**Solution**: Avatar only bounces during "talking" and "thinking" states

### Issue: Glow not pulsing
**Solution**: Pulsing runs automatically - ensure `pulse_active = True`

---

## 🎨 Color Reference

```python
COLORS = {
    "bg_dark": "#0a0a0a",           # Deep charcoal
    "neon_blue": "#00f2ff",         # Borders & title
    "listening_glow": "#50fa7b",    # Emerald green
    "thinking_glow": "#bd93f9",     # Electric violet
    "stressed_glow": "#dc143c",     # Deep crimson
    "talking_glow": "#8be9fd",      # Cyan
    "happy_glow": "#f1fa8c",        # Yellow
    "idle_glow": "#60a5fa",         # Soft blue
}
```

---

## 📚 Next Steps

1. **Add Your Contacts**: Edit `CONTACTS` dictionary in `raven_core.py`
2. **Test All Features**: Try mood detection, file opening, voice commands
3. **Customize**: Change `USER_NAME` to your actual name
4. **Enjoy**: Experience Raven's emotionally intelligent assistance!

---

## 🙏 Credits

**Raven Elite Version** - Complete transformation with glassmorphism UI, emotional intelligence, and universal file handling.

**Developer**: Emergent AI  
**Version**: Elite 1.0  
**Date**: 2025

---

**🦅 Welcome to the Elite Raven experience!** 🦅
