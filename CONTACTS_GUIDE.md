# 📱 WhatsApp Contacts Configuration Guide

## 🎯 How to Add Your Contacts

### Step 1: Open the Core File
Navigate to `/app/raven_core.py` and find lines 31-37:

```python
# Contacts dictionary for WhatsApp
CONTACTS = {
    "mom": "+8801234567890",
    "dad": "+8801234567891",
    "brother": "+8801234567892",
    "sister": "+8801234567893",
    # Add your contacts here
}
```

### Step 2: Add Your Contacts
Replace the placeholder numbers with your actual contacts:

```python
CONTACTS = {
    "mom": "+8801712345678",
    "dad": "+8801812345679",
    "brother": "+8801912345680",
    "sister": "+8801512345681",
    "best friend": "+8801612345682",
    "wife": "+8801912345683",
    "boss": "+8801712345684",
    "doctor": "+8801812345685",
}
```

---

## 📝 Format Rules

### ✅ CORRECT Format
```python
"contact name": "+country_code_phone_number"
```

### Examples:
- Bangladesh: `"+8801712345678"`
- India: `"+919876543210"`
- USA: `"+14155551234"`
- UK: `"+447911123456"`

### ❌ WRONG Formats
```python
# Missing country code
"mom": "01712345678"  # ❌ NO

# Missing +
"dad": "8801712345678"  # ❌ NO

# Spaces in number
"brother": "+880 1712 345678"  # ❌ NO (will work but better without)

# Using dashes
"sister": "+880-171-2345678"  # ❌ NO (will work but better without)
```

---

## 🎭 Usage Examples

### Example 1: Simple Message
**You say:** "Send message to mom saying I love you"

**Raven does:**
1. Detects "mom" in CONTACTS
2. Extracts message: "I love you"
3. Opens WhatsApp Web: `https://web.whatsapp.com/send?phone=8801712345678&text=I%20love%20you`
4. Waits 10 seconds
5. Auto-presses Enter
6. Responds: "Thik ache! Mom ke message pathachi: 'I love you'. 10 seconds e auto-send hobe!"

### Example 2: Contact Not in List
**You say:** "Send message to John saying meet me at 5"

**Raven responds:** "Contact ta amar list e nei, bondhu. Phone number dao please, tar sathe message ta. Format: +880XXXXXXXXXX"

**You reply:** "+8801812345678 meet me at 5"

**Raven does:** Opens WhatsApp with that number

### Example 3: Multiple Word Contact Name
```python
CONTACTS = {
    "best friend": "+8801712345678",
    "office manager": "+8801812345679",
    "gym trainer": "+8801912345680",
}
```

**You say:** "Send message to best friend saying let's hangout"
**Works!** ✅

---

## 🔒 Privacy & Security

### Where is the Data Stored?
- **Location**: Only in your local file `/app/raven_core.py`
- **Cloud**: ❌ NOT uploaded anywhere
- **Shared**: ❌ NOT shared with anyone
- **Encrypted**: Stored as plain text (local only)

### Best Practices
1. **Keep it Local**: Don't commit this file to public GitHub repos
2. **Backup**: Save a copy in a secure location
3. **Update**: Keep numbers current
4. **Remove**: Delete old/unused contacts

---

## 🛠️ Advanced Configuration

### Adding More Contact Details
You can extend the dictionary with additional info:

```python
CONTACTS = {
    # Personal
    "mom": "+8801712345678",
    "dad": "+8801812345679",
    
    # Friends
    "rahul": "+8801912345680",
    "priya": "+8801512345681",
    
    # Work
    "boss": "+8801612345682",
    "colleague": "+8801712345683",
    
    # Emergency
    "doctor": "+8801812345684",
    "hospital": "+8801912345685",
}
```

### Using Nicknames
You can add multiple entries for the same number:

```python
CONTACTS = {
    "mom": "+8801712345678",
    "ma": "+8801712345678",        # Same number, different name
    "mother": "+8801712345678",    # Same number, different name
}
```

---

## 🎤 Voice Command Variations

Raven understands various command formats:

### Format 1: "Send message to [name] saying [message]"
```
You: "Send message to mom saying I'll be late"
Raven: Sends to mom
```

