import random

def handle():
    responses = [
        "You know, back in my day we used to ride turtles to school.",
        "That reminds me of the time I fought a bear with my bare hands...",
        "Speaking of that, did I tell you about my prize-winning tomatoes?",
        "This weather has been terrible lately, don't you think?",
        "You sound like my grandson Billy. He's in college studying basket weaving.",
        "Hold on, my cat is trying to tell me something important...",
        "Let me tell you about my hip replacement surgery...",
        "Back in 1962, I once caught a fish THIS big...",
        "My arthritis is acting up something fierce today...",
        "Do you know my neighbor Harold? He has one of those computer things too.",
        "I was just making some soup. Do you like soup?",
        "The birds outside are being very noisy today..."
    ]
    return random.choice(responses)
