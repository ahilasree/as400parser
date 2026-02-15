@echo off
cd /d "%~dp0.."
echo Running with email configuration:
echo.

REM Load email config from .env.local
for /f "tokens=1,2 delims==" %%a in ('findstr /i "EMAIL_TO\|SMTP_HOST\|SMTP_USER\|SMTP_PASS\|SMTP_PORT\|SMTP_TLS" .env.local 2^>nul') do (
    set "%%a=%%b"
    echo    %%a: %%b
)

echo.
echo Output: output\report_%EMAIL_TO:.=_%.pdf
echo.

REM Activate virtual environment and run
call venv\Scripts\activate
python main.py examples\example.clle examples\example.rpgle --email-to "%EMAIL_TO%" --smtp-host "%SMTP_HOST%" --smtp-user "%SMTP_USER%" --smtp-pass "%SMTP_PASS%" --smtp-port "%SMTP_PORT%" --smtp-tls --export-pdf "output\report_%EMAIL_TO:.=_%.pdf"

pause
