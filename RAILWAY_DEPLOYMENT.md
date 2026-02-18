# Complete Railway Deployment Guide

This guide will walk you through deploying your AI Research Paper Generator to Railway step-by-step.

## ✅ Why Railway?

- **Free Tier Available**: 500 hours/month free
- **Docker Support**: Full Docker container support
- **Easy Setup**: Simple deployment process
- **Persistent Storage**: Data persists between deployments
- **Auto-Deploy**: Automatic deployments from Git

---

## Prerequisites

Before starting, make sure you have:

- [ ] A **GitHub account** (free)
- [ ] A **Railway account** (free to sign up)
- [ ] Your **Google Gemini API Key** ready
- [ ] Your project code pushed to GitHub (or GitLab/Bitbucket)

---

## Step 1: Prepare Your Code on GitHub

### 1.1 Push Your Code to GitHub

If you haven't already, push your code to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Ready for Railway deployment"

# Create a repository on GitHub (go to github.com and create new repo)
# Then push (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

**Important**: Make sure `.env` is in `.gitignore` (never commit API keys!)

---

## Step 2: Create Railway Account

### 2.1 Sign Up for Railway

1. Go to **https://railway.app**
2. Click **"Start a New Project"** or **"Login"**
3. Choose **"Login with GitHub"** (recommended - easiest way)
4. Authorize Railway to access your GitHub account

### 2.2 Verify Your Account

- Check your email if verification is required
- Complete any onboarding steps

---

## Step 3: Create a New Project on Railway

### 3.1 Create New Project

1. Once logged in, you'll see the Railway dashboard
2. Click **"New Project"** button (top right or center)
3. Select **"Deploy from GitHub repo"**
4. You'll see a list of your GitHub repositories
5. **Select your repository** (ai-scholar-suite or whatever you named it)
6. Click **"Deploy Now"**

Railway will automatically:
- Detect your Dockerfile
- Start building your Docker image
- Deploy your application

**Note**: The first deployment might fail because we haven't set environment variables yet. That's okay!

---

## Step 4: Configure Environment Variables

### 4.1 Access Project Settings

1. In your Railway project dashboard, click on your **service** (the deployed app)
2. Click on the **"Variables"** tab (left sidebar)
3. Or click **"Settings"** → **"Variables"**

### 4.2 Add Environment Variables

Click **"New Variable"** and add each of these:

#### Variable 1: Google API Key
- **Name**: `GOOGLE_API_KEY`
- **Value**: `AIzaSyD20iY_DJQH6GXyy1P9YLYPtOU18K1r-pE` (your actual API key)
- Click **"Add"**

#### Variable 2: LLM Model
- **Name**: `LLM_MODEL`
- **Value**: `gemini-1.5-pro`
- Click **"Add"**

#### Variable 3: ChromaDB Path
- **Name**: `CHROMADB_PATH`
- **Value**: `/app/chroma_data`
- Click **"Add"**

#### Variable 4: Output Directory
- **Name**: `OUTPUT_DIR`
- **Value**: `/app/output`
- Click **"Add"**

#### Variable 5: API Host
- **Name**: `API_HOST`
- **Value**: `0.0.0.0`
- Click **"Add"**

#### Variable 6: API Port (Optional)
- **Name**: `API_PORT`
- **Value**: `8000`
- Click **"Add"**

**Note**: Railway automatically sets `PORT` environment variable, so `API_PORT` is optional. The app will use `PORT` if available.

### 4.3 Verify All Variables

You should see all 6 variables listed. Double-check:
- ✅ `GOOGLE_API_KEY` - Your API key
- ✅ `LLM_MODEL` - gemini-1.5-pro
- ✅ `CHROMADB_PATH` - /app/chroma_data
- ✅ `OUTPUT_DIR` - /app/output
- ✅ `API_HOST` - 0.0.0.0
- ✅ `API_PORT` - 8000

---

## Step 5: Redeploy Your Application

### 5.1 Trigger Redeployment

After adding environment variables:

1. Go to the **"Deployments"** tab
2. Click **"Redeploy"** on the latest deployment
3. Or make a small change to trigger auto-deploy:
   - Go to your GitHub repo
   - Edit README.md (add a space)
   - Commit and push
   - Railway will auto-deploy

### 5.2 Monitor Deployment

1. Click on the deployment in progress
2. Watch the **build logs**:
   - You'll see Docker building your image
   - Installing dependencies
   - Starting the application
3. Wait for **"Deploy Successful"** message

---

## Step 6: Get Your Application URL

### 6.1 Find Your Public URL

1. In your Railway project, click on your **service**
2. Go to **"Settings"** tab
3. Scroll to **"Networking"** section
4. Under **"Public Domain"**, click **"Generate Domain"**
5. Railway will create a URL like: `https://your-app-name.up.railway.app`

### 6.2 Copy Your URL

Copy the generated URL - this is your live application URL!

---

## Step 7: Test Your Deployment

### 7.1 Test the API Documentation

Open your browser and go to:
```
https://your-app-name.up.railway.app/docs
```

You should see the **FastAPI interactive documentation** (Swagger UI).

### 7.2 Test API Endpoints

