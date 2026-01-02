"""
Raven Assistant v2.0 - Code Validation Script

This script validates the code structure without requiring a display.
Run this before deploying to Windows to ensure everything is correct.
"""

import os
import sys
import ast

def check_file_exists(filepath):
    """Check if file exists"""
    if os.path.exists(filepath):
        print(f"   ✅ {os.path.basename(filepath)} exists")
        return True
    else:
        print(f"   ❌ {os.path.basename(filepath)} NOT FOUND")
        return False

def check_syntax(filepath):
    """Check Python syntax without importing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        print(f"   ✅ {os.path.basename(filepath)} syntax valid")
        return True
    except SyntaxError as e:
        print(f"   ❌ {os.path.basename(filepath)} syntax error: {e}")
        return False

def check_class_defined(filepath, class_name):
    """Check if class is defined in file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        tree = ast.parse(content)
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        if class_name in classes:
            print(f"   ✅ Class '{class_name}' defined")
            return True
        else:
            print(f"   ❌ Class '{class_name}' NOT FOUND")
            return False
    except Exception as e:
        print(f"   ❌ Error checking class: {e}")
        return False

def main():
    print("=" * 70)
    print("RAVEN ASSISTANT v2.0 - CODE VALIDATION")
    print("=" * 70)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Check files exist
    print("\n1. Checking required files...")
    files_ok = True
    files_ok &= check_file_exists(os.path.join(base_path, "raven_core.py"))
    files_ok &= check_file_exists(os.path.join(base_path, "raven_gui.py"))
    files_ok &= check_file_exists(os.path.join(base_path, "raven_assistant.py"))
    files_ok &= check_file_exists(os.path.join(base_path, "raven_requirements.txt"))
    
    # Check syntax
    print("\n2. Checking Python syntax...")
    syntax_ok = True
    syntax_ok &= check_syntax(os.path.join(base_path, "raven_core.py"))
    syntax_ok &= check_syntax(os.path.join(base_path, "raven_gui.py"))
    syntax_ok &= check_syntax(os.path.join(base_path, "raven_assistant.py"))
    
    # Check classes
    print("\n3. Checking class definitions...")
    classes_ok = True
    classes_ok &= check_class_defined(os.path.join(base_path, "raven_core.py"), "RavenCore")
    classes_ok &= check_class_defined(os.path.join(base_path, "raven_core.py"), "CommandsHandler")
    classes_ok &= check_class_defined(os.path.join(base_path, "raven_gui.py"), "RavenGUI")
    
    # Check assets folder
    print("\n4. Checking assets folder...")
    assets_path = os.path.join(base_path, "raven_assets")
    if os.path.exists(assets_path):
        print(f"   ✅ raven_assets folder exists")
        images = [f for f in os.listdir(assets_path) if f.endswith('.png')]
        if images:
            print(f"   ✅ Found {len(images)} PNG images: {', '.join(images)}")
        else:
            print("   ⚠️  No PNG images found (will use emoji placeholders)")
    else:
        print(f"   ⚠️  raven_assets folder not found (will be created on first run)")
    
    # Check requirements
    print("\n5. Checking requirements.txt...")
    req_file = os.path.join(base_path, "raven_requirements.txt")
    with open(req_file, 'r') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    print(f"   ✅ Found {len(requirements)} required packages")
    for req in requirements:
        print(f"      - {req}")
    
    # Final summary
    print("\n" + "=" * 70)
    if files_ok and syntax_ok and classes_ok:
        print("✅ ALL VALIDATION CHECKS PASSED!")
        print("=" * 70)
        print("\n📦 Raven Assistant v2.0 is ready for deployment!")
        print("\nNext steps:")
        print("1. Copy all files to your Windows PC")
        print("2. Install dependencies: pip install -r raven_requirements.txt")
        print("3. Start Ollama server: ollama serve")
        print("4. Run Raven: python raven_assistant.py")
        print("\n⚠️  Note: This is a desktop application and requires:")
        print("   - Windows 10/11")
        print("   - Python 3.8+")
        print("   - Ollama with 'Raven' and 'llama3.2-vision' models")
        return 0
    else:
        print("❌ VALIDATION FAILED - Please fix errors above")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(main())
