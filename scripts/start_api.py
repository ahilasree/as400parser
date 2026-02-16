#!/usr/bin/env python3
"""
Simple startup script for IBM i AST Parser API
"""

import sys
import os
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    from api.app import app
    print("✅ API loaded successfully")
    print("🚀 Starting server on http://localhost:5000")
    print("📖 API documentation: http://localhost:5000/api/parse")
    print("🔍 Health check: http://localhost:5000/health")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run in development mode
    app.run(host='0.0.0.0', port=5000, debug=True)
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure all dependencies are installed:")
    print("pip install flask flask-cors waitress")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error starting API: {e}")
    sys.exit(1)
