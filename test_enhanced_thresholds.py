#!/usr/bin/env python3

"""
Test the enhanced threshold system for scammer analysis
Shows how frustration level and urgency escalate with different phrases
"""

from sophisticated_engine import ScammerAnalyzer, SophisticatedResponseEngine
import json

def test_escalating_scenarios():
    """Test how the bot responds to escalating scammer frustration"""
    
    analyzer = ScammerAnalyzer()
    engine = SophisticatedResponseEngine()
    
    print("🔥 ENHANCED THRESHOLD TESTING 🔥")
    print("=" * 60)
    print()
    
    # Progressive escalation scenarios
    escalation_scenarios = [
        # Level 1: Polite approach
        "Hello sir, this is Microsoft calling about your computer",
        
        # Level 2: Adding urgency
        "Sir, your computer has a virus and needs immediate attention",
        
        # Level 3: Authority + Urgency
        "This is Agent Smith from Microsoft Security. Your computer will be destroyed!",
        
        # Level 4: Payment demands
        "You need to buy $500 iTunes gift cards RIGHT NOW to fix this!",
        
        # Level 5: Threats
        "If you don't pay immediately, police will arrest you for computer fraud!",
        
        # Level 6: High frustration
        "SIR! WHY ARE YOU NOT LISTENING?! BUY THE DAMN CARDS NOW!",
        
        # Level 7: Maximum frustration
        "ARE YOU STUPID?! JUST DO WHAT I TELL YOU! THIS IS THE FINAL WARNING!",
        
        # Level 8: Complete breakdown
        "WHAT THE HELL IS WRONG WITH YOU?! STOP WASTING MY TIME AND PAY NOW!!!"
    ]
    
    cumulative_frustration = 0
    
    for i, scenario in enumerate(escalation_scenarios, 1):
        print(f"📞 ESCALATION LEVEL {i}")
        print(f"Scammer: {scenario}")
        print()
        
        # Analyze the input
        analysis = analyzer.analyze_scammer_input(scenario)
        
        # Show detailed scoring
        print("🔍 DETAILED ANALYSIS:")
        print(f"   Urgency Score: {analysis['urgency_score']}")
        print(f"   Authority Score: {analysis['authority_score']}")
        print(f"   Payment Score: {analysis['payment_score']}")
        print(f"   Info Request Score: {analysis['info_score']}")
        print(f"   Frustration Keywords: {analysis['frustration_score']}")
        print(f"   Escalation Score: {analysis['escalation_score']}")
        print(f"   Threat Score: {analysis['threat_score']}")
        print(f"   CAPS Ratio: {analysis['caps_ratio']:.2f}")
        print(f"   Exclamation Count: {analysis['exclamation_count']}")
        print(f"   ALL CAPS Words: {analysis['all_caps_words']}")
        print()
        
        print("THRESHOLD TRIGGERS:")
        thresholds = {
            'High Urgency': analysis['is_high_urgency'],
            'Authority Claim': analysis['is_authority_claim'],
            'Payment Scam': analysis['is_payment_scam'],
            'Info Phishing': analysis['is_info_phishing'],
            'Highly Frustrated': analysis['is_highly_frustrated'],
            'Escalating': analysis['is_escalating'],
            'Threatening': analysis['is_threatening']
        }
        
        for threshold, triggered in thresholds.items():
            status = "🔴 TRIGGERED" if triggered else "⚪ Normal"
            print(f"   {threshold}: {status}")
        print()
        
        # Generate response with cumulative frustration
        engine.scammer_frustration_level = cumulative_frustration
        result = engine.generate_response(scenario)
        cumulative_frustration += analysis['frustration_level']
        
        print(f"💭 CALCULATED FRUSTRATION: {analysis['frustration_level']:.2f}")
        print(f"📈 CUMULATIVE FRUSTRATION: {cumulative_frustration:.2f}")
        print(f"🎭 SELECTED STRATEGY: {result['strategy']}")
        print(f"👴 GRANDPA RESPONSE: {result['response']}")
        print(f"⏱️  TIME WASTE: {result['estimated_time_waste']} seconds")
        print()
        print("-" * 60)
        print()

def test_specific_threshold_triggers():
    """Test specific phrases that should trigger different thresholds"""
    
    analyzer = ScammerAnalyzer()
    
    print("SPECIFIC THRESHOLD TRIGGER TESTS")
    print("=" * 50)
    print()
    
    test_cases = [
        {
            'category': 'HIGH URGENCY TRIGGERS',
            'phrases': [
                "EMERGENCY! Your computer will be destroyed in 5 minutes!",
                "FINAL NOTICE! You have 30 seconds to act!",
                "IMMEDIATE ACTION REQUIRED! Police are coming NOW!"
            ],
            'expected_threshold': 'is_high_urgency'
        },
        {
            'category': 'AUTHORITY CLAIM TRIGGERS',
            'phrases': [
                "This is Agent Johnson from the FBI calling about your warrant",
                "Microsoft Security Department here, we detected illegal activity",
                "Federal Police Department - you're under investigation"
            ],
            'expected_threshold': 'is_authority_claim'
        },
        {
            'category': 'PAYMENT SCAM TRIGGERS',
            'phrases': [
                "Buy $500 iTunes gift cards and read me the numbers",
                "Go to Target, get Google Play cards worth $300",
                "Send Bitcoin to this wallet address immediately"
            ],
            'expected_threshold': 'is_payment_scam'
        },
        {
            'category': 'HIGH FRUSTRATION TRIGGERS',
            'phrases': [
                "ARE YOU STUPID?! JUST DO WHAT I SAY!",
                "WHY THE HELL ARE YOU NOT LISTENING?!",
                "DAMN IT! STOP ASKING QUESTIONS!"
            ],
            'expected_threshold': 'is_highly_frustrated'
        },
        {
            'category': 'THREAT TRIGGERS',
            'phrases': [
                "Police will arrest you if you don't pay now",
                "You'll go to jail for tax evasion",
                "A warrant has been issued for your arrest"
            ],
            'expected_threshold': 'is_threatening'
        }
    ]
    
    for test_case in test_cases:
        print(f"📋 {test_case['category']}")
        print("=" * len(test_case['category']))
        
        for phrase in test_case['phrases']:
            analysis = analyzer.analyze_scammer_input(phrase)
            triggered = analysis[test_case['expected_threshold']]
            
            status = "TRIGGERED" if triggered else "NOT TRIGGERED"
            print(f"{status} - \"{phrase}\"")
            print(f"   Frustration Level: {analysis['frustration_level']:.2f}")
            print(f"   Total Suspicion: {analysis['total_suspicion']}")
            print()
        
        print()

if __name__ == "__main__":
    test_escalating_scenarios()
    print("\n" + "=" * 80 + "\n")
    test_specific_threshold_triggers()
