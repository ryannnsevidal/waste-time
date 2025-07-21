# Railway Account Setup & Deployment Guide

## 🚀 Step-by-Step Railway Setup

### Step 1: Create Railway Account
1. Go to **https://railway.app**
2. Click **"Start a New Project"**
3. Sign up with **GitHub** (recommended) or email
4. Verify your account

### Step 2: Login via CLI (after account creation)
```bash
railway login
```
This will open your browser to authenticate.

### Step 3: Create New Project
```bash
railway new
```
Choose: **"Empty Project"**

### Step 4: Add PostgreSQL Database
```bash
railway add postgresql
```

### Step 5: Set Environment Variables
Run these commands to generate secure keys:
```bash
# Generate API key
python -c "import secrets; print('API_KEY=' + secrets.token_hex(32))"

# Generate admin token  
python -c "import secrets; print('ADMIN_TOKEN=' + secrets.token_hex(32))"

# Generate secret key
python -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))"
```

Copy these outputs and add them in Railway dashboard under **Variables**.

### Step 6: Deploy Your App
```bash
railway up
```

### Step 7: Initialize Database
```bash
railway run python csv_to_database.py
```

### Step 8: Get Your Live URL
```bash
railway domain
```

## 🔧 What We'll Do Together

1. **I'll prepare your files** for Railway deployment
2. **You create the account** at railway.app
3. **We deploy together** step by step
4. **Your app goes live** with database

## 📋 Account Requirements

- **Email address** or **GitHub account** (GitHub recommended)
- **No credit card required** for free tier
- **$5 free credit** monthly
- **Instant activation**

Ready to create your Railway account?
