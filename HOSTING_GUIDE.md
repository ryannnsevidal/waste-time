# 🚀 Hosting Guide - Deploy Your Scammer Waste Bot

## Quick Deploy Options

### 🟢 Option 1: Railway (Recommended - Easiest)

**Step 1**: Create account at [railway.app](https://railway.app)

**Step 2**: Connect your GitHub repo
```bash
# Railway will auto-detect your Flask app
# No additional config needed!
```

**Step 3**: Set environment variables in Railway dashboard:
```
SCAMMER_WASTE_API_KEY=your-secure-api-key-here
SECRET_KEY=your-secret-key-here
PORT=5000
FLASK_ENV=production
```

**Step 4**: Deploy automatically from GitHub main branch
- ✅ Free tier available
- ✅ Auto-deploys on git push
- ✅ Custom domain support
- ✅ Built-in SSL

### 🔵 Option 2: Render (Great Free Tier)

**Step 1**: Create account at [render.com](https://render.com)

**Step 2**: Create new Web Service
- Connect GitHub repo: `ryannnsevidal/waste-time`
- Build Command: `pip install -r requirements.txt`
- Start Command: `cd src && gunicorn app:app`

**Step 3**: Environment Variables:
```
SCAMMER_WASTE_API_KEY=your-secure-api-key
SECRET_KEY=your-secret-key
FLASK_ENV=production
```

**Step 4**: Deploy
- ✅ Free tier with 750 hours/month
- ✅ Auto-deploys from GitHub
- ✅ Custom domains
- ✅ SSL included

### 🟡 Option 3: Heroku (Classic Choice)

**Step 1**: Install Heroku CLI and login
```bash
# Install Heroku CLI first
heroku login
```

**Step 2**: Create Heroku app
```bash
cd /workspaces/waste-time
heroku create your-scammer-bot-name
```

**Step 3**: Set environment variables
```bash
heroku config:set SCAMMER_WASTE_API_KEY=your-secure-api-key
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production
```

**Step 4**: Deploy
```bash
git push heroku main
```

### 🟠 Option 4: DigitalOcean App Platform

**Step 1**: Create account at [digitalocean.com](https://digitalocean.com)

**Step 2**: Create new App
- Source: GitHub `ryannnsevidal/waste-time`
- Type: Web Service
- Build Command: `pip install -r requirements.txt`
- Run Command: `cd src && gunicorn app:app --bind 0.0.0.0:$PORT`

**Step 3**: Set environment variables in DO dashboard

### 🔴 Option 5: AWS/Google Cloud (Advanced)

For enterprise deployment, use the included production scripts:

```bash
# Run on your cloud instance
./scripts/deploy_production.sh
```

## 🔧 Pre-Deployment Setup

### 1. Create requirements.txt
```bash
cd /workspaces/waste-time
cat > requirements.txt << EOF
Flask==2.3.3
Flask-CORS==4.0.0
Flask-Limiter==3.5.0
gunicorn==21.2.0
requests==2.31.0
EOF
```

### 2. Create Procfile (for Heroku/Railway)
```bash
cat > Procfile << EOF
web: cd src && gunicorn app:app --bind 0.0.0.0:\$PORT
EOF
```

### 3. Update production environment
```bash
# Set secure production keys
export SCAMMER_WASTE_API_KEY="$(openssl rand -hex 32)"
export SECRET_KEY="$(openssl rand -hex 32)"
echo "Generated secure keys - save these!"
echo "API Key: $SCAMMER_WASTE_API_KEY"
echo "Secret Key: $SECRET_KEY"
```

## 🔐 Security Checklist

### Before Going Live:
- [ ] Change default API key to secure random value
- [ ] Set strong SECRET_KEY
- [ ] Enable HTTPS/SSL (automatic on most platforms)
- [ ] Set FLASK_ENV=production
- [ ] Configure rate limiting appropriately
- [ ] Set up monitoring/logging
- [ ] Test all endpoints with production config

### Recommended Environment Variables:
```
SCAMMER_WASTE_API_KEY=your-secure-32-char-random-key
SECRET_KEY=your-secure-flask-secret-key
FLASK_ENV=production
PORT=5000
DATABASE_URL=sqlite:///data/scammer_waste.db
RATE_LIMIT_STORAGE_URL=memory://
```

## 📊 Post-Deployment

### 1. Test Your Live Site
```bash
# Test health endpoint
curl https://your-site.com/api/health

# Test frontend
curl https://your-site.com/

# Test API with your key
curl -H "X-API-Key: your-api-key" https://your-site.com/api/stats
```

### 2. Monitor Performance
- Check response times
- Monitor database size
- Watch rate limit usage
- Track conversation metrics

### 3. Custom Domain (Optional)
Most platforms support custom domains:
- Railway: yourdomain.com → Railway app
- Render: Custom domain in dashboard
- Heroku: `heroku domains:add yourdomain.com`

## 🎯 Recommended Deployment Flow

**For beginners**: Railway or Render (easiest, free tier)
**For advanced**: DigitalOcean or AWS with the included scripts
**For enterprise**: Use `./scripts/deploy_production.sh` on your server

## 🚨 Important Notes

1. **Database**: SQLite works for moderate traffic. For high traffic, consider PostgreSQL
2. **File Storage**: Static files are served efficiently by Flask
3. **Scaling**: All platforms support easy scaling when traffic grows
4. **Monitoring**: Set up alerts for downtime and performance issues
5. **Backups**: Regular database backups recommended for production

Your scammer waste bot is now ready to waste scammers' time at scale! 🎉
