# Quick Reference - Poker Chip Calculator

**Version:** 1.1 (versionCode 2)
**Status:** 99% Complete - TESTING PERIOD ACTIVE
**Last Updated:** 2026-01-14
**Live URL:** https://poker-chip-calculator.onrender.com

---

## 🚀 Start Here (New Chat Session)

1. **Read:** `START_HERE_NEW_SESSION.md` - Current status & next steps
2. **Read:** `PROJECT_STATUS.md` - Overall progress (99% complete)
3. **Read:** `SESSION_SUMMARY_2026-01-14_NATIVE-COMPONENTS.md` - Latest changes

---

## 📁 Key Files

### Documentation
- `START_HERE_NEW_SESSION.md` - Quick start guide
- `PROJECT_STATUS.md` - Progress tracking (99% complete)
- `SESSION_SUMMARY_2026-01-14_NATIVE-COMPONENTS.md` - Latest session ⭐ NEW
- `SESSION_SUMMARY_2026-01-14_FIVERR-TESTERS.md` - Tester recruitment
- `play-store-assets/PLAY_STORE_CHECKLIST.md` - Submission guide

### Code
- `backend/app.py` - Flask server with Gumroad API + test keys
- `frontend/index.html` - Main app
- `frontend/app.js` - JavaScript logic
- `frontend/manifest.json` - PWA config
- `frontend/service-worker.js` - Offline support

### Android Native (NEW in v1.1)
- `app/src/main/java/.../SplashActivity.java` - Splash screen
- `app/src/main/java/.../OnboardingActivity.java` - Walkthrough
- `app/src/main/java/.../StartActivity.java` - Start button

---

## ⚠️ TEST LICENSE KEYS (REMOVE BEFORE PRODUCTION)

```
Entry Tier:  TESTER-2026-ENTRY-KEY
Premium:     TESTER-2026-PREMIUM-KEY
```

**Location to remove:** `backend/app.py` lines 30-34 and 229-240

---

## 🔐 Gumroad Credentials

```
Access Token: mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO
Entry Product ID: FCZgbXwUtCUZICnWigdugA==
Premium Product ID: 7IdKPVIR9R6Fre-xhUzXJQ==
```

**✅ Set in Render.com environment variables**

---

## 🎯 Products

### Entry Tier - $0.99
- URL: https://debernardis6.gumroad.com/l/bvzrd
- Unlocks: Auto-Calculate mode

### Premium - $2.99
- URL: https://debernardis6.gumroad.com/l/eepjed
- Unlocks: Custom Stack mode + Chipset management

---

## 📱 App Flow (v1.1)

```
App Launch → SplashActivity (2s) → First Launch?
                                       │
                    Yes ───────────────┴───────────────── No
                     ↓                                     ↓
              OnboardingActivity                    StartActivity
              (3 swipeable screens)                      ↓
                     ↓                              User taps
              StartActivity                      "Start Calculator"
                     ↓                                     ↓
              User taps                           LauncherActivity/TWA
           "Start Calculator"                           ↓
                     ↓                              Web App loads
              LauncherActivity/TWA
                     ↓
              Web App loads
```

---

## ✅ Deployment

- **Live URL:** https://poker-chip-calculator.onrender.com
- **GitHub:** https://github.com/DEBO2626/poker-chip-calculator
- **Platform:** Render.com (auto-deploy on git push)
- **Play Console:** https://play.google.com/console
- **Package:** com.onrender.poker_chip_calculator.twa

---

## 💻 Local Development

### Start Server
```bash
cd backend
python app.py
```
Then open: http://localhost:5000

### Build Android APK/AAB
```bash
# Set environment variables
set JAVA_HOME=C:\Users\john_\.bubblewrap\jdk\jdk-17.0.11+9
set ANDROID_HOME=C:\Users\john_\AppData\Local\Android\Sdk

# Build
cd "c:\Users\john_\Desktop\Poker chip"
gradlew assembleRelease  # APK
gradlew bundleRelease    # AAB

# Sign AAB
"%JAVA_HOME%\bin\jarsigner" -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore android.keystore app\build\outputs\bundle\release\app-release.aab android
```

---

## 📊 Progress

| Phase | Status | Complete |
|-------|--------|----------|
| 1. Account Setup | Done ✅ | 100% |
| 2. Local Dev | Done ✅ | 100% |
| 3. Backend | Done ✅ | 100% |
| 4. Frontend | Done ✅ | 100% |
| 5. PWA Features | Done ✅ | 100% |
| 6. Payment Integration | Done ✅ | 100% |
| 7. Deployment | Done ✅ | 100% |
| 8. TWA Build | Done ✅ | 100% |
| 9. Play Store Assets | Done ✅ | 100% |
| 10. Play Store Submit | Testing | 98% |
| 11. Launch & Market | Not Started | 0% |

**Overall:** 99% Complete

---

## 🔄 What's Next

1. **Wait for 14-day testing period** to complete
2. **Apply for production access** in Play Console
3. **Remove test license keys** from backend/app.py
4. **Deploy clean version** to Render.com
5. **Submit for production review**

---

## 📝 Version History

| Version | versionCode | Date | Changes |
|---------|-------------|------|---------|
| 1.0 | 1 | 2026-01-13 | Initial TWA release |
| 1.1 | 2 | 2026-01-14 | Native splash, onboarding, start button |

---

## 🔗 Important Links

- **Play Console:** https://play.google.com/console
- **Render Dashboard:** https://dashboard.render.com
- **GitHub Repo:** https://github.com/DEBO2626/poker-chip-calculator
- **Gumroad Dashboard:** https://gumroad.com/dashboard
- **Live App:** https://poker-chip-calculator.onrender.com

---

**Ready for production launch after testing period!** 🚀
