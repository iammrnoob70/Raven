@echo off
echo ================================================
echo     STARTING RAVEN ASSISTANT
echo ================================================
echo.

echo Checking if Ollama is running...
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: Ollama server is not running!
    echo Please start Ollama in another terminal:
    echo    ollama serve
    echo.
    echo Press any key to try launching Raven anyway...
    pause >nul
) else (
    echo Ollama is running!
)
echo.

echo Launching Raven Assistant...
python raven_assistant.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start Raven Assistant!
    echo Please check that all dependencies are installed.
    pause
)
