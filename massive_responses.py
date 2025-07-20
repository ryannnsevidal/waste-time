# tons of responses for different scammer scenarios
# organized by type so the ai can pick the best ones

import random
import time
from gift_card_numbers import get_gift_card_number_response, get_maximum_number_time_waste

# gift card scam responses (40+ ways to confuse them)
GIFT_CARD_RESPONSES = [
    # confusion about what gift cards are
    "Gift cards? Like Christmas cards? I already sent those out in July...",
    "A card that gives gifts? Does it wrap them too?",
    "Gift cards? I thought those were just pretty pictures on cardboard...",
    "Is that like a birthday card but fancier?",
    "Do I need to sign it? My handwriting is terrible these days...",
    
    # Wrong store confusion
    "Target? I don't have a target practice range anymore...",
    "Amazon? Like the rainforest? I've never been there...",
    "Walmart? Is that like a wall made of marts?",
    "Best Buy? I always try to buy the best, that's good advice...",
    "iTunes? I don't even know what a tune is anymore...",
    
    # Physical card confusion
    "Where do I put the gift? It's just a little card...",
    "How much gift can fit on such a small card?",
    "Do I need to shrink wrap the present first?",
    "Can I put my cat on the gift card? She's very small...",
    "I tried to put a sandwich on one once, it didn't work...",
    
    # Money/payment confusion
    "Can I pay with my bingo winnings?",
    "I only have Monopoly money, is that okay?",
    "My piggy bank is full of pennies from 1962...",
    "Can I trade my collection of bottle caps?",
    "I have some Confederate dollars in my sock drawer...",
    "Will they accept payment in chickens? I have 12 good layers...",
    "My grandson paid me in Pokemon cards once...",
    
    # Process confusion
    "Do I have to go to the store to get the card to give the gift?",
    "But if I give you the card, how do I give the gift?",
    "Wait, you want me to buy something to give you nothing?",
    "So I pay money to get a card to pay more money?",
    "This sounds like paying twice for the same thing...",
    "Can you explain this again? I'm getting confused...",
    
    # Physical limitations
    "I can't drive to the store, my license expired in 1987...",
    "The store is too far, can you come pick me up?",
    "My arthritis is acting up, can my neighbor Harold go for me?",
    "I'll have to wait for my grandson to visit next month...",
    "My seeing isn't good enough to read those tiny numbers...",
    
    # Time wasting tactics
    "Let me call the store first to make sure they have gift cards...",
    "I need to ask my neighbor if this is legitimate...",
    "Can you hold while I find my reading glasses? This might take a while...",
    "Let me get my checkbook... where did I put it?",
    "I need to call my bank to see if I have enough money...",
    "Hold on, my cat is stuck in the drapes again...",
    
    # Complete misunderstanding
    "A gift card for you? It's not even your birthday!",
    "Why would I give you a gift? I don't even know you...",
    "Shouldn't you be giving ME gifts? I'm the elder here...",
    "I usually only give gifts to family members...",
    "What did you do to deserve a gift from me?",
    "My deceased husband always said 'never give gifts to strangers'..."
]

# Hold Music Responses (Trap Queen inspired but copyright-safe)
HOLD_MUSIC_RESPONSES = [
    "*plays elevator music* 🎵 Do do do do... do do do do... 🎵",
    "*puts phone down* Oh wait, let me put on some music for you... *rustling sounds*",
    "*hums off-key* 🎵 La la la la... something about a queen... 🎵",
    "*radio static* Hold on dear, I'm trying to find a good station...",
    "*plays old jazz* 🎵 This was popular when I was young... 🎵",
    "*accordion music* 🎵 My neighbor Harold plays this at block parties... 🎵",
    "*plays polka* 🎵 This reminds me of my wedding dance... 🎵",
    "*humming* 🎵 My granddaughter plays something like this... what was it? 🎵",
    "*plays harmonica badly* 🎵 *wheeze wheeze* Sorry, I'm out of breath... 🎵",
    "*old radio show* 'And now back to our regularly scheduled programming...'",
    "*plays recorder off-key* 🎵 I'm learning this in my senior center class... 🎵",
    "*singing* 🎵 Something about cooking and cleaning, that's all I remember... 🎵"
]

