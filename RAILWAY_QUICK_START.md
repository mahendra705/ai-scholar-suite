# Railway Quick Start Guide - Step by Step

Follow these steps exactly to deploy your app to Railway.

---

## 📋 Prerequisites Checklist

Before you start, make sure you have:
- [ ] GitHub account (free)
- [ ] Google Gemini API key ready
- [ ] Your code ready (or we'll help you push it)

---

## Step 1: Push Code to GitHub (5 minutes)

### If you don't have GitHub repo yet:

1. **Go to github.com** and sign in
2. Click **"+"** → **"New repository"**
3. Name it: `ai-scholar-suite` (or any name)
4. Make it **Public** or **Private** (your choice)
5. Click **"Create repository"**

### Push your code:

Open terminal in your project folder and run:

```bash
# If you haven't initialized git yet
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Railway deployment"

# Add GitHub remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**✅ Done!** Your code is now on GitHub.

---

## Step 2: Sign Up for Railway (2 minutes)

1. **Go to https://railway.app**
2. Click **"Start a New Project"** or **"Login"**
3. Click **"Login with GitHub"**
4. Click **"Authorize Railway"** (allow access to GitHub)
5. **✅ Done!** You're logged into Railway.

---

## Step 3: Create New Project (3 minutes)

1. In Railway dashboard, click **"New Project"** (big button)
2. Click **"Deploy from GitHub repo"**
3. You'll see your GitHub repositories
4. **Click on your repository** (ai-scholar-suite)
5. Railway will start deploying automatically

**⏳ Wait 2-3 minutes** for Railway to build your Docker image.

**Note**: It might fail the first time (no environment variables yet). That's OK!

---

## Step 4: Add Environment Variables (5 minutes)

### 4.1 Open Variables Settings

1. In your Railway project, click on the **service** (your app name)
2. Click **"Variables"** tab (left sidebar)
3. You'll see an empty list

### 4.2 Add Each Variable

Click **"New Variable"** for each one:

#### Variable 1:
- **Name**: `GOOGLE_API_KEY`
- **Value**: Paste your Google Gemini API key
- Click **"Add"**

#### Variable 2:
- **Name**: `LLM_MODEL`
- **Value**: `gemini-1.5-pro`
- Click **"Add"**

#### Variable 3:
- **Name**: `CHROMADB_PATH`
- **Value**: `/app/chroma_data`
- Click **"Add"**

#### Variable 4:
- **Name**: `OUTPUT_DIR`
- **Value**: `/app/output`
- Click **"Add"**

#### Variable 5:
- **Name**: `API_HOST`
- **Value**: `0.0.0.0`
- Click **"Add"**

#### Variable 6:
- **Name**: `API_PORT`
- **Value**: `8000`
- Click **"Add"**

**✅ Done!** All 6 variables added.

---

## Step 5: Redeploy (2 minutes)

1. Go to **"Deployments"** tab
2. Click **"Redeploy"** on the latest deployment
3. Or click the **three dots (⋯)** → **"Redeploy"**
4. **⏳ Wait 2-3 minutes** for deployment to complete

**✅ Done!** Your app is deploying with environment variables.

---

## Step 6: Get Your Public URL (1 minute)

1. Click on your **service**
2. Go to **"Settings"** tab
3. Scroll to **"Networking"** section
4. Under **"Public Domain"**, click **"Generate Domain"**
5. Railway creates a URL like: `https://your-app.up.railway.app`
6. **Copy this URL** - this is your live app!

**✅ Done!** You have your public URL.

---

## Step 7: Test Your App (2 minutes)

### Test 1: Open API Docs

Open in your browser:
```
https://your-app.up.railway.app/docs
```

You should see the **FastAPI documentation page**.

### Test 2: Create a Session

In terminal, run:
```bash
curl -X POST https://your-app.up.railway.app/api/v1/sessions
```

You should get a response like:
```json
{"session_id": "abc-123-def"}
```

**✅ Done!** Your app is working!

---

## 🎉 Congratulations!

Your AI Research Paper Generator is now live on Railway!

**Your app URL**: `https://your-app.up.railway.app`

---

## 🔧 Troubleshooting

### App not working?

1. **Check logs**: Railway dashboard → Service → Deployments → Latest → Logs
2. **Verify variables**: Make sure all 6 environment variables are set
3. **Check API key**: Make sure `GOOGLE_API_KEY` is correct
4. **Redeploy**: Try redeploying after fixing issues

### Need help?

- Check full guide: `RAILWAY_DEPLOYMENT.md`
- Railway docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway

---

## 📝 Quick Reference

**Your Railway Dashboard**: https://railway.app/dashboard

**Common Actions**:
- View logs: Service → Deployments → Latest → Logs
- Add variables: Service → Variables → New Variable
- Redeploy: Service → Deployments → Redeploy
- Get URL: Service → Settings → Networking → Generate Domain

---

## ✅ Final Checklist

- [ ] Code on GitHub
- [ ] Railway account created
- [ ] Project deployed
- [ ] Environment variables added
- [ ] App redeployed
- [ ] Public URL generated
- [ ] App tested and working

**You're all set! 🚀**

