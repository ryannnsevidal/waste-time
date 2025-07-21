#!/bin/bash

# Production Deployment Script for Scammer Waste Bot
# Integrates frontend and backend for production deployment

echo "🚀 Production Deployment - Scammer Waste Bot"
echo "============================================="

# Set production environment
export FLASK_ENV=production
export NODE_ENV=production

# Generate secure credentials if not provided
if [ -z "$SECRET_KEY" ]; then
    export SECRET_KEY=$(openssl rand -hex 32)
    echo "🔑 Generated SECRET_KEY"
fi

if [ -z "$SCAMMER_WASTE_API_KEY" ]; then
    export SCAMMER_WASTE_API_KEY=$(openssl rand -hex 16)
    echo "🔑 Generated API_KEY: $SCAMMER_WASTE_API_KEY"
fi

if [ -z "$SCAMMER_WASTE_ADMIN_TOKEN" ]; then
    export SCAMMER_WASTE_ADMIN_TOKEN=$(openssl rand -hex 24)
    echo "🔑 Generated ADMIN_TOKEN"
fi

# Create production environment file
echo "📝 Creating production environment file..."
cat > .env << EOF
# Production Environment Configuration - Generated $(date)
FLASK_ENV=production
SECRET_KEY=$SECRET_KEY
SCAMMER_WASTE_API_KEY=$SCAMMER_WASTE_API_KEY
SCAMMER_WASTE_ADMIN_TOKEN=$SCAMMER_WASTE_ADMIN_TOKEN

# Default production settings
PORT=5000
WORKERS=4
TIMEOUT=30
MAX_REQUESTS=1000

# AI Configuration
MAX_CONVERSATION_LENGTH=50
RESPONSE_DELAY_MIN=2
RESPONSE_DELAY_MAX=8

# Analytics
LOG_RETENTION_DAYS=30
USER_DATA_RETENTION_DAYS=365

# Compliance
GDPR_COMPLIANCE=true
CCPA_COMPLIANCE=true
COPPA_COMPLIANCE=false
EOF

echo "✅ Environment file created"

# Ensure data directories exist
echo "📁 Creating data directories..."
mkdir -p data/analytics
mkdir -p data/logs
mkdir -p data/uploads
mkdir -p data/backups

# Set proper permissions
chmod 755 data/
chmod 755 data/analytics/
chmod 755 data/logs/
chmod 644 data/static/*

echo "✅ Data directories ready"

# Check if frontend assets exist
if [ ! -f "data/static/index.html" ]; then
    echo "❌ Frontend assets not found in data/static/"
    echo "Please ensure your frontend build is in data/static/"
    exit 1
fi

echo "✅ Frontend assets found"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip install --no-cache-dir -r requirements.txt
    echo "✅ Python dependencies installed"
else
    echo "❌ requirements.txt not found"
    exit 1
fi

# Create production startup script
echo "📝 Creating production startup script..."
cat > start_production.sh << 'EOF'
#!/bin/bash

# Production Startup Script
echo "🚀 Starting Scammer Waste Bot - Production Mode"
echo "================================================"

# Load environment variables
if [ -f ".env" ]; then
    source .env
    echo "✅ Environment loaded"
else
    echo "❌ .env file not found"
    exit 1
fi

# Start with Gunicorn for production
echo "🌐 Starting Gunicorn server..."
cd src/
exec gunicorn \
    --bind 0.0.0.0:${PORT:-5000} \
    --workers ${WORKERS:-4} \
    --timeout ${TIMEOUT:-30} \
    --max-requests ${MAX_REQUESTS:-1000} \
    --access-logfile ../data/logs/access.log \
    --error-logfile ../data/logs/error.log \
    --log-level info \
    --preload \
    app:app
EOF

chmod +x start_production.sh

echo "✅ Production startup script created"

# Create Docker production configuration
echo "📝 Creating Docker production configuration..."
cat > docker-compose.prod.yml << 'EOF'
version: '3.8'

services:
  scammer-waste-bot:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=${SECRET_KEY}
      - SCAMMER_WASTE_API_KEY=${SCAMMER_WASTE_API_KEY}
      - SCAMMER_WASTE_ADMIN_TOKEN=${SCAMMER_WASTE_ADMIN_TOKEN}
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - scammer-waste-bot
    restart: unless-stopped
EOF

echo "✅ Docker production config created"

# Create nginx configuration
echo "📝 Creating Nginx configuration..."
mkdir -p ssl
cat > nginx.conf << 'EOF'
events {
    worker_connections 1024;
}

http {
    upstream app {
        server scammer-waste-bot:5000;
    }

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=api:10m rate=30r/m;
    limit_req_zone $binary_remote_addr zone=general:10m rate=100r/m;

    server {
        listen 80;
        server_name _;

        # Redirect HTTP to HTTPS
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name _;

        # SSL configuration (add your certificates)
        # ssl_certificate /etc/nginx/ssl/cert.pem;
        # ssl_certificate_key /etc/nginx/ssl/key.pem;

        # Security headers
        add_header X-Content-Type-Options nosniff;
        add_header X-Frame-Options DENY;
        add_header X-XSS-Protection "1; mode=block";
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";

        # API endpoints
        location /api/ {
            limit_req zone=api burst=10 nodelay;
            proxy_pass http://app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Static files
        location /static/ {
            limit_req zone=general burst=20 nodelay;
            proxy_pass http://app;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }

        # Main application
        location / {
            limit_req zone=general burst=20 nodelay;
            proxy_pass http://app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
EOF

echo "✅ Nginx configuration created"

# Create health check script
echo "📝 Creating health check script..."
cat > health_check.sh << 'EOF'
#!/bin/bash

# Health Check Script
echo "🏥 Performing health check..."

# Check if server is responding
HEALTH_URL="http://localhost:5000/api/health"
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)

if [ "$RESPONSE" = "200" ]; then
    echo "✅ Server is healthy"
    exit 0
else
    echo "❌ Server health check failed (HTTP $RESPONSE)"
    exit 1
fi
EOF

chmod +x health_check.sh

echo "✅ Health check script created"

# Create deployment summary
echo ""
echo "🎉 PRODUCTION DEPLOYMENT READY!"
echo "================================"
echo ""
echo "📋 Deployment Summary:"
echo "  • Environment: Production"
echo "  • API Key: $SCAMMER_WASTE_API_KEY"
echo "  • Frontend: Integrated"
echo "  • Database: File-based analytics"
echo "  • Security: API key + rate limiting"
echo "  • Monitoring: Health checks + logs"
echo ""
echo "🚀 Quick Start Options:"
echo ""
echo "1. 🐳 Docker (Recommended):"
echo "   docker-compose -f docker-compose.prod.yml up -d"
echo ""
echo "2. 🔧 Direct Python:"
echo "   ./start_production.sh"
echo ""
echo "3. ☁️ Cloud Deployment:"
echo "   - Copy .env file to your cloud platform"
echo "   - Use the generated API key for authentication"
echo "   - Set PORT environment variable if needed"
echo ""
echo "🌐 Access Points:"
echo "  • Dashboard: http://localhost:5000"
echo "  • API Docs: http://localhost:5000/api/health"
echo "  • Admin Stats: http://localhost:5000/api/admin/stats"
echo ""
echo "🔑 Important:"
echo "  • Save your API key: $SCAMMER_WASTE_API_KEY"
echo "  • Keep your .env file secure"
echo "  • Monitor logs in data/logs/"
echo ""
echo "✅ Ready for production deployment!"
