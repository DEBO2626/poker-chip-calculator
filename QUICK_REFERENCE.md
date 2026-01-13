# Quick Reference - Poker Chip Calculator

**Version:** 2.5
**Status:** 85% Complete - DEPLOYED & LIVE
**Last Updated:** 2026-01-13
**Live URL:** https://poker-chip-calculator.onrender.com

---

## 🚀 Start Here (New Chat Session)

1. **Read:** `PROJECT_STATUS.md` - Overall progress (85% complete)
2. **Read:** `PHASE_7_COMPLETE.md` - What was just finished (deployment)
3. **Next:** Ready to publish Gumroad products OR start Phase 8 (TWA build)

---

## 📁 Key Files

### Documentation
- `README.md` - Project overview
- `PROJECT_STATUS.md` - Progress tracking (85% complete)
- `PHASE_6_COMPLETE.md` - Payment integration summary
- `PHASE_7_COMPLETE.md` - Deployment summary ⭐ NEW
- `TESTING_GUMROAD.md` - Testing guide
- `SESSION_SUMMARY_2026-01-13.md` - Previous session notes

### Code
- `backend/app.py` - Flask server with Gumroad API
- `frontend/index.html` - Main app
- `frontend/app.js` - JavaScript logic
- `frontend/manifest.json` - PWA config
- `frontend/service-worker.js` - Offline support

### Credentials (PRIVATE!)
- Stored in Render.com environment variables (secure)
- `gumroad-credentials.txt` - Local backup (gitignored)
- GitHub repo: https://github.com/DEBO2626/poker-chip-calculator

---

## 🔐 Gumroad Credentials

```
Access Token: mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO
Entry Product ID: FCZgbXwUtCUZICnWigdugA==
Premium Product ID: 7IdKPVIR9R6Fre-xhUzXJQ==
```

**✅ Set in Render.com environment variables (DONE)**

---

## 🎯 Products

### Entry Tier - $0.99
- URL: https://debernardis6.gumroad.com/l/bvzrd
- Status: **Ready to publish** (app deployed and tested)
- Unlocks: Auto-Calculate mode

### Premium - $2.99
- Status: **Ready to publish** (app deployed and tested)
- Unlocks: Custom Stack mode + Chipset management
- Requires: Entry Tier purchased first

---

## ✅ Deployment Complete

- **Live URL:** https://poker-chip-calculator.onrender.com
- **GitHub:** https://github.com/DEBO2626/poker-chip-calculator
- **Platform:** Render.com (auto-deploy on git push)
- **Security:** unlock-premium.html deleted ✅

---

## 💻 Local Development

### Start Server
```bash
cd backend
python app.py
```
Then open: http://localhost:5000

### Test on Phone (Local Network)
http://192.168.68.78:5000

### Testing License Flow (Local/Live)
```javascript
// Clear all licenses (start fresh)
localStorage.clear();
location.reload();

// Simulate Entry Tier (for testing only)
localStorage.setItem('licenseKey', 'test-key');
localStorage.setItem('productTier', 'entry');
location.reload();

// Simulate Premium (for testing only)
localStorage.setItem('isPremium', 'true');
localStorage.setItem('licenseKey', 'test-key');
localStorage.setItem('productTier', 'premium');
location.reload();
```

---

## ✅ What's Complete

- [x] Flask backend
- [x] Mobile-responsive frontend
- [x] PWA features (offline, installable)
- [x] Chipset management
- [x] Gumroad integration
- [x] License verification API
- [x] Product graphics
- [x] Payment method configured
- [x] Deployed to Render.com
- [x] GitHub repository setup
- [x] Separate Entry/Premium dialogs
- [x] All paywalls tested

---

## 🔄 What's Next

**Option A: Publish Gumroad Products** (30 minutes)
1. Publish Entry Tier product
2. Publish Premium product
3. Make test purchase
4. Verify license activation on live site
5. Share with beta testers

**Option B: Phase 8 - Build Android TWA** (3-4 hours)
1. Install Bubblewrap CLI
2. Initialize TWA project
3. Build Android APK
4. Test on physical device
5. Prepare for Play Store

**See:** `PHASE_7_COMPLETE.md` for deployment details

---

## 📊 Progress

| Phase | Status | Complete |
|-------|--------|----------|
| 1. Account Setup | Partial | 50% |
| 2. Local Dev | Done | 100% |
| 3. Backend | Done | 100% |
| 4. Frontend | Done | 100% |
| 5. PWA Features | Done | 100% |
| 6. Payment Integration | Done | 100% |
| 7. Deployment | Done ✅ | 100% |
| 8. TWA Build | Not Started | 0% |
| 9. Play Store Assets | Not Started | 0% |
| 10. Play Store Submit | Not Started | 0% |
| 11. Launch & Market | Not Started | 0% |

**Overall:** 85% Complete

---

## 🎓 Learning Resources

- Gumroad Docs: https://gumroad.com/api
- Render Docs: https://render.com/docs
- PWA Guide: https://web.dev/progressive-web-apps/

---

**Ready for Phase 7!** 🚀
