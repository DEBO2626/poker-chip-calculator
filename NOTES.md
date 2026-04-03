## 2026-03-27

### Marketing - Facebook Post
- Drafted Facebook post highlighting app's unique features vs competitors
- Key differentiator: calculates based on YOUR actual chip inventory, not generic distributions
- Post includes Play Store link, pricing info, call for feedback

### Pricing Model Change - Auto-Calculate Now FREE
- Changed Auto-Calculate mode from $0.99 (Entry Tier) to FREE for all users
- Premium ($2.99) remains the only paid tier - unlocks Custom Stack mode
- Files changed:
  - index.html: badge "Entry Tier" -> "Free", custom card always visible, pricing text updated
  - app.js: removed hasLicense() gate from selectMode('auto'), removed conditional card show/hide on init
  - service-worker.js: cache bumped v2.17 -> v3.0
- NEEDS: git push to deploy via Render auto-deploy
- NOTE: entry_tier product still exists in Play Console - can leave it or remove later
- Existing entry_tier purchasers unaffected (they already have access)

### Render Free Tier Usage Warning
- Received email: 628 of 750 free instance hours used this month
- NOT traffic-related - it's because the service runs 24/7 (UptimeRobot pings every 5 min)
- One always-on service = ~720 hours/month, nearly maxes the free tier
- Will squeak by this month (122 hours left, ~84 needed for remaining 3.5 days)
- Resets April 1
- Options: do nothing (barely fits), increase UptimeRobot interval, or upgrade to Render paid ($7/mo)

---

## 2026-03-15

### Status Check
- App is LIVE on Google Play, status: Production
- 29 installed audience (up from 2 at launch)
- Backend healthy on Render (200 OK)
- Play Store listing confirmed accessible
- "Down" email was likely UptimeRobot catching a brief Render cold start

### Revenue
- 8 total orders (3 real customers + your test purchases)
- All 3 real buyers purchased BOTH Entry ($0.99) and Premium ($2.99)
- Buyers from: USA, Europe (EUR), South Korea (KRW)
- ~$12-13 total revenue after Google's 15% cut

### Marketing - Reddit Post
- Posted to r/poker (338K members, 221K weekly visitors)
- Username: u/debo262626
- Title: "I built an app to calculate poker chip distributions for home tournaments..."
- Included app icon image and Play Store link
- Post is live, monitor for comments and reply to engagement

### Play Store Link (for sharing)
- https://play.google.com/store/apps/details?id=com.onrender.poker_chip_calculator.twa

### Still TODO (Phase 14 Marketing)
- [x] Post on Reddit r/poker
- [ ] Post on r/homegames
- [ ] Post on other poker forums
- [ ] Monitor Reddit post engagement and reply to comments
- [ ] Consider crossposting to r/onlinepoker, r/Poker_Theory

### App Version
- v1.3.2 (versionCode 6)
- Service worker cache v2.17
- Last updated in Play Console: Feb 7, 2026

### Note on assetlinks.json
- The static file at frontend/.well-known/assetlinks.json still has the OLD wrong fingerprint (9F:00:3F)
- But it doesn't matter because app.py serves the CORRECT fingerprint (9F:0D:3F) dynamically at /.well-known/assetlinks.json
- The Flask route overrides the static file

---

## 2026-02-06

### Google Play Billing - WORKING
- Both Entry Tier ($0.99) and Premium ($2.99) purchases confirmed working on 2 phones
- Digital Goods API + Payment Request API flow works end-to-end
- Service account: play-billing-verify@gen-lang-client-0894919543.iam.gserviceaccount.com
- GOOGLE_PLAY_CREDENTIALS env var set on Render
- Gumroad kept as fallback for web-only users

### TWA Verification Fix (ROOT CAUSE FOUND)
- App signing key fingerprint had ONE BYTE WRONG in assetlinks.json
- Was: ...9F:00:3F (wrong) / Should be: ...9F:0D:3F (correct)
- Found via ADB: `adb shell pm get-app-links com.onrender.poker_chip_calculator.twa`
- Also fixed: ACTION_VIEW intent changed to explicit class intent in StartActivity.java
- Also fixed: UptimeRobot set up (every 5 min) to prevent Render cold starts breaking TWA verification
- CANNOT test TWA via Internal App Sharing (uses different test certificate) - MUST test via Play Store install