#### Test 1: Health Check (if available)
```bash
curl https://your-app-name.up.railway.app/
```

#### Test 2: Create a Session
```bash
curl -X POST https://your-app-name.up.railway.app/api/v1/sessions
```

Expected response:
```json
{"session_id": "some-uuid-here"}
```

#### Test 3: Check API Docs
Open in browser:
```
https://your-app-name.up.railway.app/docs
```

---

## Step 8: Configure Custom Domain (Optional)

### 8.1 Add Custom Domain

1. In Railway project → **Settings** → **Networking**
2. Under **"Custom Domain"**, enter your domain
3. Click **"Add"**
4. Follow DNS configuration instructions
5. Railway will provide DNS records to add

### 8.2 Update DNS

- Add the provided CNAME or A record to your domain's DNS
- Wait for DNS propagation (5-60 minutes)
- Railway will automatically configure SSL

---

## Step 9: Monitor Your Application

### 9.1 View Logs

1. In Railway dashboard, click on your **service**
2. Go to **"Deployments"** tab
3. Click on a deployment
4. View **"Logs"** to see:
   - Application output
   - Error messages
   - Request logs

### 9.2 Check Metrics

- **"Metrics"** tab shows:
  - CPU usage
  - Memory usage
  - Network traffic
  - Request count

### 9.3 Set Up Alerts (Optional)

1. Go to **Settings** → **Notifications**
2. Configure email alerts for:
   - Deployment failures
   - Service crashes
   - High resource usage

---

## Troubleshooting

### Issue: Build Fails

**Symptoms**: Deployment shows "Build Failed"

**Solutions**:
1. Check build logs in Railway dashboard
2. Verify Dockerfile syntax
3. Ensure all dependencies are in `pyproject.toml`
4. Check for typos in environment variables

**Common Fixes**:
```bash
# Test Docker build locally first
docker build -t test-build .
```

### Issue: Application Crashes

**Symptoms**: Deployment succeeds but app crashes

**Solutions**:
1. Check application logs in Railway
2. Verify all environment variables are set
3. Check if API key is valid
4. Verify port configuration

**Check Logs**:
- Railway dashboard → Service → Deployments → Latest → Logs

### Issue: 502 Bad Gateway

**Symptoms**: URL returns 502 error

**Solutions**:
1. App might be starting - wait 30 seconds
2. Check if app is listening on correct port
3. Verify `PORT` environment variable is being used
4. Check application logs

### Issue: Environment Variables Not Working

**Symptoms**: App runs but can't access API

**Solutions**:
1. Verify variable names match exactly (case-sensitive)
2. Ensure variables are set in Railway (not just locally)
3. Redeploy after adding variables
4. Check variable values don't have extra spaces

### Issue: Database/Storage Issues

**Symptoms**: ChromaDB errors or file write errors

**Solutions**:
1. Use `/app/chroma_data` for ChromaDB path (not `./chroma_data`)
2. Use `/app/output` for output directory
3. Railway provides persistent storage in `/app` directory
4. Files outside `/app` may be ephemeral

---

## Railway Free Tier Limits

### What's Included (Free Tier)

- ✅ **500 hours/month** of runtime
- ✅ **$5 credit** per month
- ✅ **Unlimited deployments**
- ✅ **Docker support**
- ✅ **Custom domains**
- ✅ **SSL certificates**

### When You Might Need to Upgrade

- If you exceed 500 hours/month
- If you need more resources (CPU/RAM)
- If you need multiple services
- If you need team collaboration

**Cost**: Railway charges based on usage. Free tier gives $5 credit monthly.

---

## Next Steps

### 1. Set Up Auto-Deploy

Railway automatically deploys when you push to GitHub. To configure:
- Go to **Settings** → **Source**
- Select branch (usually `main`)
- Enable **"Auto Deploy"**

### 2. Set Up Monitoring

- Use Railway's built-in metrics
- Set up external monitoring (UptimeRobot, etc.)
- Configure error tracking (Sentry, etc.)

### 3. Optimize Performance

- Monitor resource usage
- Optimize Docker image size
- Use Railway's resource limits if needed

### 4. Backup Strategy

- ChromaDB data is stored in Railway's persistent volume
- Consider backing up important data
- Use external storage (S3) for critical files

---

## Quick Reference Commands

### View Logs (CLI)

If you install Railway CLI:
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link project
railway link

# View logs
railway logs
```

### Local Testing

```bash
# Build Docker image
docker build -t ai-scholar-suite .

# Run with environment variables
docker run -p 8000:8000 \
  -e GOOGLE_API_KEY=your-key \
  -e CHROMADB_PATH=/app/chroma_data \
  -e OUTPUT_DIR=/app/output \
  ai-scholar-suite
```

---

## Support

- **Railway Docs**: https://docs.railway.app
- **Railway Discord**: https://discord.gg/railway
- **Railway Status**: https://status.railway.app

---

## Summary Checklist

- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] New project created from GitHub
- [ ] All environment variables set
- [ ] Application deployed successfully
- [ ] Public URL generated
- [ ] API tested and working
- [ ] Monitoring configured
- [ ] Custom domain added (optional)

**Congratulations! Your application is now live on Railway! 🚀**

