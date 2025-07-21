#!/usr/bin/env python3
"""
Main entry point for the Scammer Waste Bot application.
This script provides a convenient way to run the application from the root directory.
"""
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.app import app

if __name__ == '__main__':
    # Development server
    app.run(host='0.0.0.0', port=5000, debug=True)
