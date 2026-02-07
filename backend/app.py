"""
Flask Backend for Poker Chip Calculator
Converts the Python calculator into a REST API for web/mobile access
"""

from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS
import os
import sys
import json
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Import the calculator functions
from pokerchipcounter import (
    calculate_chip_distribution,
    calculate_chip_distribution_custom,
    load_chip_set
)

# Initialize Flask app
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Enable CORS for frontend to call backend

# Gumroad API Configuration
GUMROAD_ACCESS_TOKEN = os.environ.get('GUMROAD_ACCESS_TOKEN', 'mUfWqJt86a5f-A10TRmaQb92FvQkOwk8Y-LCsw3PpxO')
GUMROAD_PRODUCT_IDS = {
    'entry': os.environ.get('GUMROAD_ENTRY_PRODUCT_ID', 'FCZgbXwUtCUZICnWigdugA=='),
    'premium': os.environ.get('GUMROAD_PREMIUM_PRODUCT_ID', '7IdKPVIR9R6Fre-xhUzXJQ==')
}

# Google Play Billing Configuration
PLAY_PACKAGE_NAME = 'com.onrender.poker_chip_calculator.twa'
PLAY_CREDENTIALS_JSON = os.environ.get('GOOGLE_PLAY_CREDENTIALS', '')

def get_play_service():
    """Create Google Play Developer API service for purchase verification"""
    if not PLAY_CREDENTIALS_JSON:
        return None
    creds_dict = json.loads(PLAY_CREDENTIALS_JSON)
    credentials = service_account.Credentials.from_service_account_info(
        creds_dict,
        scopes=['https://www.googleapis.com/auth/androidpublisher']
    )
    return build('androidpublisher', 'v3', credentials=credentials)

# Owner test keys - personal use only
TEST_LICENSE_KEYS = {
    'Pizzaman26!': 'premium'
}

# Load chip set once at startup
try:
    CHIP_SET = load_chip_set()
    print("[OK] Chip set loaded successfully")
except Exception as e:
    print(f"[WARNING] Could not load chip set from file: {e}")
    # Use default chip set
    CHIP_SET = {
        1: 300,
        5: 200,
        25: 200,
        100: 200,
        500: 50,
        1000: 50
    }
    print("[OK] Using default chip set")


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/')
def serve_frontend():
    """Serve the main HTML page"""
    response = make_response(send_from_directory(app.static_folder, 'index.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/.well-known/assetlinks.json')
def serve_assetlinks():
    """Serve Digital Asset Links for TWA verification"""
    assetlinks = [
        {
            "relation": ["delegate_permission/common.handle_all_urls"],
            "target": {
                "namespace": "android_app",
                "package_name": "com.onrender.poker_chip_calculator.twa",
                "sha256_cert_fingerprints": [
                    "D0:BC:61:5C:3F:CD:A2:CC:29:1D:17:B3:74:76:BA:EF:9D:9D:49:9F:03:27:CE:99:1E:55:2A:1D:33:9F:00:3F"
                ]
            }
        },
        {
            "relation": ["delegate_permission/common.handle_all_urls"],
            "target": {
                "namespace": "android_app",
                "package_name": "com.onrender.poker_chip_calculator.twa",
                "sha256_cert_fingerprints": [
                    "1E:17:78:69:A4:05:46:0B:E9:FF:42:A7:DC:83:A0:B6:DE:42:B3:7B:A1:55:67:38:42:CC:E3:21:D8:2F:BC:30"
                ]
            }
        }
    ]
    body = json.dumps(assetlinks)
    response = make_response(body)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Content-Length'] = str(len(body))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint - verify API is running"""
    return jsonify({
        'status': 'healthy',
        'message': 'Poker Chip Calculator API is running',
        'version': '2.1'
    })


@app.route('/api/chip-set', methods=['GET'])
def get_chip_set():
    """Get available chip set inventory"""
    total_value = sum(denom * count for denom, count in CHIP_SET.items())
    return jsonify({
        'chip_set': CHIP_SET,
        'total_value': total_value,
        'total_chips': sum(CHIP_SET.values())
    })


@app.route('/api/calculate', methods=['POST'])
def calculate_auto():
    """
    Mode 1: Auto-calculate chip distribution based on tournament duration

    Expected JSON body:
    {
        "num_players": 12,
        "small_blind": 25,
        "big_blind": 50,
        "duration_hours": 5,
        "minutes_per_level": 15
    }
    """
    try:
        data = request.json

        # Validate required fields
        required_fields = ['num_players', 'small_blind', 'big_blind',
                          'duration_hours', 'minutes_per_level']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400

        # Extract parameters
        num_players = int(data['num_players'])
        small_blind = float(data['small_blind'])
        big_blind = float(data['big_blind'])
        duration_hours = float(data['duration_hours'])
        minutes_per_level = int(data['minutes_per_level'])

        # Call calculator
        result = calculate_chip_distribution(
            num_players=num_players,
            small_blind=small_blind,
            big_blind=big_blind,
            duration_hours=duration_hours,
            minutes_per_level=minutes_per_level
        )

        # Check if result has error
        if 'error' in result:
            return jsonify(result), 400

        return jsonify(result)

    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'error': f'Unexpected error: {str(e)}'
        }), 500


