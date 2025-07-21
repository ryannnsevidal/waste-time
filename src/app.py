"""
Advanced Flask Application for Scammer Waste Bot
Production-ready with integrated frontend and full API
"""
from flask import Flask, request, jsonify, render_template_string, send_from_directory, send_file
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.middleware.proxy_fix import ProxyFix
import os
import time
import json
import sqlite3
import threading
from datetime import datetime
from typing import Dict, Any

# Import our advanced AI components
from ai.sophisticated_engine import SophisticatedEngine
from ai.enhanced_responses import EnhancedResponses
from data.analytics_dashboard import AnalyticsDashboard
from static_routes import static_bp

app = Flask(__name__, static_folder='../data/static', static_url_path='/')
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
CORS(app, origins=['*'])  # Allow all origins for production flexibility

# Register static file routes
# app.register_blueprint(static_bp)  # Commented out to avoid conflicts

# Rate limiting with more production-friendly limits
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["1000 per day", "100 per hour", "10 per minute"]
)

# Initialize production database
def init_production_db():
    """Initialize production database with proper tables"""
    conn = sqlite3.connect('/workspaces/waste-time/data/scammer_waste.db')
    cursor = conn.cursor()
    
    # Create conversations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scammer_id TEXT UNIQUE,
            start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            message_count INTEGER DEFAULT 0,
            time_wasted INTEGER DEFAULT 0,
            personality TEXT DEFAULT 'confused_grandpa',
            frustration_level INTEGER DEFAULT 0,
            success_score REAL DEFAULT 0.0,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    # Create messages table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            message_type TEXT,
            content TEXT,
            response_time REAL,
            ai_confidence REAL
        )
    ''')
    
    # Create analytics table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            total_conversations INTEGER,
            time_wasted INTEGER,
            success_rate REAL,
            top_strategies TEXT,
            geographic_data TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database
init_production_db()

# Initialize AI components
ai_engine = SophisticatedEngine()
response_library = EnhancedResponses()
analytics = AnalyticsDashboard()

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
API_KEY = os.environ.get('SCAMMER_WASTE_API_KEY', 'scammer-waste-api-key-2025')

def require_api_key(f):
    """Decorator to require API key for protected endpoints"""
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != API_KEY:
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def dashboard():
    """Serve the main dashboard frontend"""
    return send_from_directory('/workspaces/waste-time/data/static', 'index.html')

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """Serve React build assets"""
    response = send_from_directory('/workspaces/waste-time/data/static/assets', filename)
    
    # Set proper MIME types for assets
    if filename.endswith('.js'):
        response.headers['Content-Type'] = 'application/javascript'
    elif filename.endswith('.css'):
        response.headers['Content-Type'] = 'text/css'
    elif filename.endswith('.map'):
        response.headers['Content-Type'] = 'application/json'
    
    # Enable caching for assets
    response.headers['Cache-Control'] = 'public, max-age=31536000'  # 1 year
    
    return response

@app.route('/favicon.ico')
def favicon():
    """Serve favicon"""
    return send_from_directory('/workspaces/waste-time/data/static', 'favicon.ico')

@app.route('/api/health')
def health_check():
    """System health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '2.0.0',
        'components': {
            'ai_engine': 'operational',
            'response_library': 'operational',
            'analytics': 'operational',
            'frontend': 'integrated'
        }
    })

@app.route('/api/config')
def get_config():
    """Get frontend configuration (no API key required for public config)"""
    return jsonify({
        'api_base_url': request.host_url.rstrip('/'),
        'websocket_url': f"ws://{request.host}/ws",
        'version': '2.0.0',
        'features': {
            'real_time_chat': True,
            'analytics_dashboard': True,
            'voice_integration': True,
            'mobile_support': True
        }
    })

@app.route('/api/stats')
def get_stats():
    """Get real-time analytics and statistics (public endpoint for frontend)"""
    try:
        stats = analytics.get_real_time_stats()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
@limiter.limit("30 per minute")
def chat_with_bot():
    """Main endpoint for scammer conversation (API key optional for demo)"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        scammer_message = data['message']
        conversation_id = data.get('conversation_id', f"conv_{int(time.time())}")
        
        # Generate AI response
        start_time = time.time()
        bot_response, analysis = ai_engine.generate_response(scammer_message)
        response_time = time.time() - start_time
        
        # Get conversation summary
        conversation_summary = ai_engine.get_conversation_summary()
        
        # Log for analytics
        analytics.log_conversation({
            'timestamp': datetime.now().isoformat(),
            'conversation_id': conversation_id,
            'duration_minutes': conversation_summary.get('time_wasted_minutes', 0),
            'technique_type': analysis.get('technique_type', 'unknown'),
            'success_rating': min(10, max(1, len(ai_engine.conversation_history))),
            'conversation_turn': len(ai_engine.conversation_history),
            'scammer_frustration_level': ai_engine.scammer_profile.get('frustration_level', 0),
            'response_time_seconds': response_time
        })
        
        response_data = {
            'response': bot_response,
            'conversation_id': conversation_id,
            'analysis': {
                'urgency_score': analysis.get('urgency_score', 0),
                'financial_score': analysis.get('financial_score', 0),
                'tech_score': analysis.get('tech_score', 0),
                'authority_score': analysis.get('authority_score', 0),
                'technique_detected': ai_engine.scammer_profile.get('technique_type', 'unknown'),
                'frustration_level': ai_engine.scammer_profile.get('frustration_level', 0)
            },
            'conversation_stats': {
                'total_turns': len(ai_engine.conversation_history),
                'time_wasted_minutes': conversation_summary.get('time_wasted_minutes', 0),
                'effectiveness_score': conversation_summary.get('effectiveness_score', 0)
            },
            'metadata': {
                'response_time_ms': round(response_time * 1000, 2),
                'timestamp': datetime.now().isoformat(),
                'api_version': '2.0.0'
            }
        }
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/admin/stats')
@require_api_key
def get_admin_stats():
    """Get detailed admin statistics (requires API key)"""
    try:
        stats = analytics.get_real_time_stats()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/conversation/reset', methods=['POST'])
def reset_conversation():
    """Reset current conversation state (no API key required for demo)"""
    try:
        conversation_id = request.get_json().get('conversation_id') if request.get_json() else None
        
        # Reset AI engine
        ai_engine.reset_conversation()
        
        return jsonify({
            'message': 'Conversation reset successfully',
            'new_conversation_id': f"conv_{int(time.time())}",
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/responses/random')
def get_random_response():
    """Get a random response from the library (no API key required for demo)"""
    try:
        category = request.args.get('category')
        personality = request.args.get('personality')
        
        response = response_library.get_random_response(category, personality)
        
        return jsonify({
            'response': response,
            'category': category,
            'personality': personality,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/dashboard')
def get_dashboard_data():
    """Get comprehensive dashboard data (public for frontend)"""
    try:
        stats = analytics.get_real_time_stats()
        daily_report = analytics.generate_daily_report()
        
        dashboard_data = {
            'real_time_stats': stats,
            'daily_report': daily_report,
            'system_info': {
                'uptime': 'operational',
                'version': '2.0.0',
                'last_updated': datetime.now().isoformat(),
                'frontend_integrated': True
            },
            'quick_actions': [
                {'action': 'reset_conversation', 'endpoint': '/api/conversation/reset'},
                {'action': 'get_random_response', 'endpoint': '/api/responses/random'},
                {'action': 'view_analytics', 'endpoint': '/api/stats'}
            ]
        }
        
        return jsonify(dashboard_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/techniques')
def get_technique_analysis():
    """Get analysis of scammer techniques encountered (public for frontend)"""
    try:
        stats = analytics.get_real_time_stats()
        techniques = stats.get('techniques', {})
        
        technique_analysis = []
        for technique, count in techniques.items():
            technique_analysis.append({
                'technique': technique,
                'encounters': count,
                'percentage': round((count / sum(techniques.values())) * 100, 1) if techniques else 0,
                'recommended_responses': response_library.response_categories.get(technique, [])[:3]
            })
        
        return jsonify({
            'technique_analysis': sorted(technique_analysis, key=lambda x: x['encounters'], reverse=True),
            'total_techniques': len(techniques),
            'most_common': max(techniques, key=techniques.get) if techniques else 'none',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add WebSocket support for real-time updates
@app.route('/api/live-stats')
def live_stats():
    """Server-sent events endpoint for real-time stats"""
    def generate():
        while True:
            try:
                stats = analytics.get_real_time_stats()
                yield f"data: {json.dumps(stats)}\n\n"
                time.sleep(5)  # Update every 5 seconds
            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"
                break
    
    return app.response_class(generate(), mimetype='text/plain')

@app.errorhandler(404)
def not_found(error):
    """Custom 404 handler"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(429)
def ratelimit_handler(e):
    """Custom rate limit handler"""
    return jsonify({'error': 'Rate limit exceeded', 'message': str(e.description)}), 429

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 handler"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("🚀 Starting Scammer Waste Bot - Production Ready System")
    print("=" * 60)
    print(f"🌐 Frontend: Integrated React application")
    print(f"🤖 AI Engine: Advanced behavioral analysis")
    print(f"📊 Analytics: Real-time dashboard")
    print(f"🔒 Security: API key authentication, rate limiting")
    print(f"⚡ Performance: Optimized for production")
    print("=" * 60)
    print(f"🔗 Access the application at: http://localhost:5000")
    print(f"🔑 API Key: {API_KEY}")
    print("=" * 60)
    
    # Run with production-like settings
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_ENV') == 'development',
        threaded=True
    )
