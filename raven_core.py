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
        """Generate context-aware Banglish greeting based on time and day"""
        now = datetime.now()
        hour = now.hour
        day_name = now.strftime("%A")
        
        # Time-based Banglish greeting with user's name
        if 5 <= hour < 12:
            greeting = f"Suprabhat! Good morning, {self.USER_NAME}!"
        elif 12 <= hour < 17:
            greeting = f"Good afternoon, {self.USER_NAME}! Kemon acho?"
        elif 17 <= hour < 22:
            greeting = f"Good evening, {self.USER_NAME}! Shondha belar shubhechha!"
        else:
            greeting = f"Hello {self.USER_NAME}! Rat e jaglei to!"
        
        # Add day context in Banglish
        if day_name in ["Saturday", "Sunday"]:
            day_context = f"Aj to {day_name}, weekend enjoy koro!"
        else:
            day_context = f"Aj {day_name}, kemon cholche din ta?"
        
        return f"{greeting} {day_context}"
    
    def load_memory(self) -> None:
        """Load last 20 messages from memory on startup"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    all_history = data.get("chat_history", [])
                    # Load last 20 messages
                    self.chat_history = all_history[-20:] if len(all_history) > 20 else all_history
                print(f"[Terminal] Memory load hoye geche: {len(self.chat_history)} messages")
            except Exception as e:
                print(f"[Terminal] Memory load korte parini: {e}")
        else:
            print("[Terminal] Kono previous memory nei, notun shuru korchi")
    
    def save_memory(self) -> None:
        """Save conversation history to JSON file"""
        try:
            data = {
                "chat_history": self.chat_history,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"[Terminal] Memory save hoye geche: {len(self.chat_history)} messages")
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
        """Send message to Ollama and get response with Banglish personality"""
        try:
            url = f"{self.ollama_base_url}/api/generate"
            
            # Build context from recent history
            context = "\n".join([f"{msg['sender']}: {msg['message']}" 
                               for msg in self.chat_history[-10:]])
            
            # Add time context
            current_time = datetime.now().strftime("%I:%M %p")
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            
            # UPGRADE: Banglish personality prompt
            prompt = f"""You are Raven, a witty and caring AI assistant who speaks in Banglish (Bengali + English mix). 

Personality traits:
- 70% witty and playful, 30% caring and supportive
- Mix Bengali and English naturally (e.g., "Ami ektu chinta korchi..." or "Wait koro, I'm checking")
- Address the user as "{self.USER_NAME}" (not "bondhu" or any other term)
- Use common Bengali phrases like "acha", "thik ache", "kemon acho", etc.
- Be conversational and warm, like a professional assistant
- When you don't understand something, say things like "Sorry {self.USER_NAME}, bujhte parini" or "Ekbar aro details dao"

Current time: {current_time}
Current date: {current_date}

Recent conversation:
{context}

User: {user_input}

