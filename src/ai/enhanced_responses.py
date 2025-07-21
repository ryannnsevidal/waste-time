"""
Enhanced Response Library for Scammer Waste Bot
Massive collection of realistic elderly responses
"""
import random
from typing import List, Dict

class EnhancedResponses:
    """Enhanced response generation with personality variants"""
    
    def __init__(self):
        self.personality_types = {
            'confused_grandpa': {
                'name': 'Harold',
                'age': 78,
                'characteristics': ['forgetful', 'friendly', 'easily_distracted'],
                'common_phrases': [
                    "Back in my day...",
                    "My grandson usually helps me with this...",
                    "I don't understand these newfangled things...",
                    "Hold on, let me find my glasses...",
                    "What was that? I was watching the news..."
                ]
            },
            'suspicious_grandma': {
                'name': 'Ethel',
                'age': 82,
                'characteristics': ['cautious', 'sharp', 'experienced'],
                'common_phrases': [
                    "That sounds fishy to me...",
                    "I've heard about scams like this...",
                    "My neighbor warned me about these calls...",
                    "I think I should hang up and call you back...",
                    "How do I know you're really who you say you are?"
                ]
            },
            'chatty_senior': {
                'name': 'Martha',
                'age': 75,
                'characteristics': ['talkative', 'lonely', 'story_telling'],
                'common_phrases': [
                    "Oh, that reminds me of a story...",
                    "Speaking of that, my late husband used to say...",
                    "I was just talking to my friend about this...",
                    "You know, when I was your age...",
                    "That's interesting. Have I told you about my cats?"
                ]
            }
        }
        
        self.response_categories = {
            'technology_confusion': self._get_tech_responses(),
            'financial_hesitation': self._get_financial_responses(),
            'family_stories': self._get_family_responses(),
            'health_distractions': self._get_health_responses(),
            'neighbor_gossip': self._get_neighbor_responses(),
            'memory_issues': self._get_memory_responses(),
            'authority_questions': self._get_authority_responses(),
            'time_wasting': self._get_time_wasting_responses()
        }
    
    def _get_tech_responses(self) -> List[str]:
        """Technology confusion responses"""
        return [
            "I don't know anything about computers. I still use a rotary phone.",
            "My computer is making strange noises. Is that normal?",
            "I clicked on something and now there are pop-ups everywhere.",
            "Do I need to unplug it and plug it back in? That's what my grandson says.",
            "I still have Windows 95. Is that the problem?",
            "What's a browser? Is that like Internet Explorer?",
            "I only know how to check my email. Everything else confuses me.",
            "My computer screen went blue. Does that mean it's broken?",
            "I don't understand passwords. I write them all down on sticky notes.",
            "Can you help me find the 'any' key? I can't seem to locate it.",
            "Is WiFi the same as the internet? I'm not sure what I have.",
            "My grandson set this up for me. I don't know what he did.",
            "I accidentally deleted something important. Can you help me get it back?",
            "The computer keeps asking me to update things. Should I say yes?",
            "I'm afraid I'll break something if I click the wrong button."
        ]
    
    def _get_financial_responses(self) -> List[str]:
        """Financial hesitation and confusion responses"""
        return [
            "I need to check with my son. He handles all my financial matters now.",
            "My bank is closed until Monday. Can we do this then?",
            "I don't do online banking. I prefer to go to the branch in person.",
            "How much money are we talking about? I keep most of it in coffee cans.",
            "My Social Security check doesn't come until the 3rd of the month.",
            "I'm on a fixed income. I can't afford to lose any money.",
            "The bank froze my account last week. Something about suspicious activity.",
            "I don't have a credit card. I pay for everything with cash or check.",
            "My late husband always handled the finances. I'm still learning.",
            "I need to ask my daughter first. She's my power of attorney.",
            "Can I pay with a money order? I don't trust these electronic things.",
            "I have about $50 in my checking account. Is that enough?",
            "My pension doesn't cover much these days. Everything's so expensive.",
            "I'm worried about identity theft. Are you sure this is safe?",
            "Let me call my bank first to make sure this is legitimate."
        ]
    
    def _get_family_responses(self) -> List[str]:
        """Family-related distractions and stories"""
        return [
            "Hold on, my daughter is calling on the other line.",
            "My grandchildren are visiting this week. It's quite chaotic here.",
            "I need to check on my husband. His Alzheimer's is getting worse.",
            "My son is coming over later to help me with this computer stuff.",
            "My daughter warned me about calls like this. She's very protective.",
            "I have to pick up my granddaughter from school in an hour.",
            "My neighbor's cat got into my yard again. Such a nuisance.",
            "I'm expecting the doctor to call about my test results.",
            "My bridge club is coming over in a few minutes.",
            "I need to start dinner soon. My husband gets cranky when he's hungry.",
            "My grandson is in college studying computers. Maybe I should ask him.",
            "My daughter works at a bank. She might know about this.",
            "I'm babysitting my great-grandchildren today. They're so energetic.",
            "My son is a lawyer. He always tells me to be careful about these things.",
            "My late husband would have known what to do. I miss his advice."
        ]
    
    def _get_health_responses(self) -> List[str]:
        """Health-related distractions and concerns"""
        return [
            "I'm sorry, I need to take my medication. Can you hold on?",
            "My arthritis is acting up today. It's hard to type.",
            "I have a doctor's appointment in an hour. Can we make this quick?",
            "My hearing isn't what it used to be. Could you speak louder?",
            "I need to check my blood sugar. Diabetes, you know.",
            "My eyes are getting tired. These screens are too bright.",
            "I have to use the bathroom. When you get to my age...",
            "My back is killing me from sitting too long. Let me stand up.",
            "I need to find my reading glasses. I can't see anything without them.",
            "My heart medication makes me dizzy sometimes. Give me a moment.",
            "I have to eat something. My blood sugar is getting low.",
            "This phone call is giving me a headache. Can we continue later?",
            "I need to lie down for a bit. My blood pressure is acting up.",
            "My memory isn't what it used to be. Can you repeat that?",
            "I get confused easily since my stroke. Please be patient with me."
        ]
    
    def _get_neighbor_responses(self) -> List[str]:
        """Neighbor gossip and community distractions"""
        return [
            "My neighbor just told me about a scam exactly like this.",
            "The lady next door said never to give out personal information.",
            "There's been a lot of crime in the neighborhood lately.",
            "My neighbor's package was stolen yesterday. People can't be trusted.",
            "The mailman warned us about suspicious phone calls.",
            "Someone at the senior center mentioned this type of fraud.",
            "My neighbor's cousin got scammed out of $500 last month.",
            "The police came to our neighborhood meeting about phone scams.",
            "My bridge partner said her brother-in-law got fooled by something similar.",
            "There's been a lot of talk at church about these phone calls.",
            "My neighbor works at the bank and warned me about this.",
            "The lady across the street fell for something like this last year.",
            "Everyone in my building has been getting these calls.",
            "My neighbor's dog is barking again. Something must be wrong.",
            "I should ask my neighbor what she thinks about this."
        ]
    
    def _get_memory_responses(self) -> List[str]:
        """Memory-related confusion and delays"""
        return [
            "I'm sorry, what were we talking about? I got distracted.",
            "Could you repeat that? I didn't catch what you said.",
            "Hold on, let me write this down so I don't forget.",
            "What company did you say you were from again?",
            "I'm having trouble remembering. Can you start over?",
            "My memory isn't what it used to be. Please be patient.",
            "I wrote something down, but I can't find where I put it.",
            "Wait, did I already give you that information?",
            "I'm getting confused. Can you explain this more slowly?",
            "Let me think about this. My mind is a bit foggy today.",
            "I need to call you back. I can't remember what we were discussing.",
            "Can you hold on while I find my notes from our last conversation?",
            "I'm sorry, did we talk before? I don't remember.",
            "My son usually helps me remember important things.",
            "I need to write this down, but I can't find a pen."
        ]
    
    def _get_authority_responses(self) -> List[str]:
        """Questioning authority and legitimacy"""
        return [
            "How do I know you're really from the government?",
            "Can you give me a phone number so I can call you back?",
            "I think I should verify this with the local police first.",
            "My lawyer told me never to give out information over the phone.",
            "Can you send me something in writing before we proceed?",
            "I need to see some official identification. Can you come in person?",
            "This doesn't sound like how the government usually handles things.",
            "I'm going to report this call to the Better Business Bureau.",
            "My accountant handles all my tax matters. You should call him.",
            "I think there's been a mistake. I've never had problems with the IRS.",
            "Can you transfer me to your supervisor? I want to speak to someone in charge.",
            "I'm recording this call for my own protection. Is that okay?",
            "My son is a police officer. He warned me about calls like this.",
            "I'm going to hang up and call the official number myself.",
            "This sounds too urgent to be real. Government agencies don't work this way."
        ]
    
    def _get_time_wasting_responses(self) -> List[str]:
        """Maximum time-wasting responses"""
        return [
            "Oh, that reminds me of a funny story from 1967...",
            "You know, I was just talking to my deceased husband about this...",
            "Let me tell you about my 47 cats and their different personalities...",
            "Speaking of computers, have I mentioned my collection of typewriters?",
            "That's interesting. Did I tell you about my bunion surgery?",
            "Hold on, I need to feed my fish. There are 23 of them and they all have names...",
            "My granddaughter is studying marine biology. She loves dolphins...",
            "I once met a man who looked just like you at a bus stop in Toledo...",
            "That reminds me, I need to check if my stories are recording on TV...",
            "You sound like my nephew Jerry. He sells insurance in Phoenix...",
            "Let me tell you about the time I met Frank Sinatra...",
            "I have 47 photo albums. Would you like me to describe each one?",
            "My late husband collected stamps from 127 different countries...",
            "That's fascinating. Have I told you about my prize-winning tomatoes?",
            "You know, back in 1952, things were very different..."
        ]
    
    def get_random_response(self, category: str = None, personality: str = None) -> str:
        """Get a random response from specified category and personality"""
        if category and category in self.response_categories:
            responses = self.response_categories[category]
        else:
            # Get random category
            all_responses = []
            for cat_responses in self.response_categories.values():
                all_responses.extend(cat_responses)
            responses = all_responses
        
        base_response = random.choice(responses)
        
        # Add personality flavor if specified
        if personality and personality in self.personality_types:
            personality_data = self.personality_types[personality]
            if random.random() < 0.3:  # 30% chance to add personality phrase
                phrase = random.choice(personality_data['common_phrases'])
                base_response = f"{phrase} {base_response}"
        
        return base_response
    
    def get_escalation_sequence(self) -> List[str]:
        """Get a sequence of responses that escalate suspicion"""
        return [
            "This is starting to sound suspicious...",
            "My neighbor warned me about calls exactly like this.",
            "I think I should hang up and call you back at your official number.",
            "You know what, I'm not comfortable with this anymore.",
            "I'm going to report this to the police.",
            "Goodbye!"
        ]
    
    def get_confusion_sequence(self) -> List[str]:
        """Get a sequence of increasingly confused responses"""
        return [
            "I'm sorry, could you repeat that?",
            "I'm not sure I understand what you're asking.",
            "This is all very confusing to me.",
            "Maybe you should call my son instead. He's better with these things.",
            "I think there's been some kind of mistake.",
            "I'm going to hang up now. This is too complicated for me."
        ]


# Example usage
if __name__ == "__main__":
    responses = EnhancedResponses()
    
    print("🎭 Enhanced Response Library Demo")
    print("=" * 50)
    
    categories = list(responses.response_categories.keys())
    personalities = list(responses.personality_types.keys())
    
    for i in range(5):
        category = random.choice(categories)
        personality = random.choice(personalities)
        response = responses.get_random_response(category, personality)
        
        print(f"\n📂 Category: {category}")
        print(f"👤 Personality: {personality}")
        print(f"💬 Response: {response}")
    
    print(f"\n🔄 Escalation Sequence:")
    for i, response in enumerate(responses.get_escalation_sequence(), 1):
        print(f"  {i}. {response}")
