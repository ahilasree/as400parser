@echo off
echo Starting IBM i AST Parser API...
cd /d "%~dp0\.."
call venv\Scripts\activate
echo.
echo API will be available at: http://localhost:5000
echo Health check: http://localhost:5000/health
echo Parse endpoint: http://localhost:5000/api/parse
echo.
echo Press Ctrl+C to stop the server
echo.
python test_api.py
pause
