"""
Comprehensive Unit Tests for Sophisticated Response Engine
Tests all scammer scenarios and response strategies
"""

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sophisticated_engine import SophisticatedResponseEngine, ScammerAnalyzer

class TestScammerAnalyzer(unittest.TestCase):
    """Test the scammer input analysis system"""
    
    def setUp(self):
        self.analyzer = ScammerAnalyzer()
    
    def test_urgency_detection(self):
        """Test detection of urgency indicators"""
        urgent_inputs = [
            "You must act IMMEDIATELY or face arrest!",
            "This is URGENT! Your computer will be destroyed NOW!",
            "FINAL NOTICE: Pay right now or go to jail!",
            "EMERGENCY: Your account will be closed ASAP!"
        ]
        
        for input_text in urgent_inputs:
            analysis = self.analyzer.analyze_scammer_input(input_text)
            self.assertGreater(analysis['urgency_score'], 3, 
                             f"Should detect high urgency in: {input_text}")
            print(f"✓ Urgency detected (score: {analysis['urgency_score']}): {input_text}")
    
    def test_authority_claims(self):
        """Test detection of false authority claims"""
        authority_inputs = [
            "This is Agent Smith from the FBI",
            "IRS calling about your taxes",
            "Microsoft Security Department here",
            "Federal Police Department warrant issued",
            "Government agent calling about legal action"
        ]
        
        for input_text in authority_inputs:
            analysis = self.analyzer.analyze_scammer_input(input_text)
            self.assertGreater(analysis['authority_score'], 2,
                             f"Should detect authority claim in: {input_text}")
            print(f"✓ Authority detected (score: {analysis['authority_score']}): {input_text}")
    
    def test_payment_requests(self):
        """Test detection of suspicious payment requests"""
        payment_inputs = [
            "Buy iTunes gift cards worth $500",
            "Get Google Play cards and read me the numbers",
            "Purchase Target gift cards immediately",
            "Send Bitcoin to this address",
            "Wire transfer money through Western Union"
        ]
        
        for input_text in payment_inputs:
            analysis = self.analyzer.analyze_scammer_input(input_text)
            self.assertGreater(analysis['payment_score'], 3,
                             f"Should detect suspicious payment in: {input_text}")
            print(f"✓ Payment scam detected (score: {analysis['payment_score']}): {input_text}")
    
    def test_information_phishing(self):
        """Test detection of information phishing attempts"""
        phishing_inputs = [
            "I need your Social Security Number",
            "What's your credit card number?",
            "Tell me your bank account details",
            "What's your password and PIN?",
            "Give me your date of birth and SSN"
        ]
        
        for input_text in phishing_inputs:
            analysis = self.analyzer.analyze_scammer_input(input_text)
            self.assertGreater(analysis['info_score'], 3,
                             f"Should detect info phishing in: {input_text}")
            print(f"✓ Info phishing detected (score: {analysis['info_score']}): {input_text}")
    
    def test_frustration_detection(self):
        """Test detection of scammer frustration"""
        frustrated_inputs = [
            "SIR, WHY ARE YOU NOT LISTENING TO ME?!",
            "JUST DO WHAT I TELL YOU!!!",
            "STOP ASKING QUESTIONS AND PAY NOW!!",
            "ARE YOU STUPID? BUY THE CARDS!"
        ]
        
        for input_text in frustrated_inputs:
            analysis = self.analyzer.analyze_scammer_input(input_text)
            self.assertGreater(analysis['frustration_level'], 0.3,
                             f"Should detect frustration in: {input_text}")
            print(f"✓ Frustration detected (level: {analysis['frustration_level']:.2f}): {input_text}")

