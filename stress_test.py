#!/usr/bin/env python3
"""
Stress Testing Suite for Scammer Waste Bot Backend
Tests load capacity, security under pressure, and performance
"""

import requests
import threading
import time
import statistics
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class StressTester:
    def __init__(self, base_url="http://localhost:5001"):
        self.base_url = base_url
        self.api_key = "scammer-waste-api-key-2025"
        self.admin_token = "admin-secure-token-2025"
        self.results = {
            'response_times': [],
            'status_codes': [],
            'errors': [],
            'timestamps': []
        }
    
    def single_request(self, endpoint, method="GET", headers=None, data=None):
        """Make a single request and record metrics"""
        start_time = time.time()
        try:
            if method == "GET":
                response = requests.get(f"{self.base_url}{endpoint}", headers=headers, timeout=10)
            elif method == "POST":
                response = requests.post(f"{self.base_url}{endpoint}", headers=headers, json=data, timeout=10)
            
            end_time = time.time()
            response_time = (end_time - start_time) * 1000  # Convert to ms
            
            return {
                'response_time': response_time,
                'status_code': response.status_code,
                'success': response.status_code < 400,
                'timestamp': datetime.now(),
                'endpoint': endpoint
            }
        except Exception as e:
            end_time = time.time()
            return {
                'response_time': (end_time - start_time) * 1000,
                'status_code': 0,
                'success': False,
                'error': str(e),
                'timestamp': datetime.now(),
                'endpoint': endpoint
            }
    
    def test_homepage_load(self, num_requests=100, concurrent_users=10):
        """Test homepage under load"""
        print(f"\n🏠 TESTING HOMEPAGE LOAD")
        print(f"📊 {num_requests} requests with {concurrent_users} concurrent users")
        
        results = []
        
        def worker():
            return self.single_request("/")
        
        with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            futures = [executor.submit(worker) for _ in range(num_requests)]
            
            for i, future in enumerate(as_completed(futures)):
                result = future.result()
                results.append(result)
                if (i + 1) % 10 == 0:
                    print(f"   Completed {i + 1}/{num_requests} requests")
        
        self.analyze_results(results, "Homepage Load Test")
        return results
    
    def test_api_stress(self, num_requests=200, concurrent_users=20):
        """Test API endpoints under stress"""
        print(f"\n📊 TESTING API STRESS")
        print(f"📈 {num_requests} API requests with {concurrent_users} concurrent users")
        
        results = []
        headers = {'X-API-Key': self.api_key}
        
        def worker():
            return self.single_request("/api/stats", headers=headers)
        
        with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            futures = [executor.submit(worker) for _ in range(num_requests)]
            
            for i, future in enumerate(as_completed(futures)):
                result = future.result()
                results.append(result)
                if (i + 1) % 20 == 0:
                    print(f"   Completed {i + 1}/{num_requests} API requests")
        
        self.analyze_results(results, "API Stress Test")
        return results
    
    def test_rate_limiting(self, requests_per_second=15, duration=60):
        """Test rate limiting effectiveness"""
        print(f"\n🚦 TESTING RATE LIMITING")
        print(f"⚡ {requests_per_second} req/sec for {duration} seconds")
        
        results = []
        start_time = time.time()
        
        while time.time() - start_time < duration:
            batch_start = time.time()
            
            # Send burst of requests
            for _ in range(requests_per_second):
                result = self.single_request("/")
                results.append(result)
                
                # Check if we got rate limited
                if result['status_code'] == 429:
                    print(f"   ✅ Rate limit triggered at {len(results)} requests")
            
            # Wait for next second
            elapsed = time.time() - batch_start
            if elapsed < 1.0:
                time.sleep(1.0 - elapsed)
        
        self.analyze_results(results, "Rate Limiting Test")
        return results
    
    def test_security_under_load(self, num_attacks=50):
        """Test security features under attack conditions"""
        print(f"\n🔒 TESTING SECURITY UNDER LOAD")
        print(f"⚔️  {num_attacks} security tests")
        
        results = []
        
        # Test invalid API keys
        for i in range(num_attacks // 2):
            headers = {'X-API-Key': f'invalid-key-{i}'}
            result = self.single_request("/api/stats", headers=headers)
            results.append(result)
        
        # Test admin endpoint without token
        for i in range(num_attacks // 2):
            result = self.single_request(f"/api/calls/fake-call-{i}/end", method="POST")
            results.append(result)
        
        self.analyze_results(results, "Security Under Load Test")
        return results
    
    def test_memory_leak(self, duration=300, requests_per_minute=60):
        """Test for memory leaks over extended period"""
        print(f"\n🧠 TESTING MEMORY LEAKS")
        print(f"⏰ Running for {duration//60} minutes at {requests_per_minute} req/min")
        
        results = []
        start_time = time.time()
        request_count = 0
        
        while time.time() - start_time < duration:
            result = self.single_request("/api/stats", headers={'X-API-Key': self.api_key})
            results.append(result)
            request_count += 1
            
            if request_count % 10 == 0:
                elapsed = time.time() - start_time
                print(f"   {request_count} requests in {elapsed:.1f}s")
            
            time.sleep(60 / requests_per_minute)  # Pace requests
        
        self.analyze_results(results, "Memory Leak Test")
        return results
    
    def analyze_results(self, results, test_name):
        """Analyze and display test results"""
        if not results:
            print("❌ No results to analyze")
            return
        
        response_times = [r['response_time'] for r in results if 'response_time' in r]
        status_codes = [r['status_code'] for r in results]
        success_count = sum(1 for r in results if r.get('success', False))
        
        print(f"\n📊 {test_name} Results:")
        print(f"   Total Requests: {len(results)}")
        print(f"   Successful: {success_count} ({success_count/len(results)*100:.1f}%)")
        print(f"   Failed: {len(results) - success_count}")
        
        if response_times:
            print(f"   Avg Response Time: {statistics.mean(response_times):.2f}ms")
            print(f"   Min Response Time: {min(response_times):.2f}ms")
            print(f"   Max Response Time: {max(response_times):.2f}ms")
            print(f"   95th Percentile: {np.percentile(response_times, 95):.2f}ms")
        
        # Count status codes
        status_summary = {}
        for code in status_codes:
            status_summary[code] = status_summary.get(code, 0) + 1
        
        print(f"   Status Codes:")
        for code, count in sorted(status_summary.items()):
            print(f"     {code}: {count} requests")
    
    def generate_report(self, all_results):
        """Generate comprehensive test report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"stress_test_report_{timestamp}.json"
        
        report = {
            'timestamp': timestamp,
            'test_results': all_results,
            'summary': {
                'total_requests': sum(len(results) for results in all_results.values()),
                'test_duration': 'varies',
                'overall_success_rate': self.calculate_overall_success_rate(all_results)
            }
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n📄 Report saved to: {report_file}")
        return report_file
    
    def calculate_overall_success_rate(self, all_results):
        """Calculate overall success rate across all tests"""
        total_requests = 0
        total_successful = 0
        
        for results in all_results.values():
            total_requests += len(results)
            total_successful += sum(1 for r in results if r.get('success', False))
        
        return (total_successful / total_requests * 100) if total_requests > 0 else 0
    
    def run_full_stress_test(self):
        """Run comprehensive stress test suite"""
        print("🚀 STARTING COMPREHENSIVE STRESS TEST")
        print("="*60)
        
        all_results = {}
        
        try:
            # Test 1: Homepage load
            all_results['homepage_load'] = self.test_homepage_load(50, 5)
            
            # Test 2: API stress
            all_results['api_stress'] = self.test_api_stress(100, 10)
            
            # Test 3: Rate limiting
            all_results['rate_limiting'] = self.test_rate_limiting(12, 30)
            
            # Test 4: Security under load
            all_results['security_load'] = self.test_security_under_load(30)
            
            # Test 5: Quick memory test (shorter for demo)
            all_results['memory_test'] = self.test_memory_leak(60, 30)
            
        except KeyboardInterrupt:
            print("\n⚠️  Stress test interrupted by user")
        
        print("\n🏁 STRESS TEST COMPLETE")
        print("="*60)
        
        # Generate final report
        report_file = self.generate_report(all_results)
        
        print(f"\n📊 FINAL SUMMARY:")
        print(f"   Overall Success Rate: {self.calculate_overall_success_rate(all_results):.1f}%")
        print(f"   Report File: {report_file}")
        
        return all_results

def quick_stress_test():
    """Quick stress test for immediate feedback"""
    print("⚡ QUICK STRESS TEST")
    
    tester = StressTester()
    
    # Quick tests
    print("\n1. Testing basic connectivity...")
    result = tester.single_request("/")
    if result['success']:
        print("   ✅ Server responding")
    else:
        print("   ❌ Server not responding")
        return
    
    print("\n2. Testing API with valid key...")
    headers = {'X-API-Key': tester.api_key}
    result = tester.single_request("/api/stats", headers=headers)
    if result['success']:
        print("   ✅ API working")
    else:
        print("   ❌ API not working")
    
    print("\n3. Testing rate limiting...")
    rate_limited = False
    for i in range(15):  # Try to trigger rate limit
        result = tester.single_request("/")
        if result['status_code'] == 429:
            rate_limited = True
            break
    
    if rate_limited:
        print("   ✅ Rate limiting active")
    else:
        print("   ⚠️  Rate limiting may not be working")
    
    print("\n✅ Quick stress test complete!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "quick":
        quick_stress_test()
    else:
        tester = StressTester()
        tester.run_full_stress_test()
