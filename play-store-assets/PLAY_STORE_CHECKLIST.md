# Google Play Store Submission Checklist

## Files Ready ✅

- [x] **App Bundle:** `app-release-bundle.aab` (4.0 MB)
- [x] **App Icon:** `frontend/assets/app-icon.png` (512x512)
- [x] **Signing Key:** `android.keystore` (KEEP THIS SAFE!)
- [x] **App Descriptions:** `play-store-assets/app-descriptions.txt`
- [x] **Privacy Policy:** `play-store-assets/privacy-policy.html`

## To Do Before Submission

### 1. Take Screenshots 📱
- [ ] Mode Selection screen
- [ ] Entry Tier paywall
- [ ] Auto-Calculate results
- [ ] Premium paywall
- [ ] (Optional) 2-4 more screenshots

**Guide:** See `SCREENSHOT_GUIDE.md`

**Save to:** `play-store-assets/screenshots/`

### 2. Deploy Privacy Policy 🔒
- [ ] Copy `privacy-policy.html` to `frontend/` folder
- [ ] Git commit and push
- [ ] Verify at: https://poker-chip-calculator.onrender.com/privacy-policy.html

**Guide:** See `DEPLOY_PRIVACY_POLICY.md`

### 3. Create Feature Graphic (Optional) 🎨
- [ ] Create 1024x500px banner image
- [ ] Or use existing header-banner.png (will need resizing)

**Alternative:** Skip this for now, you can add it later

### 4. Google Play Developer Account 💳
- [ ] Sign in to: https://play.google.com/console
- [ ] One-time fee: $25 (if not already paid)
- [ ] Verify you can access the console

---

## Play Store Submission Steps

### A. Create App Listing

1. **Go to:** https://play.google.com/console
2. **Click:** "Create app"
3. **Fill in:**
   - App name: Poker Chip Calculator
   - Default language: English (United States)
   - App or game: Game
   - Free or paid: Free (with in-app purchases)

### B. Store Listing

1. **Upload assets:**
   - App icon (512x512): `frontend/assets/app-icon.png`
   - Feature graphic (1024x500): Optional
   - Screenshots (2-8): From your phone

2. **Enter descriptions:**
   - Copy from `app-descriptions.txt`
   - Short description (80 chars max)
   - Full description (4000 chars max)

3. **Categorization:**
   - Category: Games > Card
   - Tags: poker, chip calculator, tournament

4. **Contact details:**
   - Email: johndebernardis@gmail.com
   - Website: https://poker-chip-calculator.onrender.com
   - Privacy policy: https://poker-chip-calculator.onrender.com/privacy-policy.html

### C. App Content

1. **Privacy Policy:**
   - URL: https://poker-chip-calculator.onrender.com/privacy-policy.html

2. **Ads:**
   - Select "No" (app doesn't contain ads)

3. **Target Audience:**
   - Age: 18+
   - (Poker/gambling content requires mature audience)

4. **Content Rating:**
   - Fill out questionnaire
   - Should get "Everyone" or "Teen" rating

5. **Data Safety:**
   - Minimal data collection
   - License keys verified with Gumroad
   - No personal data collected

### D. App Release

1. **Production Track:**
   - Upload: `app-release-bundle.aab`

2. **Release Name:**
   - Version 1.0 - Initial Release

3. **Release Notes:**
   ```
   Initial release of Poker Chip Calculator

   Features:
   - Auto-Calculate tournament distributions
   - Custom Stack mode for advanced users
   - Save and manage chipsets
   - Offline support
   - Professional chip calculations
   ```

4. **Countries:**
   - Select all countries (or specific ones)

5. **Review and Publish:**
   - Review all sections
   - Click "Send for review"

---

## After Submission

- ⏰ **Review time:** 1-7 days typically
- 📧 **Email notifications:** Google will email you updates
- 🔍 **Check status:** In Play Console dashboard

### If Rejected

- Check email for reason
- Fix issues
- Resubmit

### If Approved

- 🎉 **Your app is live!**
- Share Play Store link
- Start marketing

---

## Important Reminders

⚠️ **KEEP SAFE:**
- `android.keystore` file
- Keystore password: (you wrote it down)
- Key alias: android
- Key password: (same as keystore)

🔐 **Why important:**
- You NEED this keystore to update your app
- If you lose it, you can NEVER update your app
- Back it up to multiple locations!

📧 **Support Email:**
- Make sure johndebernardis@gmail.com is active
- Google will email you there
- Users can contact you there

---

## Estimated Timeline

- Screenshots: 15 minutes
- Privacy policy deploy: 5 minutes
- Play Console setup: 30 minutes
- Filling out forms: 45 minutes
- **Total:** ~2 hours
- **Review:** 1-7 days

---

## Questions?

- **Play Console:** https://support.google.com/googleplay/android-developer
- **App Reviews:** Check Play Console dashboard
- **Updates:** Same process, just upload new AAB with higher version code

---

**You're almost there! Just need screenshots and you're ready to submit!** 🚀

