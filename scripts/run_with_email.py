#!/usr/bin/env python3
"""
Run pipeline with auto-populated email settings from .env.local
"""

import os
import sys
import subprocess
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def load_email_config():
    """Load email configuration from .env.local file"""
    env_file = ROOT / ".env.local"
    config = {}
    
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    config[key] = value
    
    return config

def main():
    # Load email config
    config = load_email_config()
    
    # Build command line args
    args = [sys.executable, "main.py"]
    
    # Add files if provided
    if len(sys.argv) > 1:
        args.extend(sys.argv[1:])
    else:
        # Default example files
        args.extend([
            "examples/example.clle",
            "examples/example.rpgle", 
            "examples/schema.sql",
            "examples/display.dspf"
        ])
    
    # Add email settings if available
    if config.get('EMAIL_TO') and config.get('SMTP_HOST'):
        args.extend([
            "--email-to", config['EMAIL_TO'],
            "--smtp-host", config['SMTP_HOST'],
            "--smtp-port", config.get('SMTP_PORT', '587'),
            "--export-pdf", f"output/report_{config.get('EMAIL_TO', 'auto').split('@')[0]}.pdf"
        ])
        
        if config.get('SMTP_USER'):
            args.extend(["--smtp-user", config['SMTP_USER']])
        if config.get('SMTP_PASS'):
            args.extend(["--smtp-pass", config['SMTP_PASS']])
        if config.get('SMTP_TLS', 'true').lower() == 'true':
            args.append("--smtp-tls")
    
    print("Running with email configuration:")
    print(f"   To: {config.get('EMAIL_TO', 'Not set')}")
    print(f"   SMTP: {config.get('SMTP_HOST', 'Not set')}")
    print(f"   User: {config.get('SMTP_USER', 'Not set')}")
    print(f"   TLS: {config.get('SMTP_TLS', 'Not set')}")
    print(f"   Output: output/report_{config.get('EMAIL_TO', 'auto').split('@')[0]}.pdf")
    print(f"   Command: {' '.join(args[2:])}")  # Skip python and main.py
    print()
    
    # Run in virtual environment
    try:
        result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Error running command: {e}")

if __name__ == "__main__":
    main()
