# Gumroad License Testing Guide

## Phase 6 Complete! ✅

The Gumroad payment integration is now fully implemented. Here's how to test it:

---

## What's Been Implemented

1. **Backend License Verification** ([backend/app.py](backend/app.py))
   - Real Gumroad API integration
   - Verifies license keys against Gumroad's servers
   - Supports both Entry and Premium tiers
   - Returns purchase information (email, date, product name)

2. **Frontend License Activation** ([frontend/app.js](frontend/app.js))
   - Updated `activateLicense()` function
   - Calls backend API for verification
   - Tries Entry tier first, then Premium if needed
   - Saves license info to localStorage
   - Shows user-friendly success/error messages

3. **Gumroad Products Created**
   - Entry Tier: $0.99 (Product ID: FCZgbXwUtCUZICnWigdugA==)
   - Premium Upgrade: $2.99 (Product ID: 7IdKPVIR9R6Fre-xhUzXJQ==)
   - Both products have license key generation enabled

---

## How to Test (Without Making Real Purchases)

### Option 1: Use Gumroad Test Mode

1. Go to your Gumroad products
2. For each product, look for a "Test purchase" or "Preview" option
3. Complete a test purchase to get a real test license key
4. Enter that key in the app to verify it works

### Option 2: Test the API Directly

You can test the backend API with curl:

```bash
# Test Entry Tier (replace with actual license key from Gumroad test)
curl -X POST http://localhost:5000/api/verify-license \
  -H "Content-Type: application/json" \
  -d "{\"license_key\": \"YOUR-LICENSE-KEY-HERE\", \"product_id\": \"entry\"}"

# Test Premium Tier
curl -X POST http://localhost:5000/api/verify-license \
  -H "Content-Type: application/json" \
  -d "{\"license_key\": \"YOUR-LICENSE-KEY-HERE\", \"product_id\": \"premium\"}"
```

### Option 3: Test Invalid License

Test that invalid licenses are rejected:

```bash
curl -X POST http://localhost:5000/api/verify-license \
  -H "Content-Type: application/json" \
  -d "{\"license_key\": \"INVALID-KEY-1234\", \"product_id\": \"entry\"}"
```

Expected response:
```json
{
  "success": true,
  "valid": false,
  "error": "That license does not exist for the provided product."
}
```

---

## Testing in the App

1. **Start the server** (already running at http://localhost:5000)

2. **Open the app** in your browser:
   - Local: http://localhost:5000
   - Phone (same network): http://192.168.68.78:5000

3. **Try to access Premium features**:
   - Click the "Custom Stack" tab
   - You'll see the premium lock screen

4. **Click "Unlock Premium"**

5. **Enter a license key**:
   - For testing, you'll need to either:
     - Make a test purchase on Gumroad
     - Use Gumroad's test mode to generate a key
     - Contact Gumroad support for sandbox testing

6. **Verify the license activates**:
   - Should see success message with purchase details
   - Premium features should unlock
   - License info saved in localStorage

---

## Making Real Test Purchases

To fully test the end-to-end flow:

### Step 1: Purchase Entry Tier

1. Go to: https://debernardis6.gumroad.com/l/bvzrd
2. Complete purchase ($0.99)
3. Check email for license key
4. Enter license key in app
5. Verify Entry Tier features unlock

### Step 2: Purchase Premium Upgrade (Optional)

1. Go to Premium product URL (get permalink from Gumroad)
2. Complete purchase ($2.99)
3. Check email for license key
4. Enter license key in app
5. Verify all Premium features unlock

---

## Expected Behavior

### Valid License (Success Response)

```json
{
  "success": true,
  "valid": true,
  "product_tier": "entry",
  "purchase_email": "customer@example.com",
  "purchase_date": "2026-01-13T12:00:00Z",
  "product_name": "Poker Chip Calculator - Entry Tier"
}
```

### Invalid License (Error Response)

```json
{
  "success": true,
  "valid": false,
  "error": "That license does not exist for the provided product."
}
```

### Network Error (500 Response)

```json
{
  "success": false,
  "error": "Network error: Connection timeout"
}
```

---

## Troubleshooting

### "Network error" when activating

- Check that Flask server is running
- Check internet connection (needs to reach Gumroad API)
- Check browser console for CORS errors

### "Invalid license key" for valid key

- Make sure you're testing with correct product tier
- Verify license key was copied correctly (no extra spaces)
- Check that product IDs in backend/app.py match Gumroad

### License activates but features don't unlock

- Check browser console for JavaScript errors
- Verify checkPremiumStatus() is working
- Clear localStorage and try again

---

## API Credentials (Keep Private!)

Stored in: `gumroad-credentials.txt`

- Access Token: mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO
- Entry Product ID: FCZgbXwUtCUZICnWigdugA==
- Premium Product ID: 7IdKPVIR9R6Fre-xhUzXJQ==

**IMPORTANT**: When deploying to production (Render.com), these will be stored as environment variables, NOT in code!

---

## What Happens Next

Once testing is complete and you're satisfied with the payment flow:

1. ✅ Remove `frontend/unlock-premium.html` test file
2. ✅ Set up environment variables on Render.com
3. ✅ Deploy to production
4. ✅ Make real test purchases
5. ✅ Launch!

---

## Testing Checklist

- [ ] Server starts without errors
- [ ] Can access app in browser
- [ ] Premium lock screen appears for locked features
- [ ] Invalid license key shows error message
- [ ] Valid Entry license unlocks Entry features
- [ ] Valid Premium license unlocks all features
- [ ] License info persists after page reload
- [ ] Works on mobile device (http://192.168.68.78:5000)

---

## Notes

- The backend is now using the REAL Gumroad API
- License verification happens server-side for security
- Frontend can't bypass the paywall (unlike test mode)
- Each license key is unique per purchase
- License keys don't expire (unless you configure it in Gumroad)

Ready to test! 🎉