@app.route('/api/calculate-custom', methods=['POST'])
def calculate_custom():
    """
    Mode 2: Calculate chip distribution for custom stack size

    Expected JSON body:
    {
        "num_players": 10,
        "small_blind": 25,
        "big_blind": 50,
        "target_stack": 8500
    }
    """
    try:
        data = request.json

        # Validate required fields
        required_fields = ['num_players', 'small_blind', 'big_blind', 'target_stack']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400

        # Extract parameters
        num_players = int(data['num_players'])
        small_blind = float(data['small_blind'])
        big_blind = float(data['big_blind'])
        target_stack = float(data['target_stack'])

        # Call calculator
        result = calculate_chip_distribution_custom(
            num_players=num_players,
            small_blind=small_blind,
            big_blind=big_blind,
            target_stack=target_stack
        )

        # Check if result has error
        if 'error' in result:
            return jsonify(result), 400

        return jsonify(result)

    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'error': f'Unexpected error: {str(e)}'
        }), 500


@app.route('/api/verify-license', methods=['POST'])
def verify_license():
    """
    Verify Gumroad license key

    Expected JSON body:
    {
        "license_key": "XXXX-XXXX-XXXX-XXXX",
        "product_id": "entry" or "premium"
    }
    """
    try:
        data = request.json
        license_key = data.get('license_key')
        product_tier = data.get('product_id')  # "entry" or "premium"

        if not license_key:
            return jsonify({
                'success': False,
                'error': 'Missing license_key'
            }), 400

        if not product_tier or product_tier not in GUMROAD_PRODUCT_IDS:
            return jsonify({
                'success': False,
                'error': 'Invalid product_id. Must be "entry" or "premium"'
            }), 400

        # Owner test keys
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

        # Get the actual Gumroad product ID
        gumroad_product_id = GUMROAD_PRODUCT_IDS[product_tier]

        # Call Gumroad License Verification API
        # Documentation: https://gumroad.com/api#license-key-verification
        api_url = "https://api.gumroad.com/v2/licenses/verify"

        payload = {
            'product_id': gumroad_product_id,
            'license_key': license_key,
            'increment_uses_count': 'false'  # Don't count this as a "use"
        }

        headers = {
            'Authorization': f'Bearer {GUMROAD_ACCESS_TOKEN}'
        }

        response = requests.post(api_url, data=payload, headers=headers, timeout=10)
        gumroad_data = response.json()

        # Check if the license is valid
        if gumroad_data.get('success') and gumroad_data.get('purchase'):
            purchase_info = gumroad_data['purchase']

            return jsonify({
                'success': True,
                'valid': True,
                'product_tier': product_tier,
                'purchase_email': purchase_info.get('email'),
                'purchase_date': purchase_info.get('created_at'),
                'product_name': purchase_info.get('product_name')
            })
        else:
            # License is invalid
            return jsonify({
                'success': True,
                'valid': False,
                'error': gumroad_data.get('message', 'Invalid license key')
            })

    except requests.exceptions.Timeout:
        return jsonify({
            'success': False,
            'error': 'Gumroad API request timed out. Please try again.'
        }), 504
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'Network error: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500


