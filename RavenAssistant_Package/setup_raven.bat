@echo off
echo ================================================
echo     RAVEN ASSISTANT - INSTALLATION SCRIPT
echo ================================================
echo.

echo Step 1: Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.8+ from python.org
    pause
    exit /b
)
echo Python found!
echo.

echo Step 2: Installing Python dependencies...
pip install -r raven_requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b
)
echo Dependencies installed successfully!
echo.

echo Step 3: Creating assets folder...
if not exist "raven_assets" mkdir raven_assets
echo Assets folder created at: %cd%\raven_assets
echo.

echo Step 4: Creating memory folder...
if not exist "D:\Raven\Memory" mkdir "D:\Raven\Memory"
echo Memory folder created at: D:\Raven\Memory
echo.

echo ================================================
echo     INSTALLATION COMPLETE!
echo ================================================
echo.
echo IMPORTANT - Next Steps:
echo.
echo 1. Install Ollama from: https://ollama.ai
echo.
echo 2. Open a new command prompt and run:
echo    ollama pull raven
echo    ollama pull llama3.2-vision
echo.
echo 3. Start Ollama server:
echo    ollama serve
echo.
echo 4. Place your 5 state images in:
echo    %cd%\raven_assets\
echo    - raven_idle.png
echo    - raven_blinking.png
echo    - raven_thinking.png
echo    - raven_talking.png
echo    - raven_happy.png
echo.
echo 5. Run Raven Assistant:
echo    python raven_assistant.py
echo.
echo ================================================
pause
