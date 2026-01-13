# 🎯 PWA/TWA Development Checklist

Quick reference checklist - print this out and check off as you go!

---

## Week 1 - Setup & Backend

### Day 1: Accounts ⏱️ 1-2 hours
- [ ] Create Google Play Developer account ($25)
- [ ] Create Gumroad account (free)
- [ ] (Optional) Buy domain name ($12)

### Day 2: Environment ⏱️ 2-3 hours
- [ ] Check Python version (need 3.7+)
- [ ] Install Flask: `pip install flask flask-cors`
- [ ] Download & install Node.js from nodejs.org
- [ ] Create project folder structure
- [ ] Copy pokerchipcounter.py to backend/ folder

### Days 3-4: Flask Backend ⏱️ 4-6 hours
- [ ] Create backend/app.py
- [ ] Add API endpoint: /api/calculate
- [ ] Add API endpoint: /api/calculate-custom
- [ ] Test in browser: http://localhost:5000
- [ ] Verify calculations work correctly

---

## Week 2 - Frontend & PWA

### Days 5-7: HTML/CSS ⏱️ 8-10 hours
- [ ] Create frontend/index.html
- [ ] Create frontend/styles.css (poker theme)
- [ ] Add mode selection screen
- [ ] Add Mode 1 input form
- [ ] Add Mode 2 input form (locked)
- [ ] Add results display
- [ ] Test on phone browser

### Days 8-10: JavaScript ⏱️ 6-8 hours
- [ ] Create frontend/app.js
- [ ] Implement form validation
- [ ] Connect to Flask API
- [ ] Display results dynamically
- [ ] Add error handling
- [ ] Test all calculations

### Days 11-12: PWA Features ⏱️ 4-5 hours
- [ ] Create manifest.json
- [ ] Create service-worker.js
- [ ] Add PWA meta tags
- [ ] Test "Add to Home Screen" on phone
- [ ] Verify app opens without browser bar

### Days 13-14: Gumroad ⏱️ 3-4 hours
- [ ] Create Gumroad product ($4.99)
- [ ] Enable license keys
- [ ] Add "Unlock Premium" button
- [ ] Implement license verification
- [ ] Test payment flow (test mode)

---

## Week 3 - Deploy & Package

### Day 15: Deploy ⏱️ 2-3 hours
- [ ] Sign up for Render.com
- [ ] Deploy Flask backend
- [ ] Deploy frontend (static site)
- [ ] Test live site on phone
- [ ] Verify HTTPS works

### Days 16-18: TWA ⏱️ 4-6 hours
- [ ] Install Bubblewrap: `npm install -g @bubblewrap/cli`
- [ ] Run: `bubblewrap init --manifest https://yoursite.com/manifest.json`
- [ ] Answer all prompts
- [ ] Run: `bubblewrap build`
- [ ] Install APK on Android phone
- [ ] Test full app functionality

### Days 19-20: Play Store Assets ⏱️ 4-6 hours
- [ ] Create app icon (512×512)
- [ ] Take 2+ screenshots
- [ ] Create feature graphic (1024×500)
- [ ] Write app title
- [ ] Write short description (80 chars)
- [ ] Write full description
- [ ] Choose keywords for SEO

### Day 21: Submit ⏱️ 2-3 hours
- [ ] Go to play.google.com/console
- [ ] Create new app
- [ ] Upload APK
- [ ] Add all assets
- [ ] Complete store listing
- [ ] Submit for review
- [ ] Wait for approval (1-7 days)

---

## Week 4+ - Launch

### On Approval
- [ ] App goes live
- [ ] Post on r/poker
- [ ] Post on poker forums
- [ ] Share on social media
- [ ] Monitor reviews daily

### Ongoing
- [ ] Respond to reviews
- [ ] Track installs
- [ ] Track Gumroad sales
- [ ] Fix bugs
- [ ] Add features

---

## 📊 Progress Tracking

**Started:** __________
**Phase 1 Complete:** __________
**Phase 2 Complete:** __________
**Phase 3 Complete:** __________
**Submitted to Play Store:** __________
**App Approved:** __________
**First Sale:** __________

---

## 🚨 Common Issues & Solutions

**Flask won't start:**
```bash
pip install flask flask-cors
python backend/app.py
```

**Can't access from phone:**
- Check firewall settings
- Use computer's local IP (192.168.x.x)
- Or deploy to Render first

**Bubblewrap errors:**
- Make sure Node.js installed
- Check manifest.json is valid
- Ensure HTTPS on your live site

**APK won't install:**
- Enable "Unknown sources" on Android
- Or use: `adb install app.apk`

---

## 💡 Quick Commands Reference

```bash
# Start Flask backend
cd backend
python app.py

# Install Bubblewrap
npm install -g @bubblewrap/cli

# Create TWA
bubblewrap init --manifest https://yoursite.com/manifest.json

# Build APK
bubblewrap build

# Install on phone
adb install app-release-signed.apk
```

---

**Print this page and check off tasks as you complete them!**