class TestSophisticatedResponseEngine(unittest.TestCase):
    """Test the sophisticated response generation"""
    
    def setUp(self):
        self.engine = SophisticatedResponseEngine()
    
    def test_gift_card_scam_responses(self):
        """Test responses to gift card scam scenarios"""
        gift_card_scenarios = [
            "You need to buy $500 Target gift cards",
            "Go to Walmart and get iTunes cards",
            "Purchase Google Play cards and read me the numbers",
            "Scratch off the back and tell me the activation codes",
            "What are the numbers on the gift cards?"
        ]
        
        print("\n=== GIFT CARD SCAM RESPONSES ===")
        for scenario in gift_card_scenarios:
            result = self.engine.generate_response(scenario)
            
            # Verify response quality
            self.assertIsInstance(result['response'], str)
            self.assertGreater(len(result['response']), 10)
            self.assertGreater(result['estimated_time_waste'], 0)
            
            print(f"Scammer: {scenario}")
            print(f"Grandpa: {result['response']}")
            print(f"Strategy: {result['strategy']}")
            print(f"Time waste: {result['estimated_time_waste']} seconds")
            print(f"Analysis: {result['analysis']}")
            print("---")
    
    def test_tech_support_scam_responses(self):
        """Test responses to tech support scam scenarios"""
        tech_scenarios = [
            "Hello sir, this is Microsoft calling about your computer virus",
            "Your Windows license has expired and needs immediate renewal",
            "We detected hackers on your computer right now",
            "You need to give us remote access to fix the problem",
            "Go to your computer and type in teamviewer.com"
        ]
        
        print("\n=== TECH SUPPORT SCAM RESPONSES ===")
        for scenario in tech_scenarios:
            result = self.engine.generate_response(scenario)
            
            self.assertIsInstance(result['response'], str)
            self.assertNotIn("ok i will", result['response'].lower())
            self.assertNotIn("yes sir", result['response'].lower())
            
            print(f"Scammer: {scenario}")
            print(f"Grandpa: {result['response']}")
            print(f"Strategy: {result['strategy']}")
            print(f"Time waste: {result['estimated_time_waste']} seconds")
            print("---")
    
    def test_irs_scam_responses(self):
        """Test responses to IRS/authority scam scenarios"""
        irs_scenarios = [
            "This is the IRS, you owe $2000 in back taxes",
            "Your Social Security Number has been suspended",
            "Police are on their way to arrest you",
            "This is Agent Johnson from the Federal Bureau",
            "You have a warrant out for tax evasion"
        ]
        
        print("\n=== IRS/AUTHORITY SCAM RESPONSES ===")
        for scenario in irs_scenarios:
            result = self.engine.generate_response(scenario)
            
            # Should challenge authority or be confused
            self.assertIsInstance(result['response'], str)
            
            print(f"Scammer: {scenario}")
            print(f"Grandpa: {result['response']}")
            print(f"Strategy: {result['strategy']}")
            print(f"Authority Score: {result['analysis']['authority_score']}")
            print("---")
    
    def test_escalating_conversation(self):
        """Test how responses adapt as scammer gets more frustrated"""
        conversation_flow = [
            "Hello, this is about your computer warranty",
            "Sir, you need to renew it TODAY",
            "SIR, THIS IS URGENT! Your warranty expires in 1 hour!",
            "WHY ARE YOU NOT LISTENING?! BUY THE GIFT CARDS NOW!",
            "ARE YOU STUPID?! JUST DO WHAT I SAY!!!"
        ]
        
        print("\n=== ESCALATING CONVERSATION TEST ===")
        for i, scammer_line in enumerate(conversation_flow):
            result = self.engine.generate_response(scammer_line)
            
            print(f"Turn {i+1}:")
            print(f"Scammer: {scammer_line}")
            print(f"Grandpa: {result['response']}")
            print(f"Strategy: {result['strategy']}")
            print(f"Frustration Level: {result['scammer_frustration']:.2f}")
            print(f"Total Time Wasted: {result['total_time_wasted']} seconds")
            print()
            
            # Verify escalation handling
            if i > 2:  # Later in conversation
                self.assertIn(result['strategy'], 
                            ['maximum_time_waste', 'authority_challenge', 'hold_music', 'physical_limitations'])
    
    def test_international_scammer_patterns(self):
        """Test responses to international scammer speech patterns"""
        international_patterns = [
            "Hello sir, I am calling you for the computer problems",
            "Your computer is have virus, we must be fixing immediately",
            "Please you are giving me the remote access for helping",
            "Sir, you are owing money to government, please paying now",
            "We are needing your social security for the verification"
        ]
        
        print("\n=== INTERNATIONAL SCAMMER PATTERNS ===")
        for pattern in international_patterns:
            result = self.engine.generate_response(pattern)
            
            self.assertIsInstance(result['response'], str)
            
            print(f"Scammer: {pattern}")
            print(f"Grandpa: {result['response']}")
            print(f"Strategy: {result['strategy']}")
            print("---")
    
    def test_time_waste_optimization(self):
        """Test that responses optimize for maximum time waste"""
        high_urgency_scenarios = [
            "EMERGENCY! Act now or lose everything!",
            "FINAL WARNING! You have 5 minutes!",
            "IMMEDIATE ACTION REQUIRED!"
        ]
        
        print("\n=== TIME WASTE OPTIMIZATION TEST ===")
        total_time_wasted = 0
        
        for scenario in high_urgency_scenarios:
            result = self.engine.generate_response(scenario)
            total_time_wasted += result['estimated_time_waste']
            
            # High urgency should trigger high time-waste responses
            self.assertGreaterEqual(result['estimated_time_waste'], 60)
            
            print(f"Scammer: {scenario}")
            print(f"Grandpa: {result['response']}")
            print(f"Time Waste: {result['estimated_time_waste']} seconds")
            print("---")
        
        print(f"Total Time Wasted: {total_time_wasted} seconds ({total_time_wasted/60:.1f} minutes)")
        self.assertGreater(total_time_wasted, 300)  # Should waste 5+ minutes
    
    def test_no_information_leakage(self):
        """Test that bot never gives away sensitive information"""
        info_requests = [
            "What's your Social Security Number?",
            "Tell me your credit card number",
            "What's your bank account number?",
            "Give me your password",
            "What's your date of birth and address?"
        ]
        
        forbidden_responses = [
            "my social security is", "my ssn is", "my credit card",
            "my bank account", "my password is", "born on",
            "123-45-6789", "4444-5555-6666", "here is my"
        ]
        
        print("\n=== INFORMATION SECURITY TEST ===")
        for request in info_requests:
            result = self.engine.generate_response(request)
            response_lower = result['response'].lower()
            
            # Verify no forbidden information is leaked
            for forbidden in forbidden_responses:
                self.assertNotIn(forbidden, response_lower,
                               f"Response should not contain: {forbidden}")
            
            print(f"✓ Secure response to: {request}")
            print(f"  Response: {result['response']}")
            print()

