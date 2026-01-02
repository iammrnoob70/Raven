"""Raven Assistant - GUI Interface (UPGRADED)

This module handles all the visual interface, state animations, and user interactions.
Upgraded with modern floating overlay, draggable window, and enhanced glow effects.
"""

import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import time
import os
from datetime import datetime
from raven_core import RavenCore


class RavenGUI:
    """Modern Floating Overlay GUI for Raven Assistant with state-based visual feedback"""
    
    # UPGRADE: Enhanced cyberpunk color scheme
    COLORS = {
        "bg_dark": "#121212",           # Deep charcoal background (semi-transparent)
        "bg_medium": "#1a1a1a",         # Medium dark
        "bg_light": "#252525",          # Lighter panels
        "idle_glow": "#60a5fa",         # Soft blue for idle
        "listening_glow": "#50fa7b",    # Emerald green for listening
        "thinking_glow": "#bd93f9",     # Electric violet for thinking
        "talking_glow": "#8be9fd",      # Cyan for talking
        "happy_glow": "#f1fa8c",        # Yellow for happy
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
        self.root.title("Raven Assistant")
        self.root.geometry("800x920")
        
        # UPGRADE: Floating window setup
        self.root.overrideredirect(True)  # Remove title bar
        self.root.attributes('-alpha', 0.9)  # Semi-transparent
        self.root.attributes('-topmost', True)  # Always on top
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # State tracking
        self.current_state = "idle"
        self.is_processing = False
        
        # UPGRADE: Draggable window variables
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
        
        # Start idle animation
        self.start_idle_animation()
        
        # Start voice listener if enabled
        self.voice_thread = None
    
    def build_gui(self):
        """Build the complete modern GUI interface"""
        # Main container with rounded corners effect
        self.main_frame = ctk.CTkFrame(
            self.root, 
            fg_color=self.COLORS["bg_dark"],
            corner_radius=20,
            border_width=2,
            border_color=self.COLORS["accent"]
        )
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # UPGRADE: Title bar with drag functionality and close button
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
            text="RAVEN ASSISTANT",
            font=("Consolas", 18, "bold"),
            text_color=self.COLORS["accent"]
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
        
        # Status indicator
        self.status_label = ctk.CTkLabel(
            title_frame,
            text="● Idle",
            font=("Consolas", 11),
            text_color=self.COLORS["idle_glow"]
        )
        self.status_label.pack(side="right", padx=15)
        
        # UPGRADE: Avatar frame with enhanced state-based glow
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
        
        # UPGRADE: Modern icon-based control buttons
        self.build_controls()
        
        # UPGRADE: Chat display with bubble style
        self.build_chat_display()
        
        # UPGRADE: Modern input area
        self.build_input_area()
    
    def start_drag(self, event):
        """UPGRADE: Start dragging the window"""
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
    
    def on_drag(self, event):
        """UPGRADE: Handle window dragging"""
        x = self.root.winfo_x() + event.x - self.drag_data["x"]
        y = self.root.winfo_y() + event.y - self.drag_data["y"]
        self.root.geometry(f"+{x}+{y}")
    
    def build_controls(self):
        """UPGRADE: Build modern control buttons panel"""
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
        """UPGRADE: Build chat display area with modern styling"""
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
        """UPGRADE: Build modern input area with sleek design"""
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
            border_color=self.COLORS["accent"],
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
                text="RAVEN\n\n(Place PNG images in raven_assets folder)",
                font=("Consolas", 16, "bold"),
                text_color=self.COLORS["text_secondary"]
            )
    
    def update_state(self, state: str):
        """UPGRADE: Update visual state with enhanced glow transitions"""
        self.current_state = state
        
        # Update avatar image
        if state in self.state_images:
            self.avatar_label.configure(image=self.state_images[state], text="")
        else:
            # Emoji fallback
            emojis = {
                "idle": "😌",
                "listening": "🎤",
                "thinking": "🤔",
                "talking": "💬",
                "happy": "😊"
            }
            self.avatar_label.configure(
                text=emojis.get(state, "🤖"),
                font=("Consolas", 80),
                text_color=self.COLORS["text_primary"]
            )
        
        # UPGRADE: Enhanced border glow based on state
        glow_colors = {
            "idle": self.COLORS["idle_glow"],
            "listening": self.COLORS["listening_glow"],
            "thinking": self.COLORS["thinking_glow"],
            "talking": self.COLORS["talking_glow"],
            "happy": self.COLORS["happy_glow"]
        }
        self.avatar_container.configure(border_color=glow_colors.get(state, self.COLORS["idle_glow"]))
        
        # Update status indicator
        state_labels = {
            "idle": "● Idle",
            "listening": "● Listening",
            "thinking": "● Thinking",
            "talking": "● Speaking",
            "happy": "● Happy"
        }
        self.status_label.configure(
            text=state_labels.get(state, "● Active"),
            text_color=glow_colors.get(state, self.COLORS["idle_glow"])
        )
    
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
        """Add message to chat display (user-visible only)"""
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
            return  # Don't show system messages in chat
        
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
            # Process with core
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
        """Continuous voice listening loop"""
        while self.core.voice_enabled and self.core.mic_available:
            if not self.is_processing:
                self.update_state("listening")
                text = self.core.listen_for_voice()
                
                if text:
                    self.add_message_to_chat("You (voice)", text)
                    self._process_message(text)
                else:
                    self.update_state("idle")
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
        self.core.save_memory()
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.update_state("idle")
        self.root.mainloop()
