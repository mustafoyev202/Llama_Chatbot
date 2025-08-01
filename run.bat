@echo off
echo 🦙 Llama 4 Chat Interface
echo =========================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if requirements are installed
echo 📦 Checking dependencies...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
)

REM Check if model exists
if not exist "llama_models\Llama-4-Scout-17B\Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf" (
    echo 📥 Model not found. Downloading...
    python download.py
)

REM Check if llama.cpp exists
if not exist "llama.cpp\llama-cli.exe" (
    echo 🔧 llama.cpp not found. Please run setup first.
    echo Run: python scripts/setup.py
    pause
    exit /b 1
)

REM Start the application
echo 🚀 Starting Llama 4 Chat Interface...
echo.
echo The application will open in your browser at: http://localhost:8501
echo Press Ctrl+C to stop the application
echo.
streamlit run app.py

pause 