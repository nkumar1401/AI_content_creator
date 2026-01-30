@echo off
REM Windows One-Click Setup for AI/ML Career System
REM Double-click this file to set up everything!

echo ======================================================================
echo   AI/ML CAREER LAUNCH SYSTEM - WINDOWS SETUP
echo ======================================================================
echo.

REM Set console to UTF-8
chcp 65001 >nul 2>&1
echo Step 1: Console encoding set to UTF-8
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from python.org
    echo.
    pause
    exit /b 1
)

echo Step 2: Python detected
python --version
echo.

REM Fix all Python files for Windows
echo Step 3: Fixing encoding in all Python files...
python FIX_ALL_WINDOWS.py
echo.

REM Run setup
echo Step 4: Running main setup...
python setup.py
echo.

echo ======================================================================
echo   SETUP COMPLETE!
echo ======================================================================
echo.
echo Next steps:
echo   1. Edit: data\your_profile.json (add your details)
echo   2. Run: python run_daily.py
echo   3. Open: content_creator_dashboard.html
echo.
echo Press any key to exit...
pause >nul
