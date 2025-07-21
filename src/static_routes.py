"""
Static file serving and frontend integration
"""
from flask import Blueprint, send_from_directory, request, current_app
import os
import mimetypes

static_bp = Blueprint('static', __name__)

@static_bp.route('/')
def index():
    """Serve the main React application"""
    return send_from_directory('/workspaces/waste-time/data/static', 'index.html')

@static_bp.route('/assets/<path:filename>')
def assets(filename):
    """Serve React build assets with proper MIME types"""
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

@static_bp.route('/favicon.ico')
def favicon():
    """Serve favicon"""
    return send_from_directory('/workspaces/waste-time/data/static', 'favicon.ico')

@static_bp.route('/<path:path>')
def catch_all(path):
    """Catch all routes and serve React app (for client-side routing)"""
    # If it's an API route, don't serve static files
    if path.startswith('api/'):
        return {'error': 'API endpoint not found'}, 404
    
    # For all other routes, serve the React app
    return send_from_directory('/workspaces/waste-time/data/static', 'index.html')
