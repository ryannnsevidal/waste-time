#!/bin/bash

# Quick Deploy Script - Deploy to Railway/Render/Heroku
# Run this script to quickly deploy your scammer waste bot

set -e

echo "🚀 Quick Deploy Script for Scammer Waste Bot"
echo "=============================================="

# Check if git repo is clean
if [[ -n $(git status --porcelain) ]]; then
    echo "📝 Committing latest changes..."
    git add .
    git commit -m "deploy: prepare for production deployment"
else
    echo "✅ Git repo is clean"
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push origin main

echo ""
echo "🎯 Deployment Options:"
echo ""
echo "1. 🟢 Railway (Recommended - Easiest)"
echo "   • Go to https://railway.app"
echo "   • Connect GitHub repo: ryannnsevidal/waste-time"
echo "   • Add environment variables:"
echo "     SCAMMER_WASTE_API_KEY=your-secure-key"
echo "     SECRET_KEY=your-secret-key"
echo "     FLASK_ENV=production"
echo "   • Deploy automatically!"
echo ""
echo "2. 🔵 Render (Great Free Tier)"
echo "   • Go to https://render.com"
echo "   • Create Web Service from GitHub"
echo "   • Build: pip install -r requirements.txt"
echo "   • Start: cd src && gunicorn app:app"
echo ""
echo "3. 🟡 Heroku (Classic)"
echo "   Run: heroku create your-app-name"
echo "   Run: git push heroku main"
echo ""

# Generate secure keys
echo "🔐 Generated Secure Keys for Production:"
API_KEY=$(openssl rand -hex 32)
SECRET_KEY=$(openssl rand -hex 32)

echo "┌─────────────────────────────────────────────────────────────────┐"
echo "│ 🔑 SAVE THESE KEYS - You'll need them for deployment:           │"
echo "├─────────────────────────────────────────────────────────────────┤"
echo "│ SCAMMER_WASTE_API_KEY=$API_KEY │"
echo "│ SECRET_KEY=$SECRET_KEY │"
echo "└─────────────────────────────────────────────────────────────────┘"

echo ""
echo "📋 Your deployment checklist:"
echo "✅ Code committed and pushed to GitHub"
echo "🔲 Choose hosting platform (Railway recommended)"
echo "🔲 Set environment variables with keys above"
echo "🔲 Deploy and test your live site"
echo "🔲 Configure custom domain (optional)"
echo ""
echo "🎉 Your scammer waste bot is ready for the world!"
echo "📖 See HOSTING_GUIDE.md for detailed instructions"
