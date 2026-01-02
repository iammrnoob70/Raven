# RAVEN ASSET PLACEMENT GUIDE

## 📁 Required Folder Structure

```
your_project_folder/
│
├── 📄 raven_assistant.py          ← Main Python script
├── 📄 raven_requirements.txt      ← Dependencies list
├── 📄 RAVEN_README.md             ← Full documentation
├── 📄 SETUP_GUIDE.md              ← Setup instructions
├── 📄 setup_raven.bat             ← Windows installer
├── 📄 start_raven.bat             ← Quick launcher
│
└── 📁 raven_assets/               ← CREATE THIS FOLDER
    ├── 🖼️ raven_idle.png          ← Default resting state
    ├── 🖼️ raven_blinking.png      ← Eye blink animation
    ├── 🖼️ raven_thinking.png      ← Processing indicator
    ├── 🖼️ raven_talking.png       ← Speaking animation
    └── 🖼️ raven_happy.png         ← Success/joy expression
```

## 🎨 Image Specifications

### File Requirements
| Property | Specification |
|----------|--------------|
| **Format** | PNG (preferred) or JPG |
| **Recommended Size** | 300x300 to 500x500 pixels |
| **Background** | Transparent (PNG) or solid color |
| **Color Depth** | 24-bit or 32-bit (with alpha) |
| **Max File Size** | < 2MB per image |

### Naming Convention (EXACT NAMES REQUIRED)
- ✅ `raven_idle.png` - Correct
- ❌ `Raven_Idle.PNG` - Wrong (case matters on some systems)
- ❌ `raven-idle.png` - Wrong (underscore, not hyphen)
- ❌ `idle.png` - Wrong (missing prefix)

## 🎭 State Descriptions

### 1. Idle State (`raven_idle.png`)
**When Used**: Default state, waiting for user input
**Visual Suggestions**:
- Neutral, calm expression
- Eyes open, looking forward or slightly down
- Relaxed posture
- Subtle breathing animation position (if creating multiple frames)

**Example Prompts for AI Generation**:
```
"Pixel art AI assistant character named Raven, idle standing pose, 
calm neutral expression, purple and black color scheme, 
cute anime style, transparent background"
```

### 2. Blinking State (`raven_blinking.png`)
**When Used**: Cycles with idle every 3 seconds
**Visual Suggestions**:
- Eyes closed or half-closed
- Same pose as idle, just different eye state
- Can be subtle or exaggerated
- Maintains the same body position as idle

**Example Prompts**:
```
"Same character as idle state, but with eyes closed, 
blinking animation frame, transparent background"
```

### 3. Thinking State (`raven_thinking.png`)
**When Used**: Processing user request, analyzing, searching
**Visual Suggestions**:
- Thoughtful expression
- Hand on chin, or looking up
- Thought bubble or question marks above head
- Slightly tilted head
- Loading/processing indicator (optional)

**Example Prompts**:
```
"AI assistant character in thinking pose, hand on chin, 
looking upward thoughtfully, question marks or thought bubble, 
purple theme, transparent background"
```

### 4. Talking State (`raven_talking.png`)
**When Used**: Delivering response, speaking, TTS active
**Visual Suggestions**:
- Mouth open or smiling
- Animated expression
- Sound waves or speech bubbles (optional)
- Cheerful, engaged look
- Slight forward lean

**Example Prompts**:
```
"AI assistant character talking, mouth open with friendly smile, 
sound waves, cheerful expression, purple theme, 
transparent background"
```

### 5. Happy State (`raven_happy.png`)
**When Used**: Successful task completion, positive sentiment detected
**Visual Suggestions**:
- Big smile or laugh
- Sparkles or stars around character
- Excited pose (jumping, hands up)
- Bright, celebratory expression
- Hearts or confetti (optional)

**Example Prompts**:
```
"AI assistant character celebrating, big happy smile, 
excited pose with sparkles, joyful expression, purple theme, 
transparent background"
```

## 🖼️ Image Creation Options

### Option 1: AI Image Generators
**Recommended Tools**:
- DALL-E 3 (via ChatGPT Plus)
- Midjourney
- Stable Diffusion (free, local)
- Leonardo.ai
- Bing Image Creator (free)

**Workflow**:
1. Generate one "idle" character design
2. Use that design as reference
3. Generate variations for other states
4. Maintain consistency in style and colors

### Option 2: Commission an Artist
**Where to Find Artists**:
- Fiverr (affordable pixel art commissions)
- r/HungryArtists (Reddit)
- ArtStation
- DeviantArt

**What to Provide**:
- This document
- Your preferred style (pixel art, anime, realistic, etc.)
- Color preferences
- Reference images

