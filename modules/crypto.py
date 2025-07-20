import random
from massive_responses import GIFT_CARD_RESPONSES

def handle():
    # mix crypto responses with gift card confusion
    crypto_responses = [
        "I only use CrankshaftCoin or Fentcoin, none of that PayPal stuff.",
        "Bitcoin? Is that like Chuck E. Cheese tokens?",
        "Can I pay with Confederate dollars? I have a whole shoebox full.",
        "I keep my money in mason jars buried in the backyard.",
        "Do you accept payment in chickens? I have 12 good layers.",
        "What about Green Stamps? I've been collecting them since 1965.",
        "Can I write you a check? Let me find my checkbook...",
        "I only deal in cash. Can you come pick it up?",
        "My bank is the First National Bank of Under My Mattress.",
        "I use the barter system. I'll trade you 3 turnips for that service.",
        "Let me call my financial advisor... Harold! Get over here!",
        "Can I pay you in bottle caps? They're going to be worth something someday."
    ]
    
    # 70% chance of gift card response, 30% crypto response  
    if random.random() < 0.7:
        return random.choice(GIFT_CARD_RESPONSES)
    else:
        return random.choice(crypto_responses)
