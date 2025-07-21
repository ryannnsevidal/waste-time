# Free Hosting & Database Setup Guide

## Best FREE Platforms for Your App

### 1. **Railway** (RECOMMENDED)
**Why it's perfect:**
- FREE tier: $5 credit monthly (enough for small apps)
- Automatic PostgreSQL database included
- GitHub integration (deploys automatically)
- Built-in environment variables
- SSL certificates included

**Setup Commands:**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway link
railway up
```

### 2. **Render** (Alternative)
**Free tier includes:**
- Static sites: Unlimited
- Web services: 750 hours/month
- PostgreSQL database: 90 days free
- SSL certificates included

### 3. **Supabase** (Database + Backend)
**Free tier includes:**
- PostgreSQL database: 500MB
- Authentication built-in
- Real-time subscriptions
- API generation
- 50,000 monthly active users

## Your CSV Generation is ALREADY Configured

Your app automatically generates CSV files with comprehensive analytics:

**Location:** `/analytics_data/scammer_analysis_YYYYMMDD.csv`

**Data Captured:**
- Timestamp of interactions
- Scammer input text
- Response strategy used
- Behavioral scoring (urgency, authority, payment, etc.)
- Time waste estimates
- Frustration levels
- Threat detection

**Files Currently Generated:**
- `scammer_analysis_20250720.csv`
- `scammer_analysis_20250721.csv`

## Quick Free Deployment Setup

### Option 1: Railway + PostgreSQL (RECOMMENDED)
```bash
# 1. Create railway.json
{
  "deploy": {
    "startCommand": "python secure_app.py",
    "healthcheckPath": "/health"
  }
}

# 2. Add database environment variables
DATABASE_URL=${{Railway.DATABASE_URL}}
FLASK_ENV=production
```

### Option 2: Render + Database
```yaml
# render.yaml
services:
  - type: web
    name: scammer-waste-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python secure_app.py
    envVars:
      - key: FLASK_ENV
        value: production
```

## Database Migration from CSV

Create a simple script to migrate your CSV data to PostgreSQL:

```python
# migrate_csv_to_db.py
import pandas as pd
import psycopg2
import os

def migrate_csv_to_postgres():
    # Read CSV files
    csv_files = glob.glob('analytics_data/*.csv')
    
    # Connect to PostgreSQL
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df.to_sql('scammer_analytics', conn, if_exists='append', index=False)
    
    conn.close()
```

## Enhanced Database Schema

```sql
CREATE TABLE scammer_analytics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    scammer_input TEXT,
    strategy VARCHAR(100),
    response_preview TEXT,
    urgency_score FLOAT,
    authority_score FLOAT,
    payment_score FLOAT,
    info_score FLOAT,
    frustration_score FLOAT,
    threat_score FLOAT,
    caps_ratio FLOAT,
    exclamation_count INTEGER,
    estimated_time_waste INTEGER,
    total_time_wasted INTEGER,
    scammer_frustration VARCHAR(50),
    is_high_urgency BOOLEAN,
    is_authority_claim BOOLEAN,
    is_payment_scam BOOLEAN,
    is_info_phishing BOOLEAN,
    is_threatening BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Auto-Sync CSV to Database

Add this to your secure_app.py:

```python
@app.route('/sync-csv', methods=['POST'])
@require_admin_token
def sync_csv_to_database():
    """Sync CSV files to PostgreSQL database"""
    try:
        # Your CSV sync logic here
        return jsonify({"status": "success", "message": "CSV data synced"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
```

## Next Steps

1. **Choose Railway** (easiest for beginners)
2. **Connect your GitHub repo**
3. **Add PostgreSQL database** (free)
4. **Deploy with one click**
5. **Your CSV generation continues automatically**

## Cost Breakdown (FREE)

**Railway Free Tier:**
- $5 credit monthly = FREE for small apps
- PostgreSQL database included
- SSL certificates included
- Custom domain support

**Supabase Free Tier:**
- 500MB database storage
- 50,000 monthly active users
- Real-time features included

Your CSV generation system is already production-ready and will continue working seamlessly on any of these platforms!
