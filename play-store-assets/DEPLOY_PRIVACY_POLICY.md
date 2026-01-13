# Deploy Privacy Policy to Live Site

Google Play requires a publicly accessible privacy policy URL.

## Step 1: Add Privacy Policy to Your Frontend

Copy the privacy policy HTML file to your frontend folder:

```bash
cp play-store-assets/privacy-policy.html frontend/privacy-policy.html
```

## Step 2: Deploy to Render

```bash
git add frontend/privacy-policy.html
git commit -m "Add privacy policy for Play Store"
git push origin main
```

Render will auto-deploy in 2-3 minutes.

## Step 3: Verify It Works

Visit: https://poker-chip-calculator.onrender.com/privacy-policy.html

You should see the privacy policy page.

## Step 4: Use This URL in Play Store

When filling out the Play Store form, enter:
```
https://poker-chip-calculator.onrender.com/privacy-policy.html
```

---

**Ready to deploy?** Run the commands above when you're ready to submit to Play Store.

