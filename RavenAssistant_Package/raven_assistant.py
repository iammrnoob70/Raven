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