### Format 2: "WhatsApp [name] [message]"
```
You: "WhatsApp dad call me when free"
Raven: Sends to dad
```

### Format 3: "Text [name] [message]"
```
You: "Text sister happy birthday"
Raven: Sends to sister
```

### Format 4: Without Message
```
You: "Send message to brother"
Raven: "Thik ache! brother ke message pathabo. But ki bolte chao? Type koro message ta."
Then you type: "Coming home early"
```

---

## 📊 Example Contacts List (Template)

Copy and customize this template:

```python
CONTACTS = {
    # Family
    "mom": "+880XXXXXXXXXX",
    "dad": "+880XXXXXXXXXX",
    "brother": "+880XXXXXXXXXX",
    "sister": "+880XXXXXXXXXX",
    "wife": "+880XXXXXXXXXX",
    "husband": "+880XXXXXXXXXX",
    
    # Best Friends
    "best friend": "+880XXXXXXXXXX",
    "friend1": "+880XXXXXXXXXX",
    "friend2": "+880XXXXXXXXXX",
    
    # Work Contacts
    "boss": "+880XXXXXXXXXX",
    "manager": "+880XXXXXXXXXX",
    "colleague": "+880XXXXXXXXXX",
    
    # Services
    "doctor": "+880XXXXXXXXXX",
    "mechanic": "+880XXXXXXXXXX",
    "electrician": "+880XXXXXXXXXX",
    
    # Emergency
    "emergency": "+880XXXXXXXXXX",
    "police": "+880XXXXXXXXXX",
    "hospital": "+880XXXXXXXXXX",
}
```

---

## 🐛 Troubleshooting

### Problem 1: "Contact not found"
**Solution**: Check spelling in CONTACTS dictionary matches your command

```python
# In code
CONTACTS = {"mom": "+880..."}

# Command
"Send message to mum"  # ❌ Won't work (different spelling)
"Send message to mom"  # ✅ Works!
```

### Problem 2: WhatsApp Web not loading
**Solution**: 
1. Make sure you're logged into WhatsApp Web in your default browser
2. Open WhatsApp Web manually first: https://web.whatsapp.com
3. Scan QR code to login
4. Keep the tab open or bookmark it
5. Try Raven's command again

### Problem 3: Auto-send not working
**Solution**: 
- The 10-second delay might not be enough if your internet is slow
- Manually press Enter if needed
- Consider increasing the delay in `raven_core.py`:

```python
# Change from:
time.sleep(10)

# To:
time.sleep(15)  # 15 seconds instead
```

### Problem 4: Wrong number format
**Solution**: 
- Always include country code with +
- Remove spaces and dashes
- Example: `"+8801712345678"` not `"01712345678"`

---

## 🎉 Tips & Tricks

1. **Quick Access**: Add your most-used contacts at the top of the dictionary

2. **Multiple Numbers**: Add work/home numbers separately
   ```python
   "mom home": "+8801712345678",
   "mom mobile": "+8801912345679",
   ```

3. **Group Chats**: WhatsApp Web doesn't support group chat links easily, so use individual contacts only

4. **Testing**: Test with your own number first:
   ```python
   "me": "+880YOURNUMBER",
   ```

5. **Backup**: Export your CONTACTS dictionary to a separate file for backup

---

## 📞 Quick Reference

| Command Type | Example | Result |
|--------------|---------|--------|
| Simple message | "Send message to mom saying hi" | Opens WhatsApp with "hi" |
| Without message | "Send message to dad" | Asks for message |
| Unknown contact | "Send message to stranger" | Asks for phone number |
| WhatsApp keyword | "WhatsApp brother I'm coming" | Sends "I'm coming" |
| Voice command | 🎤 "Message mom love you" | Sends "love you" |

---

## ✅ Configuration Checklist

- [ ] Open `/app/raven_core.py`
- [ ] Locate CONTACTS dictionary (lines 31-37)
- [ ] Add your contacts with +country_code
- [ ] Save the file
- [ ] Restart Raven Assistant
- [ ] Test with: "Send message to [contact] saying test"
- [ ] Verify WhatsApp Web opens correctly
- [ ] Check auto-send works after 10 seconds

---

**Happy messaging, bondhu! 📱✨**
