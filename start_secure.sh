#!/bin/bash

# Secure Production Startup Script for Scammer Waste Bot

echo "🔒 Starting Secure Scammer Waste Bot..."

# Set production environment variables
export FLASK_ENV=production
export SECRET_KEY=$(openssl rand -hex 32)
export API_KEY=$(openssl rand -hex 16)
export ADMIN_TOKEN=$(openssl rand -hex 24)

echo "🔑 Generated secure credentials"
echo "📝 API Key: $API_KEY"
echo "🔐 Admin Token: $ADMIN_TOKEN"

# Build frontend if needed
if [ ! -d "static" ] || [ -z "$(ls -A static)" ]; then
    echo "📁 Building React frontend..."
    cd interface-imagine-integrate-main
    npm run build
    cd ..
    cp -r interface-imagine-integrate-main/dist/* static/
fi

# Start secure backend
echo "🚀 Starting secure Flask backend..."
python secure_app.py

echo "✅ Secure Scammer Waste Bot started!"
echo "🌐 Access dashboard at: https://localhost:5001"
echo "📊 API endpoint: https://localhost:5001/api/stats"
echo "🔒 Remember to use HTTPS in production!"
