@echo off
cd /d "%~dp0.."
echo Launching IBM i Parser UI...
echo Email settings will be loaded (but only activated when you enable email)
echo.

if exist .env.local (
    echo ✅ Email configuration found and loaded:
    for /f "tokens=1,2 delims==" %%a in ('findstr /i "EMAIL_TO\|SMTP_HOST\|SMTP_USER\|SMTP_PASS\|SMTP_PORT\|SMTP_TLS" .env.local 2^>nul') do (
        if "%%a"=="SMTP_PASS" (
            echo    %%a: [HIDDEN]
        ) else (
            echo    %%a: %%b
        )
    )
    echo    → Check 'Email report' checkbox in UI to activate
) else (
    echo ⚠️  No .env.local file found - email settings will not be available
)

echo.
echo Starting UI...
call venv\Scripts\activate
python ui\main_ui.py
if %ERRORLEVEL% NEQ 0 (
    echo Error occurred while running UI
)
echo.
echo UI closed or press any key to exit...
pause > nul