Raven (respond in Banglish, naturally mixing Bengali and English, address user as {self.USER_NAME}):"""
            
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
        
        # Check for system time/date commands
        if any(word in user_input.lower() for word in ["time", "what time", "clock", "somoy", "koyta baje"]):
            return self.commands.get_time(), "happy"
        
        if any(word in user_input.lower() for word in ["date", "what day", "today", "aj", "ajke", "tarikh"]):
            return self.commands.get_date(), "happy"
        
        # UPGRADE: Enhanced WhatsApp command
        if "whatsapp" in user_input.lower() or "message" in user_input.lower() and "send" in user_input.lower():
            result = self.commands.execute_whatsapp_command(user_input, self.CONTACTS)
            return result, "happy"
        
        # UPGRADE: Enhanced search command
        if "search" in user_input.lower() or "google" in user_input.lower() or "khoj" in user_input.lower() or "khuje" in user_input.lower():
            result = self.commands.execute_search_command(user_input)
            return result, "happy"
        
        # Check for system commands
        if "open" in user_input.lower() and any(app in user_input.lower() for app in ["chrome", "whatsapp", "code", "notepad"]):
            result = self.commands.open_application(user_input)
            return result, "happy"
        
        if "type this" in user_input.lower() or "type:" in user_input.lower():
            result = self.commands.type_text(user_input)
            return result, "happy"
        
        if "minimize" in user_input.lower() and "everything" in user_input.lower():
            result = self.commands.minimize_all()
            return result, "happy"
        
        if "screenshot" in user_input.lower():
            image_data = self.take_screenshot()
            if image_data:
                response = self.chat_with_ollama("Describe what you see in this screenshot in detail.", image_data)
                return response, "talking"
            return "Screenshot nite parini, bondhu.", "idle"
        
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
    
    def get_time(self) -> str:
        """Return current time in Banglish"""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Ekhon somoy holo {current_time}, bondhu!"
    
    def get_date(self) -> str:
        """Return current date in Banglish"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Ajker date holo {current_date}."
    
    def execute_whatsapp_command(self, command: str, contacts: Dict[str, str]) -> str:
        """UPGRADE: Smart WhatsApp messaging with contacts dictionary"""
        command_lower = command.lower()
        
        # Check if a contact name is mentioned
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
                return f"Thik ache! {contact_name} ke message pathabo. But ki bolte chao? Type koro message ta."
            
            # Send WhatsApp message
            return self._send_whatsapp_message(phone_number, message, contact_name)
        else:
            # Name not in contacts, ask for number
            return "Contact ta amar list e nei, bondhu. Phone number dao please, tar sathe message ta. Format: +880XXXXXXXXXX"
    
    def _extract_message_from_command(self, command: str) -> Optional[str]:
        """Extract message from command"""
        keywords = ["message", "text", "tell", "say"]
        for keyword in keywords:
            if keyword in command.lower():
                parts = command.lower().split(keyword, 1)
                if len(parts) > 1:
                    return parts[1].strip()
        return None
    
    def _send_whatsapp_message(self, phone: str, message: str, contact_name: str = None) -> str:
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
            
            # Auto-press Enter after 10 seconds (user needs to be logged in to WhatsApp Web)
            def auto_send():
                time.sleep(10)
                pyautogui.press('enter')
                print("[Terminal] Auto-pressed Enter to send message")
            
            import threading
            threading.Thread(target=auto_send, daemon=True).start()
            
            name_text = f"{contact_name} ke" if contact_name else "WhatsApp e"
            return f"Thik ache! {name_text} message pathachi: '{message}'. 10 seconds e auto-send hobe!"
            
        except Exception as e:
            print(f"[Terminal] WhatsApp error: {e}")
            return "WhatsApp open korte problem hoyeche, bondhu."
    
    def execute_search_command(self, query: str) -> str:
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
                return f"Thik ache! Google e khujchi '{search_term}'..."
            except Exception as e:
                print(f"[Terminal] Search error: {e}")
                return "Browser open korte parchi na, bondhu."
        
        return "Ki search korbo? Ektu clearly bolo."
    
    def open_application(self, command: str) -> str:
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
                return f"{app_name} khulchi, ek second..."
            except Exception as e:
                print(f"[Terminal] Error opening {app_name}: {e}")
                return f"{app_name} open korte problem hoyeche."
        
        return "Kon application ta khulbo? Clearly bolo."
    
    def type_text(self, command: str) -> str:
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
                return f"Lekha hoyeche: {text}"
            except Exception as e:
                print(f"[Terminal] Type error: {e}")
                return "Type korte parini, bondhu."
        
        return "Ki type korbo? Bolo to."
    
    def minimize_all(self) -> str:
        """Minimize all windows and show desktop"""
        try:
            # Windows key + D to show desktop
            pyautogui.hotkey('win', 'd')
            print("[Terminal] Minimized all windows")
            return "Shob window minimize kore dilam!"
        except Exception as e:
            print(f"[Terminal] Minimize error: {e}")
            return "Minimize korte problem hoyeche."
