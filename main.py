#!/usr/bin/env python3
"""
Scammer Waste Bot - Main Entry Point

This script provides a simple way to run the application.
For production use, use the secure_app.py with proper configuration.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Main entry point for the application."""
    try:
        from src.app import app
        print("Starting Scammer Waste Bot...")
        print("Access the dashboard at: http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    except ImportError as e:
        print(f"Error importing application: {e}")
        print("Make sure all dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
