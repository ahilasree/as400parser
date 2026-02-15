#!/usr/bin/env python3
"""
Launch the IBM i Parser UI with auto-populated email settings
"""

import os
import sys
import subprocess
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

def main():
    print("Launching IBM i Parser UI...")
    print("Email settings will be loaded (but only activated when you enable email)")
    print()
    
    # Check if .env.local exists
    env_file = ROOT / ".env.local"
    if env_file.exists():
        print("✅ Email configuration found and loaded:")
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if 'PASS' in key:
                        print(f"   {key}: [HIDDEN]")
                    else:
                        print(f"   {key}: {value}")
        print("   → Check 'Email report' checkbox in UI to activate")
    else:
        print("⚠️  No .env.local file found - email settings will not be available")
        print("   Create .env.local with your email configuration")
    
    print()
    print("Starting UI...")
    
    # Launch UI in virtual environment
    try:
        subprocess.run([sys.executable, "ui/main_ui.py"], cwd=ROOT)
    except KeyboardInterrupt:
        print("\nUI closed by user")
    except Exception as e:
        print(f"Error launching UI: {e}")

if __name__ == "__main__":
    main()
