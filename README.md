# 🎰 Poker Chip Calculator - TWA Development Guide

A professional poker chip distribution calculator that helps tournament organizers determine optimal chip allocations based on player count, tournament duration, and available chip inventory.

**Version:** 2.5 (Deployed to Production)
**Status:** Live and deployed - Ready to publish products
**Target Platform:** Android (Play Store) + iOS (Web) + Desktop
**Live URL:** https://poker-chip-calculator.onrender.com

---

## 🚀 Quick Start

### Start the Server
```bash
# Option 1: Use batch file (Windows)
START-SERVER.bat

# Option 2: Manual start
cd backend
python app.py
```

Then open http://localhost:5000 in your browser.

### Kill Server Easily
```bash
# Find Python processes running app.py
wmic process where "commandline like '%app.py%'" get processid

# Kill specific process
taskkill //F //PID <process_id>
```

### Test Premium Features (Development Only)
```javascript
// In browser console:
localStorage.setItem('isPremium', 'true');
location.reload();
```

---

## ✅ Recent Changes (v2.4)

### Gumroad Payment Integration (NEW!)
- ✅ Two-tier pricing: Entry ($0.99) + Premium ($2.99)
- ✅ License key generation enabled for both products
- ✅ Backend API license verification with Gumroad
- ✅ Frontend license activation flow
- ✅ Professional product graphics created
- ✅ Payment method configured (bank account)
- ⏳ Products unpublished until deployment

### PWA Features (v2.3)
- ✅ manifest.json configured for app installability
- ✅ Service worker with offline caching
- ✅ Apple PWA meta tags for iOS support
- ✅ Automatic service worker registration
- ✅ Cache-first strategy for static assets
- ✅ Network fallback for API calls

### Chipset Management System
- ✅ Create, edit, delete custom chip sets
- ✅ Save multiple chipsets to localStorage
- ✅ Set default chipset
- ✅ First-time user flow (direct to create)
- ✅ Returning user flow (chipset selection)
- ✅ Dynamic denomination rows (add/remove)
- ✅ Full validation (no duplicates, positive values)

### Flask Server Improvements
- ✅ Added catch-all route for static file serving
- ✅ No-cache headers on all responses (HTML, CSS, JS, images)
- ✅ Fixed browser caching issues
- ✅ Created START-SERVER.bat for easy management

---

## 🔧 Technical Stack

- **Backend:** Flask (Python 3.13+) with Flask-CORS
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **PWA:** Service Worker, Web App Manifest
- **Data:** localStorage (client-side persistence)
- **Graphics:** AI-generated poker assets
- **Hosting:** Render.com (next step)
- **Android:** Bubblewrap TWA (planned)

---

## 📁 Project Structure

```
Poker chip/
├── backend/
│   ├── app.py                      # Flask REST API
│   ├── pokerchipcounter.py         # Calculator logic
│   └── poker chip set counts.txt   # Default chipset
├── frontend/
│   ├── assets/
│   │   ├── chip-*.png              # Poker chip graphics
│   │   ├── felt-background.png     # Green felt texture
│   │   └── header-banner.png       # Header image
│   ├── index.html                  # Main app (5 screens + PWA meta)
│   ├── styles.css                  # Poker-themed CSS
│   ├── app.js                      # App logic + chipset CRUD
│   ├── manifest.json               # PWA configuration
│   └── service-worker.js           # Offline support
├── START-SERVER.bat                # Easy server start
├── README.md                       # This file
└── PROJECT_STATUS.md               # Detailed progress tracking
```

---

## 🎯 Features

### Mode 1: Auto-Calculate (Entry Tier - $0.99)
- Calculate chip distribution from tournament parameters
- Duration-based blind structure
- Auto-adjustment when inventory insufficient
- Professional results display

### Mode 2: Custom Stack (Premium - $2.99)
- Specify exact starting stack amount
- Create unlimited custom chipsets
- Save chipsets to browser
- Edit/delete chipsets
- Set default chipset
- Full denomination control

### PWA Features (All Users)
- **Installable:** Add to home screen on any device
- **Offline Mode:** Works without internet connection
- **Fast Loading:** Cached assets load instantly
- **App-like:** Runs in standalone mode (no browser UI)
- **iOS Support:** Works on iPhone/iPad

---

## 🛠️ Development Roadmap

### ✅ Completed (Phases 2-5)
- ✅ Python calculator (94.9% test pass rate)
- ✅ Flask REST API with no-cache headers
- ✅ Mobile-responsive UI with professional graphics
- ✅ Chipset management system (CRUD)
- ✅ PWA manifest.json
- ✅ Service worker with offline caching
- ✅ PWA meta tags (including Apple)

### 🔄 Next Steps (Phase 6-7)
- [ ] Gumroad payment integration
- [ ] Deploy to Render.com hosting
- [ ] Test live PWA installation

### 📋 Future (Phase 8-11)
- [ ] Create Android TWA with Bubblewrap
- [ ] Submit to Google Play Store
- [ ] Launch and marketing

**Progress:** 50% Complete (5 of 11 phases done)
**Time to Launch:** ~15-22 hours remaining

---

## 💰 Pricing Strategy

**Two-Tier Model:**
- **Entry:** $0.99 - Auto-calculate mode
- **Premium:** +$2.99 ($3.98 total) - Custom stacks + chipsets
- **Target:** 60-70% entry, 30-40% upgrade to premium
- **Year 1 Goal:** $950 revenue from 500 users
- **Break-even:** 7 entry + 3 premium sales (~$16)

---

## 🐛 Troubleshooting

### Graphics Not Loading?
1. Kill all Flask processes
2. Start fresh server: `START-SERVER.bat`
3. Hard refresh browser: Ctrl+Shift+R

### Server Won't Start?
```bash
# Check if port 5000 is in use
netstat -ano | findstr :5000

# Kill process
taskkill //F //PID <process_id>
```

### Service Worker Issues?
```javascript
// In browser console - unregister service worker
navigator.serviceWorker.getRegistrations().then(registrations => {
  registrations.forEach(r => r.unregister());
});
location.reload();
```

### Need to Reset Premium?
```javascript
// In browser console
localStorage.removeItem('isPremium');
location.reload();
```

---

## 📞 Resources

- Flask Docs: https://flask.palletsprojects.com/
- PWA Guide: https://web.dev/progressive-web-apps/
- Service Workers: https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
- Bubblewrap: https://github.com/GoogleChromeLabs/bubblewrap
- Gumroad: https://help.gumroad.com/

---

## 📈 What's Next?

**Immediate priorities:**
1. **Phase 6:** Integrate Gumroad payments (3-4 hours)
2. **Phase 7:** Deploy to Render.com (2-3 hours)
3. **Phase 8:** Create Android TWA (4-6 hours)

**See PROJECT_STATUS.md for detailed progress tracking.**

---

**Last Updated:** 2026-01-13 (v2.3 - PWA Features Complete)

---

## ⚠️ Important: Internet Connection Required

**This app requires an active internet connection to function.**

- The Android app (TWA) loads the live website from Render.com
- All calculations are performed on the server
- License verification requires internet access
- Offline mode is not supported

This is normal for TWA (Trusted Web Activity) apps - they are web apps packaged for the Play Store, not native offline apps.

---
