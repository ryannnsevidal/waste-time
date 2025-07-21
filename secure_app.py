from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from functools import wraps
from twilio_handler import handle_call
import os
import glob
import csv
import hashlib
import hmac
import secrets
import time
from datetime import datetime, timedelta
import json
import logging

# Configure logging for security monitoring
logging.basicConfig(level=logging.INFO)
security_logger = logging.getLogger('security')
handler = logging.FileHandler('security.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
security_logger.addHandler(handler)

app = Flask(__name__, static_folder='static', static_url_path='')

# Security Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
API_KEY = os.environ.get('API_KEY', 'scammer-waste-api-key-2025')
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN', 'admin-secure-token-2025')

# Configure CORS for production security
if os.environ.get('FLASK_ENV') == 'production':
    # Production: restrict to your domain
    CORS(app, origins=['https://yourdomain.com', 'https://www.yourdomain.com'])
else:
    # Development: allow localhost
    CORS(app, origins=['http://localhost:5001', 'http://127.0.0.1:5001'])

# Rate limiting to prevent abuse
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Security decorators
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for API key in header or query param
        api_key = request.headers.get('X-API-Key') or request.args.get('api_key')
        
        if not api_key:
            security_logger.warning(f"API access attempted without key from {get_remote_address()}")
            return jsonify({'error': 'API key required'}), 401
        
        if not hmac.compare_digest(api_key, API_KEY):
            security_logger.warning(f"Invalid API key attempted from {get_remote_address()}")
            return jsonify({'error': 'Invalid API key'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

def require_admin_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for admin token
        token = request.headers.get('Authorization')
        if token:
            token = token.replace('Bearer ', '')
        
        if not token or not hmac.compare_digest(token, ADMIN_TOKEN):
            security_logger.warning(f"Admin access attempted with invalid token from {get_remote_address()}")
            return jsonify({'error': 'Admin access denied'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

def sanitize_input(data):
    """Sanitize input data"""
    if isinstance(data, str):
        # Remove potentially dangerous characters
        return ''.join(char for char in data if char.isprintable() and char not in '<>&"\'')
    elif isinstance(data, dict):
        return {k: sanitize_input(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_input(item) for item in data]
    return data

# Global state for active calls
active_calls = {}

@app.route('/')
@limiter.limit("10 per minute")
def home():
    # Serve react dashboard if static files exist, otherwise show basic info
    static_path = os.path.join(app.static_folder, 'index.html')
    
    if os.path.exists(static_path):
        return send_file(static_path)
    else:
        return '''
        <h1>Scammer Waste Bot</h1>
        <p>🤖 Bot is running and ready to waste scammer time! 👴</p>
        <p><strong>✅ Secure API endpoints:</strong></p>
        <ul>
            <li><code>POST /voice</code> - Twilio webhook (rate limited)</li>
            <li><code>GET /api/stats</code> - Dashboard statistics (API key required)</li>
            <li><code>POST /api/calls/:id/end</code> - End active call (admin token required)</li>
        </ul>
        <p><strong>🔒 Security features enabled:</strong> Rate limiting, API authentication, input sanitization, CORS protection</p>
        '''

@app.route('/dashboard')
@limiter.limit("5 per minute")
def dashboard():
    # Explicit dashboard route
    if os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_file(os.path.join(app.static_folder, 'index.html'))
    else:
        return "Dashboard not available. Please build the React frontend first."

# Catch-all route for react router
@app.route('/<path:path>')
def serve_react_app(path):
    # Sanitize path to prevent directory traversal
    if '..' in path or path.startswith('/'):
        security_logger.warning(f"Suspicious path access attempted: {path} from {get_remote_address()}")
        return "Access denied", 403
    
    # Serve static files or fallback to index.html for SPA routing
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_file(os.path.join(app.static_folder, 'index.html'))
    else:
        return "File not found", 404

@app.route('/voice', methods=['POST'])
@limiter.limit("30 per minute")  # Limit Twilio webhook calls
def voice():
    try:
        # Log incoming calls for security monitoring
        security_logger.info(f"Incoming call from {get_remote_address()}")
        return handle_call()
    except Exception as e:
        security_logger.error(f"Error handling call: {str(e)}")
        return "Internal error", 500

@app.route('/api/stats', methods=['GET'])
@require_api_key
@limiter.limit("60 per minute")
def get_stats():
    """Get dashboard statistics - requires API key"""
    try:
        # Collect data from CSV files
        analytics_data = get_analytics_data()
        
        # Calculate stats
        total_calls = len(analytics_data)
        total_time_wasted = sum(row.get('call_duration', 0) for row in analytics_data)
        successful_calls = len([row for row in analytics_data if row.get('success_score', 0) > 7])
        success_rate = (successful_calls / total_calls * 100) if total_calls > 0 else 0
        
        # Format time
        hours = int(total_time_wasted // 3600)
        minutes = int((total_time_wasted % 3600) // 60)
        time_formatted = f"{hours}h {minutes}m"
        
        # Estimate money saved (avg scam attempt = $500)
        money_saved = successful_calls * 500
        
        # Recent calls data (sanitized)
        recent_calls = []
        for i, row in enumerate(analytics_data[-5:]):  # last 5 calls
            recent_calls.append({
                'id': f"call-{i+1}",
                'phoneNumber': sanitize_input(row.get('caller_number', 'Unknown'))[:20],  # Limit length
                'duration': int(row.get('call_duration', 0)),
                'scamType': sanitize_input(row.get('scam_type', 'Unknown'))[:50],
                'strategy': sanitize_input(row.get('strategy_used', 'Confused Grandpa'))[:50],
                'timestamp': datetime.now() - timedelta(hours=i+1),
                'success': row.get('success_score', 0) > 7,
                'wastedTime': int(row.get('call_duration', 0))
            })
        
        # Check for active calls
        current_call = None
        if len(active_calls) > 0:
            call_id = list(active_calls.keys())[0]
            call_data = active_calls[call_id]
            current_call = {
                'id': sanitize_input(call_id)[:50],
                'phoneNumber': sanitize_input(call_data.get('phone_number', 'Unknown'))[:20],
                'duration': int((datetime.now() - call_data.get('start_time', datetime.now())).total_seconds()),
                'status': 'active',
                'scamType': sanitize_input(call_data.get('scam_type', 'Unknown'))[:50],
                'strategy': 'Confused Grandpa',
                'wastedTime': int((datetime.now() - call_data.get('start_time', datetime.now())).total_seconds())
            }
        
        return jsonify({
            'totalTimeWasted': time_formatted,
            'totalCalls': total_calls,
            'activeNow': len(active_calls),
            'successRate': f"{success_rate:.0f}%",
            'totalSaved': f"${money_saved:,}",
            'thisWeek': "+15%",  # placeholder - could calculate from timestamps
            'recentCalls': recent_calls,
            'currentCall': current_call,
            'lastUpdated': datetime.now().isoformat(),
            'systemStatus': 'operational'
        })
        
    except Exception as e:
        security_logger.error(f"Error getting stats: {str(e)}")
        # Return sanitized error in production
        return jsonify({
            'totalTimeWasted': "0h 0m",
            'totalCalls': 0,
            'activeNow': 0,
            'successRate': "0%",
            'totalSaved': "$0",
            'thisWeek': "0%",
            'recentCalls': [],
            'currentCall': None,
            'lastUpdated': datetime.now().isoformat(),
            'systemStatus': 'error'
        })

@app.route('/api/calls/<call_id>/end', methods=['POST'])
@require_admin_token
@limiter.limit("10 per minute")
def end_call(call_id):
    """End an active call - requires admin token"""
    try:
        # Sanitize call_id
        call_id = sanitize_input(call_id)[:100]
        
        if call_id in active_calls:
            del active_calls[call_id]
            security_logger.info(f"Call {call_id} ended by admin from {get_remote_address()}")
            return jsonify({'status': 'success', 'message': 'Call ended'})
        else:
            return jsonify({'status': 'error', 'message': 'Call not found'}), 404
    except Exception as e:
        security_logger.error(f"Error ending call: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Internal error'}), 500

# Security endpoint to get API credentials (for demo purposes only)
@app.route('/api/auth/demo-credentials', methods=['GET'])
@limiter.limit("5 per minute")
def get_demo_credentials():
    """Get demo API credentials - remove in production"""
    if os.environ.get('FLASK_ENV') == 'production':
        return jsonify({'error': 'Not available in production'}), 404
    
    return jsonify({
        'api_key': API_KEY,
        'admin_token': ADMIN_TOKEN,
        'usage': {
            'api_key': 'Include in X-API-Key header or ?api_key= query param',
            'admin_token': 'Include in Authorization: Bearer <token> header'
        }
    })

def get_analytics_data():
    """Read analytics data from CSV files"""
    analytics_data = []
    
    # Look for CSV files in analytics_data directory
    if os.path.exists('analytics_data'):
        csv_files = glob.glob('analytics_data/*.csv')
        
        for csv_file in csv_files:
            try:
                with open(csv_file, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Convert numeric fields and sanitize
                        for field in ['call_duration', 'success_score', 'response_time', 'conversation_turns']:
                            if field in row and row[field]:
                                try:
                                    row[field] = float(row[field])
                                except:
                                    row[field] = 0
                        # Sanitize text fields
                        for field in ['caller_number', 'scam_type', 'strategy_used']:
                            if field in row:
                                row[field] = sanitize_input(row[field])
                        analytics_data.append(row)
            except Exception as e:
                security_logger.error(f"Error reading {csv_file}: {str(e)}")
    
    return analytics_data

# Helper function to track active calls
def start_call_tracking(call_id, phone_number, scam_type):
    """Start tracking an active call"""
    # Sanitize inputs
    call_id = sanitize_input(call_id)
    phone_number = sanitize_input(phone_number)
    scam_type = sanitize_input(scam_type)
    
    active_calls[call_id] = {
        'phone_number': phone_number,
        'start_time': datetime.now(),
        'scam_type': scam_type
    }
    security_logger.info(f"Started tracking call {call_id}")

# Error handlers
@app.errorhandler(429)
def ratelimit_handler(e):
    security_logger.warning(f"Rate limit exceeded from {get_remote_address()}")
    return jsonify(error="Rate limit exceeded"), 429

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Not found"), 404

@app.errorhandler(500)
def internal_error(e):
    security_logger.error(f"Internal error: {str(e)}")
    return jsonify(error="Internal server error"), 500

if __name__ == '__main__':
    # Security headers middleware
    @app.after_request
    def add_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        if os.environ.get('FLASK_ENV') == 'production':
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    
    # Run with security considerations
    # Railway deployment configuration
    port = int(os.environ.get('PORT', 5001))
    
    if os.environ.get('FLASK_ENV') == 'production':
        print("🔒 Running in PRODUCTION mode with enhanced security")
        app.run(host='0.0.0.0', port=port, debug=False)  # Railway needs 0.0.0.0
    else:
        print("🔧 Running in DEVELOPMENT mode")
        print(f"🔑 Demo API Key: {API_KEY}")
        print(f"🔐 Demo Admin Token: {ADMIN_TOKEN}")
        app.run(host='0.0.0.0', port=port, debug=True)

@app.route('/health')
def health_check():
    """Health check endpoint for Railway"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "scammer-waste-bot"
    })