# Tech Support Deep Responses (50+ variations)
TECH_SUPPORT_DEEP = [
    # Computer confusion
    "Computer? I thought that was a person who computed things...",
    "Is that the big beige box next to my television?",
    "Does it need to be plugged in? Mine's been unplugged since Christmas...",
    "The screen is black. Is it sleeping? Should I wake it up gently?",
    "There's a mouse but I don't see any cheese for it...",
    "My computer keeps asking for cookies but I already ate them all...",
    "It says 'Press any key' but I can't find the 'any' key...",
    "Windows? I have plenty of windows. Which one has the virus?",
    "The computer is making beeping sounds. Is it trying to talk to me?",
    "I think I broke it when I tried to clean the screen with soap and water...",
    
    # Virus misunderstanding  
    "A computer virus? Like the flu? Should I give it chicken soup?",
    "Can I catch the virus from my computer? I'm immunocompromised...",
    "Is this virus contagious? Should I warn my neighbors?",
    "Do I need to take my computer to the doctor?",
    "Should I put a mask on my computer?",
    "Can I give it some vitamin C to help fight the virus?",
    "My computer hasn't been coughing or sneezing though...",
    "Is there a vaccine for computer viruses?",
    "Should I quarantine my computer in the garage?",
    "Can I use hand sanitizer on the keyboard?",
    
    # Microsoft confusion
    "Microsoft? I thought that was a type of fabric softener...",
    "Are you related to Bill Gates? He seems like a nice young man...",
    "Microsoft... is that like macrohard?",
    "Do you work in that big building with all the windows?",
    "I use Apple computers. Do you know Johnny Appleseed?",
    "Microsoft Office? I don't have an office, just a kitchen table...",
    "Is Microsoft like regular soft but smaller?",
    "My grandson mentions Microsoft all the time. Are you his friend?",
    
    # Remote access confusion
    "Remote? Like my TV remote? It needs new batteries...",
    "How can you access my computer remotely? Do you have really long arms?",
    "Remote access? Are you calling from very far away?",
    "Can you see through my windows from where you are?",
    "Remote control? I can barely control my own life...",
    "Is this like those remote control airplanes kids play with?",
    "Remote access sounds expensive. How much does the remote cost?",
    "If you're remote, how do I know you're really there?",
    
    # Error message confusion
    "Error messages? Let me read them to you... E-R-R... what comes next?",
    "The error message says 'Error 404'. Is that an address?",
    "It says 'Page not found'. I didn't lose any pages...",
    "The message says 'Fatal error'. Oh my! Is someone hurt?",
    "Blue screen? My screen isn't blue, it's beige...",
    "It says 'System failure'. Did my whole system fail at life?",
    "The error says 'Access denied'. That's very rude of my computer...",
    "It keeps saying 'OK' but nothing is OK about this situation..."
]

# IRS/Authority Deep Responses (40+ variations)
IRS_AUTHORITY_DEEP = [
    # IRS confusion
    "The IRS? Is that the IRS-A or IRS-B? I always get them confused...",
    "Internal Revenue Service? What's so internal about it?",
    "I thought the IRS was just a myth, like Bigfoot...",
    "Are you calling from that big building in Washington?",
    "IRS? I thought that stood for 'I Really Suck' at taxes...",
    "Do you know my tax preparer? His name is Harold...",
    
    # Social Security confusion
    "Social Security suspended? But I just got my check yesterday...",
    "How can my number be suspended? It's just a number...",
    "Did someone else try to use my social security? That's identity theft!",
    "My social security number is older than you are, young man...",
    "Suspended like a bridge? Will it fall down?",
    "Can I get a new social security number? Maybe a smaller one?",
    
    # Legal threats confusion
    "Arrest me? I'm 87 years old! What am I going to do, shuffle away menacingly?",
    "Legal action? Is that like illegal action but opposite?",
    "Jail time? Do they have senior discounts at jail?",
    "Court appearance? I don't like appearing in public anymore...",
    "Warrant? Like a warranty? Did my existence expire?",
    "Federal charges? That sounds expensive. Who pays for federal things?",
    
    # Payment demand confusion
    "Pay immediately? It's Sunday and all the banks are closed...",
    "Back taxes? I thought once you paid taxes they stayed paid...",
    "Outstanding taxes? Mine were pretty mediocre, not outstanding...",
    "Tax lien? What's a lien? Is it like lying down?",
    "Penalty fees? What did I do wrong? I've been very good...",
    "Interest charges? I'm not that interesting anymore...",
    
    # Badge/authority confusion
    "Badge number? Can you describe the badge? What color is it?",
    "Agent Smith? Like in that movie with the sunglasses?",
    "Federal agent? Do you get federal holidays off?",
    "Can you show me your badge through the phone?",
    "What's your supervisor's name? Is it also Harold?",
    "Department of Treasury? Do you know where the treasure is buried?"
]

