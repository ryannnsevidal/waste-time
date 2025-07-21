from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS
from twilio_handler import handle_call
import os
import glob
import csv
from datetime import datetime, timedelta
import json

app = Flask(__name__, static_folder='static', static_url_path='')
# enable CORS for frontend communication
CORS(app)

# global state for active calls
active_calls = {}

@app.route('/')
def home():
    # serve react dashboard if static files exist, otherwise show basic info
    static_path = os.path.join(app.static_folder, 'index.html')
    
    if os.path.exists(static_path):
        return send_file(static_path)
    else:
        return '''
        <h1>waste time bot</h1>
        <p>bot is running and ready to waste scammer time 🤖👴</p>
        <p>endpoints:</p>
        <ul>
            <li><code>POST /voice</code> - twilio webhook for incoming calls</li>
            <li><code>GET /api/stats</code> - dashboard statistics</li>
            <li><code>POST /api/calls/:id/end</code> - end active call</li>
        </ul>
        <p><strong>✅ React dashboard is built and ready!</strong> Visit <a href="/dashboard">/dashboard</a> for the full interface.</p>
        '''

@app.route('/dashboard')
def dashboard():
    # explicit dashboard route
    if os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_file(os.path.join(app.static_folder, 'index.html'))
    else:
        return "Dashboard not available. Please build the React frontend first."

# catch-all route for react router
@app.route('/<path:path>')
def serve_react_app(path):
    # serve static files or fallback to index.html for SPA routing
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_file(os.path.join(app.static_folder, 'index.html'))
    else:
        return "File not found", 404

@app.route('/voice', methods=['POST'])
def voice():
    return handle_call()

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """get dashboard statistics for frontend"""
    try:
        # collect data from CSV files
        analytics_data = get_analytics_data()
        
        # calculate stats
        total_calls = len(analytics_data)
        total_time_wasted = sum(row.get('call_duration', 0) for row in analytics_data)
        successful_calls = len([row for row in analytics_data if row.get('success_score', 0) > 7])
        success_rate = (successful_calls / total_calls * 100) if total_calls > 0 else 0
        
        # format time
        hours = int(total_time_wasted // 3600)
        minutes = int((total_time_wasted % 3600) // 60)
        time_formatted = f"{hours}h {minutes}m"
        
        # estimate money saved (avg scam attempt = $500)
        money_saved = successful_calls * 500
        
        # recent calls data
        recent_calls = []
        for i, row in enumerate(analytics_data[-5:]):  # last 5 calls
            recent_calls.append({
                'id': f"call-{i+1}",
                'phoneNumber': row.get('caller_number', 'Unknown'),
                'duration': int(row.get('call_duration', 0)),
                'scamType': row.get('scam_type', 'Unknown'),
                'strategy': row.get('strategy_used', 'Confused Grandpa'),
                'timestamp': datetime.now() - timedelta(hours=i+1),
                'success': row.get('success_score', 0) > 7,
                'wastedTime': int(row.get('call_duration', 0))
            })
        
        # check for active calls
        current_call = None
        if len(active_calls) > 0:
            call_id = list(active_calls.keys())[0]
            call_data = active_calls[call_id]
            current_call = {
                'id': call_id,
                'phoneNumber': call_data.get('phone_number', 'Unknown'),
                'duration': int((datetime.now() - call_data.get('start_time', datetime.now())).total_seconds()),
                'status': 'active',
                'scamType': call_data.get('scam_type', 'Unknown'),
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
        print(f"error getting stats: {e}")
        # return default data if error
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
def end_call(call_id):
    """end an active call"""
    try:
        if call_id in active_calls:
            del active_calls[call_id]
            return jsonify({'status': 'success', 'message': 'call ended'})
        else:
            return jsonify({'status': 'error', 'message': 'call not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def get_analytics_data():
    """read analytics data from CSV files"""
    analytics_data = []
    
    # look for CSV files in analytics_data directory
    if os.path.exists('analytics_data'):
        csv_files = glob.glob('analytics_data/*.csv')
        
        for csv_file in csv_files:
            try:
                with open(csv_file, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # convert numeric fields
                        for field in ['call_duration', 'success_score', 'response_time', 'conversation_turns']:
                            if field in row and row[field]:
                                try:
                                    row[field] = float(row[field])
                                except:
                                    row[field] = 0
                        analytics_data.append(row)
            except Exception as e:
                print(f"error reading {csv_file}: {e}")
    
    return analytics_data

# helper function to track active calls
def start_call_tracking(call_id, phone_number, scam_type):
    """start tracking an active call"""
    active_calls[call_id] = {
        'phone_number': phone_number,
        'start_time': datetime.now(),
        'scam_type': scam_type
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # changed to 5001 to match frontend
