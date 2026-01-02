# 🎯 PERSONALIZATION GUIDE - Set Your Name

## 📝 How to Set Your Name

Raven will call you by your name (or "Sir") instead of generic terms like "bondhu".

### Step 1: Open the Core File
Open `/app/raven_core.py`

### Step 2: Find the USER_NAME Configuration
Look for lines 29-31 at the top of the `RavenCore` class:

```python
# ========== PERSONALIZATION ==========
# Set your name here - Raven will call you by this name
USER_NAME = "Sir"  # Change to your name or keep "Sir"
```

### Step 3: Change to Your Name
Replace `"Sir"` with your actual name:

**Examples:**
```python
# Option 1: Use your first name
USER_NAME = "Arif"

# Option 2: Use your full name
USER_NAME = "Arif Rahman"

# Option 3: Keep it formal
USER_NAME = "Sir"

# Option 4: Use a title + name
USER_NAME = "Mr. Ahmed"

# Option 5: Use a nickname
USER_NAME = "Boss"
```

### Step 4: Save and Restart
- Save the file
- Restart Raven Assistant
- Done! Raven will now call you by your name

---

## 🎭 Examples of How Raven Will Address You

### If USER_NAME = "Arif"

**Greetings:**
- Morning: "Suprabhat! Good morning, Arif!"
- Evening: "Good evening, Arif! Shondha belar shubhechha!"

**Responses:**
- Time: "Ekhon somoy holo 3:45 PM, Arif!"
- WhatsApp: "Thik ache, Arif! Mom ke message pathachi!"
- Search: "Thik ache, Arif! Google e khujchi 'weather'..."
- Error: "Ami ektu error face korchi, Arif. Try again koro?"
- Contact not found: "Contact ta amar list e nei, Arif. Phone number dao please."

### If USER_NAME = "Sir"

**Greetings:**
- Morning: "Suprabhat! Good morning, Sir!"
- Evening: "Good evening, Sir! Shondha belar shubhechha!"

**Responses:**
- Time: "Ekhon somoy holo 3:45 PM, Sir!"
- WhatsApp: "Thik ache, Sir! Mom ke message pathachi!"
- Search: "Thik ache, Sir! Google e khujchi 'weather'..."

### If USER_NAME = "Boss"

**Greetings:**
- Morning: "Suprabhat! Good morning, Boss!"
- Evening: "Good evening, Boss! Shondha belar shubhechha!"

**Responses:**
- WhatsApp: "Thik ache, Boss! Message pathachi!"
- Commands: "Chrome khulchi, Boss..."

---

## 🌟 Where Your Name Appears

Raven will use your name in:

1. **Greetings** - Every time she starts
2. **Time/Date Responses** - "Ekhon somoy holo 3:45 PM, [YOUR NAME]!"
3. **Command Confirmations** - "Thik ache, [YOUR NAME]! Message pathachi!"
4. **Error Messages** - "Sorry [YOUR NAME], bujhte parini"
5. **AI Conversations** - Throughout natural chat responses
6. **WhatsApp** - "Thik ache, [YOUR NAME]! Mom ke message pathachi!"
7. **Search** - "Thik ache, [YOUR NAME]! Google e khujchi..."
8. **Type Commands** - "Lekha hoyeche, [YOUR NAME]: [text]"

---

## ⚠️ Important Notes

1. **Case Sensitive**: The name is case-sensitive
   - `"Arif"` vs `"arif"` - choose your preference

2. **Special Characters**: You can use:
   - Spaces: `"Arif Rahman"` ✅
   - Dots: `"Mr. Ahmed"` ✅
   - Hyphens: `"Al-Amin"` ✅

3. **Bengali Names**: Fully supported!
   - `"আরিফ"` ✅
   - `"রহিম"` ✅
   - Bengali text in voice output works perfectly

4. **Length**: Keep it reasonable (2-20 characters recommended)
   - Too long might sound awkward in responses

---

## 🎯 Quick Change Steps

```bash
# 1. Open file
nano /app/raven_core.py
# or use any text editor

# 2. Find line 31
USER_NAME = "Sir"

# 3. Change to your name
USER_NAME = "Arif"

# 4. Save (Ctrl+O, Enter, Ctrl+X for nano)

# 5. Restart Raven
python raven_assistant.py
```

---

## 🔄 Before & After Examples

### ❌ BEFORE (Generic "bondhu")
```
User: "What time is it?"
Raven: "Ekhon somoy holo 3:45 PM, bondhu!"

User: "Send message to mom"
Raven: "Thik ache! Mom ke message pathabo. But ki bolte chao?"
```

### ✅ AFTER (Your Name "Arif")
```
User: "What time is it?"
Raven: "Ekhon somoy holo 3:45 PM, Arif!"

User: "Send message to mom"
Raven: "Thik ache, Arif! Mom ke message pathabo. But ki bolte chao?"
```

---

## 💡 Pro Tips

1. **Professional Setting**: Use "Sir" or "Mr. [Name]"
2. **Casual Setting**: Use your first name or nickname
3. **Family Members**: Each person can set their own name
4. **Multiple Devices**: Different names on different computers
5. **Voice Output**: Your name will be spoken by Raven in Bengali voice!

---

## 🎊 That's It!

Your name is now configured. Raven will address you personally in every interaction!

**"Ami tomar sathe achi, [YOUR NAME]! Let's make magic together! 🚀✨"**
