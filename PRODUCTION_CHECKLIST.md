# Production Deployment Checklist

## ⚠️ CRITICAL - Security & Cleanup

### Before Deploying to Render.com:

- [ ] **DELETE** `frontend/unlock-premium.html`
  - This file allows free premium unlock
  - Created for local testing only
  - **Must be removed before production!**

- [ ] **Review** all localStorage premium checks
  - Ensure actual Gumroad license verification is required
  - Remove any testing bypasses

- [ ] **Update** version numbers
  - Update footer version in index.html
  - Update README.md version
  - Update manifest.json version if needed

- [ ] **Remove** development comments
  - Search for TODO, FIXME, TESTING, etc.
  - Clean up console.log statements (optional)

- [ ] **Test** premium paywall
  - Verify non-premium users see paywall
  - Verify Gumroad link works
  - Verify license activation works

### Environment Configuration:

- [ ] Set up environment variables on Render.com:
  - `FLASK_ENV=production`
  - `GUMROAD_API_KEY` (when implemented)
  - Any other secrets

- [ ] Update CORS settings for production domain

- [ ] Configure proper cache headers for production

### Final Testing Before Launch:

- [ ] Test on real Android device
- [ ] Test on real iPhone
- [ ] Test PWA installation
- [ ] Test offline mode
- [ ] Test all calculator modes
- [ ] Test premium unlock (with real payment)
- [ ] Verify analytics/tracking (if added)

### Post-Deployment:

- [ ] Verify HTTPS is working
- [ ] Test PWA installation from live URL
- [ ] Check service worker registration
- [ ] Monitor error logs
- [ ] Test on multiple devices

---

**Created:** 2026-01-13
**Last Updated:** 2026-01-13
