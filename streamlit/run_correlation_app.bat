@echo off
echo Starting Correlation Analysis Dashboard...
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

REM Run Streamlit app
echo Starting Streamlit application...
echo.
echo The app will open in your default web browser.
echo Press Ctrl+C to stop the application.
echo.

streamlit run correlation_app.py

pause