# Railway Deployment - Complete Step-by-Step Instructions

Follow these instructions **exactly in order**. Each step is numbered and explained clearly.

---

## 🎯 Goal
Deploy your AI Research Paper Generator to Railway so it's accessible on the internet.

---

## 📝 Step 1: Prepare Your Code (5 minutes)

### What you need:
- Your project code
- A GitHub account

### Actions:

1. **Open Terminal** in your project folder:
   ```bash
   cd /Users/mahendraagrawal/Desktop/Mahendra/Research/ai-scholar-suite
   ```

2. **Check if git is initialized:**
   ```bash
   git status
   ```
   
   If you see "not a git repository", run:
   ```bash
   git init
   ```

3. **Add all files:**
   ```bash
   git add .
   ```

4. **Commit:**
   ```bash
   git commit -m "Ready for Railway deployment"
   ```

5. **Create GitHub repository:**
   - Go to https://github.com
   - Click **"+"** (top right) → **"New repository"**
   - Name: `ai-scholar-suite`
   - Choose **Public** or **Private**
   - **DO NOT** check "Initialize with README"
   - Click **"Create repository"**

6. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/ai-scholar-suite.git
   git branch -M main
   git push -u origin main
   ```
   (Replace `YOUR_USERNAME` with your GitHub username)

**✅ Step 1 Complete!** Your code is now on GitHub.

---

## 📝 Step 2: Create Railway Account (2 minutes)

### Actions:

1. **Go to Railway:**
   - Open browser: https://railway.app

2. **Sign up:**
   - Click **"Start a New Project"** or **"Login"**
   - Click **"Login with GitHub"**
   - Click **"Authorize Railway"** (allow access)

3. **Verify:**
   - You should see the Railway dashboard
   - Your GitHub profile should be connected

**✅ Step 2 Complete!** You're logged into Railway.

---

## 📝 Step 3: Create New Project (3 minutes)

### Actions:

1. **In Railway dashboard:**
   - Click the big **"New Project"** button (top right or center)

2. **Select deployment method:**
   - Click **"Deploy from GitHub repo"**

3. **Select repository:**
   - You'll see a list of your GitHub repositories
   - **Click on "ai-scholar-suite"** (or whatever you named it)

4. **Deploy:**
   - Railway will automatically start deploying
   - You'll see "Building..." status

5. **Wait:**
   - ⏳ Wait 2-3 minutes for Railway to build your Docker image
   - You can watch the build logs

**Note:** The first deployment might show an error because we haven't set environment variables yet. **This is normal!**

**✅ Step 3 Complete!** Your project is created on Railway.

---

## 📝 Step 4: Add Environment Variables (10 minutes)

### What are environment variables?
These are secret settings your app needs to run (like your API key).

### Actions:

1. **Open your project:**
   - In Railway dashboard, click on your project
   - Click on the **service** (it will have a name like "ai-scholar-suite")

2. **Go to Variables:**
   - Click **"Variables"** tab in the left sidebar
   - You'll see an empty list

3. **Add Variable 1 - Google API Key:**
   - Click **"New Variable"** button
   - **Name**: Type exactly: `GOOGLE_API_KEY`
   - **Value**: Paste your Google Gemini API key: `AIzaSyD20iY_DJQH6GXyy1P9YLYPtOU18K1r-pE`
   - Click **"Add"**
   - ✅ You should see it in the list

4. **Add Variable 2 - LLM Model:**
   - Click **"New Variable"** again
   - **Name**: `LLM_MODEL`
   - **Value**: `gemini-1.5-pro`
   - Click **"Add"**

5. **Add Variable 3 - ChromaDB Path:**
   - Click **"New Variable"**
   - **Name**: `CHROMADB_PATH`
   - **Value**: `/app/chroma_data`
   - Click **"Add"**

6. **Add Variable 4 - Output Directory:**
   - Click **"New Variable"**
   - **Name**: `OUTPUT_DIR`
   - **Value**: `/app/output`
   - Click **"Add"**

7. **Add Variable 5 - API Host:**
   - Click **"New Variable"**
   - **Name**: `API_HOST`
   - **Value**: `0.0.0.0`
   - Click **"Add"**

8. **Add Variable 6 - API Port:**
   - Click **"New Variable"**
   - **Name**: `API_PORT`
   - **Value**: `8000`
   - Click **"Add"**

9. **Verify all 6 variables:**
   - You should see:
     - ✅ GOOGLE_API_KEY
     - ✅ LLM_MODEL
     - ✅ CHROMADB_PATH
     - ✅ OUTPUT_DIR
     - ✅ API_HOST
     - ✅ API_PORT

**✅ Step 4 Complete!** All environment variables are set.

---

## 📝 Step 5: Redeploy Application (3 minutes)

### Why redeploy?
The app needs to restart with the new environment variables.

### Actions:

1. **Go to Deployments:**
   - Click **"Deployments"** tab (left sidebar)

2. **Redeploy:**
   - Find the latest deployment
   - Click the **three dots (⋯)** next to it
   - Click **"Redeploy"**
   - OR click **"Redeploy"** button if visible

3. **Wait for deployment:**
   - ⏳ Wait 2-3 minutes
   - Watch the build logs
   - Status will change: Building → Deploying → Active

4. **Check status:**
   - When you see **"Active"** or **"Deploy Successful"**, you're done!

**✅ Step 5 Complete!** Your app is deployed with all settings.

---

## 📝 Step 6: Get Your Public URL (2 minutes)

### Actions:

1. **Open Settings:**
   - Click on your **service**
   - Click **"Settings"** tab (left sidebar)

2. **Generate Domain:**
   - Scroll down to **"Networking"** section
   - Under **"Public Domain"**, click **"Generate Domain"** button
   - Railway will create a URL like: `https://ai-scholar-suite-production-xxxx.up.railway.app`