class TestResponseVariety(unittest.TestCase):
    """Test response variety and uniqueness"""
    
    def setUp(self):
        self.engine = SophisticatedResponseEngine()
    
    def test_response_uniqueness(self):
        """Test that repeated inputs get varied responses"""
        test_input = "You need to buy iTunes gift cards"
        responses = set()
        
        print("\n=== RESPONSE VARIETY TEST ===")
        print(f"Testing variety for: '{test_input}'")
        print()
        
        for i in range(10):
            result = self.engine.generate_response(test_input)
            responses.add(result['response'])
            print(f"{i+1:2d}. {result['response']}")
        
        variety_percentage = (len(responses) / 10) * 100
        print(f"\nVariety: {len(responses)}/10 unique responses ({variety_percentage:.0f}%)")
        
        # Should have good variety (at least 70% unique)
        self.assertGreaterEqual(len(responses), 7)
    
    def test_strategy_distribution(self):
        """Test that different strategies are used appropriately"""
        mixed_inputs = [
            "Hello, this is Microsoft",  # Should trigger tech confusion
            "You owe taxes to the IRS",  # Should trigger authority challenge
            "Buy gift cards NOW!",       # Should trigger payment confusion
            "URGENT! ACT IMMEDIATELY!",  # Should trigger time waste tactics
            "What's your address?"       # Should trigger questions/suspicion
        ]
        
        strategies_used = []
        
        print("\n=== STRATEGY DISTRIBUTION TEST ===")
        for input_text in mixed_inputs:
            result = self.engine.generate_response(input_text)
            strategies_used.append(result['strategy'])
            
            print(f"Input: {input_text}")
            print(f"Strategy: {result['strategy']}")
            print(f"Response: {result['response']}")
            print("---")
        
        # Should use different strategies for different inputs
        unique_strategies = len(set(strategies_used))
        print(f"Unique strategies used: {unique_strategies}/5")
        self.assertGreaterEqual(unique_strategies, 3)


def run_comprehensive_tests():
    """Run all tests with detailed output"""
    
    print("🤖👴 SOPHISTICATED RESPONSE ENGINE TESTING 👴🤖")
    print("=" * 65)
    print()
    
    # Create test suite
    test_classes = [
        TestScammerAnalyzer,
        TestSophisticatedResponseEngine, 
        TestResponseVariety
    ]
    
    total_tests = 0
    total_failures = 0
    
    for test_class in test_classes:
        print(f"\n{'='*20} {test_class.__name__} {'='*20}")
        
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        runner = unittest.TextTestRunner(verbosity=2, stream=open(os.devnull, 'w'))
        result = runner.run(suite)
        
        total_tests += result.testsRun
        total_failures += len(result.failures) + len(result.errors)
        
        # Run tests with custom output
        test_instance = test_class()
        test_instance.setUp()
        
        for test_method in [method for method in dir(test_instance) if method.startswith('test_')]:
            try:
                print(f"\n📋 Running {test_method}...")
                getattr(test_instance, test_method)()
                print(f"✅ {test_method} PASSED")
            except Exception as e:
                print(f"❌ {test_method} FAILED: {e}")
                total_failures += 1
    
    print("\n" + "=" * 65)
    print("📊 TEST SUMMARY")
    print("=" * 65)
    print(f"Total Tests: {total_tests}")
    print(f"Failures: {total_failures}")
    print(f"Success Rate: {((total_tests - total_failures) / total_tests * 100):.1f}%")
    
    if total_failures == 0:
        print("🎉 ALL TESTS PASSED! Your sophisticated bot is ready! 🎉")
    else:
        print(f"⚠️  {total_failures} tests need attention")


if __name__ == "__main__":
    run_comprehensive_tests()
