"""Raven Assistant - Core Logic Engine (UPGRADED)

This module contains all the business logic, AI integration, and system commands.
Upgraded with Bengali voice, better hearing, and enhanced computer control.
"""

import os
import json
import time
import base64
import io
import asyncio
import tempfile
from datetime import datetime
from typing import Optional, List, Dict, Any
import requests
import pyautogui
import webbrowser
import speech_recognition as sr
import edge_tts
import pygame
from duckduckgo_search import DDGS
from PIL import Image


class RavenCore:
    """Core logic and AI integration for Raven Assistant"""
    
    # ========== PERSONALIZATION ==========
    # Set your name here - Raven will call you by this name
    USER_NAME = "Sir"  # Change to your name (e.g., "Arif", "Rahul", "Ahmed") or keep "Sir"
    
    # Contacts dictionary for WhatsApp
    CONTACTS = {
        "mom": "+8801234567890",
        "dad": "+8801234567891",
        "brother": "+8801234567892",
        "sister": "+8801234567893",
        # Add your contacts here
    }
    
    def __init__(self):
        # Ollama configuration
        self.ollama_base_url = "http://localhost:11434"
        self.text_model = "Raven"  # User's custom model
        self.vision_model = "llama3.2-vision"
        
        # Memory configuration
        self.memory_path = "D:/Raven/Memory"
        os.makedirs(self.memory_path, exist_ok=True)
        self.memory_file = os.path.join(self.memory_path, "history.json")
        self.chat_log_file = os.path.join(self.memory_path, f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        
        # State tracking
        self.chat_history: List[Dict[str, Any]] = []
        self.current_state = "idle"
        self.vision_enabled = False
        self.voice_enabled = False
        self.language_mode = "banglish"  # Can be "english" or "banglish"
        
        # Speech engines
        self.recognizer = sr.Recognizer()
        # UPGRADE: Better hearing settings
        self.recognizer.pause_threshold = 1.0  # Don't cut off while speaking
        self.recognizer.energy_threshold = 4000
        
        self.mic_available = True
        
        # UPGRADE: Bengali TTS with edge-tts
        self.tts_voice = "bn-BD-NabanitaNeural"  # Bengali female voice
        pygame.mixer.init()
        self.temp_audio_path = os.path.join(tempfile.gettempdir(), "raven_speech.mp3")
        
        # Load memory on startup
        self.load_memory()
        
        # Initialize commands handler
        self.commands = CommandsHandler()
        
        print("[Terminal] Raven Core initialized with Bengali voice and enhanced controls")
        
    def get_greeting(self) -> str:
        """Generate context-aware greeting based on time, day, and language mode"""
        now = datetime.now()
        hour = now.hour
        day_name = now.strftime("%A")
        
        if self.language_mode == "english":
            # Pure English greeting
            if 5 <= hour < 12:
                greeting = f"Good morning, {self.USER_NAME}!"
            elif 12 <= hour < 17:
                greeting = f"Good afternoon, {self.USER_NAME}!"
            elif 17 <= hour < 22:
                greeting = f"Good evening, {self.USER_NAME}!"
            else:
                greeting = f"Hello {self.USER_NAME}! Still up late?"
            
            # Add day context
            if day_name in ["Saturday", "Sunday"]:
                day_context = f"It's {day_name}, enjoy your weekend!"
            else:
                day_context = f"It's {day_name}, how's your day going?"
            
            return f"{greeting} {day_context}"
        else:
            # Banglish greeting with proper Bengali
            if 5 <= hour < 12:
                greeting = f"সুপ্রভাত! Good morning, {self.USER_NAME}!"
            elif 12 <= hour < 17:
                greeting = f"Good afternoon, {self.USER_NAME}! কেমন আছো?"
            elif 17 <= hour < 22:
                greeting = f"Good evening, {self.USER_NAME}! সন্ধ্যা বেলার শুভেচ্ছা!"
            else:
                greeting = f"Hello {self.USER_NAME}! রাত এ জাগলে তো!"
            
            # Add day context in Banglish
            if day_name in ["Saturday", "Sunday"]:
                day_context = f"আজ তো {day_name}, weekend enjoy করো!"
            else:
                day_context = f"আজ {day_name}, কেমন চলছে দিন টা?"
            
            return f"{greeting} {day_context}"
    
    def load_memory(self) -> None:
        """Load last 20 messages and language mode from memory on startup"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    all_history = data.get("chat_history", [])
                    # Load last 20 messages
                    self.chat_history = all_history[-20:] if len(all_history) > 20 else all_history
                    # Load language mode
                    self.language_mode = data.get("language_mode", "banglish")
                print(f"[Terminal] Memory load hoye geche: {len(self.chat_history)} messages, Language: {self.language_mode}")
            except Exception as e:
                print(f"[Terminal] Memory load korte parini: {e}")
        else:
            print("[Terminal] Kono previous memory nei, notun shuru korchi")
    
    def save_memory(self) -> None:
        """Save conversation history and language mode to JSON file"""
        try:
            data = {
                "chat_history": self.chat_history,
                "language_mode": self.language_mode,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"[Terminal] Memory save hoye geche: {len(self.chat_history)} messages, Language: {self.language_mode}")
        except Exception as e:
            print(f"[Terminal] Memory save korte problem: {e}")
    
    def log_chat(self, sender: str, message: str) -> None:
        """Log chat message to file and history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_msg = f"[{timestamp}] {sender}: {message}\n"
        
        # Save to chat log file
        try:
            with open(self.chat_log_file, "a", encoding="utf-8") as f:
                f.write(formatted_msg)
        except Exception as e:
            print(f"[Terminal] Chat log write korte problem: {e}")
        
        # Add to history
        self.chat_history.append({
            "timestamp": timestamp,
            "sender": sender,
            "message": message
        })
    
    def chat_with_ollama(self, user_input: str, image_data: Optional[str] = None) -> str:
        """Send message to Ollama and get response with language mode awareness"""
        try:
            url = f"{self.ollama_base_url}/api/generate"
            
            # Build context from recent history
            context = "\n".join([f"{msg['sender']}: {msg['message']}" 
                               for msg in self.chat_history[-10:]])
            
            # Add time context
            current_time = datetime.now().strftime("%I:%M %p")
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            
            # Dynamic prompt based on language mode
            if self.language_mode == "english":
                prompt = f"""You are Raven, a witty and caring AI assistant who speaks in English.

Personality traits:
- 70% witty and playful, 30% caring and supportive
- Speak ONLY in English - clear, natural, and professional
- Address the user as "{self.USER_NAME}"
- Be conversational and warm, like a professional assistant
- When you don't understand something, say "Sorry {self.USER_NAME}, I didn't understand that" or "Could you please provide more details?"

Current time: {current_time}
Current date: {current_date}

Recent conversation:
{context}

User: {user_input}

Raven (respond in English ONLY, address user as {self.USER_NAME}):"""
            else:
                # Banglish mode with improved Bengali quality
                prompt = f"""You are Raven, a witty and caring AI assistant who speaks in Banglish (Bengali + English mix).

Personality traits:
- 70% witty and playful, 30% caring and supportive
- Mix Bengali and English naturally (e.g., "আমি একটু ভাবছি..." or "Wait koro, I'm checking")
- Use STANDARD BENGALI only - NO Hindi words, NO broken grammar
- Address the user as "{self.USER_NAME}" (not "bondhu" or any other term)
- Use common Bengali phrases like "আচ্ছা", "ঠিক আছে", "কেমন আছো", etc.
- Be conversational and warm, like a professional assistant
- When you don't understand something, say things like "Sorry {self.USER_NAME}, বুঝতে পারিনি" or "একবার আরো details দাও"

Current time: {current_time}
Current date: {current_date}

Recent conversation:
{context}

User: {user_input}

Raven (respond in Banglish with proper Standard Bengali, naturally mixing Bengali and English, address user as {self.USER_NAME}):"""
            
            payload = {
                "model": self.vision_model if image_data else self.text_model,
                "prompt": prompt,
                "stream": False
            }
            
            if image_data:
                payload["images"] = [image_data]
            
            response = requests.post(url, json=payload, timeout=120)
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", f"Ami ektu confused, sorry {self.USER_NAME}!")
            else:
                print(f"[Terminal] Ollama error: Status {response.status_code}")
                return "Ami ektu technical problem face korchi. Thik kore nebo!"
                
        except requests.exceptions.ConnectionError:
            print("[Terminal] Cannot connect to Ollama server")
            return "Error: Ollama er sathe connection nei. Please check if Ollama is running (ollama serve)"
        except Exception as e:
            print(f"[Terminal] Ollama communication error: {e}")
            return f"Ami ektu error face korchi, {self.USER_NAME}. Try again koro?"
    
    def process_message(self, user_input: str) -> tuple[str, str]:
        """Process user message and return (response, new_state)"""
        
        # Check for language switching commands
        user_lower = user_input.lower().strip()
        
        # Switch to English mode
        if user_lower == "english" or user_lower == "speak english" or user_lower == "switch to english":
            self.language_mode = "english"
            return f"Switching to English mode, {self.USER_NAME}. I will speak only in English now until you speak Bengali again.", "happy"
        
        # Detect Bengali language and switch to Banglish mode
        # Check for Bengali script or common Bengali words
        bengali_indicators = ['আমি', 'তুমি', 'কি', 'কেমন', 'আছো', 'বলো', 'করো', 'হয়েছে', 'যাও', 'দাও']
        has_bengali_script = any('\u0980' <= char <= '\u09FF' for char in user_input)
        has_bengali_words = any(word in user_input for word in bengali_indicators)
        
        if (has_bengali_script or has_bengali_words) and self.language_mode == "english":
            self.language_mode = "banglish"
            return f"ঠিক আছে {self.USER_NAME}! Banglish mode e switch korchi. Now I'll mix Bengali and English naturally.", "happy"
        
        # Check for system time/date commands
        if any(word in user_input.lower() for word in ["time", "what time", "clock", "somoy", "koyta baje"]):
            return self.commands.get_time(self.language_mode), "happy"
        
        if any(word in user_input.lower() for word in ["date", "what day", "today", "aj", "ajke", "tarikh"]):
            return self.commands.get_date(self.language_mode), "happy"
        
        # UPGRADE: Enhanced WhatsApp command with flexible opening
        if "whatsapp" in user_input.lower():
            result = self.commands.execute_whatsapp_command(user_input, self.CONTACTS, self.language_mode)
            return result, "happy"
        
        # Handle "send message" separately
        if "message" in user_input.lower() and "send" in user_input.lower():
            result = self.commands.execute_whatsapp_command(user_input, self.CONTACTS, self.language_mode)
            return result, "happy"
        
        # UPGRADE: Enhanced search command
        if "search" in user_input.lower() or "google" in user_input.lower() or "khoj" in user_input.lower() or "khuje" in user_input.lower():
            result = self.commands.execute_search_command(user_input, self.language_mode)
            return result, "happy"
        
        # Check for system commands
        if "open" in user_input.lower() and any(app in user_input.lower() for app in ["chrome", "whatsapp", "code", "notepad"]):
            result = self.commands.open_application(user_input, self.language_mode)
            return result, "happy"
        
        if "type this" in user_input.lower() or "type:" in user_input.lower():
            result = self.commands.type_text(user_input, self.language_mode)
            return result, "happy"
        
        if "minimize" in user_input.lower() and "everything" in user_input.lower():
            result = self.commands.minimize_all(self.language_mode)
            return result, "happy"
        
        if "screenshot" in user_input.lower():
            image_data = self.take_screenshot()
            if image_data:
                response = self.chat_with_ollama("Describe what you see in this screenshot in detail.", image_data)
                return response, "talking"
            return f"Screenshot nite parini, {self.USER_NAME}." if self.language_mode == "banglish" else f"Couldn't take screenshot, {self.USER_NAME}.", "idle"
        
        # Vision mode: automatically capture screen if enabled
        image_data = None
        if self.vision_enabled:
            print("[Terminal] Vision mode active - screen capture korchi for context")
            image_data = self.take_screenshot()
        
        # Regular chat with Ollama
        response = self.chat_with_ollama(user_input, image_data)
        
        # Determine response state based on sentiment
        if any(word in response.lower() for word in ["great", "excellent", "success", "done", "perfect", "!", "haha", "lol"]):
            new_state = "happy"
        else:
            new_state = "talking"
        
        return response, new_state
    
    def take_screenshot(self) -> Optional[str]:
        """Take screenshot and return as base64 string"""
        try:
            screenshot = pyautogui.screenshot()
            
            # Convert to base64
            buffered = io.BytesIO()
            screenshot.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            
            # Save screenshot with timestamp
            screenshot_path = os.path.join(
                self.memory_path, 
                f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )
            screenshot.save(screenshot_path)
            
            # Delete old screenshots (keep only last 20)
            self._cleanup_old_screenshots()
            
            print(f"[Terminal] Screenshot saved: {screenshot_path}")
            return img_base64
            
        except Exception as e:
            print(f"[Terminal] Screenshot error: {e}")
            return None
    
    def _cleanup_old_screenshots(self) -> None:
        """Keep only the last 20 screenshots to save disk space"""
        try:
            screenshots = [f for f in os.listdir(self.memory_path) if f.startswith("screenshot_")]
            screenshots.sort(reverse=True)
            
            # Delete old screenshots
            for old_screenshot in screenshots[20:]:
                os.remove(os.path.join(self.memory_path, old_screenshot))
                print(f"[Terminal] Deleted old screenshot: {old_screenshot}")
        except Exception as e:
            print(f"[Terminal] Screenshot cleanup error: {e}")
    
    def speak(self, text: str) -> None:
        """UPGRADE: Convert text to speech using edge-tts with Bengali voice"""
        try:
            # Run async TTS in sync context
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self._async_speak(text))
            loop.close()
        except Exception as e:
            print(f"[Terminal] TTS error: {e}")
    
    async def _async_speak(self, text: str) -> None:
        """Async method to generate and play speech"""
        try:
            # Generate speech using edge-tts
            communicate = edge_tts.Communicate(text, self.tts_voice)
            await communicate.save(self.temp_audio_path)
            
            # Play the audio using pygame
            pygame.mixer.music.load(self.temp_audio_path)
            pygame.mixer.music.play()
            
            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.1)
            
            print("[Terminal] Speech playback complete")
            
        except Exception as e:
            print(f"[Terminal] Async TTS error: {e}")
    
    def listen_for_voice(self) -> Optional[str]:
        """UPGRADE: Listen for voice input with better ambient noise handling"""
        if not self.mic_available:
            return None
        
        try:
            with sr.Microphone() as source:
                print("[Terminal] Listening for voice input... (better hearing enabled)")
                # UPGRADE: Better ambient noise adjustment
                self.recognizer.adjust_for_ambient_noise(source, duration=1.0)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            text = self.recognizer.recognize_google(audio)
            print(f"[Terminal] Voice recognized: {text}")
            return text
            
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except Exception as e:
            print(f"[Terminal] Voice recognition error: {e}")
            self.mic_available = False
            return None


