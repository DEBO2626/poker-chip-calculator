# Phase 7: Deployment Guide

**Status:** Ready to Start
**Prerequisites:** ✅ All complete
**Estimated Time:** 2-3 hours

---

## Overview

Deploy the Poker Chip Calculator to Render.com (free hosting) to make it publicly accessible.

---

## Pre-Deployment Checklist

### ✅ Ready to Deploy
- [x] Backend API complete with Gumroad integration
- [x] Frontend complete with PWA features
- [x] License verification working
- [x] Gumroad products created (unpublished)
- [x] Payment method configured
- [x] Product graphics uploaded

### ⚠️ Before Deploying
- [ ] Delete `frontend/unlock-premium.html` (security risk!)
- [ ] Test locally one more time
- [ ] Commit all changes to git

---

## Step-by-Step Deployment

### Step 1: Prepare Code for Deployment

**1.1 Delete Test File**
```bash
del frontend\unlock-premium.html
```

**1.2 Create `.gitignore`**
Create file: `.gitignore`
```
__pycache__/
*.pyc
*.pyo
.env
gumroad-credentials.txt
graphics/
*.output
.DS_Store
```

**1.3 Create `runtime.txt`** (for Python version)
Create file in project root: `runtime.txt`
```
python-3.13.0
```

**1.4 Verify `requirements.txt`**
Should contain:
```
Flask==3.0.0
flask-cors==4.0.0
requests==2.31.0
```

---

### Step 2: Create GitHub Repository

**2.1 Initialize Git** (if not already)
```bash
cd "C:\Users\john_\Desktop\Poker chip"
git init
git add .
git commit -m "Initial commit - Ready for deployment"
```

**2.2 Create GitHub Repo**
1. Go to https://github.com/new
2. Repository name: `poker-chip-calculator`
3. Description: "Professional poker chip distribution calculator"
4. **Private** repository (recommended for now)
5. Click "Create repository"

**2.3 Push to GitHub**
```bash
git remote add origin https://github.com/YOUR_USERNAME/poker-chip-calculator.git
git branch -M main
git push -u origin main
```

---

### Step 3: Deploy to Render.com

**3.1 Create Render Account**
1. Go to https://render.com
2. Sign up with GitHub account (easiest)
3. Authorize Render to access repositories

**3.2 Create New Web Service**
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select `poker-chip-calculator`

**3.3 Configure Web Service**

**Basic Settings:**
- **Name:** `poker-chip-calculator`
- **Region:** Oregon (US West) or closest to you
- **Branch:** `main`
- **Root Directory:** `.` (leave empty)
- **Runtime:** Python 3
- **Build Command:** `pip install -r backend/requirements.txt`
- **Start Command:** `cd backend && python app.py`

**Advanced Settings:**
- **Environment:** Python 3

**3.4 Set Environment Variables**
Click "Environment" tab, add these:

```
GUMROAD_ACCESS_TOKEN = mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO
GUMROAD_ENTRY_PRODUCT_ID = FCZgbXwUtCUZICnWigdugA==
GUMROAD_PREMIUM_PRODUCT_ID = 7IdKPVIR9R6Fre-xhUzXJQ==
```

**3.5 Deploy**
- Click "Create Web Service"
- Wait 5-10 minutes for first deployment
- Watch logs for any errors

---

### Step 4: Test Deployed Site

**4.1 Get Your URL**
- Render will give you URL like: `https://poker-chip-calculator.onrender.com`

**4.2 Test Basic Functionality**
- [ ] Site loads
- [ ] Auto-Calculate mode works
- [ ] Custom Stack tab shows premium lock
- [ ] Click "Unlock Premium" - dialog opens

**4.3 Test Invalid License Key**
- [ ] Enter fake key: `TEST-1234-5678`
- [ ] Should show error from Gumroad

---

### Step 5: Make Test Purchase

**5.1 Publish Entry Tier Product**
1. Go to Gumroad → Products
2. Click "Poker Chip Calculator - Entry Tier"
3. Click "Publish"

**5.2 Make Purchase**
1. Go to your product URL: https://debernardis6.gumroad.com/l/bvzrd
2. Purchase for $0.99
3. Check email for license key

**5.3 Test License Activation**
1. Go to your deployed app
2. Click "Custom Stack"
3. Click "Unlock Premium"
4. Enter your license key
5. Should activate successfully!

---

### Step 6: Publish Premium Product

**6.1 Publish Premium Tier**
1. Go to Gumroad → Products
2. Click "Poker Chip Calculator - Premium Upgrade"
3. Click "Publish"

**6.2 Update Product Descriptions**
Add link to your app in both product descriptions:
```
Access the calculator at: https://poker-chip-calculator.onrender.com
```

---

### Step 7: Final Verification

**Deployment Checklist:**
- [ ] App loads on desktop browser
- [ ] App loads on mobile browser
- [ ] Auto-Calculate works
- [ ] Premium lock appears
- [ ] License activation works
- [ ] Invalid keys rejected
- [ ] Valid keys activate premium
- [ ] PWA installable (HTTPS required)
- [ ] Works offline after first load
- [ ] Both Gumroad products published
- [ ] Product links point to deployed app

---

## Troubleshooting

### Build Fails
**Error:** `requirements.txt not found`
- **Fix:** Build command should be: `pip install -r backend/requirements.txt`

### App Won't Start
**Error:** `Address already in use`
- **Fix:** Update `app.py` to use Render's PORT:
```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)
```

### Environment Variables Not Working
- **Check:** Environment tab in Render dashboard
- **Verify:** Variable names match code exactly
- **Restart:** Redeploy after adding variables

### Gumroad API Errors
- **Check:** Environment variables set correctly
- **Verify:** Access token is valid
- **Test:** Use curl to test API manually

---

## Post-Deployment Tasks

### Update Documentation
- [ ] Update README with live URL
- [ ] Update Gumroad product descriptions
- [ ] Add app URL to Gumroad "Share" tab

### Monitor
- [ ] Check Render logs for errors
- [ ] Test app regularly
- [ ] Monitor Gumroad sales dashboard

### Optimize (Optional)
- [ ] Set up custom domain
- [ ] Add Google Analytics
- [ ] Implement error tracking
- [ ] Set up uptime monitoring

---

## Custom Domain (Optional)

### If You Want: pokerchipcalc.com

**1. Buy Domain**
- Namecheap, Google Domains, or GoDaddy
- Cost: ~$12/year

**2. Configure DNS**
In your domain registrar:
```
Type: CNAME
Name: www
Value: poker-chip-calculator.onrender.com
```

**3. Add to Render**
1. Render dashboard → Custom Domain
2. Add domain: `www.pokerchipcalc.com`
3. Wait for SSL certificate (automatic)

---

## Costs

**Render.com Free Tier:**
- ✅ Free for first 750 hours/month
- ✅ Automatic HTTPS
- ✅ Enough for testing and low traffic
- ⚠️ Spins down after 15 min inactivity (first load slower)

**Paid Tier ($7/month):**
- Always on (no spin-down)
- Faster performance
- More resources

**Recommendation:** Start with free tier, upgrade if needed

---

## Next Steps After Deployment

### Phase 8: Create TWA for Play Store
- Install Bubblewrap
- Generate Android APK
- Test on phone

### Phase 9: Play Store Submission
- Screenshots
- Store listing
- Submit for review

---

**Ready to Deploy?** Start with Step 1!

**Need Help?** Check Render docs: https://render.com/docs
