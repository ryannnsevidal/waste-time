import random
from massive_responses import HOLD_MUSIC_RESPONSES

def handle():
    hearing_responses = [
        "Can you speak up, dear? I can't hear so well these days.",
        "What? Hold on, let me get my hearing aid...",
        "I'm sorry, the connection is terrible. Can you repeat that slowly?",
        "Speak louder! My TV is on and I can't find the remote.",
        "Wait, what did you say? I was feeding my cat.",
        "Can you hold on? I need to turn down my radio first.",
        "I can barely hear you. Are you calling from far away?",
        "Let me get my good ear closer to the phone...",
        "Can you spell that for me? My hearing isn't what it used to be.",
        "Hold on dear, let me get my neighbor - she has better hearing."
    ]
    
    # 40% chance of annoying hold music, 60% hearing problems
    if random.random() < 0.4:
        return random.choice(HOLD_MUSIC_RESPONSES)
    else:
        return random.choice(hearing_responses)
