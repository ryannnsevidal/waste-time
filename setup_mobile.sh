#!/bin/bash

# Mobile App Development Setup Script
# Run this to set up the React Native mobile app

echo "🤖 Setting up Scammer Waste Bot Mobile App..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Node.js and npm found"

# Navigate to mobile app directory
cd "$(dirname "$0")/mobile-app" || exit 1

echo "📦 Installing dependencies..."
npm install

# Install Expo CLI globally if not present
if ! command -v expo &> /dev/null; then
    echo "📱 Installing Expo CLI globally..."
    npm install -g @expo/cli
fi

# Install EAS CLI globally if not present
if ! command -v eas &> /dev/null; then
    echo "🏗️ Installing EAS CLI globally..."
    npm install -g @expo/cli
fi

echo "✅ Dependencies installed successfully!"

echo ""
echo "🚀 Mobile app setup complete!"
echo ""
echo "Next steps:"
echo "1. cd mobile-app"
echo "2. npx expo start"
echo "3. Scan QR code with Expo Go app on your phone"
echo ""
echo "Development commands:"
echo "- npx expo start --android  (for Android emulator)"
echo "- npx expo start --ios      (for iOS simulator)"
echo "- npx expo start --web      (for web browser)"
echo ""
echo "📱 Your mobile app is ready to develop!"
