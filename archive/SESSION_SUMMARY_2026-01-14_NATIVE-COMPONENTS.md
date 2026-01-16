# Session Summary: Native Android Components & Test Keys

**Date:** January 14, 2026
**Duration:** ~3 hours
**Focus:** Adding native Android screens and test license keys for testers

---

## Overview

Based on feedback from Fiverr tester Reda Timi, we added native Android components to improve Play Store approval chances. TWA (Trusted Web Activity) apps often face rejection, and adding native screens (splash, onboarding, start button) has helped similar apps pass review.

---

## What Was Done

### 1. Native Android Components Added

#### SplashActivity
- 2-second branded splash screen
- Shows app logo and title
- Checks if first launch using SharedPreferences
- Routes to OnboardingActivity (first launch) or StartActivity (returning users)
- **File:** `app/src/main/java/.../SplashActivity.java`

#### OnboardingActivity
- 3 swipeable screens using ViewPager2
- Screen 1: Welcome - "Poker Chip Calculator"
- Screen 2: Auto Mode - "Auto-Calculate Mode"
- Screen 3: Custom Mode - "Custom Stack Mode"
- Skip button and Next/Get Started buttons
- Page indicator dots
- Sets `first_launch = false` when completed
- **File:** `app/src/main/java/.../OnboardingActivity.java`

#### StartActivity
- Native screen with "Start Calculator" button
- Button launches TWA via ACTION_VIEW intent with app URL
- Professional poker-themed styling
- **File:** `app/src/main/java/.../StartActivity.java`

### 2. App Version Bumped
- **From:** 1.0 (versionCode 1)
- **To:** 1.1 (versionCode 2)
- Updated in `app/build.gradle`

### 3. Test License Keys Added

Added temporary test license keys to `backend/app.py` for testers to bypass the paywall:

```python
TEST_LICENSE_KEYS = {
    'TESTER-2026-ENTRY-KEY': 'entry',
    'TESTER-2026-PREMIUM-KEY': 'premium'
}
```

- Entry key unlocks Auto-Calculate mode
- Premium key unlocks Custom Stack mode + chipset management
- Keys check added to `verify_license()` function
- Changes pushed to GitHub and auto-deployed to Render.com

### 4. New AAB Built and Signed
- Built with Gradle (bundleRelease)
- Signed with jarsigner using android.keystore
- Keystore password: pizzaman26
- Uploaded to Play Store Closed testing

---

## Files Created/Modified

### New Java Files
- `app/src/main/java/com/onrender/poker_chip_calculator/twa/SplashActivity.java`
- `app/src/main/java/com/onrender/poker_chip_calculator/twa/OnboardingActivity.java`
- `app/src/main/java/com/onrender/poker_chip_calculator/twa/StartActivity.java`

### New Layout XML Files
- `app/src/main/res/layout/activity_splash.xml`
- `app/src/main/res/layout/activity_onboarding.xml`
- `app/src/main/res/layout/item_onboarding.xml`
- `app/src/main/res/layout/activity_start.xml`

### New Drawable Resources
- `app/src/main/res/drawable/button_primary.xml`
- `app/src/main/res/drawable/button_outline.xml`
- `app/src/main/res/drawable/dot_active.xml`
- `app/src/main/res/drawable/dot_inactive.xml`
- `app/src/main/res/drawable/onboarding_welcome.xml`
- `app/src/main/res/drawable/onboarding_auto.xml`
- `app/src/main/res/drawable/onboarding_custom.xml`

### New/Modified Resource Files
- `app/src/main/res/values/themes.xml` (NEW)
- `app/src/main/res/values/colors.xml` (MODIFIED - added splash_background, gold, white variants)

### Modified Configuration Files
- `app/src/main/AndroidManifest.xml` - Added new activities, updated launcher
- `app/build.gradle` - Version bump, new dependencies

### Backend Changes
- `backend/app.py` - Added TEST_LICENSE_KEYS and verify check

---

## Issues Encountered and Fixed

### 1. Java Version Error
- **Problem:** Gradle required JDK 11+, was using Java 8
- **Solution:** Set JAVA_HOME to bubblewrap's JDK 17 at `C:/Users/john_/.bubblewrap/jdk/jdk-17.0.11+9`

### 2. ANDROID_HOME Not Set
- **Problem:** SDK location not found
- **Solution:** Set ANDROID_HOME to `C:/Users/john_/AppData/Local/Android/Sdk`

