#!/bin/bash

# Quick Railway Deployment Script
echo "🚀 Setting up Railway deployment for Scammer Waste Bot..."

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📦 Installing Railway CLI..."
    npm install -g @railway/cli
fi

# Create railway.json configuration
echo "📝 Creating Railway configuration..."
cat > railway.json << EOF
{
  "deploy": {
    "startCommand": "python secure_app.py",
    "healthcheckPath": "/health"
  }
}
EOF

# Create Procfile for additional compatibility
echo "📝 Creating Procfile..."
cat > Procfile << EOF
web: python secure_app.py
EOF

# Update requirements.txt with database dependencies
echo "📦 Adding database dependencies..."
cat >> requirements.txt << EOF
psycopg2-binary==2.9.9
pandas==2.0.3
sqlalchemy==2.0.23
EOF

# Create database initialization script
echo "🗄️ Creating database setup script..."
cat > init_database.py << EOF
from csv_to_database import CSVtoDatabaseMigrator
import os

def setup_database():
    """Initialize database for Railway deployment"""
    if os.environ.get('DATABASE_URL'):
        print("🗄️ Setting up database...")
        migrator = CSVtoDatabaseMigrator()
        migrator.create_analytics_table()
        migrator.migrate_csv_files()
        print("✅ Database setup complete!")
    else:
        print("❌ DATABASE_URL not found")

if __name__ == "__main__":
    setup_database()
EOF

# Add health check endpoint to secure_app.py
echo "🏥 Adding health check endpoint..."
cat >> secure_app.py << EOF

@app.route('/health')
def health_check():
    """Health check endpoint for Railway"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "scammer-waste-bot"
    })
EOF

# Create deployment instructions
echo "📋 Creating deployment instructions..."
cat > RAILWAY_DEPLOY.md << EOF
# Railway Deployment Instructions

## 1. Install Railway CLI
\`\`\`bash
npm install -g @railway/cli
\`\`\`

## 2. Login to Railway
\`\`\`bash
railway login
\`\`\`

## 3. Create New Project
\`\`\`bash
railway new
# Choose: "Deploy from GitHub repo"
\`\`\`

## 4. Add PostgreSQL Database
\`\`\`bash
railway add postgresql
\`\`\`

## 5. Set Environment Variables
In Railway dashboard, add:
- \`FLASK_ENV=production\`
- \`API_KEY=\$(generate with: python -c "import secrets; print(secrets.token_hex(32))")\`
- \`ADMIN_TOKEN=\$(generate with: python -c "import secrets; print(secrets.token_hex(32))")\`
- \`SECRET_KEY=\$(generate with: python -c "import secrets; print(secrets.token_hex(32))")\`

## 6. Deploy
\`\`\`bash
railway up
\`\`\`

## 7. Initialize Database
\`\`\`bash
railway run python init_database.py
\`\`\`

## 8. Get Your URL
\`\`\`bash
railway domain
\`\`\`

Your app will be live at: https://your-app.railway.app
EOF

echo "✅ Railway deployment setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Run: railway login"
echo "2. Run: railway new"
echo "3. Add PostgreSQL database in Railway dashboard"
echo "4. Set environment variables"
echo "5. Run: railway up"
echo ""
echo "📖 Full instructions in RAILWAY_DEPLOY.md"
