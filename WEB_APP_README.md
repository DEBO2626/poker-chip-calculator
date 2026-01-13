# Poker Chip Calculator

A professional poker chip distribution calculator web app for tournament organizers.

## Features

- **Auto-Calculate Mode**: Calculate optimal chip distribution based on tournament duration and blind structure
- **Custom Stack Mode** (Premium): Specify exact stack amounts per player
- **Mobile-Optimized**: Progressive Web App (PWA) with offline support
- **Professional Graphics**: AI-generated poker chip designs and casino-themed UI

## Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python Flask
- **Graphics**: AI-generated assets (Nanobanana)
- **PWA**: Service Worker for offline functionality

## Project Structure

```
poker-chip-web/
├── frontend/
│   ├── assets/
│   │   ├── app-icon.png          # PWA app icon (512x512)
│   │   ├── chip-5-red.png        # Red $5 poker chip
│   │   ├── chip-25-green.png     # Green $25 poker chip
│   │   ├── chip-100-black.png    # Black $100 poker chip
│   │   ├── chip-500-purple.png   # Purple $500 poker chip
│   │   ├── felt-background.png   # Green poker felt texture
│   │   └── header-banner.png     # Professional poker scene banner
│   ├── index.html                # Main HTML structure
│   ├── styles.css                # Styling and layout
│   ├── app.js                    # Frontend logic
│   ├── manifest.json             # PWA manifest
│   └── service-worker.js         # Offline caching
├── backend/
│   ├── app.py                    # Flask server
│   └── pokerchipcounter.py       # Chip calculation logic
├── crop_chips.py                 # Utility to crop chip images
└── README.md
```

## Chip Color Standards

- Red = $5
- Green = $25
- Black = $100
- Purple = $500

## Assets

All graphics were generated using AI (Nanobanana) with consistent styling:
- Professional casino-quality poker chips
- 3D depth effects with glossy finish
- Transparent backgrounds for UI flexibility
- Consistent white stripe pattern across all denominations

## Setup

1. Install dependencies:
   ```bash
   pip install flask pillow
   ```

2. Run the backend:
   ```bash
   cd backend
   python app.py
   ```

3. Open browser:
   ```
   http://localhost:5000
   ```

## Development Notes

- Graphics cropped from `all4chips.png` using `crop_chips.py`
- Service worker caches assets for offline use
- Mobile-first responsive design
- Premium features require license key activation

## Version

v2.1 - Professional Graphics Update

## License

Proprietary - Entry tier ($0.99) / Premium tier (+$2.99)
