# Scammer Waste Bot

## Overview
Automated system designed to intercept fraudulent phone calls and implement strategic time-wasting protocols through conversational AI simulation, thereby reducing scammer efficiency and protecting legitimate targets.

## Core Features
- AI-powered conversation analysis and scam detection
- Real-time dashboard with comprehensive analytics
- Twilio integration for seamless call handling
- CSV data export for detailed analysis
- Docker deployment capabilities
- Advanced time-wasting conversation strategies

## System Operation
- Flask application monitors incoming calls through Twilio integration
- AI engine analyzes caller patterns to identify fraud attempts
- System deploys appropriate conversational responses to maximize call duration
- Comprehensive time tracking and analytics provide performance metrics
- Real-time statistics monitor effectiveness and operational status

## Docker Deployment Options

### Automated Deployment
```bash
./deploy.sh
```
Select option 1 for development environment or option 2 for production deployment

### Manual Docker Configuration
```bash
# Development deployment (dashboard accessible on port 5001)
docker-compose up --build -d

# Production deployment (with nginx reverse proxy on port 80)
docker-compose --profile production up --build -d
```

### Testing Deployment
```bash
docker-compose up --build -d
./test-deployment.sh
```

## Local Development Environment
1. Copy config_template.py to config.py and configure production API keys
2. Install dependencies: `pip install -r requirements.txt`
3. Launch application: `python app.py`
4. Configure ngrok tunnel: `ngrok http 5000`
5. Set Twilio webhook endpoint to ngrok URL with `/voice` path

## Docker Implementation
For containerized deployment, execute `docker-compose up --build`
Application will be accessible at http://localhost:5001

## Backend Testing Protocols

### Flask API Testing
```bash
# Test primary endpoint
curl http://localhost:5001/

# Test with active Docker container
curl http://localhost:5001/
```

### AI Engine Validation
```python
# Test individual scammer analysis functionality
from sophisticated_engine import get_sophisticated_response

result = get_sophisticated_response("You need to buy gift cards NOW!")
print(f"Strategy: {result['strategy']}")
print(f"Time waste: {result['estimated_time_waste']}s")
print(f"Response: {result['response']}")
```

### Comprehensive Testing Suite
Execute the sophisticated demo for complete AI system validation:
```bash
python sophisticated_demo.py
```

This provides testing options for:
1. **Advanced scammer profiling** - Comprehensive analysis of scammer behavior patterns
2. **ML strategy optimization** - Machine learning powered response optimization  
3. **Real-time conversation analyzer** - Live metrics and performance tracking
4. **Full analytics suite** - Complete testing with comprehensive reporting

## CSV Analytics and Data Export

### Automated CSV Logging
The AI engine automatically logs all conversations to CSV files:
- Files saved to `analytics_data/scammer_analysis_YYYYMMDD.csv`
- Includes timestamps, scammer input, AI strategy used, response previews
- Tracks urgency scores, authority claims, payment scam detection
- Measures time waste effectiveness and frustration levels

### CSV Data Structure
```csv
timestamp,scammer_input,strategy,response_preview,urgency_score,authority_score,payment_score,info_score,frustration_score,threat_score,caps_ratio,exclamation_count,estimated_time_waste,total_time_wasted,scammer_frustration,is_high_urgency,is_authority_claim,is_payment_scam,is_info_phishing,is_threatening
```

### Manual CSV Export from Demos
```python
from sophisticated_demo import AdvancedAnalytics

analytics = AdvancedAnalytics()
# run tests...
filename = analytics.export_to_csv()
print(f"Data exported to: {filename}")
```

### Data Privacy Protocol
- All CSV files are automatically excluded from version control
- Analytics data remains local and is never committed to GitHub
- Files stored in `analytics_data/` directory with restricted access

## Advanced AI Features
The AI engine includes:
- **Scammer type detection** - Identifies IRS, tech support, gift card scams
- **Frustration tracking** - Measures scammer emotional state over time
- **Strategy optimization** - Selects optimal time-wasting responses
- **Threat analysis** - Detects when scammers make legal threats
- **Urgency scoring** - Measures caller desperation levels
- **Payment scam detection** - Identifies gift card and wire transfer requests

## Project Architecture
```
├── app.py                    # Main Flask application
├── sophisticated_engine.py   # AI analysis and response generation
├── sophisticated_demo.py     # Advanced testing suite with analytics
├── massive_responses.py      # Database of conversational responses
├── gift_card_numbers.py      # Simulated gift card numbers
├── twilio_handler.py         # Phone call integration
├── analytics_data/           # CSV files (excluded from version control)
└── static/                   # Hold music and assets
```