# Romance/Inheritance Deep Responses (35+ variations)
ROMANCE_INHERITANCE_DEEP = [
    # Nigerian prince responses
    "A prince? My late husband was a king... well, King of the local bowling league...",
    "Nigeria? I had a pen pal from there in 1962. Do you know Mildred Johnson?",
    "Prince? Do you have a crown? Can you describe it?",
    "Nigerian royalty? What's the exchange rate on Nigerian dollars?",
    "Are you related to the Queen of England? She seems nice...",
    
    # Inheritance confusion
    "Inheritance? My uncle died and left me his collection of bottle caps...",
    "Millions? In what currency? I hope it's American dollars...",
    "Distant relative? How distant? Are we talking miles or years?",
    "Family fortune? My family's fortune was three chickens and a goat...",
    "Estate? I live in a mobile home, is that an estate?",
    "Will and testament? I have a will but it's mostly about my cat...",
    
    # Gold/money confusion
    "Gold? I have some dental work that might be worth something...",
    "Bars of gold? Like granola bars? Those are delicious...",
    "Safety deposit box? Is that like a safe but more polite?",
    "Bank transfer? I keep my money in coffee cans buried in the yard...",
    "Account number? I lost count after twelve...",
    "Routing number? Is that like directions to my house?",
    
    # Romance scam responses
    "Love? That's sweet dear, but I'm married to my recliner now...",
    "Soldier deployed? My grandson is in the Boy Scouts, is that the same?",
    "Visa problems? Like the credit card? I cut mine up after watching the news...",
    "Beautiful photos? I can't see them through the phone...",
    "Meet in person? I don't go out after 4 PM anymore...",
    "True love? I found that once, his name was Herbert..."
]

def get_response_by_category(category, subcategory=None):
    """Get a random response from a specific category"""
    
    categories = {
        'gift_cards': GIFT_CARD_RESPONSES,
        'hold_music': HOLD_MUSIC_RESPONSES, 
        'tech_support': TECH_SUPPORT_DEEP,
        'irs_authority': IRS_AUTHORITY_DEEP,
        'romance_inheritance': ROMANCE_INHERITANCE_DEEP
    }
    
    if category in categories:
        return random.choice(categories[category])
    else:
        # Fallback to any random response
        all_responses = []
        for responses in categories.values():
            all_responses.extend(responses)
        return random.choice(all_responses)

def get_contextual_response(scammer_input=""):
    """Get contextually appropriate response with deep variety"""
    
    scammer_lower = scammer_input.lower()
    
    # Gift card NUMBER requests (most specific)
    if any(phrase in scammer_lower for phrase in ['read the numbers', 'card numbers', 'code on the card', 'scratch off', 'activation code', 'card code']):
        return get_gift_card_number_response()
    
    # Gift card keywords (general)
    elif any(word in scammer_lower for word in ['gift card', 'target', 'walmart', 'amazon', 'itunes', 'visa', 'prepaid']):
        return get_response_by_category('gift_cards')
    
    # Tech support keywords
    elif any(word in scammer_lower for word in ['computer', 'virus', 'microsoft', 'windows', 'technical', 'support', 'remote']):
        return get_response_by_category('tech_support')
        
    # IRS/authority keywords
    elif any(word in scammer_lower for word in ['irs', 'tax', 'arrest', 'police', 'government', 'social security', 'legal']):
        return get_response_by_category('irs_authority')
        
    # Romance/inheritance keywords
    elif any(word in scammer_lower for word in ['prince', 'love', 'inheritance', 'gold', 'nigeria', 'soldier', 'money']):
        return get_response_by_category('romance_inheritance')
    
    # Hold music trigger words
    elif any(word in scammer_lower for word in ['hold', 'wait', 'music', 'pause']):
        return get_response_by_category('hold_music')
        
    # Default to random from any category
    else:
        return get_response_by_category(random.choice(['gift_cards', 'tech_support', 'irs_authority', 'romance_inheritance']))

# Special combination responses for maximum time wasting
COMBO_RESPONSES = [
    "Hold on, let me put on some music while I get my gift cards... 🎵 *humming* 🎵 Now what was the question?",
    "Gift cards? *plays hold music* 🎵 La la la 🎵 Sorry, what Microsoft problem were we talking about?",
    "IRS? Let me get my tax papers... *elevator music* 🎵 This might take 20 minutes... 🎵",
    "Prince from Nigeria? *plays polka music* 🎵 That reminds me of my wedding... what inheritance? 🎵",
    "Read the numbers? Let me find my magnifying glass first... 🎵 *trap queen inspired humming* 🎵 ...what numbers were we talking about?"
]

def get_maximum_time_waster():
    """Get the most time-wasting response possible"""
    # 30% chance of specialized number time waste, 70% regular combo
    if random.random() < 0.3:
        return get_maximum_number_time_waste()
    else:
        return random.choice(COMBO_RESPONSES)
