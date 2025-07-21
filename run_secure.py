#!/usr/bin/env python3
"""
Production entry point for the Scammer Waste Bot application.
Runs the secure version with all security features enabled.
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.secure_app import app

if __name__ == '__main__':
    # Production server with Gunicorn
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
