"""Raven Assistant - Core Logic Engine

This module contains all the business logic, AI integration, and system commands.
Separated from GUI for easier updates and maintenance.
"""

import os
import json
import time
import base64
import io
from datetime import datetime
from typing import Optional, List, Dict, Any
import requests
import pyautogui
import webbrowser
import speech_recognition as sr
import pyttsx3
from duckduckgo_search import DDGS
from PIL import Image


class RavenCore:
    """Core logic and AI integration for Raven Assistant"""
    
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
        self.tts_engine = None
        self.mic_available = True
        
        # Initialize TTS
        try:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 150)
            self.tts_engine.setProperty('volume', 0.9)
        except Exception as e:
            print(f"[Terminal] TTS initialization failed: {e}")
        
        # Load memory on startup
        self.load_memory()
        
        # Initialize commands handler
        self.commands = CommandsHandler()
        
    def get_greeting(self) -> str:
        """Generate context-aware greeting based on time and day"""
        now = datetime.now()
        hour = now.hour
        day_name = now.strftime("%A")
        
        # Time-based greeting
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        elif 17 <= hour < 22:
            greeting = "Good evening"
        else:
            greeting = "Hello"
        
        # Add day context
        if day_name in ["Saturday", "Sunday"]:
            day_context = f"Happy {day_name}!"
        else:
            day_context = f"Hope your {day_name} is going well."
        
        return f"{greeting}! {day_context}"
    
    def load_memory(self) -> None:
        """Load last 20 messages from memory on startup"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    all_history = data.get("chat_history", [])
                    # Load last 20 messages
                    self.chat_history = all_history[-20:] if len(all_history) > 20 else all_history
                print(f"[Terminal] Memory loaded: {len(self.chat_history)} messages")
            except Exception as e:
                print(f"[Terminal] Error loading memory: {e}")
        else:
            print("[Terminal] No previous memory found, starting fresh")
    
    def save_memory(self) -> None:
        """Save conversation history to JSON file"""
        try:
            data = {
                "chat_history": self.chat_history,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"[Terminal] Memory saved: {len(self.chat_history)} messages")
        except Exception as e:
            print(f"[Terminal] Error saving memory: {e}")
    
    def log_chat(self, sender: str, message: str) -> None:
        """Log chat message to file and history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_msg = f"[{timestamp}] {sender}: {message}\n"
        
        # Save to chat log file
        try:
            with open(self.chat_log_file, "a", encoding="utf-8") as f:
                f.write(formatted_msg)
        except Exception as e:
            print(f"[Terminal] Error writing to chat log: {e}")
        
        # Add to history
        self.chat_history.append({
            "timestamp": timestamp,
            "sender": sender,
            "message": message
        })
    
    def chat_with_ollama(self, user_input: str, image_data: Optional[str] = None) -> str:
        """Send message to Ollama and get response"""
        try:
            url = f"{self.ollama_base_url}/api/generate"
            
            # Build context from recent history
            context = "\n".join([f"{msg['sender']}: {msg['message']}" 
                               for msg in self.chat_history[-10:]])
            
            # Add time context
            current_time = datetime.now().strftime("%I:%M %p")
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            
            prompt = f"""Current time: {current_time}
Current date: {current_date}

Recent conversation:
{context}

User: {user_input}

Raven (respond naturally and helpfully):"""
            
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
                return result.get("response", "I'm having trouble generating a response.")
            else:
                print(f"[Terminal] Ollama error: Status {response.status_code}")
                return "I'm having trouble connecting to my AI brain right now."
                
        except requests.exceptions.ConnectionError:
            print("[Terminal] Cannot connect to Ollama server")
            return "Error: Cannot connect to Ollama. Please ensure Ollama is running (ollama serve)"
        except Exception as e:
            print(f"[Terminal] Ollama communication error: {e}")
            return f"I encountered an error while processing your request."
    
    def process_message(self, user_input: str) -> tuple[str, str]:
        """Process user message and return (response, new_state)"""
        
        # Check for system time/date commands
        if any(word in user_input.lower() for word in ["time", "what time", "clock"]):
            return self.commands.get_time(), "happy"
        
        if any(word in user_input.lower() for word in ["date", "what day", "today"]):
            return self.commands.get_date(), "happy"
        
        # Check for system commands
        if "open" in user_input.lower() and any(app in user_input.lower() for app in ["chrome", "whatsapp", "code", "notepad"]):
            result = self.commands.open_application(user_input)
            return result, "happy"
        
        if "search for" in user_input.lower() or "look up" in user_input.lower():
            result = self.commands.search_web(user_input)
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
            return "I couldn't capture the screenshot.", "idle"
        
        # Vision mode: automatically capture screen if enabled
        image_data = None
        if self.vision_enabled:
            print("[Terminal] Vision mode active - capturing screen for context")
            image_data = self.take_screenshot()
        
        # Regular chat with Ollama
        response = self.chat_with_ollama(user_input, image_data)
        
        # Determine response state based on sentiment
        if any(word in response.lower() for word in ["great", "excellent", "success", "done", "perfect", "!"]):
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
        """Convert text to speech if TTS is available"""
        if self.tts_engine:
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except Exception as e:
                print(f"[Terminal] TTS error: {e}")
        else:
            print("[Terminal] TTS not available")
    
    def listen_for_voice(self) -> Optional[str]:
        """Listen for voice input and return transcribed text"""
        if not self.mic_available:
            return None
        
        try:
            with sr.Microphone() as source:
                print("[Terminal] Listening for voice input...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
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
    """Handle system automation commands"""
    
    def get_time(self) -> str:
        """Return current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    def get_date(self) -> str:
        """Return current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}."
    
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
                return f"Opening {app_name}..."
            except Exception as e:
                print(f"[Terminal] Error opening {app_name}: {e}")
                return f"I had trouble opening {app_name}."
        
        return "I'm not sure which application to open."
    
    def search_web(self, query: str) -> str:
        """Open browser and search for query"""
        # Extract search term
        search_term = query.lower().replace("search for", "").replace("look up", "").strip()
        
        if search_term:
            try:
                url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
                webbrowser.open(url)
                print(f"[Terminal] Searching for: {search_term}")
                return f"Searching for '{search_term}'..."
            except Exception as e:
                print(f"[Terminal] Search error: {e}")
                return "I had trouble opening the browser."
        
        return "What would you like me to search for?"
    
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
                return f"Typed: {text}"
            except Exception as e:
                print(f"[Terminal] Type error: {e}")
                return "I had trouble typing the text."
        
        return "What would you like me to type?"
    
    def minimize_all(self) -> str:
        """Minimize all windows and show desktop"""
        try:
            # Windows key + D to show desktop
            pyautogui.hotkey('win', 'd')
            print("[Terminal] Minimized all windows")
            return "All windows minimized."
        except Exception as e:
            print(f"[Terminal] Minimize error: {e}")
            return "I had trouble minimizing windows."
