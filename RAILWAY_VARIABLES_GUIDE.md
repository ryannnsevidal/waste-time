# Railway Dashboard Environment Variables Setup

## Step-by-Step Guide to Add Environment Variables in Railway

### 1. **After Creating Your Railway Account and Project:**

1. Go to **https://railway.app**
2. Click on your **project name**
3. You'll see your project dashboard

### 2. **Navigate to Variables Section:**

1. In your project dashboard, click on your **service** (it might be named after your repo)
2. Click the **"Variables"** tab at the top
3. You'll see an interface to add environment variables

### 3. **Add These EXACT Variables:**

Click **"Add Variable"** for each one:

```
Variable Name: FLASK_ENV
Value: production
```

```
Variable Name: API_KEY  
Value: 504e1415ef349991d815cd7b3b91d8dee931664bcfb818d8120dc4aa3327624a
```

```
Variable Name: ADMIN_TOKEN
Value: 1a8cc8eaf1e01ed175204c6de955efc792d8ff1ba40b01953a2d15d48249f130
```

```
Variable Name: SECRET_KEY
Value: 643f8724918f0819b408c380a12cfe4183bf0407092512ea663aeb2b5e07e12b
```

### 4. **Railway Will Auto-Add Database URL:**

When you add PostgreSQL, Railway automatically creates:
```
DATABASE_URL=postgresql://[auto-generated]
```

**Don't manually add DATABASE_URL** - Railway handles this automatically.

### 5. **Visual Guide:**

```
Railway Dashboard → Your Project → Your Service → Variables Tab

┌─────────────────────────────────────┐
│ Environment Variables               │
├─────────────────────────────────────┤
│ + Add Variable                      │
│                                     │
│ FLASK_ENV        = production       │
│ API_KEY          = 504e1415ef...    │
│ ADMIN_TOKEN      = 1a8cc8eaf...     │
│ SECRET_KEY       = 643f8724918...   │
│ DATABASE_URL     = postgresql://... │ (auto-added)
└─────────────────────────────────────┘
```

### 6. **After Adding Variables:**

1. Click **"Deploy"** (if not auto-deployed)
2. Wait for deployment to complete
3. Your app will restart with new environment variables

### 7. **Verify Variables Are Set:**

Your app should show:
- **"Running in PRODUCTION mode with enhanced security"** in logs
- No demo keys printed (they're hidden in production)

## **IMPORTANT Security Notes:**

- **Never commit these keys to git** (already protected by .gitignore)
- **These are your production secrets** - keep them secure
- **DATABASE_URL is auto-generated** by Railway when you add PostgreSQL

## **Ready to Deploy?**

After setting these variables:
```bash
railway up
```

Your app will be live with enterprise-grade security
