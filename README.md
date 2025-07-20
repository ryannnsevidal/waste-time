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

## advanced testing & analytics
run `python sophisticated_demo.py` for the advanced ai testing suite with:
- deep learning scammer behavior profiling
- ml-powered strategy optimization 
- real-time conversation analysis with live metrics
- comprehensive performance analytics and scoring
- sophisticated threat detection and response optimization

the sophisticated_engine.py file has all the ai logic for analyzing scammer tactics and dynamically selecting optimal time-wasting responses based on machine learning insights
