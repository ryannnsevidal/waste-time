"""
Gift Card Number Confusion Responses
Specialized responses for when scammers ask for gift card codes/numbers
"""

import random
import time

# Responses when scammer asks for gift card numbers/codes
GIFT_CARD_NUMBER_RESPONSES = [
    # Reading wrong numbers
    "Let me read you the numbers... 1... 2... 3... 4... wait, that's my house number...",
    "The numbers are... hold on... B-I-N-G-O... wait, that's letters...",
    "It says... 'Expires 12/99'... that seems old, is that okay?",
    "The number is... let me get my magnifying glass... this might take a while...",
    "It says 'Scratch off to reveal'... do I use a coin or my fingernail?",
    "The numbers are very small... 8008135... wait, that spells something funny...",
    
    # Physical card problems
    "I scratched too hard and tore the card... can you still use half numbers?",
    "My cat sat on the card and it's all wrinkled now...",
    "I spilled coffee on it... can you still read wet numbers?",
    "The card fell behind my refrigerator... can you wait while I get a broom?",
    "I accidentally put it in the washing machine... the numbers are all faded...",
    "My neighbor Harold borrowed it to clean his glasses...",
    
    # Confusion about which numbers
    "Which numbers? There are so many numbers on this card...",
    "Do you want the big numbers or the little numbers?",
    "There's a number on the front and back... which one matters?",
    "Some numbers are shiny and some are flat... which type do you need?",
    "It has my birthday on it... wait, that's my driver's license...",
    
    # Reading very slowly with interruptions
    "The first number is... 4... wait, my phone is ringing... sorry, what were we doing?",
    "3... 7... 9... hold on, someone's at the door... I'll be right back...",
    "Let me read them slowly so you get them right... 2... *cough*... sorry, allergies...",
    "The numbers are... oh wait, my cat is doing something cute... where was I?",
    "First digit is... actually, can you hold? My soap opera is starting...",
    
    # Giving completely wrong information
    "The activation code is 'BANANA'... wait, that's my WiFi password...",
    "It says the PIN is 1234... that's also my safe combination...",
    "The security code is my Social Security number... wait, you're not supposed to ask for that!",
    "The numbers are... actually, let me call the store to make sure this is legitimate...",
    "Hold on, my grandson said never give these numbers to strangers...",
    
    # Time-wasting tactics with numbers
    "I need to write this down... where did I put my pen? This could take 20 minutes...",
    "Let me call my neighbor to double-check I'm reading this right...",
    "I should probably put on my good glasses first... they're upstairs...",
    "Can you explain what you're going to do with these numbers first?",
    "My neighbor Harold says this might be a scam... can you prove you're legitimate?",
    
    # Physical limitations preventing number reading
    "My eyesight isn't good enough to read these tiny numbers...",
    "The lighting in here is terrible... can you call back during daylight?",
    "My hands are shaking too much to hold the card steady...",
    "I can't find my reading glasses... they might be in my car...",
    "These numbers are smaller than the print in my medicine bottles...",
    
    # Creating fake urgency/problems
    "Oh no! The numbers are disappearing! Is that supposed to happen?",
    "The card is making a beeping sound... is it supposed to do that?",
    "Some of the numbers fell off... can you send me new ones?",
    "The card expired while I was reading it... does that matter?",
    "My neighbor says these cards are radioactive... is that true?"
]

# Hold responses specifically for when reading numbers
NUMBER_READING_HOLDS = [
    "*puts phone down* Let me get my magnifying glass... 🎵 *humming* 🎵",
    "*long pause* Sorry, I was looking for my reading glasses... 🎵 *elevator music* 🎵",
    "*rustling sounds* I'm trying to find better lighting... 🎵 *old jazz* 🎵",
    "*muffled* Harold! Can you help me read this? 🎵 *polka music* 🎵",
    "*sound of papers shuffling* Where did I put that card... 🎵 *radio static* 🎵"
]

def get_gift_card_number_response():
    """Get a response when scammer asks for gift card numbers"""
    
    # 20% chance of hold music, 80% confusion
    if random.random() < 0.2:
        return random.choice(NUMBER_READING_HOLDS)
    else:
        return random.choice(GIFT_CARD_NUMBER_RESPONSES)

def simulate_number_reading_disaster():
    """Simulate a complete disaster when trying to read gift card numbers"""
    
    responses = [
        "Okay, let me read the numbers... wait, which side of the card?",
        "*long pause* Sorry, I dropped my glasses...",
        "The first number is... actually, is this the right card?",
        "*sound of papers rustling* I think I grabbed my grocery receipt instead...",
        "Let me start over... the numbers are... oh, my cat just knocked over my coffee...",
        "*phone gets muffled* Harold! Come help me with this electronic thing!",
        "Sorry about that... now where were we? Oh yes, the numbers...",
        "*long pause* I think I need to call my grandson about this..."
    ]
    
    return responses

# Responses that waste maximum time when asked for numbers
MAX_TIME_WASTE_NUMBERS = [
    "Let me get my special number-reading glasses... they're in my bedroom... upstairs... this might take a while... 🎵 *plays hold music* 🎵",
    "Oh, I need to call the store first to make sure these numbers are still good... can you hold for about 30 minutes? 🎵 *elevator music* 🎵",
    "I should probably have my neighbor Harold verify these numbers are correct... he's very good with numbers... let me go get him... 🎵 *polka music* 🎵",
    "Wait, my grandson told me never to give these numbers over the phone... let me call him first to ask permission... he's at work so this might take a while... 🎵 *jazz music* 🎵"
]

def get_maximum_number_time_waste():
    """Get the most time-wasting response for number requests"""
    return random.choice(MAX_TIME_WASTE_NUMBERS)
