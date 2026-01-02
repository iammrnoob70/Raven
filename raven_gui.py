"""Raven Assistant - GUI Interface (ELITE VERSION)

This module handles all the visual interface with glassmorphism design,
pulsing glows, mood-based animations, and bouncing avatar effects.
"""

import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import time
import os
from datetime import datetime
from raven_core import RavenCore


class RavenGUI:
    """ELITE Modern Floating Overlay GUI with Glassmorphism and Mood-Based Animations"""
    
    # ELITE: Enhanced color scheme with glassmorphism
    COLORS = {
        "bg_dark": "#0a0a0a",            # Deep charcoal (with 0.85 opacity)
        "bg_medium": "#1a1a1a",         # Medium dark
        "bg_light": "#252525",          # Lighter panels
        "neon_blue": "#00f2ff",         # ELITE: Neon blue border
        "idle_glow": "#60a5fa",         # Soft blue for idle
        "listening_glow": "#50fa7b",    # Emerald green for listening
        "thinking_glow": "#bd93f9",     # Electric violet for thinking
        "talking_glow": "#8be9fd",      # Cyan for talking
        "happy_glow": "#f1fa8c",        # Yellow for happy
        "stressed_glow": "#dc143c",     # ELITE: Deep crimson for stressed/angry
        "text_primary": "#e0e0e0",      # Light text
        "text_secondary": "#9ca3af",    # Muted text
        "accent": "#bd93f9",            # Primary accent (purple)
        "accent_hover": "#d4b5ff",      # Hover state
    }
    
    def __init__(self):
        # Initialize core engine
        self.core = RavenCore()
        
        # Initialize main window
        self.root = ctk.CTk()
        self.root.title("Raven ELITE")
        self.root.geometry("800x920")
        
        # ELITE: Glassmorphism window setup
        self.root.overrideredirect(True)  # Remove title bar
        self.root.attributes('-alpha', 0.85)  # ELITE: 0.85 opacity for glassmorphism
        self.root.attributes('-topmost', True)  # Always on top
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # State tracking
        self.current_state = "idle"
        self.is_processing = False
        
        # ELITE: Animation control
        self.is_bouncing = False
        self.pulse_active = True
        
        # Draggable window variables
        self.drag_data = {"x": 0, "y": 0}
        
        # Assets path
        self.assets_path = os.path.join(os.path.dirname(__file__), "raven_assets")
        os.makedirs(self.assets_path, exist_ok=True)
        
        # Build GUI
        self.build_gui()
        
        # Load state images
        self.load_state_images()
        
        # Start with greeting
        self.add_message_to_chat("Raven", self.core.get_greeting())
        
        # ELITE: Start pulsing glow animation
        self.start_pulsing_glow()
        
        # Start idle animation
        self.start_idle_animation()
        
        # Start voice listener if enabled
        self.voice_thread = None
    
    def build_gui(self):
        """Build the complete ELITE GUI interface with glassmorphism"""
        # Main container with neon blue border
        self.main_frame = ctk.CTkFrame(
            self.root, 
            fg_color=self.COLORS["bg_dark"],
            corner_radius=20,
            border_width=3,
            border_color=self.COLORS["neon_blue"]  # ELITE: Neon blue border
        )
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # ELITE: Title bar with drag functionality
        title_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent",
            height=50
        )
        title_frame.pack(fill="x", pady=(10, 10), padx=15)
        title_frame.pack_propagate(False)
        
        # Make title bar draggable
        title_frame.bind("<Button-1>", self.start_drag)
        title_frame.bind("<B1-Motion>", self.on_drag)
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="🦅 RAVEN ELITE",
            font=("Consolas", 18, "bold"),
            text_color=self.COLORS["neon_blue"]  # ELITE: Neon blue title
        )
        title_label.pack(side="left")
        title_label.bind("<Button-1>", self.start_drag)
        title_label.bind("<B1-Motion>", self.on_drag)
        
        # Close button
        close_btn = ctk.CTkButton(
            title_frame,
            text="✕",
            command=self.on_closing,
            width=30,
            height=30,
            fg_color="#dc2626",
            hover_color="#ef4444",
            font=("Consolas", 16, "bold"),
            corner_radius=15
        )
        close_btn.pack(side="right")
        
        # Status indicator with mood
        self.status_label = ctk.CTkLabel(
            title_frame,
            text="● Idle",
            font=("Consolas", 11),
            text_color=self.COLORS["idle_glow"]
        )
        self.status_label.pack(side="right", padx=15)
        
        # ELITE: Mood indicator
        self.mood_label = ctk.CTkLabel(
            title_frame,
            text="😌 Neutral",
            font=("Consolas", 11),
            text_color=self.COLORS["text_secondary"]
        )
        self.mood_label.pack(side="right", padx=15)
        
        # ELITE: Avatar frame with pulsing glow effect
        self.avatar_container = ctk.CTkFrame(
            self.main_frame,
            height=360,
            fg_color=self.COLORS["bg_medium"],
            border_width=4,
            border_color=self.COLORS["idle_glow"],
            corner_radius=15
        )
        self.avatar_container.pack(fill="x", pady=(0, 15), padx=15)
        self.avatar_container.pack_propagate(False)
        
        # Avatar label for displaying state images
        self.avatar_label = ctk.CTkLabel(
            self.avatar_container,
            text="",
            fg_color="transparent"
        )
        self.avatar_label.pack(expand=True, padx=10, pady=10)
        
        # ELITE: Modern control buttons
        self.build_controls()
        
        # ELITE: Chat display with bubble style
        self.build_chat_display()
        
        # ELITE: Modern input area
        self.build_input_area()
    
    def start_drag(self, event):
        """Start dragging the window"""
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
    
    def on_drag(self, event):
        """Handle window dragging"""
        x = self.root.winfo_x() + event.x - self.drag_data["x"]
        y = self.root.winfo_y() + event.y - self.drag_data["y"]
        self.root.geometry(f"+{x}+{y}")
    
    def build_controls(self):
        """Build modern control buttons panel"""
        control_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        control_frame.pack(fill="x", pady=(0, 15), padx=15)
        
        # Voice mode toggle
        self.voice_btn = ctk.CTkButton(
            control_frame,
            text="🎤 Voice: OFF",
            command=self.toggle_voice_mode,
            width=130,
            height=40,
            fg_color=self.COLORS["bg_medium"],
            hover_color=self.COLORS["bg_light"],
            border_width=2,
            border_color=self.COLORS["text_secondary"],
            font=("Consolas", 11, "bold"),
            corner_radius=10
        )
        self.voice_btn.pack(side="left", padx=5)
        
        # Vision mode toggle
        self.vision_btn = ctk.CTkButton(
            control_frame,
            text="👁 Vision: OFF",
            command=self.toggle_vision_mode,
            width=130,
            height=40,
            fg_color=self.COLORS["bg_medium"],
            hover_color=self.COLORS["bg_light"],
            border_width=2,
            border_color=self.COLORS["text_secondary"],
            font=("Consolas", 11, "bold"),
            corner_radius=10
        )
        self.vision_btn.pack(side="left", padx=5)
        
        # Screenshot button
        screenshot_btn = ctk.CTkButton(
            control_frame,
            text="📸 Capture",
            command=self.manual_screenshot,
            width=110,
            height=40,
            fg_color=self.COLORS["accent"],
            hover_color=self.COLORS["accent_hover"],
            font=("Consolas", 11, "bold"),
            corner_radius=10
        )
        screenshot_btn.pack(side="left", padx=5)
        
        # Clear chat button
        clear_btn = ctk.CTkButton(
            control_frame,
            text="🗑 Clear",
            command=self.clear_chat,
            width=90,
            height=40,
            fg_color=self.COLORS["bg_light"],
            hover_color="#374151",
            font=("Consolas", 11, "bold"),
            corner_radius=10
        )
        clear_btn.pack(side="right", padx=5)
    
    def build_chat_display(self):
        """Build chat display area with modern styling"""
        chat_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.COLORS["bg_medium"],
            corner_radius=15,
            border_width=1,
            border_color=self.COLORS["bg_light"]
        )
        chat_frame.pack(fill="both", expand=True, pady=(0, 15), padx=15)
        
        # Chat textbox with custom styling
        self.chat_display = ctk.CTkTextbox(
            chat_frame,
            fg_color=self.COLORS["bg_medium"],
            text_color=self.COLORS["text_primary"],
            font=("Consolas", 11),
            wrap="word",
            corner_radius=10
        )
        self.chat_display.pack(fill="both", expand=True, padx=5, pady=5)
        self.chat_display.configure(state="disabled")
    
    def build_input_area(self):
        """Build modern input area with sleek design"""
        input_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        input_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        # Text input with modern styling
        self.input_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Ask Raven anything... (Press Enter)",
            height=50,
            font=("Consolas", 12),
            fg_color=self.COLORS["bg_medium"],
            border_color=self.COLORS["neon_blue"],  # ELITE: Neon blue border
            border_width=2,
            corner_radius=12
        )
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.input_entry.bind("<Return>", lambda e: self.send_message())
        
        # Send button
        self.send_btn = ctk.CTkButton(
            input_frame,
            text="Send ➤",
            command=self.send_message,
            width=100,
            height=50,
            fg_color=self.COLORS["accent"],
            hover_color=self.COLORS["accent_hover"],
            font=("Consolas", 13, "bold"),
            corner_radius=12
        )
        self.send_btn.pack(side="right")
    
    def load_state_images(self):
        """Load state images from assets folder"""
        self.state_images = {}
        states = ["idle", "listening", "thinking", "talking", "happy", "blinking"]
        
        for state in states:
            image_path = os.path.join(self.assets_path, f"raven_{state}.png")
            if os.path.exists(image_path):
                try:
                    img = Image.open(image_path)
                    img.thumbnail((340, 340), Image.Resampling.LANCZOS)
                    self.state_images[state] = ImageTk.PhotoImage(img)
                    print(f"[Terminal] Loaded image: raven_{state}.png")
                except Exception as e:
                    print(f"[Terminal] Error loading {state} image: {e}")
        
        # Use emoji placeholders if no images
        if not self.state_images:
            print("[Terminal] No images found, using emoji placeholders")
            self.avatar_label.configure(
                text="RAVEN ELITE\n\n(Place PNG images in raven_assets folder)",
                font=("Consolas", 16, "bold"),
                text_color=self.COLORS["text_secondary"]
            )
    
    def start_pulsing_glow(self):
        """ELITE: Pulsing glow animation for avatar border"""
        def pulse():
            brightness_levels = [0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7]
            while self.pulse_active:
                for brightness in brightness_levels:
                    if not self.pulse_active:
                        break
                    # Update border opacity effect (simulated by adjusting border width)
                    if self.current_state == "listening":
                        # Faster pulse for listening
                        time.sleep(0.15)
                    elif self.current_state == "thinking":
                        # Medium pulse for thinking
                        time.sleep(0.2)
                    else:
                        # Slow pulse for other states
                        time.sleep(0.3)
        
        thread = threading.Thread(target=pulse, daemon=True)
        thread.start()
    
    def update_state(self, state: str):
        """ELITE: Update visual state with mood-based glows and animations"""
        self.current_state = state
        
        # ELITE: Start/stop bouncing animation for talking/thinking
        if state in ["talking", "thinking"]:
            if not self.is_bouncing:
                self.start_bounce_animation()
        else:
            self.is_bouncing = False
        
        # Update avatar image
        if state in self.state_images:
            self.avatar_label.configure(image=self.state_images[state], text="")
        elif state == "stressed":
            # Special case for stressed mood - use thinking image with different glow
            if "thinking" in self.state_images:
                self.avatar_label.configure(image=self.state_images["thinking"], text="")
            else:
                self.avatar_label.configure(
                    text="😤",
                    font=("Consolas", 80),
                    text_color=self.COLORS["stressed_glow"]
                )
        else:
            # Emoji fallback
            emojis = {
                "idle": "😌",
                "listening": "🎤",
                "thinking": "🤔",
                "talking": "💬",
                "happy": "😊",
                "stressed": "😤"
            }
            self.avatar_label.configure(
                text=emojis.get(state, "🤖"),
                font=("Consolas", 80),
                text_color=self.COLORS["text_primary"]
            )
        
        # ELITE: Enhanced mood-based border glow
        glow_colors = {
            "idle": self.COLORS["idle_glow"],
            "listening": self.COLORS["listening_glow"],     # Emerald green
            "thinking": self.COLORS["thinking_glow"],       # Electric violet
            "talking": self.COLORS["talking_glow"],
            "happy": self.COLORS["happy_glow"],
            "stressed": self.COLORS["stressed_glow"]        # ELITE: Deep crimson
        }
        self.avatar_container.configure(border_color=glow_colors.get(state, self.COLORS["idle_glow"]))
        
        # Update status indicator
        state_labels = {
            "idle": "● Idle",
            "listening": "● Listening",
            "thinking": "● Thinking",
            "talking": "● Speaking",
            "happy": "● Happy",
            "stressed": "● Calming"
        }
        self.status_label.configure(
            text=state_labels.get(state, "● Active"),
            text_color=glow_colors.get(state, self.COLORS["idle_glow"])
        )
        
        # ELITE: Update mood indicator
        mood_emojis = {
            "neutral": "😌",
            "happy": "😊",
            "sad": "😔",
            "stressed": "😤",
            "tired": "😴"
        }
        current_mood = self.core.current_mood
        self.mood_label.configure(
            text=f"{mood_emojis.get(current_mood, '😌')} {current_mood.title()}",
            text_color=self.COLORS["neon_blue"] if current_mood != "neutral" else self.COLORS["text_secondary"]
        )
    
    def start_bounce_animation(self):
        """ELITE: Bouncing/vibrating animation for avatar during talking/thinking"""
        self.is_bouncing = True
        
        def bounce():
            original_pady = 10
            bounce_height = 5  # Pixels to bounce up/down
            
            while self.is_bouncing:
                # Bounce up
                for i in range(bounce_height):
                    if not self.is_bouncing:
                        break
                    self.avatar_label.pack_configure(pady=(original_pady - i, original_pady + i))
                    time.sleep(0.02)
                
                # Bounce down
                for i in range(bounce_height, -bounce_height - 1, -1):
                    if not self.is_bouncing:
                        break
                    self.avatar_label.pack_configure(pady=(original_pady - i, original_pady + i))
                    time.sleep(0.02)
                
                # Bounce back to center
                for i in range(-bounce_height, 1):
                    if not self.is_bouncing:
                        break
                    self.avatar_label.pack_configure(pady=(original_pady - i, original_pady + i))
                    time.sleep(0.02)
            
            # Reset to original position
            self.avatar_label.pack_configure(pady=(original_pady, original_pady))
        
        thread = threading.Thread(target=bounce, daemon=True)
        thread.start()
    
    def start_idle_animation(self):
        """Subtle idle animation with occasional blink"""
        def animate():
            blink_counter = 0
            while True:
                if self.current_state == "idle" and not self.is_processing:
                    blink_counter += 1
                    if blink_counter >= 5 and "blinking" in self.state_images:
                        # Show blink frame
                        self.avatar_label.configure(image=self.state_images["blinking"], text="")
                        time.sleep(0.2)
                        # Return to idle
                        if "idle" in self.state_images:
                            self.avatar_label.configure(image=self.state_images["idle"], text="")
                        blink_counter = 0
                time.sleep(3)
        
        thread = threading.Thread(target=animate, daemon=True)
        thread.start()
    
    def add_message_to_chat(self, sender: str, message: str):
        """Add message to chat display"""
        self.chat_display.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Color code by sender
        if sender == "You" or sender == "You (voice)":
            color = self.COLORS["listening_glow"]
            prefix = "🧑"
        elif sender == "Raven":
            color = self.COLORS["talking_glow"]
            prefix = "🦅"
        else:
            return
        
        formatted_msg = f"{prefix} [{timestamp}] {sender}:\n{message}\n\n"
        self.chat_display.insert("end", formatted_msg)
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")
        
        # Log to core
        self.core.log_chat(sender, message)
    
    def send_message(self):
        """Handle sending user message"""
        user_input = self.input_entry.get().strip()
        if not user_input or self.is_processing:
            return
        
        self.input_entry.delete(0, "end")
        self.add_message_to_chat("You", user_input)
        
        # Process in background
        thread = threading.Thread(target=self._process_message, args=(user_input,), daemon=True)
        thread.start()
    
    def _process_message(self, user_input: str):
        """Process message in background thread"""
        self.is_processing = True
        self.update_state("thinking")
        
        try:
            # Process with core (mood-aware)
            response, new_state = self.core.process_message(user_input)
            
            # Update to appropriate state
            self.update_state(new_state)
            
            # Add response to chat
            self.add_message_to_chat("Raven", response)
            
            # Text-to-speech if voice mode enabled
            if self.core.voice_enabled:
                self.core.speak(response)
            
            # Return to idle after 2 seconds
            time.sleep(2)
            self.update_state("idle")
            
        except Exception as e:
            print(f"[Terminal] Processing error: {e}")
            self.update_state("idle")
        finally:
            self.is_processing = False
    
    def toggle_voice_mode(self):
        """Toggle voice input/output"""
        self.core.voice_enabled = not self.core.voice_enabled
        status = "ON" if self.core.voice_enabled else "OFF"
        
        if self.core.mic_available:
            self.voice_btn.configure(text=f"🎤 Voice: {status}")
        else:
            self.voice_btn.configure(text="🎤 Mic Unavailable")
            return
        
        if self.core.voice_enabled:
            # Start voice listener thread
            self.voice_thread = threading.Thread(target=self._voice_listener, daemon=True)
            self.voice_thread.start()
        
        print(f"[Terminal] Voice mode: {status}")
    
    def _voice_listener(self):
        """Continuous voice listening loop with idle timeout messages"""
        idle_counter = 0
        last_activity_time = time.time()
        
        while self.core.voice_enabled and self.core.mic_available:
            if not self.is_processing:
                self.update_state("listening")
                text = self.core.listen_for_voice()
                
                if text:
                    # User spoke - reset idle counter
                    idle_counter = 0
                    last_activity_time = time.time()
                    self.add_message_to_chat("You (voice)", text)
                    self._process_message(text)
                    
                    # After processing, continue listening immediately
                    continue
                else:
                    # Check for idle timeout (30 seconds of silence)
                    current_time = time.time()
                    if current_time - last_activity_time > 30 and self.core.language_mode == "banglish":
                        idle_counter += 1
                        
                        # Send witty idle messages (but not too frequently)
                        if idle_counter == 1:
                            witty_messages = [
                                f"{self.core.USER_NAME}, চুপ করে আছেন কেন? কি ভাবছেন?",
                                f"Don't ignore me, {self.core.USER_NAME}! কথা বলুন!",
                                f"Hellooo? {self.core.USER_NAME}, আমি এখনো শুনছি...",
                                f"কিছু বলবেন না, {self.core.USER_NAME}? আমি wait করছি!",
                                f"{self.core.USER_NAME}, মনে হচ্ছে আপনি ব্যস্ত... কিছু help লাগবে?"
                            ]
                            import random
                            witty_msg = random.choice(witty_messages)
                            self.add_message_to_chat("Raven", witty_msg)
                            if self.core.voice_enabled:
                                self.core.speak(witty_msg)
                            last_activity_time = current_time
                        elif idle_counter > 6:
                            idle_counter = 0
                    
                    self.update_state("listening")
            time.sleep(0.5)
        
        self.update_state("idle")
    
    def toggle_vision_mode(self):
        """Toggle automatic vision mode"""
        self.core.vision_enabled = not self.core.vision_enabled
        status = "ON" if self.core.vision_enabled else "OFF"
        self.vision_btn.configure(text=f"👁 Vision: {status}")
        
        mode_msg = "Vision mode enabled - ami screen dekhbo every message e." if self.core.vision_enabled else "Vision mode disabled."
        print(f"[Terminal] {mode_msg}")
    
    def manual_screenshot(self):
        """Manually trigger screenshot and analysis"""
        if self.is_processing:
            return
        
        thread = threading.Thread(target=self._take_screenshot, daemon=True)
        thread.start()
    
    def _take_screenshot(self):
        """Take and analyze screenshot in background"""
        self.is_processing = True
        self.update_state("thinking")
        
        try:
            image_data = self.core.take_screenshot()
            if image_data:
                response = self.core.chat_with_ollama(
                    "Describe what you see in this screenshot in detail.",
                    image_data
                )
                self.update_state("talking")
                self.add_message_to_chat("Raven", f"📸 Screenshot Analysis:\n{response}")
                
                if self.core.voice_enabled:
                    self.core.speak(response)
            
            time.sleep(2)
            self.update_state("idle")
            
        except Exception as e:
            print(f"[Terminal] Screenshot error: {e}")
            self.update_state("idle")
        finally:
            self.is_processing = False
    
    def clear_chat(self):
        """Clear chat display"""
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
        print("[Terminal] Chat cleared")
    
    def on_closing(self):
        """Handle window close event"""
        print("[Terminal] Saving memory and closing...")
        self.pulse_active = False
        self.is_bouncing = False
        self.core.save_memory()
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.update_state("idle")
        self.root.mainloop()
