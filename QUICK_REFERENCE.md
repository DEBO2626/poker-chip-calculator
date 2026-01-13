# Quick Reference - Poker Chip Calculator

**Version:** 2.6
**Status:** 95% Complete - ANDROID APP READY FOR PLAY STORE
**Last Updated:** 2026-01-13
**Live URL:** https://poker-chip-calculator.onrender.com

---

## 🚀 Start Here (New Chat Session)

1. **Read:** `PROJECT_STATUS.md` - Overall progress (95% complete)
2. **Read:** `PHASE_8_9_COMPLETE.md` - Android TWA built & Play Store ready
3. **Next:** Submit to Google Play Store (Phase 10)

---

## 📁 Key Files

### Documentation
- `README.md` - Project overview
- `PROJECT_STATUS.md` - Progress tracking (95% complete)
- `PHASE_6_COMPLETE.md` - Payment integration summary
- `PHASE_7_COMPLETE.md` - Deployment summary
- `PHASE_8_9_COMPLETE.md` - Android TWA & Play Store assets ⭐ NEW
- `TESTING_GUMROAD.md` - Testing guide
- `play-store-assets/PLAY_STORE_CHECKLIST.md` - Submission guide ⭐ NEW

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
- [x] Android TWA built (APK + AAB)
- [x] Tested on Galaxy S25
- [x] Play Store screenshots (4 images)
- [x] Privacy policy deployed

---

## 🔄 What's Next

**Phase 10: Submit to Google Play Store** (1-2 hours)
1. Go to: https://play.google.com/console
2. Create app listing
3. Upload `app-release-bundle.aab`
4. Upload screenshots from `play-store-assets/screenshots/`
5. Upload app icon: `frontend/assets/app-icon.png`
6. Copy descriptions from `play-store-assets/app-descriptions.txt`
7. Enter privacy policy URL: https://poker-chip-calculator.onrender.com/privacy-policy.html
8. Submit for review

**Review time:** 1-7 days

**See:** `play-store-assets/PLAY_STORE_CHECKLIST.md` for detailed steps

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
| 8. TWA Build | Done ✅ | 100% |
| 9. Play Store Assets | Done ✅ | 100% |
| 10. Play Store Submit | Ready | 0% |
| 11. Launch & Market | Not Started | 0% |

**Overall:** 95% Complete

---

## 🎓 Learning Resources

- Gumroad Docs: https://gumroad.com/api
- Render Docs: https://render.com/docs
- PWA Guide: https://web.dev/progressive-web-apps/

---

**Ready for Phase 7!** 🚀
