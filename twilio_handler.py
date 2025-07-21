from flask import request, Response
from utils.whisper_api import transcribe
from utils.audio_utils import prepare_audio_response
from modules import hearing, questions, tangents, crypto
from massive_responses import get_contextual_response, get_maximum_time_waster
from sophisticated_engine import get_sophisticated_response, SophisticatedResponseEngine
import random

def handle_call():
    # get caller info from twilio
    caller_phone = request.form.get('From', 'Unknown')
    
    # Get any speech input from the call (currently mocked)
    transcript = transcribe('dummy.wav')
    
    # Try to get actual input from Twilio if available
    speech_input = request.form.get('SpeechResult', '') or transcript
    
    # 50% chance of using sophisticated AI response engine
    if random.random() < 0.5 and speech_input and speech_input != 'Mock transcription: Hello, I\'m calling about your account.':
        # Use sophisticated response engine with caller info for real input
        try:
            # create engine instance with caller phone for tracking
            engine = SophisticatedResponseEngine(caller_phone=caller_phone)
            result = engine.generate_response(speech_input)
            reply_text = result['response']
            
            # Add metadata as HTML comment for debugging
            metadata = f"<!-- Strategy: {result['strategy']}, Time Waste: {result['estimated_time_waste']}s, Caller: {caller_phone} -->"
        except Exception as e:
            print(f"sophisticated engine failed: {e}")
            # fallback to old method
            result = get_sophisticated_response(speech_input)
            reply_text = result['response']
            metadata = f"<!-- Fallback Strategy: {result['strategy']}, Time Waste: {result['estimated_time_waste']}s -->"
        
    else:
        # Fallback to original system
        # 10% chance of maximum time waster combo response
        if random.random() < 0.1:
            reply_text = get_maximum_time_waster()
        # 30% chance of contextual response based on transcript
        elif random.random() < 0.3:
            reply_text = get_contextual_response(speech_input)
        # 60% chance of regular module response
        else:
            modules = [hearing, questions, tangents, crypto]
            chosen_module = random.choice(modules)
            reply_text = chosen_module.handle()
        
        metadata = f"<!-- Basic response system, Caller: {caller_phone} -->"
    
    # Prepare audio response (currently not implemented)
    audio_stream = prepare_audio_response(reply_text)
    
    # Return TwiML response
    twiml = f'{metadata}<Response><Say>{reply_text}</Say></Response>'
    return Response(twiml, mimetype='text/xml')