### Purchase Flow Fixes
- Hidden "Upgrade to Premium" for users without Entry Tier
- Hidden Custom Stack mode card for brand new users
- Fixed broken Gumroad Premium link (was wrong URL, corrected to debernardis6.gumroad.com/l/eepjed)
- Bumped service worker cache to v2.17

### Build: v1.3.2 (versionCode 6)
- Explicit class intent fix + correct fingerprint
- Debug banner removed (console-only logging now)
- Published to Play Store production

---

## 2026-02-05

### App Published to Google Play
- Passed Google review (including paywall restriction fix)
- App access credentials provided for reviewers (key: Pizzaman26!)
- Google Play Billing integrated (15% fee vs Gumroad's 40%+)
- Added Digital Goods API + Payment Request API to frontend app.js
- Added /api/verify-play-purchase endpoint to backend app.py
- Created entry_tier ($0.99) and premium_tier ($2.99) products in Play Console
- Set up Google Cloud Service Account for purchase verification
- Built AAB v1.2 (versionCode 3) with billing support
- Added johndebernardis@gmail.com to License testing list

---

## 2026-01-14

### Native Android Components Added
- Native splash screen (SplashActivity.java) - 2 second display
- Onboarding walkthrough (OnboardingActivity.java) - 3 pages with ViewPager2
- Start button screen (StartActivity.java) - launches TWA via explicit class intent
- Vector drawable icons for onboarding (welcome chip, calculator, chip stack)
- First launch detection via SharedPreferences

### File Cleanup
- Deleted 52 unnecessary files (11,062 lines removed)
- 82% documentation clutter eliminated
- Moved session summaries to archive/ folder

---

## 2026-01-13

### Play Store Submission (Phase 10)
- Built initial TWA with Bubblewrap
- Created Play Store listing, screenshots, descriptions
- Submitted AAB v1.0 (versionCode 1) for review
- Privacy policy deployed to /privacy-policy.html

### Earlier Development (Phases 1-9)
- Python poker chip calculator built
- Flask REST API created
- Mobile-responsive PWA frontend built
- Gumroad payment integration (Entry $0.99, Premium $2.99)
- Deployed to Render.com (auto-deploy from GitHub main)
- PWA manifest, service worker, offline support
- Professional poker-themed UI with chip graphics

---

## KEY REFERENCE INFO

### Build Commands
```bash
set JAVA_HOME=C:\Users\john_\.bubblewrap\jdk\jdk-17.0.11+9
set ANDROID_HOME=C:\Users\john_\AppData\Local\Android\Sdk
gradlew bundleRelease
"%JAVA_HOME%\bin\jarsigner" -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore android.keystore app\build\outputs\bundle\release\app-release.aab android
# Password: pizzaman26
```

### Keystore
- File: android.keystore
- Alias: android
- Password: pizzaman26

### Owner Test Key
- Key: Pizzaman26!
- Unlocks all features (enter as license key)

### Important Links
- Play Console: https://play.google.com/console
- Render Dashboard: https://dashboard.render.com
- GitHub: https://github.com/DEBO2626/poker-chip-calculator
- Live App: https://poker-chip-calculator.onrender.com
- UptimeRobot: https://uptimerobot.com
- Play Store: https://play.google.com/store/apps/details?id=com.onrender.poker_chip_calculator.twa

### Environment Variables (Render)
- GUMROAD_ACCESS_TOKEN
- GUMROAD_ENTRY_PRODUCT_ID
- GUMROAD_PREMIUM_PRODUCT_ID
- GOOGLE_PLAY_CREDENTIALS (service account JSON)

### Wireless ADB
- Developer Options > Wireless debugging > Pair
- `adb shell pm get-app-links com.onrender.poker_chip_calculator.twa`