3. **Copy the URL:**
   - Click the copy icon next to the URL
   - Or manually copy it
   - **This is your live application URL!**

**✅ Step 6 Complete!** You have your public URL.

---

## 📝 Step 7: Test Your Application (5 minutes)

### Actions:

1. **Test API Documentation:**
   - Open your browser
   - Go to: `https://your-url.up.railway.app/docs`
   - You should see the FastAPI interactive documentation
   - ✅ If you see this, your app is working!

2. **Test Create Session (Browser):**
   - In the docs page, find **"POST /api/v1/sessions"**
   - Click **"Try it out"**
   - Click **"Execute"**
   - You should see a response with a `session_id`
   - ✅ If you see this, your API is working!

3. **Test Create Session (Terminal):**
   - Open terminal
   - Run:
     ```bash
     curl -X POST https://your-url.up.railway.app/api/v1/sessions
     ```
   - You should get JSON response: `{"session_id": "..."}`
   - ✅ If you see this, everything is working!

**✅ Step 7 Complete!** Your app is live and working!

---

## 🎉 Congratulations!

Your AI Research Paper Generator is now deployed and accessible on the internet!

**Your app URL**: `https://your-url.up.railway.app`

---

## 🔧 Troubleshooting

### Problem: Build Failed
**Solution:**
1. Check build logs: Service → Deployments → Latest → Logs
2. Make sure Dockerfile exists
3. Verify all files are pushed to GitHub

### Problem: App Crashes
**Solution:**
1. Check application logs: Service → Deployments → Latest → Logs
2. Verify all 6 environment variables are set correctly
3. Check if API key is valid

### Problem: 502 Bad Gateway
**Solution:**
1. Wait 30 seconds (app might be starting)
2. Check logs for errors
3. Verify PORT environment variable is being used

### Problem: Can't see API docs
**Solution:**
1. Make sure URL is correct: `https://your-url.up.railway.app/docs`
2. Check if deployment is "Active"
3. Try the root URL: `https://your-url.up.railway.app/`

---

## 📚 Additional Resources

- **Full Guide**: See `RAILWAY_DEPLOYMENT.md` for detailed information
- **Quick Reference**: See `RAILWAY_QUICK_START.md` for a condensed version
- **Railway Docs**: https://docs.railway.app
- **Railway Support**: https://discord.gg/railway

---

## ✅ Final Checklist

Before you finish, verify:

- [ ] Code is on GitHub
- [ ] Railway account created
- [ ] Project deployed on Railway
- [ ] All 6 environment variables added
- [ ] App redeployed successfully
- [ ] Public URL generated
- [ ] API docs accessible at `/docs`
- [ ] Can create sessions via API

**If all checked, you're done! 🚀**

---

## 🆘 Need Help?

If you're stuck:
1. Check the logs in Railway dashboard
2. Read the full deployment guide: `RAILWAY_DEPLOYMENT.md`
3. Visit Railway Discord: https://discord.gg/railway
4. Check Railway status: https://status.railway.app

