#!/bin/bash

# Quick Start Script for Development and Testing
# Sets up the environment and starts the integrated system

set -e

echo "🚀 Starting Scammer Waste Bot System..."

# Change to project directory
cd /workspaces/waste-time

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q flask flask-cors flask-limiter requests gunicorn

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p data logs

# Initialize database
echo "💾 Initializing database..."
python3 -c "
import sys
sys.path.append('src')
from app import init_production_db
init_production_db()
print('Database initialized successfully!')
"

# Start the application
echo "🌐 Starting application on http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""

export FLASK_APP=src/app.py
export FLASK_ENV=development
export SCAMMER_WASTE_API_KEY=scammer-waste-api-key-2025

cd src
python3 app.py