@app.route('/api/verify-play-purchase', methods=['POST'])
def verify_play_purchase():
    """
    Verify a Google Play in-app purchase

    Expected JSON body:
    {
        "purchase_token": "token-from-play-billing",
        "product_id": "entry_tier" or "premium_tier"
    }
    """
    try:
        data = request.json
        purchase_token = data.get('purchase_token')
        product_id = data.get('product_id')

        if not purchase_token or not product_id:
            return jsonify({
                'success': False,
                'error': 'Missing purchase_token or product_id'
            }), 400

        service = get_play_service()
        if not service:
            return jsonify({
                'success': False,
                'error': 'Google Play verification not configured'
            }), 500

        result = service.purchases().products().get(
            packageName=PLAY_PACKAGE_NAME,
            productId=product_id,
            token=purchase_token
        ).execute()

        # purchaseState: 0 = purchased, 1 = canceled, 2 = pending
        if result.get('purchaseState') == 0:
            # Acknowledge the purchase if not already acknowledged
            if result.get('acknowledgementState') == 0:
                service.purchases().products().acknowledge(
                    packageName=PLAY_PACKAGE_NAME,
                    productId=product_id,
                    token=purchase_token
                ).execute()

            tier = 'premium' if product_id == 'premium_tier' else 'entry'
            return jsonify({
                'success': True,
                'valid': True,
                'product_tier': tier
            })
        else:
            return jsonify({
                'success': True,
                'valid': False,
                'error': 'Purchase not valid'
            })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Verification error: ' + str(e)
        }), 500


# ============================================================================

@app.route("/<path:path>")
def serve_static(path):
    """Serve static files (CSS, JS, images, etc.)"""
    # Skip API routes - they are handled above
    if path.startswith("api/"):
        return jsonify({"error": "API endpoint not found"}), 404
    
    # Serve static files
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        response = make_response(send_from_directory(app.static_folder, path))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    
    # File not found
    return jsonify({"error": "File not found"}), 404


# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'The requested API endpoint does not exist'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred on the server'
    }), 500


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("POKER CHIP CALCULATOR API")
    print("="*60)
    print(f"[OK] Chip set loaded: {len(CHIP_SET)} denominations")
    print(f"[OK] Total chip value: ${sum(denom * count for denom, count in CHIP_SET.items()):,}")
    print("\n[SERVER] Starting server...")
    print("   Local:   http://localhost:5000")
    print("   Network: http://192.168.x.x:5000 (check your local IP)")
    print("\n[API] Endpoints:")
    print("   GET  /api/health          - Health check")
    print("   GET  /api/chip-set        - Get chip inventory")
    print("   POST /api/calculate       - Mode 1 (auto-calculate)")
    print("   POST /api/calculate-custom - Mode 2 (custom stack)")
    print("   POST /api/verify-license  - Verify Gumroad license")
    print("\n[INFO] Press CTRL+C to stop the server")
    print("="*60 + "\n")

    # Run the Flask development server
    # Use PORT from environment (for Render.com) or default to 5000 for local dev
    port = int(os.environ.get('PORT', 5000))
    app.run(
        host='0.0.0.0',  # Listen on all network interfaces
        port=port,
        debug=False  # Disable debug mode in production
    )
