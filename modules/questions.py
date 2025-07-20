import random

def handle():
    responses = [
        "What's your mother's maiden name? I just need to verify...",
        "Can I get your badge number? I need to write this down.",
        "What's your supervisor's name? Let me speak to them first.",
        "How do I know you're really from the government?",
        "What company did you say you're from again?",
        "Can you hold while I get my grandson? He handles all my business.",
        "What's your employee ID number?",
        "Do you have a website? I want to look you up online.",
        "Can you send me something in writing first?",
        "What's your direct phone number so I can call you back?",
        "Are you calling from India? You sound foreign.",
        "Let me get my neighbor Harold - he knows about these things."
    ]
    return random.choice(responses)
