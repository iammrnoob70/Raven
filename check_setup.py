"""
Raven Assistant - System Check Script
This script verifies that all dependencies and requirements are properly set up.
"""

import sys
import os

def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - OUTDATED (need 3.8+)")
        return False

def check_dependencies():
    """Check if all required packages are installed"""
    print("\nChecking Python dependencies...")
    
    dependencies = {
        'customtkinter': 'CustomTkinter',
        'PIL': 'Pillow',
        'requests': 'requests',
        'pyautogui': 'PyAutoGUI',
        'speech_recognition': 'SpeechRecognition',
        'pyttsx3': 'pyttsx3',
        'duckduckgo_search': 'duckduckgo-search'
    }
    
    all_installed = True
    for module, package in dependencies.items():
        try:
            __import__(module)
            print(f"✓ {package} - Installed")
        except ImportError:
            print(f"✗ {package} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_ollama():
    """Check if Ollama is accessible"""
    print("\nChecking Ollama connection...")
    
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            print("✓ Ollama server - Running")
            
            # Check models
            data = response.json()
            models = [model['name'] for model in data.get('models', [])]
            
            print("\nInstalled models:")
            for model in models:
                print(f"  • {model}")
            
            # Check for required models
            has_text_model = any('raven' in m or 'llama' in m for m in models)
            has_vision_model = any('vision' in m or 'llava' in m for m in models)
            
            if has_text_model:
                print("✓ Text model available")
            else:
                print("⚠ No suitable text model found (recommended: raven, llama2)")
            
            if has_vision_model:
                print("✓ Vision model available")
            else:
                print("⚠ No vision model found (recommended: llama3.2-vision, llava)")
            
            return True
        else:
            print("✗ Ollama server - Not responding properly")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Ollama server - NOT RUNNING")
        print("  Start with: ollama serve")
        return False
    except Exception as e:
        print(f"✗ Ollama check failed: {e}")
        return False

def check_assets():
    """Check if asset folder and images exist"""
    print("\nChecking asset files...")
    
    assets_path = os.path.join(os.path.dirname(__file__), "raven_assets")
    
    if not os.path.exists(assets_path):
        print(f"⚠ Assets folder not found: {assets_path}")
        print("  App will use emoji placeholders")
        return False
    
    print(f"✓ Assets folder exists: {assets_path}")
    
    required_images = [
        'raven_idle.png',
        'raven_blinking.png',
        'raven_thinking.png',
        'raven_talking.png',
        'raven_happy.png'
    ]
    
    found_images = 0
    for image in required_images:
        image_path = os.path.join(assets_path, image)
        if os.path.exists(image_path):
            print(f"✓ {image} - Found")
            found_images += 1
        else:
            print(f"⚠ {image} - Missing")
    
    if found_images == 0:
        print("\n⚠ No custom images found - app will use emoji placeholders")
        return False
    elif found_images < 5:
        print(f"\n⚠ Only {found_images}/5 images found - some states will use placeholders")
        return False
    else:
        print("\n✓ All custom images found!")
        return True

def check_memory_path():
    """Check if memory folder exists"""
    print("\nChecking memory folder...")
    
    memory_path = "D:/Raven/Memory"
    
    if os.path.exists(memory_path):
        print(f"✓ Memory folder exists: {memory_path}")
        return True
    else:
        print(f"⚠ Memory folder not found: {memory_path}")
        print("  Folder will be created automatically on first run")
        return False

def main():
    """Run all checks"""
    print("=" * 60)
    print("   RAVEN ASSISTANT - SYSTEM CHECK")
    print("=" * 60)
    
    checks = {
        "Python Version": check_python_version(),
        "Dependencies": check_dependencies(),
        "Ollama": check_ollama(),
        "Assets": check_assets(),
        "Memory Folder": check_memory_path()
    }
    
    print("\n" + "=" * 60)
    print("   SUMMARY")
    print("=" * 60)
    
    for check_name, passed in checks.items():
        status = "✓ OK" if passed else "⚠ NEEDS ATTENTION"
        print(f"{check_name:20} {status}")
    
    print("\n" + "=" * 60)
    
    critical_checks = ["Python Version", "Dependencies", "Ollama"]
    critical_passed = all(checks[check] for check in critical_checks if check in checks)
    
    if critical_passed:
        print("\n✓ ALL CRITICAL CHECKS PASSED!")
        print("\nYou can now run: python raven_assistant.py")
    else:
        print("\n✗ SOME CRITICAL CHECKS FAILED")
        print("\nPlease fix the issues above before running Raven Assistant.")
        print("\nQuick fixes:")
        if not checks.get("Python Version"):
            print("  • Install Python 3.8+ from python.org")
        if not checks.get("Dependencies"):
            print("  • Run: pip install -r raven_requirements.txt")
        if not checks.get("Ollama"):
            print("  • Install Ollama from ollama.ai")
            print("  • Run: ollama serve")
            print("  • Pull models: ollama pull raven && ollama pull llama3.2-vision")
    
    if not checks.get("Assets"):
        print("\n⚠ Note: Custom images not found")
        print("  • App will work with emoji placeholders")
        print("  • Place images in 'raven_assets' folder for custom look")
    
    print("\n" + "=" * 60)
    print()

if __name__ == "__main__":
    main()
