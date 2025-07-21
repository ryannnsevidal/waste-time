"""
Advanced AI Engine for Scammer Waste Bot
Sophisticated conversation management with adaptive responses
"""
import random
import time
import json
import csv
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class SophisticatedEngine:
    """Advanced AI engine for realistic scammer engagement"""
    
    def __init__(self):
        self.conversation_history = []
        self.scammer_profile = {
            'frustration_level': 0,
            'persistence_score': 0,
            'technique_type': 'unknown',
            'estimated_experience': 'novice'
        }
        self.analytics_data = []
        self.response_strategies = self._load_strategies()
        
    def _load_strategies(self) -> Dict:
        """Load response strategies based on scammer behavior"""
        return {
            'confusion': [
                "I'm sorry, could you repeat that? My hearing isn't what it used to be.",
                "Wait, what was that about? I was making tea.",
                "Hold on, my cat is doing something strange. What did you say?",
                "I need to find my glasses. Could you speak slower?",
                "My grandson usually helps me with these things. Is he there?"
            ],
            'tech_confusion': [
                "I don't understand these computer things. Is this like AOL?",
                "My computer is making beeping sounds. Is that normal?",
                "Do I need to turn it off and on again? That's what my grandson says.",
                "I still use Windows 95. Will that work?",
                "What's a password? I just click on everything until it works."
            ],
            'financial_stalling': [
                "Let me check with my bank. They're closed until Monday though.",
                "I need to ask my son about this. He handles my money now.",
                "My Social Security check doesn't come until the 3rd.",
                "I keep my money in coffee cans. How much did you need?",
                "The bank froze my account last week. Something about suspicious activity."
            ],
            'family_distractions': [
                "Hold on, my daughter is calling on the other line.",
                "My grandchildren are visiting. It's quite loud here.",
                "I need to check on my husband. He's not feeling well.",
                "The dog is barking at something. Let me see what's wrong.",
                "Someone's at the door. This better not be those Jehovah's Witnesses again."
            ],
            'escalation': [
                "You know what, I'm getting suspicious about this.",
                "My neighbor warned me about calls like this.",
                "I think I should hang up and call you back.",
                "This doesn't sound right. Are you really from the bank?",
                "I'm going to report this to the police."
            ]
        }
    
    def analyze_scammer_input(self, message: str) -> Dict:
        """Analyze scammer message for behavioral patterns"""
        message_lower = message.lower()
        
        # Detect urgency indicators
        urgency_keywords = ['urgent', 'immediately', 'now', 'quickly', 'hurry', 'emergency']
        urgency_score = sum(1 for word in urgency_keywords if word in message_lower)
        
        # Detect financial requests
        financial_keywords = ['money', 'payment', 'card', 'account', 'bank', 'transfer', 'fee']
        financial_score = sum(1 for word in financial_keywords if word in message_lower)
        
        # Detect tech support angle
        tech_keywords = ['computer', 'virus', 'security', 'microsoft', 'windows', 'error']
        tech_score = sum(1 for word in tech_keywords if word in message_lower)
        
        # Detect authority claims
        authority_keywords = ['police', 'government', 'irs', 'social security', 'federal', 'arrest']
        authority_score = sum(1 for word in authority_keywords if word in message_lower)
        
        analysis = {
            'urgency_score': urgency_score,
            'financial_score': financial_score,
            'tech_score': tech_score,
            'authority_score': authority_score,
            'message_length': len(message),
            'timestamp': datetime.now().isoformat()
        }
        
        # Update scammer profile based on analysis
        self._update_scammer_profile(analysis)
        
        return analysis
    
    def _update_scammer_profile(self, analysis: Dict):
        """Update scammer behavioral profile"""
        # Increase frustration if they're being urgent
        if analysis['urgency_score'] > 2:
            self.scammer_profile['frustration_level'] += 1
            
        # Determine technique type
        if analysis['tech_score'] > analysis['financial_score']:
            self.scammer_profile['technique_type'] = 'tech_support'
        elif analysis['authority_score'] > 0:
            self.scammer_profile['technique_type'] = 'authority_impersonation'
        elif analysis['financial_score'] > 0:
            self.scammer_profile['technique_type'] = 'financial_fraud'
        
        # Estimate experience based on sophistication
        if analysis['message_length'] > 100 and analysis['urgency_score'] < 2:
            self.scammer_profile['estimated_experience'] = 'experienced'
        elif analysis['urgency_score'] > 3:
            self.scammer_profile['estimated_experience'] = 'desperate'
    
    def generate_response(self, scammer_message: str) -> Tuple[str, Dict]:
        """Generate contextually appropriate response"""
        analysis = self.analyze_scammer_input(scammer_message)
        
        # Choose strategy based on conversation stage and scammer behavior
        strategy = self._choose_strategy(analysis)
        
        # Generate response with natural delays and variations
        response = self._craft_response(strategy, analysis)
        
        # Log interaction for analytics
        self._log_interaction(scammer_message, response, analysis)
        
        return response, analysis
    
    def _choose_strategy(self, analysis: Dict) -> str:
        """Choose optimal response strategy"""
        frustration = self.scammer_profile['frustration_level']
        conversation_length = len(self.conversation_history)
        
        # Early conversation - build trust with confusion
        if conversation_length < 3:
            return 'confusion'
        
        # Mid conversation - adapt to their technique
        elif conversation_length < 10:
            if analysis['tech_score'] > 0:
                return 'tech_confusion'
            elif analysis['financial_score'] > 0:
                return 'financial_stalling'
            else:
                return 'family_distractions'
        
        # Late conversation - escalate based on frustration
        elif frustration > 5 or conversation_length > 15:
            return 'escalation'
        
        # Default to random strategy
        else:
            strategies = ['confusion', 'tech_confusion', 'financial_stalling', 'family_distractions']
            return random.choice(strategies)
    
    def _craft_response(self, strategy: str, analysis: Dict) -> str:
        """Craft natural-sounding response with variations"""
        base_responses = self.response_strategies.get(strategy, self.response_strategies['confusion'])
        base_response = random.choice(base_responses)
        
        # Add natural variations
        variations = [
            "Oh my...",
            "Well, you see...",
            "I'm sorry, but...",
            "Let me think about this...",
            "That's interesting...",
        ]
        
        if random.random() < 0.3:  # 30% chance to add variation
            variation = random.choice(variations)
            base_response = f"{variation} {base_response}"
        
        return base_response
    
    def _log_interaction(self, scammer_message: str, bot_response: str, analysis: Dict):
        """Log interaction for analytics and learning"""
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'scammer_message': scammer_message,
            'bot_response': bot_response,
            'analysis': analysis,
            'scammer_profile': self.scammer_profile.copy(),
            'conversation_turn': len(self.conversation_history)
        }
        
        self.conversation_history.append(interaction)
        self.analytics_data.append(interaction)
        
        # Save to CSV for analysis
        self._save_to_csv(interaction)
    
    def _save_to_csv(self, interaction: Dict):
        """Save interaction data to CSV file"""
        csv_file = os.path.join('data', 'analytics', 'conversations.csv')
        os.makedirs(os.path.dirname(csv_file), exist_ok=True)
        
        # Check if file exists to determine if we need headers
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            if not file_exists:
                # Write headers
                headers = [
                    'timestamp', 'conversation_turn', 'scammer_message_length',
                    'bot_response', 'urgency_score', 'financial_score', 'tech_score',
                    'authority_score', 'frustration_level', 'technique_type', 'estimated_experience'
                ]
                writer.writerow(headers)
            
            # Write data
            row = [
                interaction['timestamp'],
                interaction['conversation_turn'],
                len(interaction['scammer_message']),
                interaction['bot_response'],
                interaction['analysis']['urgency_score'],
                interaction['analysis']['financial_score'],
                interaction['analysis']['tech_score'],
                interaction['analysis']['authority_score'],
                interaction['scammer_profile']['frustration_level'],
                interaction['scammer_profile']['technique_type'],
                interaction['scammer_profile']['estimated_experience']
            ]
            writer.writerow(row)
    
    def get_conversation_summary(self) -> Dict:
        """Get detailed conversation analytics"""
        if not self.conversation_history:
            return {'status': 'no_conversation'}
        
        total_turns = len(self.conversation_history)
        avg_response_time = 2.5  # Simulated for demo
        
        return {
            'total_conversation_turns': total_turns,
            'time_wasted_minutes': total_turns * 1.5,  # Estimate 1.5 min per turn
            'scammer_profile': self.scammer_profile,
            'average_response_time': avg_response_time,
            'technique_detected': self.scammer_profile['technique_type'],
            'effectiveness_score': min(100, total_turns * 5),  # Max 100%
            'estimated_cost_to_scammer': total_turns * 0.25  # $0.25 per minute estimate
        }
    
    def reset_conversation(self):
        """Reset for new conversation"""
        self.conversation_history = []
        self.scammer_profile = {
            'frustration_level': 0,
            'persistence_score': 0,
            'technique_type': 'unknown',
            'estimated_experience': 'novice'
        }


# Example usage and testing
if __name__ == "__main__":
    engine = SophisticatedEngine()
    
    # Test conversation
    test_messages = [
        "Hello, this is Microsoft. Your computer has a virus.",
        "You need to give me remote access to fix it immediately.",
        "This is very urgent! Your computer will crash if you don't act now!",
        "I need you to go to your computer and type some commands.",
        "Why are you not listening? This is important!"
    ]
    
    print("🤖 Sophisticated AI Engine Demo")
    print("=" * 50)
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n👤 Scammer (Turn {i}): {message}")
        
        response, analysis = engine.generate_response(message)
        
        print(f"🧓 Bot Response: {response}")
        print(f"📊 Analysis: Urgency={analysis['urgency_score']}, Tech={analysis['tech_score']}")
        
        # Simulate realistic delay
        time.sleep(1)
    
    # Show final summary
    summary = engine.get_conversation_summary()
    print(f"\n📈 Conversation Summary:")
    print(f"   • Total turns: {summary['total_conversation_turns']}")
    print(f"   • Time wasted: {summary['time_wasted_minutes']:.1f} minutes")
    print(f"   • Technique: {summary['technique_detected']}")
    print(f"   • Effectiveness: {summary['effectiveness_score']}%")
