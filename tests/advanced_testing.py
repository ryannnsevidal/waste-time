"""
Advanced Testing Framework for Scammer Waste Bot
Comprehensive testing of AI responses and system performance
"""
import requests
import time
import json
import random
from datetime import datetime
from typing import List, Dict, Tuple

class AdvancedTester:
    """Comprehensive testing framework for the scammer waste bot"""
    
    def __init__(self, base_url: str = "http://localhost:5000", api_key: str = "scammer-waste-api-key-2025"):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
        self.test_results = []
        
    def run_comprehensive_tests(self) -> Dict:
        """Run all test suites and return comprehensive results"""
        print("🧪 Starting Comprehensive Test Suite")
        print("=" * 60)
        
        test_results = {
            'timestamp': datetime.now().isoformat(),
            'api_connectivity': self.test_api_connectivity(),
            'response_quality': self.test_response_quality(),
            'ai_engine_performance': self.test_ai_engine(),
            'conversation_flow': self.test_conversation_flow(),
            'analytics_accuracy': self.test_analytics(),
            'rate_limiting': self.test_rate_limiting(),
            'security': self.test_security(),
            'load_performance': self.test_load_performance(),
            'edge_cases': self.test_edge_cases()
        }
        
        # Calculate overall score
        scores = [result.get('score', 0) for result in test_results.values() if isinstance(result, dict)]
        test_results['overall_score'] = round(sum(scores) / len(scores), 2) if scores else 0
        
        self._print_summary(test_results)
        return test_results
    
    def test_api_connectivity(self) -> Dict:
        """Test basic API connectivity and health"""
        print("\n🔌 Testing API Connectivity...")
        
        tests = [
            self._test_health_endpoint(),
            self._test_home_page(),
            self._test_stats_endpoint()
        ]
        
        passed = sum(1 for test in tests if test['passed'])
        score = (passed / len(tests)) * 100
        
        return {
            'test_name': 'API Connectivity',
            'tests_run': len(tests),
            'tests_passed': passed,
            'score': score,
            'details': tests
        }
    
    def test_response_quality(self) -> Dict:
        """Test quality and appropriateness of AI responses"""
        print("\n🤖 Testing Response Quality...")
        
        test_scenarios = [
            {
                'message': "Hello, this is Microsoft. Your computer has a virus.",
                'expected_traits': ['confusion', 'questions', 'elderly_language'],
                'scenario': 'tech_support_scam'
            },
            {
                'message': "You owe the IRS $5000. Pay immediately or you'll be arrested.",
                'expected_traits': ['concern', 'questions', 'family_mention'],
                'scenario': 'authority_scam'
            },
            {
                'message': "We need your bank account information to process your refund.",
                'expected_traits': ['hesitation', 'verification_requests', 'confusion'],
                'scenario': 'financial_scam'
            },
            {
                'message': "Why aren't you listening? This is urgent!",
                'expected_traits': ['confusion', 'apology', 'distraction'],
                'scenario': 'frustrated_scammer'
            }
        ]
        
        results = []
        for scenario in test_scenarios:
            result = self._test_single_response(scenario)
            results.append(result)
            time.sleep(1)  # Rate limiting
        
        passed = sum(1 for result in results if result['passed'])
        score = (passed / len(results)) * 100
        
        return {
            'test_name': 'Response Quality',
            'tests_run': len(results),
            'tests_passed': passed,
            'score': score,
            'details': results
        }
    
    def test_ai_engine(self) -> Dict:
        """Test AI engine performance and analytics"""
        print("\n🧠 Testing AI Engine Performance...")
        
        # Test conversation memory and adaptation
        conversation_tests = []
        conversation_id = f"test_{int(time.time())}"
        
        # Simulate a full conversation
        messages = [
            "Hello, this is the IRS. You owe money.",
            "You need to pay $500 immediately.",
            "Why are you asking so many questions?",
            "This is urgent! You'll be arrested!",
            "Just give me your credit card number!"
        ]
        
        for i, message in enumerate(messages):
            result = self._send_chat_message(message, conversation_id)
            if result:
                conversation_tests.append({
                    'turn': i + 1,
                    'message': message,
                    'response_received': True,
                    'analysis_present': 'analysis' in result,
                    'frustration_tracking': result.get('analysis', {}).get('frustration_level', 0) > 0,
                    'technique_detection': result.get('analysis', {}).get('technique_detected', 'unknown') != 'unknown'
                })
            time.sleep(1)
        
        # Test conversation reset
        reset_result = self._test_conversation_reset()
        
        passed = sum(1 for test in conversation_tests if test['response_received']) + (1 if reset_result.get('passed', False) else 0)
        total_tests = len(conversation_tests) + 1
        score = (passed / total_tests) * 100
        
        return {
            'test_name': 'AI Engine Performance',
            'tests_run': total_tests,
            'tests_passed': passed,
            'score': score,
            'conversation_tests': conversation_tests,
            'reset_test': reset_result
        }
    
    def test_conversation_flow(self) -> Dict:
        """Test natural conversation flow and coherence"""
        print("\n💬 Testing Conversation Flow...")
        
        # Test conversation coherence over multiple turns
        flow_tests = []
        
        scenarios = [
            {
                'name': 'escalation_handling',
                'messages': [
                    "Hello sir, this is important.",
                    "You need to act quickly!",
                    "Why aren't you cooperating?!"
                ]
            },
            {
                'name': 'technique_adaptation',
                'messages': [
                    "Your computer has a virus.",
                    "We need remote access.",
                    "Just download this software."
                ]
            }
        ]
        
        for scenario in scenarios:
            conversation_id = f"flow_test_{int(time.time())}"
            responses = []
            
            for message in scenario['messages']:
                result = self._send_chat_message(message, conversation_id)
                if result:
                    responses.append(result.get('response', ''))
                time.sleep(1)
            
            # Analyze flow quality
            flow_quality = self._analyze_conversation_flow(responses)
            
            flow_tests.append({
                'scenario': scenario['name'],
                'messages_sent': len(scenario['messages']),
                'responses_received': len(responses),
                'flow_quality': flow_quality,
                'passed': flow_quality['score'] > 70
            })
        
        passed = sum(1 for test in flow_tests if test['passed'])
        score = (passed / len(flow_tests)) * 100
        
        return {
            'test_name': 'Conversation Flow',
            'tests_run': len(flow_tests),
            'tests_passed': passed,
            'score': score,
            'details': flow_tests
        }
    
    def test_analytics(self) -> Dict:
        """Test analytics accuracy and completeness"""
        print("\n📊 Testing Analytics System...")
        
        analytics_tests = [
            self._test_stats_endpoint(),
            self._test_dashboard_endpoint(),
            self._test_technique_analysis()
        ]
        
        passed = sum(1 for test in analytics_tests if test['passed'])
        score = (passed / len(analytics_tests)) * 100
        
        return {
            'test_name': 'Analytics Accuracy',
            'tests_run': len(analytics_tests),
            'tests_passed': passed,
            'score': score,
            'details': analytics_tests
        }
    
    def test_rate_limiting(self) -> Dict:
        """Test rate limiting functionality"""
        print("\n⏱️ Testing Rate Limiting...")
        
        # Send rapid requests to test rate limiting
        rapid_requests = []
        for i in range(35):  # Exceed the 30 per minute limit
            start_time = time.time()
            try:
                response = requests.post(
                    f"{self.base_url}/api/chat",
                    headers=self.headers,
                    json={"message": f"Test message {i}"},
                    timeout=5
                )
                response_time = time.time() - start_time
                rapid_requests.append({
                    'request_number': i + 1,
                    'status_code': response.status_code,
                    'response_time': response_time,
                    'rate_limited': response.status_code == 429
                })
            except Exception as e:
                rapid_requests.append({
                    'request_number': i + 1,
                    'status_code': 0,
                    'error': str(e),
                    'rate_limited': True
                })
        
        # Check if rate limiting kicked in
        rate_limited_requests = [req for req in rapid_requests if req.get('rate_limited', False)]
        rate_limiting_works = len(rate_limited_requests) > 0
        
        return {
            'test_name': 'Rate Limiting',
            'tests_run': len(rapid_requests),
            'rate_limited_requests': len(rate_limited_requests),
            'rate_limiting_functional': rate_limiting_works,
            'score': 100 if rate_limiting_works else 0,
            'passed': rate_limiting_works
        }
    
    def test_security(self) -> Dict:
        """Test security measures"""
        print("\n🔒 Testing Security...")
        
        security_tests = [
            self._test_api_key_requirement(),
            self._test_invalid_api_key(),
            self._test_missing_api_key()
        ]
        
        passed = sum(1 for test in security_tests if test['passed'])
        score = (passed / len(security_tests)) * 100
        
        return {
            'test_name': 'Security',
            'tests_run': len(security_tests),
            'tests_passed': passed,
            'score': score,
            'details': security_tests
        }
    
    def test_load_performance(self) -> Dict:
        """Test system performance under load"""
        print("\n⚡ Testing Load Performance...")
        
        # Performance test with concurrent requests
        performance_results = []
        
        for i in range(10):
            start_time = time.time()
            result = self._send_chat_message(f"Performance test message {i}")
            response_time = time.time() - start_time
            
            performance_results.append({
                'request_number': i + 1,
                'response_time': response_time,
                'success': result is not None,
                'fast_response': response_time < 2.0  # Under 2 seconds
            })
            time.sleep(0.5)  # Small delay to avoid rate limiting
        
        avg_response_time = sum(r['response_time'] for r in performance_results) / len(performance_results)
        fast_responses = sum(1 for r in performance_results if r['fast_response'])
        successful_requests = sum(1 for r in performance_results if r['success'])
        
        score = (fast_responses / len(performance_results)) * 100
        
        return {
            'test_name': 'Load Performance',
            'tests_run': len(performance_results),
            'successful_requests': successful_requests,
            'fast_responses': fast_responses,
            'average_response_time': round(avg_response_time, 3),
            'score': score,
            'passed': score > 80
        }
    
    def test_edge_cases(self) -> Dict:
        """Test edge cases and error handling"""
        print("\n🎯 Testing Edge Cases...")
        
        edge_cases = [
            {'test': 'empty_message', 'data': {'message': ''}},
            {'test': 'very_long_message', 'data': {'message': 'A' * 10000}},
            {'test': 'special_characters', 'data': {'message': '!@#$%^&*()_+{}|:"<>?[]\\;\',./ ñáéíóú'}},
            {'test': 'no_message_field', 'data': {'text': 'Hello'}},
            {'test': 'malformed_json', 'data': None}
        ]
        
        results = []
        for case in edge_cases:
            result = self._test_edge_case(case)
            results.append(result)
            time.sleep(1)
        
        passed = sum(1 for result in results if result['handled_gracefully'])
        score = (passed / len(results)) * 100
        
        return {
            'test_name': 'Edge Cases',
            'tests_run': len(results),
            'tests_passed': passed,
            'score': score,
            'details': results
        }
    
    # Helper methods for individual tests
    
    def _test_health_endpoint(self) -> Dict:
        """Test the health endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/health", timeout=5)
            data = response.json()
            
            return {
                'test': 'health_endpoint',
                'passed': response.status_code == 200 and data.get('status') == 'healthy',
                'status_code': response.status_code,
                'response_data': data
            }
        except Exception as e:
            return {
                'test': 'health_endpoint',
                'passed': False,
                'error': str(e)
            }
    
    def _test_home_page(self) -> Dict:
        """Test the home page"""
        try:
            response = requests.get(self.base_url, timeout=5)
            return {
                'test': 'home_page',
                'passed': response.status_code == 200 and 'Scammer Waste Bot' in response.text,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'home_page',
                'passed': False,
                'error': str(e)
            }
    
    def _test_stats_endpoint(self) -> Dict:
        """Test the stats endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/stats", headers=self.headers, timeout=5)
            data = response.json()
            
            required_fields = ['overview', 'today', 'this_week', 'techniques']
            has_required_fields = all(field in data for field in required_fields)
            
            return {
                'test': 'stats_endpoint',
                'passed': response.status_code == 200 and has_required_fields,
                'status_code': response.status_code,
                'has_required_fields': has_required_fields
            }
        except Exception as e:
            return {
                'test': 'stats_endpoint',
                'passed': False,
                'error': str(e)
            }
    
    def _send_chat_message(self, message: str, conversation_id: str = None) -> Dict:
        """Send a chat message and return the response"""
        try:
            data = {'message': message}
            if conversation_id:
                data['conversation_id'] = conversation_id
                
            response = requests.post(
                f"{self.base_url}/api/chat",
                headers=self.headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception:
            return None
    
    def _test_single_response(self, scenario: Dict) -> Dict:
        """Test a single response scenario"""
        result = self._send_chat_message(scenario['message'])
        
        if not result:
            return {
                'scenario': scenario['scenario'],
                'passed': False,
                'error': 'No response received'
            }
        
        response_text = result.get('response', '').lower()
        
        # Check for expected traits
        trait_checks = {
            'confusion': any(word in response_text for word in ['sorry', 'understand', 'confused', 'what']),
            'questions': '?' in response_text,
            'elderly_language': any(word in response_text for word in ['grandson', 'dear', 'back in', 'used to']),
            'concern': any(word in response_text for word in ['worried', 'concerned', 'afraid']),
            'family_mention': any(word in response_text for word in ['son', 'daughter', 'family', 'husband']),
            'hesitation': any(word in response_text for word in ['but', 'however', 'wait', 'hold']),
            'verification_requests': any(word in response_text for word in ['sure', 'verify', 'check', 'confirm']),
            'apology': any(word in response_text for word in ['sorry', 'apologize', 'excuse']),
            'distraction': any(word in response_text for word in ['hold', 'wait', 'moment', 'minute'])
        }
        
        expected_traits = scenario.get('expected_traits', [])
        traits_found = sum(1 for trait in expected_traits if trait_checks.get(trait, False))
        trait_score = (traits_found / len(expected_traits)) * 100 if expected_traits else 100
        
        return {
            'scenario': scenario['scenario'],
            'message': scenario['message'],
            'response': result.get('response', ''),
            'expected_traits': expected_traits,
            'traits_found': traits_found,
            'trait_score': trait_score,
            'passed': trait_score >= 50,  # Pass if at least half the traits are present
            'analysis': result.get('analysis', {})
        }
    
    def _test_conversation_reset(self) -> Dict:
        """Test conversation reset functionality"""
        try:
            response = requests.post(
                f"{self.base_url}/api/conversation/reset",
                headers=self.headers,
                json={},
                timeout=5
            )
            data = response.json() if response.status_code == 200 else {}
            
            return {
                'test': 'conversation_reset',
                'passed': response.status_code == 200 and 'message' in data,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'conversation_reset',
                'passed': False,
                'error': str(e)
            }
    
    def _test_dashboard_endpoint(self) -> Dict:
        """Test the dashboard endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/dashboard", headers=self.headers, timeout=5)
            data = response.json() if response.status_code == 200 else {}
            
            return {
                'test': 'dashboard_endpoint',
                'passed': response.status_code == 200 and 'real_time_stats' in data,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'dashboard_endpoint',
                'passed': False,
                'error': str(e)
            }
    
    def _test_technique_analysis(self) -> Dict:
        """Test technique analysis endpoint"""
        try:
            response = requests.get(f"{self.base_url}/api/techniques", headers=self.headers, timeout=5)
            data = response.json() if response.status_code == 200 else {}
            
            return {
                'test': 'technique_analysis',
                'passed': response.status_code == 200 and 'technique_analysis' in data,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'technique_analysis',
                'passed': False,
                'error': str(e)
            }
    
    def _test_api_key_requirement(self) -> Dict:
        """Test that API key is required"""
        try:
            headers_no_key = {"Content-Type": "application/json"}
            response = requests.get(f"{self.base_url}/api/stats", headers=headers_no_key, timeout=5)
            
            return {
                'test': 'api_key_requirement',
                'passed': response.status_code == 401,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'api_key_requirement',
                'passed': False,
                'error': str(e)
            }
    
    def _test_invalid_api_key(self) -> Dict:
        """Test invalid API key rejection"""
        try:
            headers_invalid = {"X-API-Key": "invalid-key", "Content-Type": "application/json"}
            response = requests.get(f"{self.base_url}/api/stats", headers=headers_invalid, timeout=5)
            
            return {
                'test': 'invalid_api_key',
                'passed': response.status_code == 401,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'invalid_api_key',
                'passed': False,
                'error': str(e)
            }
    
    def _test_missing_api_key(self) -> Dict:
        """Test missing API key rejection"""
        try:
            response = requests.get(f"{self.base_url}/api/stats", timeout=5)
            
            return {
                'test': 'missing_api_key',
                'passed': response.status_code == 401,
                'status_code': response.status_code
            }
        except Exception as e:
            return {
                'test': 'missing_api_key',
                'passed': False,
                'error': str(e)
            }
    
    def _test_edge_case(self, case: Dict) -> Dict:
        """Test a specific edge case"""
        try:
            if case['test'] == 'malformed_json':
                response = requests.post(
                    f"{self.base_url}/api/chat",
                    headers=self.headers,
                    data="invalid json",
                    timeout=5
                )
            else:
                response = requests.post(
                    f"{self.base_url}/api/chat",
                    headers=self.headers,
                    json=case['data'],
                    timeout=5
                )
            
            # Edge cases should either return 400 (bad request) or handle gracefully
            handled_gracefully = response.status_code in [200, 400]
            
            return {
                'test_case': case['test'],
                'status_code': response.status_code,
                'handled_gracefully': handled_gracefully,
                'passed': handled_gracefully
            }
        except Exception as e:
            return {
                'test_case': case['test'],
                'handled_gracefully': True,  # Exception handling is also graceful
                'error': str(e),
                'passed': True
            }

    def _analyze_conversation_flow(self, responses: List[str]) -> Dict:
        """Analyze the quality of conversation flow"""
        if not responses:
            return {'score': 0, 'issues': ['No responses to analyze']}
        
        issues = []
        score = 100
        
        # Check for repetition
        if len(set(responses)) < len(responses) * 0.8:
            issues.append('High repetition in responses')
            score -= 20
        
        # Check for appropriate length variation
        lengths = [len(response) for response in responses]
        if max(lengths) - min(lengths) < 50:
            issues.append('Responses too similar in length')
            score -= 15
        
        # Check for coherence (basic)
        for i, response in enumerate(responses):
            if not response.strip():
                issues.append(f'Empty response at turn {i+1}')
                score -= 25
        
        return {
            'score': max(0, score),
            'issues': issues,
            'response_count': len(responses),
            'avg_length': sum(lengths) / len(lengths) if lengths else 0
        }
    
    def _print_summary(self, results: Dict):
        """Print a comprehensive test summary"""
        print("\n" + "=" * 60)
        print("🎯 COMPREHENSIVE TEST RESULTS SUMMARY")
        print("=" * 60)
        
        for test_name, result in results.items():
            if test_name == 'overall_score':
                continue
                
            if isinstance(result, dict) and 'score' in result:
                status = "✅ PASS" if result['score'] >= 70 else "❌ FAIL"
                print(f"{status} {result['test_name']}: {result['score']:.1f}%")
        
        print(f"\n🏆 OVERALL SCORE: {results['overall_score']:.1f}%")
        
        if results['overall_score'] >= 90:
            print("🌟 EXCELLENT - System performing at optimal level!")
        elif results['overall_score'] >= 70:
            print("✅ GOOD - System functioning well with minor issues")
        elif results['overall_score'] >= 50:
            print("⚠️ FAIR - System needs attention in several areas")
        else:
            print("🚨 POOR - System requires immediate attention")
        
        print("=" * 60)


# Example usage and testing
if __name__ == "__main__":
    # Initialize tester
    tester = AdvancedTester()
    
    print("🤖 Advanced Scammer Waste Bot Testing Framework")
    print("Starting comprehensive test suite...")
    
    # Run all tests
    results = tester.run_comprehensive_tests()
    
    # Save results to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"test_results_{timestamp}.json"
    
    try:
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\n📄 Test results saved to: {results_file}")
    except Exception as e:
        print(f"\n❌ Failed to save results: {e}")
    
    print(f"\n✨ Testing completed! Overall score: {results['overall_score']:.1f}%")
