#!/usr/bin/env python3

"""
Detailed breakdown of what factors contribute to each threshold score
Shows the supporting elements that indirectly build up scores
"""

from sophisticated_engine import ScammerAnalyzer

def show_scoring_breakdown():
    """Show what keywords and patterns contribute to each score"""
    
    analyzer = ScammerAnalyzer()
    
    print("📊 DETAILED SCORING BREAKDOWN 📊")
    print("=" * 50)
    print()
    
    print("🔥 URGENCY KEYWORDS (Direct Contributors):")
    for keyword, score in sorted(analyzer.urgency_keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{keyword}' = +{score} points")
    print()
    
    print("👮 AUTHORITY KEYWORDS (Direct Contributors):")
    for keyword, score in sorted(analyzer.authority_keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{keyword}' = +{score} points")
    print()
    
    print("💰 PAYMENT KEYWORDS (Direct Contributors):")
    for keyword, score in sorted(analyzer.payment_keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{keyword}' = +{score} points")
    print()
    
    print("🔒 INFO REQUEST KEYWORDS (Direct Contributors):")
    for keyword, score in sorted(analyzer.info_keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{keyword}' = +{score} points")
    print()
    
    print("😡 FRUSTRATION KEYWORDS (Direct Contributors):")
    for keyword, score in sorted(analyzer.frustration_keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{keyword}' = +{score} points")
    print()
    
    print("📈 ESCALATION KEYWORDS (Direct Contributors):")
    for keyword, score in sorted(analyzer.escalation_keywords.items(), key=lambda x: x[1], reverse=True):
        print(f"   '{keyword}' = +{score} points")
    print()
    
    print("⚡ SUPPORTING FACTORS (Indirect Contributors):")
    print("   CAPS RATIO: Higher percentage of capital letters = more frustration")
    print("   EXCLAMATION COUNT: More !!! = higher frustration")
    print("   ALL CAPS WORDS: Words in ALL CAPS = frustration boost")
    print("   COMMAND PATTERNS: More commands (go, buy, get) = more suspicious")
    print("   QUESTION COUNT: More questions = info phishing potential")
    print("   THREAT PATTERNS: arrest, jail, police, warrant = threat score")
    print()
    
    print("🎯 THRESHOLD LEVELS:")
    print("   High Urgency: ≥8 urgency points")
    print("   Authority Claim: ≥6 authority points")
    print("   Payment Scam: ≥8 payment points")
    print("   Info Phishing: ≥8 info points")
    print("   Highly Frustrated: ≥1.5 frustration level")
    print("   Escalating: ≥5 escalation points")
    print("   Threatening: ≥4 threat points")
    print()

def test_composite_scoring():
    """Test how multiple small factors combine into high scores"""
    
    analyzer = ScammerAnalyzer()
    
    print("🧮 COMPOSITE SCORING EXAMPLES 🧮")
    print("=" * 40)
    print()
    
    test_cases = [
        {
            'phrase': "Sir, this is urgent! You need to pay now immediately! Final notice!",
            'description': "Multiple urgency words combining"
        },
        {
            'phrase': "Agent Johnson from FBI Police Department calling about federal warrant",
            'description': "Multiple authority words stacking"
        },
        {
            'phrase': "Buy iTunes gift cards at Target using cash and send Bitcoin",
            'description': "Multiple payment methods mentioned"
        },
        {
            'phrase': "Give me your social security, credit card, bank account and password",
            'description': "Multiple sensitive info requests"
        },
        {
            'phrase': "DAMN IT! WHY ARE YOU SO STUPID?! LISTEN TO ME!",
            'description': "Multiple frustration indicators + caps"
        },
        {
            'phrase': "Final warning! This is your last chance! Stop wasting time!",
            'description': "Multiple escalation phrases"
        }
    ]
    
    for test_case in test_cases:
        print(f"📝 {test_case['description'].upper()}")
        print(f"   Phrase: \"{test_case['phrase']}\"")
        
        analysis = analyzer.analyze_scammer_input(test_case['phrase'])
        
        print(f"   📊 Scores:")
        print(f"      Urgency: {analysis['urgency_score']}")
        print(f"      Authority: {analysis['authority_score']}")
        print(f"      Payment: {analysis['payment_score']}")
        print(f"      Info: {analysis['info_score']}")
        print(f"      Frustration Level: {analysis['frustration_level']:.2f}")
        print(f"      Total Suspicion: {analysis['total_suspicion']}")
        
        print(f"   🎯 Triggered Thresholds:")
        thresholds = []
        if analysis['is_high_urgency']: thresholds.append("High Urgency")
        if analysis['is_authority_claim']: thresholds.append("Authority Claim")
        if analysis['is_payment_scam']: thresholds.append("Payment Scam")
        if analysis['is_info_phishing']: thresholds.append("Info Phishing")
        if analysis['is_highly_frustrated']: thresholds.append("Highly Frustrated")
        if analysis['is_escalating']: thresholds.append("Escalating")
        if analysis['is_threatening']: thresholds.append("Threatening")
        
        if thresholds:
            print(f"      {', '.join(thresholds)}")
        else:
            print("      None")
        
        print()

if __name__ == "__main__":
    show_scoring_breakdown()
    print("\n" + "=" * 80 + "\n")
    test_composite_scoring()
