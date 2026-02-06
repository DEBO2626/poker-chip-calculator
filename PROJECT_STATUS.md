# PROJECT STATUS - Poker Chip Calculator

## Overall Progress: LIVE + Google Play Billing

**Last Updated:** 2026-02-06

---

## Current Status

- App is LIVE on Google Play Store (published Feb 5, 2026)
- 2 installs, 17 device acquisitions, 15 MAU
- Google Play Billing integration complete
- AAB v1.2 (versionCode 3) submitted for review with billing support
- In-app products active: entry_tier ($0.99), premium_tier ($2.99)
- Backend deployed with Google Play purchase verification

---

## PHASE COMPLETION

### Phase 1-9: Development (100% COMPLETE)
All development phases complete - account setup, backend, frontend, PWA, payments, deployment, TWA build, Play Store assets.

### Phase 10: Play Store Submit (100% COMPLETE)
- App published to production on Google Play
- Passed Google review (including paywall restriction fix)
- App access credentials provided for reviewers (key: Pizzaman26!)
- 2 installs confirmed

### Phase 11: Google Play Billing (100% COMPLETE)
- [x] Research Google Play Billing vs Gumroad fees
- [x] Add Digital Goods API + Payment Request API to frontend (app.js)
- [x] Add /api/verify-play-purchase endpoint to backend (app.py)
- [x] Update purchase buttons to use Play Billing with Gumroad fallback
- [x] Enable playBilling in twa-manifest.json
- [x] Add billing:1.1.0 dependency to build.gradle
- [x] Add DigitalGoodsRequestHandler to DelegationService.java
- [x] Add PaymentActivity + PaymentService to AndroidManifest.xml
- [x] Build AAB v1.2 (versionCode 3) with billing support
- [x] Upload AAB to Play Console Production (in review)
- [x] Create entry_tier one-time product ($0.99) in Play Console
- [x] Create premium_tier one-time product ($2.99) in Play Console
- [x] Enable Google Play Android Developer API in Cloud Console
- [x] Create service account (play-billing-verify)
- [x] Link service account to Play Console (Users and permissions)
- [x] Add GOOGLE_PLAY_CREDENTIALS env var to Render
- [x] Deploy backend with billing verification
- [x] Push all code changes to GitHub

### Phase 12: Purchase Flow Fixes (100% COMPLETE)
- [x] Hide "Upgrade to Premium" for users without Entry Tier
- [x] Hide Custom Stack mode card for brand new users
- [x] Fix broken Gumroad Premium link (was gumroad.com/l/poker-calc-premium)
- [x] Bump service worker cache to v2.4

### Phase 13: Marketing (IN PROGRESS)
- [x] Facebook friends announcement post
- [ ] Post on Reddit r/poker
- [ ] Post on poker forums
- [ ] Monitor reviews and metrics

---

## APP VERSION HISTORY

| Version | versionCode | Date | Changes |
|---------|-------------|------|---------|
| 1.0 | 1 | 2026-01-13 | Initial TWA release |
| 1.1 | 2 | 2026-01-14 | Native splash, onboarding, start button |
| 1.2 | 3 | 2026-02-06 | Google Play Billing, purchase flow fixes |

---

## Revenue Comparison

| Platform | Per $0.99 Sale | You Keep |
|----------|---------------|----------|
| Gumroad | $0.30 flat + 10% | $0.06 |
| Google Play (15%) | $0.15 | $0.84 |

---

## What's Next

1. Wait for v1.2 review approval (auto-publishes)
2. Test in-app purchases once live
3. Service account may take 24-36 hours to fully activate
4. Monitor purchases in Play Console financial reports
5. Consider removing Gumroad once Play Billing confirmed working
6. Continue marketing efforts

---