### 3. App Crash on Start Button (First Attempt)
- **Problem:** App crashed when tapping "Start Calculator"
- **Solution:** Added `android:theme="@android:style/Theme.Translucent.NoTitleBar"` to LauncherActivity

### 4. App Crash on Start Button (Second Attempt)
- **Problem:** Still crashed when launching LauncherActivity directly
- **Solution:** Changed to launch via ACTION_VIEW intent with URL instead of direct activity launch

### 5. AAB Not Signed Error
- **Problem:** Play Console rejected unsigned AAB
- **Solution:** Used jarsigner with JDK 17 to sign the AAB

---

## New App Flow

```
App Launch
    ↓
[SplashActivity] (2 seconds)
    ↓
First Launch? ─Yes→ [OnboardingActivity] (3 screens)
    │                      ↓
    No              [StartActivity]
    │                      ↓
    └─────────────→ User taps "Start Calculator"
                           ↓
                   [LauncherActivity/TWA]
                           ↓
                   Web App loads
```

---

## Test License Keys

### For Testers Only

| Key | Tier | Access |
|-----|------|--------|
| `TESTER-2026-ENTRY-KEY` | Entry | Auto-Calculate mode |
| `TESTER-2026-PREMIUM-KEY` | Premium | All features |

### How Testers Use Keys
1. Launch app and go through onboarding
2. Tap "Start Calculator" to reach the web app
3. When prompted to pay, enter the test license key
4. Key validates against Render.com backend

---

## Before Production Launch

### CRITICAL: Remove Test Keys

The following must be removed from `backend/app.py` before production:

**Lines 30-34 - Delete:**
```python
TEST_LICENSE_KEYS = {
    'TESTER-2026-ENTRY-KEY': 'entry',
    'TESTER-2026-PREMIUM-KEY': 'premium'
}
```

**Lines 229-240 - Delete the entire if block:**
```python
if license_key in TEST_LICENSE_KEYS:
    test_tier = TEST_LICENSE_KEYS[license_key]
    if test_tier == product_tier or (test_tier == 'premium' and product_tier == 'entry'):
        return jsonify({
            'success': True,
            'valid': True,
            'product_tier': product_tier,
            'purchase_email': 'tester@test.com',
            'purchase_date': '2026-01-14',
            'product_name': f'Test {product_tier.title()} License'
        })
```

---

## Tester Instructions (Send to Testers)

```
To test the app:

1. Install the app from the Play Store closed testing link
2. Go through the splash screen and onboarding
3. Tap "Start Calculator"
4. When you see the paywall, use these test keys:

   - For Entry Tier: TESTER-2026-ENTRY-KEY
   - For Premium: TESTER-2026-PREMIUM-KEY

5. Test all features:
   - Auto-Calculate mode (entry)
   - Custom Stack mode (premium)
   - Chipset management (premium)

Please report any issues you find!
```

---

## Next Steps

1. Monitor Play Console for tester activity
2. Wait for 14-day testing period
3. Apply for production access
4. **Remove test keys before production**
5. Submit for production review

---

## Technical Notes

### Build Commands (for reference)
```bash
# Set environment
set JAVA_HOME=C:\Users\john_\.bubblewrap\jdk\jdk-17.0.11+9
set ANDROID_HOME=C:\Users\john_\AppData\Local\Android\Sdk

# Build AAB
gradlew bundleRelease

# Sign AAB
"%JAVA_HOME%\bin\jarsigner" -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore android.keystore app\build\outputs\bundle\release\app-release.aab android
```

### Keystore Info
- File: `android.keystore`
- Alias: `android`
- Password: `pizzaman26`

---

---

## Issue: Missing pokerchipcounter.py

### What Happened
A previous Claude session (commit `9b6f9ce`) accidentally deleted `backend/pokerchipcounter.py` during a "cleanup" operation, thinking it was a duplicate file. This caused Render deployments to fail with:
```
ModuleNotFoundError: No module named 'pokerchipcounter'
```

### Resolution
- The file existed in the root folder as a backup
- Copied `pokerchipcounter.py` from root to `backend/` folder
- Committed and pushed to GitHub (commit `980bca6`)
- Render deployment succeeded at 11:28 AM

### Lesson Learned
**NEVER delete Python source files during cleanup without verifying they are truly duplicates and not required imports.**

The `pokerchipcounter.py` file is the **core calculator logic** - the heart of the entire application.

---

**Session Complete**
