# Quick Reference - Poker Chip Calculator

**Version:** 2.4
**Status:** 75% Complete - Ready for Phase 7 Deployment
**Last Updated:** 2026-01-13

---

## 🚀 Start Here (New Chat Session)

1. **Read:** `PROJECT_STATUS.md` - Overall progress
2. **Read:** `PHASE_6_COMPLETE.md` - What was just finished
3. **Next:** `PHASE_7_DEPLOYMENT_GUIDE.md` - What to do next

---

## 📁 Key Files

### Documentation
- `README.md` - Project overview
- `PROJECT_STATUS.md` - Progress tracking (75% complete)
- `PHASE_6_COMPLETE.md` - Payment integration summary
- `PHASE_7_DEPLOYMENT_GUIDE.md` - Deployment steps
- `TESTING_GUMROAD.md` - Testing guide

### Code
- `backend/app.py` - Flask server with Gumroad API
- `frontend/index.html` - Main app
- `frontend/app.js` - JavaScript logic
- `frontend/manifest.json` - PWA config
- `frontend/service-worker.js` - Offline support

### Credentials (PRIVATE!)
- `gumroad-credentials.txt` - API keys (DO NOT commit!)

---

## 🔐 Gumroad Credentials

```
Access Token: mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO
Entry Product ID: FCZgbXwUtCUZICnWigdugA==
Premium Product ID: 7IdKPVIR9R6Fre-xhUzXJQ==
```

**Set these as environment variables on Render.com!**

---

## 🎯 Products

### Entry Tier - $0.99
- URL: https://debernardis6.gumroad.com/l/bvzrd
- Status: Unpublished (waiting for deployment)

### Premium - $2.99
- Status: Unpublished (waiting for deployment)

---

## ⚠️ CRITICAL

**DELETE BEFORE DEPLOYING:**
- `frontend/unlock-premium.html` (security bypass!)

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

### Enable Premium (Testing)
```javascript
localStorage.setItem('isPremium', 'true');
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

---

## 🔄 What's Next

**Phase 7: Deploy to Render.com** (2-3 hours)

1. Delete unlock-premium.html
2. Create GitHub repo
3. Deploy to Render.com
4. Set environment variables
5. Test live site
6. Publish products
7. Test with real purchase

**See:** `PHASE_7_DEPLOYMENT_GUIDE.md`

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
| 7. Deployment | Not Started | 0% |
| 8. TWA Build | Not Started | 0% |
| 9. Play Store Assets | Not Started | 0% |
| 10. Play Store Submit | Not Started | 0% |
| 11. Launch & Market | Not Started | 0% |

**Overall:** 75% Complete

---

## 🎓 Learning Resources

- Gumroad Docs: https://gumroad.com/api
- Render Docs: https://render.com/docs
- PWA Guide: https://web.dev/progressive-web-apps/

---

**Ready for Phase 7!** 🚀