class CommandsHandler:
    """UPGRADE: Handle system automation commands with enhanced features"""
    
    def get_time(self, language_mode: str = "banglish") -> str:
        """Return current time based on language mode"""
        current_time = datetime.now().strftime("%I:%M %p")
        user_name = RavenCore.USER_NAME
        
        if language_mode == "english":
            return f"The time is {current_time}, {user_name}!"
        else:
            return f"এখন সময় হলো {current_time}, {user_name}!"
    
    def get_date(self, language_mode: str = "banglish") -> str:
        """Return current date based on language mode"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        
        if language_mode == "english":
            return f"Today's date is {current_date}."
        else:
            return f"আজকের date হলো {current_date}."
    
    def execute_whatsapp_command(self, command: str, contacts: Dict[str, str], language_mode: str = "banglish") -> str:
        """UPGRADE: Smart WhatsApp with flexible opening"""
        command_lower = command.lower()
        user_name = RavenCore.USER_NAME
        
        # Check if user just wants to open WhatsApp without sending a message
        open_only_keywords = ["open whatsapp", "whatsapp open", "launch whatsapp", "start whatsapp"]
        if any(keyword in command_lower for keyword in open_only_keywords) and "send" not in command_lower and "message" not in command_lower:
            try:
                webbrowser.open('https://web.whatsapp.com')
                print("[Terminal] Opening WhatsApp Web")
                
                if language_mode == "english":
                    return f"Opening WhatsApp for you, {user_name}!"
                else:
                    return f"WhatsApp খুলছি, {user_name}!"
            except Exception as e:
                print(f"[Terminal] WhatsApp open error: {e}")
                if language_mode == "english":
                    return f"Couldn't open WhatsApp, {user_name}."
                else:
                    return f"WhatsApp খুলতে problem হয়েছে, {user_name}."
        
        # Check if a contact name is mentioned for messaging
        contact_name = None
        phone_number = None
        
        for name, number in contacts.items():
            if name in command_lower:
                contact_name = name
                phone_number = number
                break
        
        if phone_number:
            # Extract message if provided
            message = self._extract_message_from_command(command)
            if not message:
                if language_mode == "english":
                    return f"Okay! I'll message {contact_name}. But what do you want to say? Type the message."
                else:
                    return f"ঠিক আছে! {contact_name} কে message পাঠাবো। But কি বলতে চাও? Type করো message টা।"
            
            # Send WhatsApp message
            return self._send_whatsapp_message(phone_number, message, contact_name, language_mode)
        else:
            # Extract potential contact name from "send message to [name]"
            potential_name = self._extract_contact_name(command)
            
            if language_mode == "english":
                if potential_name:
                    return f"I don't have {potential_name}'s number yet, {user_name}. Please type it once so I can save it, or just tell me to 'open WhatsApp' and you can click their name."
                else:
                    return f"I don't have that contact, {user_name}. Please type their number, or just say 'open WhatsApp' and you can find them yourself."
            else:
                if potential_name:
                    return f"{potential_name} এর number আমার কাছে নেই, {user_name}। একবার number টা দাও save করে রাখি, অথবা শুধু 'open WhatsApp' বলো তুমি নিজেই তার name এ click করতে পারবে।"
                else:
                    return f"Contact টা আমার list এ নেই, {user_name}। Phone number দাও please, বা শুধু 'open WhatsApp' বলো তুমি নিজে খুঁজে নাও।"
    
    def _extract_contact_name(self, command: str) -> Optional[str]:
        """Extract potential contact name from command"""
        # Look for patterns like "send message to [name]" or "message [name]"
        patterns = ["send message to ", "message to ", "text to ", "send to "]
        for pattern in patterns:
            if pattern in command.lower():
                parts = command.lower().split(pattern, 1)
                if len(parts) > 1:
                    # Extract first word after pattern as potential name
                    name_part = parts[1].strip().split()[0] if parts[1].strip() else None
                    return name_part
        return None
    
    def _extract_message_from_command(self, command: str) -> Optional[str]:
        """Extract message from command"""
        keywords = ["message", "text", "tell", "say"]
        for keyword in keywords:
            if keyword in command.lower():
                parts = command.lower().split(keyword, 1)
                if len(parts) > 1:
                    return parts[1].strip()
        return None
    
    def _send_whatsapp_message(self, phone: str, message: str, contact_name: str = None, language_mode: str = "banglish") -> str:
        """Send WhatsApp message using web.whatsapp.com"""
        try:
            # Format phone number (remove spaces and special chars)
            phone_clean = phone.replace("+", "").replace("-", "").replace(" ", "")
            
            # URL encode the message
            import urllib.parse
            message_encoded = urllib.parse.quote(message)
            
            # Open WhatsApp Web
            url = f"https://web.whatsapp.com/send?phone={phone_clean}&text={message_encoded}"
            webbrowser.open(url)
            
            print(f"[Terminal] Opening WhatsApp for {contact_name or phone}")
            
            # Auto-press Enter after 2 seconds (user needs to be logged in to WhatsApp Web)
            def auto_send():
                time.sleep(2)
                pyautogui.press('enter')
                print("[Terminal] Auto-pressed Enter to send message")
            
            import threading
            threading.Thread(target=auto_send, daemon=True).start()
            
            user_name = RavenCore.USER_NAME
            name_text = f"{contact_name}" if contact_name else "WhatsApp"
            
            if language_mode == "english":
                return f"Okay, {user_name}! Sending message to {name_text}: '{message}'. Will auto-send in 2 seconds!"
            else:
                return f"ঠিক আছে, {user_name}! {name_text} কে message পাঠাচ্ছি: '{message}'. ২ seconds এ auto-send হবে!"
            
        except Exception as e:
            print(f"[Terminal] WhatsApp error: {e}")
            user_name = RavenCore.USER_NAME
            if language_mode == "english":
                return f"Couldn't open WhatsApp, {user_name}."
            else:
                return f"WhatsApp open করতে problem হয়েছে, {user_name}."
    
    def execute_search_command(self, query: str, language_mode: str = "banglish") -> str:
        """UPGRADE: Enhanced Google search command"""
        # Extract search term
        search_keywords = ["search", "search for", "google", "look up", "khoj", "khuje dao"]
        search_term = query
        
        for keyword in search_keywords:
            if keyword in query.lower():
                search_term = query.lower().replace(keyword, "").strip()
                break
        
        if search_term:
            try:
                url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
                webbrowser.open(url)
                print(f"[Terminal] Searching for: {search_term}")
                user_name = RavenCore.USER_NAME
                
                if language_mode == "english":
                    return f"Okay, {user_name}! Searching Google for '{search_term}'..."
                else:
                    return f"ঠিক আছে, {user_name}! Google এ খুঁজছি '{search_term}'..."
            except Exception as e:
                print(f"[Terminal] Search error: {e}")
                user_name = RavenCore.USER_NAME
                if language_mode == "english":
                    return f"Couldn't open browser, {user_name}."
                else:
                    return f"Browser open করতে পারছি না, {user_name}."
        
        if language_mode == "english":
            return "What should I search for? Please be more specific."
        else:
            return "কি search করবো? একটু clearly বলো।"
    
    def open_application(self, command: str, language_mode: str = "banglish") -> str:
        """Open application using Windows start menu"""
        app_name = ""
        
        if "chrome" in command.lower():
            app_name = "chrome"
        elif "whatsapp" in command.lower():
            app_name = "whatsapp"
        elif "code" in command.lower() or "vscode" in command.lower():
            app_name = "code"
        elif "notepad" in command.lower():
            app_name = "notepad"
        elif "calculator" in command.lower():
            app_name = "calculator"
        
        if app_name:
            try:
                print(f"[Terminal] Opening {app_name}...")
                # Press Windows key
                pyautogui.press('win')
                time.sleep(0.5)
                # Type app name
                pyautogui.write(app_name, interval=0.1)
                time.sleep(0.3)
                # Press Enter
                pyautogui.press('enter')
                
                if language_mode == "english":
                    return f"Opening {app_name}, just a second..."
                else:
                    return f"{app_name} খুলছি, এক second..."
            except Exception as e:
                print(f"[Terminal] Error opening {app_name}: {e}")
                if language_mode == "english":
                    return f"Couldn't open {app_name}."
                else:
                    return f"{app_name} open করতে problem হয়েছে।"
        
        if language_mode == "english":
            return "Which application should I open? Please specify."
        else:
            return "কোন application টা খুলবো? Clearly বলো।"
    
    def type_text(self, command: str, language_mode: str = "banglish") -> str:
        """Type text at current cursor position"""
        # Extract text to type
        text = ""
        if "type this:" in command.lower():
            text = command.split("type this:", 1)[1].strip()
        elif "type:" in command.lower():
            text = command.split("type:", 1)[1].strip()
        
        if text:
            try:
                time.sleep(1)  # Give user time to click where they want text
                pyautogui.write(text, interval=0.05)
                print(f"[Terminal] Typed: {text}")
                user_name = RavenCore.USER_NAME
                
                if language_mode == "english":
                    return f"Typed it, {user_name}: {text}"
                else:
                    return f"লেখা হয়েছে, {user_name}: {text}"
            except Exception as e:
                print(f"[Terminal] Type error: {e}")
                user_name = RavenCore.USER_NAME
                if language_mode == "english":
                    return f"Couldn't type that, {user_name}."
                else:
                    return f"Type করতে পারিনি, {user_name}."
        
        if language_mode == "english":
            return "What should I type? Please tell me."
        else:
            return "কি type করবো? বলো তো।"
    
    def minimize_all(self, language_mode: str = "banglish") -> str:
        """Minimize all windows and show desktop"""
        try:
            # Windows key + D to show desktop
            pyautogui.hotkey('win', 'd')
            print("[Terminal] Minimized all windows")
            
            if language_mode == "english":
                return "Minimized all windows!"
            else:
                return "সব window minimize করে দিলাম!"
        except Exception as e:
            print(f"[Terminal] Minimize error: {e}")
            if language_mode == "english":
                return "Couldn't minimize windows."
            else:
                return "Minimize করতে problem হয়েছে।"
