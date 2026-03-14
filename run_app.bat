@echo off
echo.
echo 🏥 Medical Lab Markdown Manager
echo ===============================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.7 or higher.
    echo    Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing required packages...
    echo.
    python setup.py
    if errorlevel 1 (
        echo ❌ Installation failed. Please check the error messages above.
        pause
        exit /b 1
    )
)

echo 🚀 Starting Medical Lab Markdown Manager...
echo.
echo 💡 The app will open in your default web browser
echo    URL: http://localhost:8501
echo.
echo 🛑 To stop the app, press Ctrl+C in this window
echo.

REM Start the Streamlit app
streamlit run app.py

echo.
echo 👋 Medical Lab Markdown Manager stopped.
pause