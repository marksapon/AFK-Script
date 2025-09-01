@echo off
echo Starting Script
 
:: Run main using venv
"%~dp0venv\Scripts\python.exe" "%~dp0main.py"
 
pause