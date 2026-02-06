# Quick Reference - Poker Chip Calculator

**Version:** 1.3.1 (versionCode 5) in review
**Status:** LIVE ON GOOGLE PLAY - TWA billing fix in review
**Last Updated:** 2026-02-06
**Live URL:** https://poker-chip-calculator.onrender.com

---

## Start Here (New Chat Session)

1. **Read:** `START_HERE_NEW_SESSION.md` - Current status & next steps

---

## Key Files

### Backend
- `backend/app.py` - Flask server + Gumroad API + Google Play verification
- `backend/requirements.txt` - Python deps (google-api-python-client, google-auth)
- `backend/pokerchipcounter.py` - Core calculator logic

### Frontend
- `frontend/index.html` - Main app
- `frontend/app.js` - JS logic + Digital Goods API + Payment Request API
- `frontend/service-worker.js` - Offline support (cache v2.12)

### Android/TWA
- `twa-manifest.json` - TWA config (playBilling enabled)
- `app/build.gradle` - v1.3.1, versionCode 5
- `app/src/main/AndroidManifest.xml` - PaymentActivity + PaymentService
- `app/src/main/java/.../DelegationService.java` - DigitalGoodsRequestHandler

---

## Payment Systems

### Google Play Billing (PRIMARY)
- Products: entry_tier ($0.99), premium_tier ($2.99)
- 15% fee (keep $0.84 per $0.99 sale)
- Service Account: play-billing-verify@gen-lang-client-0894919543.iam.gserviceaccount.com
- Uses Digital Goods API + Payment Request API in frontend

### Gumroad (FALLBACK - web only)
- Entry ($0.99): https://debernardis6.gumroad.com/l/bvzrd
- Premium ($2.99): https://debernardis6.gumroad.com/l/eepjed
- Only shown when Play Billing unavailable

---

## Environment Variables (Render)

```
GUMROAD_ACCESS_TOKEN=mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO
GUMROAD_ENTRY_PRODUCT_ID=FCZgbXwUtCUZICnWigdugA==
GUMROAD_PREMIUM_PRODUCT_ID=7IdKPVIR9R6Fre-xhUzXJQ==
GOOGLE_PLAY_CREDENTIALS=<service account JSON key>
```

---

## Products (Google Play Console)

| Product ID | Name | Price | Type |
|------------|------|-------|------|
| entry_tier | Entry Tier | $0.99 | One-time |
| premium_tier | Premium Tier | $2.99 | One-time |

---

## Owner Master Key

**Key:** `Pizzaman26!`
Unlocks all features (premium + entry). Enter as license key for either tier.

---

## Build Commands

```bash
set JAVA_HOME=C:\Users\john_\.bubblewrap\jdk\jdk-17.0.11+9
set ANDROID_HOME=C:\Users\john_\AppData\Local\Android\Sdk
gradlew bundleRelease
"%JAVA_HOME%\bin\jarsigner" -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore android.keystore app\build\outputs\bundle\release\app-release.aab android
# Password: pizzaman26
```

---

## Deployment

- **Live URL:** https://poker-chip-calculator.onrender.com
- **GitHub:** https://github.com/DEBO2626/poker-chip-calculator
- **Platform:** Render.com (auto-deploy on git push to main)
- **Play Console:** https://play.google.com/console
- **Google Cloud:** https://console.cloud.google.com (project: Gemini API)

---

## Version History

| Version | versionCode | Date | Changes |
|---------|-------------|------|---------|
| 1.0 | 1 | 2026-01-13 | Initial TWA release |
| 1.1 | 2 | 2026-01-14 | Native splash, onboarding, start button |
| 1.2 | 3 | 2026-02-06 | Google Play Billing, purchase flow fixes |
| 1.3.1 | 5 | 2026-02-06 | TWA billing debug fixes, remove debug banner |

---

## Progress

| Phase | Status |
|-------|--------|
| 1-9. Development & Assets | Complete |
| 10. Play Store Submit | Complete - LIVE |
| 11. Google Play Billing | Complete |
| 12. Purchase Flow Fixes | Complete |
| 13. TWA Verification Fix | In Progress - v1.3.1 in review |
| 14. Marketing | In Progress |

---

## UptimeRobot

- **URL:** https://uptimerobot.com
- **Monitor:** poker-chip-calculator.onrender.com (every 5 min)
- **Purpose:** Prevents Render free tier cold starts that break TWA verification

---

## Important Links

- **Play Console:** https://play.google.com/console
- **Render Dashboard:** https://dashboard.render.com
- **GitHub Repo:** https://github.com/DEBO2626/poker-chip-calculator
- **Google Cloud Console:** https://console.cloud.google.com
- **Gumroad Dashboard:** https://gumroad.com/dashboard
- **Live App:** https://poker-chip-calculator.onrender.com

---