### Option 3: Create Your Own
**Tools**:
- **Pixel Art**: Aseprite, Piskel, Lospec
- **Digital Art**: Krita (free), Photoshop, Procreate
- **3D Rendering**: Blender (free), Cinema 4D

### Option 4: Use Placeholders (Temporary)
The app works WITHOUT custom images! It will display emoji placeholders:
- 😌 Idle
- 😑 Blinking  
- 🤔 Thinking
- 😊 Talking
- 😄 Happy

## 📝 Step-by-Step Image Setup

### Method 1: Manual Setup
1. Create folder `raven_assets` next to `raven_assistant.py`
2. Save your 5 images with exact names
3. Verify file extensions are `.png` (not `.PNG`)
4. Test by running: `python raven_assistant.py`

### Method 2: Using Script
Run `setup_raven.bat` - it will create the folder automatically.

### Verification
Check your folder structure matches this:
```
C:\Users\YourName\RavenProject\
├── raven_assistant.py
└── raven_assets\
    ├── raven_idle.png      ✓
    ├── raven_blinking.png  ✓
    ├── raven_thinking.png  ✓
    ├── raven_talking.png   ✓
    └── raven_happy.png     ✓
```

## 🔍 Troubleshooting Images

### Problem: Images not showing (emoji displayed instead)
**Solutions**:
1. Check folder name is `raven_assets` (exact)
2. Verify images are in same directory as `.py` file
3. Confirm filenames exactly match (including underscores)
4. Ensure files are actual images (not corrupted)
5. Check file permissions (readable)

### Problem: Images appear stretched or blurry
**Solutions**:
1. Use higher resolution source images (500x500+)
2. Ensure aspect ratio is square (1:1)
3. Save as PNG for better quality
4. Avoid very small images (<200x200)

### Problem: Transparent background shows as black
**Solutions**:
1. Save as PNG format (JPG doesn't support transparency)
2. Use 32-bit color depth with alpha channel
3. Re-export from your image editor with transparency enabled

### Problem: Images load slowly
**Solutions**:
1. Reduce file size (compress images)
2. Use optimal dimensions (300-500px)
3. Avoid very large files (>2MB)

## 🎨 Style Consistency Tips

### Maintaining Visual Coherence
✅ **DO**:
- Use the same color palette across all states
- Keep the character size consistent
- Maintain the same art style
- Use similar lighting and shadows
- Position character in similar frame position

❌ **DON'T**:
- Mix art styles (pixel + realistic)
- Change character proportions between states
- Use vastly different colors
- Change perspective/angle dramatically

### Color Scheme Suggestions
**Dark/Tech Theme** (matches app UI):
- Primary: Purple (#533483)
- Accent: Pink/Magenta (#7209b7)
- Highlights: Cyan (#0ff)
- Background: Dark blue/black (#16213e)

**Bright/Friendly Theme**:
- Primary: Light purple (#b19cd9)
- Accent: Yellow (#ffd700)
- Highlights: White (#fff)
- Background: Soft blue (#e3f2fd)

## 📤 Sharing Your Raven

Once you have your custom Raven character:
1. Images stay in `raven_assets/` folder
2. Share the entire project folder with others
3. They'll see YOUR custom Raven design
4. Great for personalization and branding!

## 🎁 Bonus: Animation Tips

### Creating Smooth Transitions
The app automatically switches between states, but you can enhance it:

1. **Similar Poses**: Keep body position similar between states
2. **Color Consistency**: Use same color palette
3. **Frame Alignment**: Align character center in each image
4. **Subtle Differences**: Blinking should be almost identical to idle

### Advanced: Custom Fade Effects
The code includes fade capability (line 100). For best results:
- Use transparent PNGs
- Keep background consistent
- Match lighting across states

## ✅ Final Checklist

Before running Raven, verify:
- [ ] `raven_assets/` folder exists
- [ ] All 5 images present with correct names
- [ ] Files are PNG or JPG format
- [ ] Images are square-ish (similar width/height)
- [ ] File sizes are reasonable (<2MB each)
- [ ] Images have proper permissions (readable)
- [ ] Style is consistent across all states
- [ ] Tested: app runs without errors

## 🆘 Need Examples?

If you need reference images, you can:
1. **Search** "pixel art character states" for inspiration
2. **Generate** using the prompts provided above
3. **Download** creative commons characters (check licenses)
4. **Use placeholders** and upgrade later!

---

**Remember**: The app works perfectly fine with emoji placeholders! Custom images just make it more personal and visually appealing. Start with placeholders and add custom art when ready.

Happy customizing! 🎨✨
