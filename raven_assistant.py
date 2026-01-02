"""Raven Assistant - Main Launcher

A complete desktop AI assistant with:
- Natural language chat (Ollama)
- Vision capabilities (screenshot analysis)
- Voice input/output
- System automation commands
- Persistent memory
- Modern, state-based GUI

Author: Emergent AI
Version: 2.0 (Modular Production Release)
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from raven_gui import RavenGUI


def main():
    """Launch Raven Assistant"""
    print("=" * 60)
    print("RAVEN ASSISTANT v2.0 - Starting...")
    print("=" * 60)
    print("\n[Terminal] Initializing Raven Assistant...")
    print("[Terminal] All system logs will appear here.")
    print("[Terminal] User chat messages will ONLY appear in the GUI.\n")
    
    try:
        # Create and run GUI
        app = RavenGUI()
        app.run()
        
    except KeyboardInterrupt:
        print("\n[Terminal] Shutdown requested by user")
    except Exception as e:
        print(f"\n[Terminal] Fatal error: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
        
    def build_gui(self):
        # Main container
        main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Top section - Raven's avatar with state animations
        self.avatar_frame = ctk.CTkFrame(main_frame, height=400, fg_color="#1a1a2e")
        self.avatar_frame.pack(fill="x", pady=(0, 10))
        self.avatar_frame.pack_propagate(False)
        
        # Avatar label for displaying state images
        self.avatar_label = ctk.CTkLabel(self.avatar_frame, text="", fg_color="transparent")
        self.avatar_label.pack(expand=True)
        
        # Load and display default state image
        self.load_state_images()
        self.update_avatar_state("idle")
        
        # Control buttons frame
        control_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        control_frame.pack(fill="x", pady=(0, 10))
        
        # Voice mode toggle
        self.voice_btn = ctk.CTkButton(
            control_frame,
            text="🎤 Voice Mode: OFF",
            command=self.toggle_voice_mode,
            width=150,
            height=40,
            fg_color="#16213e",
            hover_color="#0f3460"
        )
        self.voice_btn.pack(side="left", padx=5)
        
        # Vision mode toggle
        self.vision_btn = ctk.CTkButton(
            control_frame,
            text="👁 Vision Mode: OFF",
            command=self.toggle_vision_mode,
            width=150,
            height=40,
            fg_color="#16213e",
            hover_color="#0f3460"
        )
        self.vision_btn.pack(side="left", padx=5)
        
        # Live vision toggle
        self.live_vision_btn = ctk.CTkButton(
            control_frame,
            text="📹 Live Vision: OFF",
            command=self.toggle_live_vision,
            width=150,
            height=40,
            fg_color="#16213e",
            hover_color="#0f3460"
        )
        self.live_vision_btn.pack(side="left", padx=5)
        
        # Screenshot button
        screenshot_btn = ctk.CTkButton(
            control_frame,
            text="📸 Screenshot",
            command=self.take_screenshot_and_analyze,
            width=120,
            height=40,
            fg_color="#533483",
            hover_color="#7209b7"
        )
        screenshot_btn.pack(side="left", padx=5)
        
        # Chat display area
        self.chat_display = ctk.CTkTextbox(
            main_frame,
            height=300,
            fg_color="#16213e",
            text_color="#e0e0e0",
            font=("Segoe UI", 12)
        )
        self.chat_display.pack(fill="both", expand=True, pady=(0, 10))
        self.chat_display.configure(state="disabled")
        
        # Input frame
        input_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        input_frame.pack(fill="x")
        
        # Text input
        self.input_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Ask Raven anything...",
            height=50,
            font=("Segoe UI", 13),
            fg_color="#16213e",
            border_color="#533483"
        )
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.input_entry.bind("<Return>", lambda e: self.send_message())
        
        # Send button
        send_btn = ctk.CTkButton(
            input_frame,
            text="Send ➤",
            command=self.send_message,
            width=100,
            height=50,
            fg_color="#533483",
            hover_color="#7209b7",
            font=("Segoe UI", 13, "bold")
        )
        send_btn.pack(side="right")
        
    def load_state_images(self):
        """Load state images from assets folder"""
        self.state_images = {}
        states = ["idle", "blinking", "thinking", "talking", "happy"]
        
        for state in states:
            image_path = os.path.join(self.assets_path, f"raven_{state}.png")
            if os.path.exists(image_path):
                try:
                    img = Image.open(image_path)
                    # Resize to fit in avatar frame (maintain aspect ratio)
                    img.thumbnail((380, 380), Image.Resampling.LANCZOS)
                    self.state_images[state] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error loading {state} image: {e}")
            else:
                # Create placeholder if image doesn't exist
                print(f"Warning: {image_path} not found. Using placeholder.")
        
        # If no images loaded, create a text placeholder
        if not self.state_images:
            self.avatar_label.configure(text="RAVEN\n(Place state images in raven_assets folder)", 
                                       font=("Segoe UI", 20, "bold"))
    
    def update_avatar_state(self, state):
        """Update avatar display based on current state"""
        self.current_state = state
        if state in self.state_images:
            self.avatar_label.configure(image=self.state_images[state], text="")
        else:
            state_emojis = {
                "idle": "😌",
                "blinking": "😑",
                "thinking": "🤔",
                "talking": "😊",
                "happy": "😄"
            }
            self.avatar_label.configure(text=state_emojis.get(state, "🤖"), font=("Segoe UI", 80))
    
    def start_idle_animation(self):
        """Cycle between idle and blinking when not active"""
        def animate():
            while True:
                if self.current_state == "idle":
                    self.update_avatar_state("blinking")
                    time.sleep(0.2)
                    self.update_avatar_state("idle")
                    time.sleep(3)
                else:
                    time.sleep(0.5)
        
        thread = threading.Thread(target=animate, daemon=True)
        thread.start()
    
    def add_message_to_chat(self, sender, message):
        """Add message to chat display"""
        self.chat_display.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_msg = f"[{timestamp}] {sender}: {message}\n\n"
        self.chat_display.insert("end", formatted_msg)
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")
        
        # Save to chat log
        with open(self.chat_log_file, "a", encoding="utf-8") as f:
            f.write(formatted_msg)
        
        # Add to history
        self.chat_history.append({
            "timestamp": timestamp,
            "sender": sender,
            "message": message
        })
    
    def send_message(self):
        """Handle sending user message"""
        user_input = self.input_entry.get().strip()
        if not user_input:
            return
        
        self.input_entry.delete(0, "end")
        self.add_message_to_chat("You", user_input)
        
        # Process message in background
        thread = threading.Thread(target=self.process_message, args=(user_input,), daemon=True)
        thread.start()
    
    def process_message(self, user_input):
        """Process user message and generate response"""
        self.update_avatar_state("thinking")
        
        try:
            # Check for special commands
            if "screenshot" in user_input.lower() or "what do you see" in user_input.lower():
                self.take_screenshot_and_analyze()
                return
            
            if "search" in user_input.lower() or "look up" in user_input.lower():
                self.perform_web_search(user_input)
                return
            
            if "whatsapp" in user_input.lower() and "message" in user_input.lower():
                self.handle_whatsapp_automation(user_input)
                return
            
            if "open" in user_input.lower():
                self.handle_browser_command(user_input)
                return
            
            # Regular chat with Ollama
            response = self.chat_with_ollama(user_input)
            
            # Analyze sentiment and update state
            if any(word in response.lower() for word in ["great", "excellent", "success", "done", "perfect"]):
                self.update_avatar_state("happy")
            else:
                self.update_avatar_state("talking")
            
            self.add_message_to_chat("Raven", response)
            
            # Text-to-speech if voice mode is on
            if self.voice_mode:
                self.speak(response)
            
            # Return to idle after response
            time.sleep(2)
            self.update_avatar_state("idle")
            
        except Exception as e:
            error_msg = f"Error processing message: {str(e)}"
            self.add_message_to_chat("System", error_msg)
            self.update_avatar_state("idle")
    
    def chat_with_ollama(self, user_input, image_data=None):
        """Send message to Ollama and get response"""
        try:
            url = f"{self.ollama_base_url}/api/generate"
            
            # Build context from recent history
            context = "\n".join([f"{msg['sender']}: {msg['message']}" 
                               for msg in self.chat_history[-5:]])
            
            prompt = f"Previous conversation:\n{context}\n\nUser: {user_input}\n\nRaven:"
            
            payload = {
                "model": self.vision_model if image_data else self.text_model,
                "prompt": prompt,
                "stream": False
            }
            
            if image_data:
                payload["images"] = [image_data]
            
            response = requests.post(url, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "I'm having trouble generating a response.")
            else:
                return f"Error: Unable to connect to Ollama (Status: {response.status_code})"
                
        except requests.exceptions.ConnectionError:
            return "Error: Cannot connect to Ollama. Please ensure Ollama is running (ollama serve)"
        except Exception as e:
            return f"Error communicating with Ollama: {str(e)}"
    
    def take_screenshot_and_analyze(self):
        """Take screenshot and analyze with vision model"""
        self.update_avatar_state("thinking")
        self.add_message_to_chat("System", "Taking screenshot...")
        
        try:
            # Take screenshot
            screenshot = pyautogui.screenshot()
            
            # Convert to base64
            buffered = io.BytesIO()
            screenshot.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            
            # Save screenshot
            screenshot_path = os.path.join(self.memory_path, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            screenshot.save(screenshot_path)
            
            # Analyze with vision model
            self.add_message_to_chat("System", "Analyzing screenshot...")
            response = self.chat_with_ollama("Describe what you see in this screenshot in detail.", img_base64)
            
            self.update_avatar_state("talking")
            self.add_message_to_chat("Raven", f"Screenshot Analysis: {response}")
            
            if self.voice_mode:
                self.speak(response)
            
            time.sleep(2)
            self.update_avatar_state("idle")
            
        except Exception as e:
            self.add_message_to_chat("System", f"Screenshot error: {str(e)}")
            self.update_avatar_state("idle")
    
    def perform_web_search(self, query):
        """Perform web search using DuckDuckGo"""
        self.add_message_to_chat("System", f"Searching the web for: {query}")
        
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=3))
            
            if results:
                search_summary = "Here's what I found:\n\n"
                for i, result in enumerate(results, 1):
                    search_summary += f"{i}. {result['title']}\n{result['body']}\n\n"
                
                self.update_avatar_state("talking")
                self.add_message_to_chat("Raven", search_summary)
                
                if self.voice_mode:
                    self.speak(f"I found {len(results)} results. {results[0]['title']}")
            else:
                self.add_message_to_chat("Raven", "I couldn't find any results for that search.")
            
            self.update_avatar_state("idle")
            
        except Exception as e:
            self.add_message_to_chat("System", f"Search error: {str(e)}")
            self.update_avatar_state("idle")
    
    def handle_whatsapp_automation(self, user_input):
        """Handle WhatsApp message automation"""
        self.add_message_to_chat("Raven", "Opening WhatsApp Web and preparing to send message...")
        
        try:
            # Open WhatsApp Web
            webbrowser.open("https://web.whatsapp.com")
            time.sleep(5)  # Wait for page to load
            
            self.add_message_to_chat("Raven", "Please manually select the contact. I'll type the message in 5 seconds...")
            time.sleep(5)
            
            # Extract message from user input (simplified - needs better parsing)
            message = user_input.replace("send", "").replace("whatsapp", "").replace("message", "").strip()
            if not message:
                message = "Hello! This is an automated message from Raven."
            
            # Type the message
            pyautogui.write(message, interval=0.05)
            time.sleep(0.5)
            pyautogui.press('enter')
            
            self.update_avatar_state("happy")
            self.add_message_to_chat("Raven", f"Message sent: {message}")
            time.sleep(2)
            self.update_avatar_state("idle")
            
        except Exception as e:
            self.add_message_to_chat("System", f"Automation error: {str(e)}")
            self.update_avatar_state("idle")
    
    def handle_browser_command(self, user_input):
        """Handle browser opening commands"""
        url = None
        
        if "youtube" in user_input.lower():
            url = "https://www.youtube.com"
        elif "google" in user_input.lower():
            url = "https://www.google.com"
        elif "gmail" in user_input.lower():
            url = "https://mail.google.com"
        else:
            # Try to extract URL from input
            words = user_input.split()
            for word in words:
                if "." in word and ("http" in word or "www" in word):
                    url = word if word.startswith("http") else f"https://{word}"
                    break
        
        if url:
            webbrowser.open(url)
            self.update_avatar_state("happy")
            self.add_message_to_chat("Raven", f"Opening {url}")
            time.sleep(2)
            self.update_avatar_state("idle")
        else:
            self.add_message_to_chat("Raven", "I'm not sure which website to open. Please be more specific.")
    
    def toggle_voice_mode(self):
        """Toggle voice input/output mode"""
        self.voice_mode = not self.voice_mode
        status = "ON" if self.voice_mode else "OFF"
        self.voice_btn.configure(text=f"🎤 Voice Mode: {status}")
        self.add_message_to_chat("System", f"Voice mode {status}")
        
        if self.voice_mode:
            thread = threading.Thread(target=self.listen_for_voice, daemon=True)
            thread.start()
    
    def toggle_vision_mode(self):
        """Toggle vision mode"""
        self.vision_mode = not self.vision_mode
        status = "ON" if self.vision_mode else "OFF"
        self.vision_btn.configure(text=f"👁 Vision Mode: {status}")
        self.add_message_to_chat("System", f"Vision mode {status}")
    
    def toggle_live_vision(self):
        """Toggle live vision mode (screenshot every 5 seconds)"""
        self.live_vision_active = not self.live_vision_active
        status = "ON" if self.live_vision_active else "OFF"
        self.live_vision_btn.configure(text=f"📹 Live Vision: {status}")
        self.add_message_to_chat("System", f"Live vision mode {status}")
        
        if self.live_vision_active:
            thread = threading.Thread(target=self.live_vision_loop, daemon=True)
            thread.start()
    
    def live_vision_loop(self):
        """Take screenshots every 5 seconds in live vision mode"""
        while self.live_vision_active:
            self.take_screenshot_and_analyze()
            time.sleep(5)
    
    def listen_for_voice(self):
        """Listen for voice input continuously"""
        while self.voice_mode:
            try:
                with sr.Microphone() as source:
                    self.add_message_to_chat("System", "Listening...")
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                text = self.recognizer.recognize_google(audio)
                self.add_message_to_chat("You (voice)", text)
                self.process_message(text)
                
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except Exception as e:
                self.add_message_to_chat("System", f"Voice recognition error: {str(e)}")
                time.sleep(1)
    
    def speak(self, text):
        """Convert text to speech"""
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"TTS error: {e}")
    
    def load_memory(self):
        """Load memory from JSON file"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    memory = json.load(f)
                    self.chat_history = memory.get("chat_history", [])
                print("Memory loaded successfully")
            except Exception as e:
                print(f"Error loading memory: {e}")
    
    def save_memory(self):
        """Save memory to JSON file"""
        try:
            memory = {
                "chat_history": self.chat_history[-100:],  # Keep last 100 messages
                "last_updated": datetime.now().isoformat()
            }
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(memory, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving memory: {e}")
    
    def on_closing(self):
        """Handle window closing"""
        self.save_memory()
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

if __name__ == "__main__":
    app = RavenAssistant()
    app.run()
