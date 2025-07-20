# waste time bot

## what this does
picks up scammer calls and pretends to be confused grandpa to waste their time so they cant scam real people

## how it works
- flask app waits for calls from twilio
- when scammers call it uses ai to figure out what scam theyre running
- responds with appropriate confused grandpa responses  
- keeps them on the phone as long as possible
- tracks total time wasted

## tech stuff
- python flask backend
- openai for smart responses and voice transcription
- elevenlabs for text to speech
- twilio handles the actual phone calls
- slack notifications when calls come in

## setup
1. copy config_template.py to config.py and add your real api keys
2. install stuff: `pip install -r requirements.txt`
3. run it: `python app.py`
4. use ngrok to expose port: `ngrok http 5000`
5. set twilio webhook to your ngrok url + `/voice`

## docker version
if you want to use docker just run `docker-compose up --build`
the app will be available at http://localhost:5001

## backend testing options

### testing the flask api
```bash
# test main endpoint
curl http://localhost:5001/

# test with docker running
curl http://localhost:5001/
```

### testing the sophisticated ai engine
```python
# test individual scammer analysis
from sophisticated_engine import get_sophisticated_response

result = get_sophisticated_response("You need to buy gift cards NOW!")
print(f"Strategy: {result['strategy']}")
print(f"Time waste: {result['estimated_time_waste']}s")
print(f"Response: {result['response']}")
```

### advanced testing suite
run the sophisticated demo for comprehensive ai testing:
```bash
python sophisticated_demo.py
```

this gives you options for:
1. **advanced scammer profiling** - deep analysis of scammer behavior patterns
2. **ml strategy optimization** - machine learning powered response optimization  
3. **real-time conversation analyzer** - live metrics and performance tracking
4. **full analytics suite** - runs all tests with comprehensive reporting

## csv analytics & data export

### automatic csv logging
the engine automatically logs all conversations to csv files:
- files saved to `analytics_data/scammer_analysis_YYYYMMDD.csv`
- includes timestamps, scammer input, ai strategy used, response previews
- tracks urgency scores, authority claims, payment scam detection
- measures time waste effectiveness and frustration levels

### csv data structure
```csv
timestamp,scammer_input,strategy,response_preview,urgency_score,authority_score,payment_score,info_score,frustration_score,threat_score,caps_ratio,exclamation_count,estimated_time_waste,total_time_wasted,scammer_frustration,is_high_urgency,is_authority_claim,is_payment_scam,is_info_phishing,is_threatening
```

### manual csv export from demos
```python
from sophisticated_demo import AdvancedAnalytics

analytics = AdvancedAnalytics()
# run tests...
filename = analytics.export_to_csv()
print(f"Data exported to: {filename}")
```

### data privacy
- all csv files are automatically gitignored
- analytics data stays local and is never committed to github
- files stored in `analytics_data/` directory

## sophisticated ai features
the ai engine includes:
- **scammer type detection** - identifies irs, tech support, gift card scams
- **frustration tracking** - measures scammer anger levels over time
- **strategy optimization** - picks best time-wasting responses
- **threat analysis** - detects when scammers make legal threats
- **urgency scoring** - measures how desperate scammers sound
- **payment scam detection** - identifies gift card and wire transfer requests

## file structure
```
├── app.py                    # main flask application
├── sophisticated_engine.py   # ai analysis and response generation
├── sophisticated_demo.py     # advanced testing suite with analytics
├── massive_responses.py      # database of grandpa responses
├── gift_card_numbers.py      # fake gift card numbers
├── twilio_handler.py         # phone call integration
├── analytics_data/           # csv files (gitignored)
└── static/                   # hold music and assets
```
