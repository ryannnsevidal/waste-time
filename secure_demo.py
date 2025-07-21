#!/usr/bin/env python3
"""
Secure Demo Client for Scammer Waste Bot Backend
Works with the new secure API endpoints
"""

import requests
import json
import time
import random
import csv
import os
from datetime import datetime
from typing import List, Dict

class SecureScammerDemo:
    def __init__(self, backend_url="http://localhost:5001"):
        self.backend_url = backend_url
        self.analytics_data = self.load_real_data()
        self.active_call_id = None
        self.api_key = None
        self.admin_token = None
        self.get_credentials()
        
    def get_credentials(self):
        """Get API credentials for demo"""
        try:
            response = requests.get(f"{self.backend_url}/api/auth/demo-credentials")
            if response.status_code == 200:
                creds = response.json()
                self.api_key = creds['api_key']
                self.admin_token = creds['admin_token']
                print("✅ Retrieved API credentials")
            else:
                print("❌ Could not get API credentials")
        except Exception as e:
            print(f"❌ Error getting credentials: {e}")
        
    def load_real_data(self) -> List[Dict]:
        """Load real scammer data from CSV"""
        data = []
        csv_path = "analytics_data/scammer_analysis_20250720.csv"
        
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        return data
    
    def print_header(self):
        """Print demo header"""
        print("="*64)
        print("    SECURE SCAMMER WASTE BOT - DEMO CLIENT")
        print("="*64)
        print("📊 Loaded {} real scammer interactions".format(len(self.analytics_data)))
        print("🔒 Security features: API authentication, rate limiting, input sanitization")
        print("🎯 Ready to waste some scammer time!")
        print()
    
    def print_menu(self):
        """Print interactive menu"""
        print("\n" + "="*50)
        print("📞 SECURE DEMO OPTIONS:")
        print("="*50)
        print("[1]  Start Gift Card Scam Call")
        print("[2]  Start Tech Support Scam Call") 
        print("[3]  Start IRS/Tax Scam Call")
        print("[4]  View Real-Time Dashboard Stats (API Key Required)")
        print("[5]  Simulate Active Call Progress")
        print("[6]  End Current Active Call (Admin Token Required)")
        print("[7]  View Analytics Data Summary")
        print("[8]  Test Security Features")
        print("[0]  Exit Demo")
        print("="*50)
    
    def check_backend_status(self):
        """Check if secure backend is running"""
        try:
            response = requests.get(f"{self.backend_url}/", timeout=5)
            if response.status_code == 200 and "Security features enabled" in response.text:
                print("✅ Secure backend is running at", self.backend_url)
                return True
            else:
                print(f"⚠️ Backend running but may not be secure version")
                return True
        except requests.exceptions.RequestException as e:
            print(f"❌ Backend connection failed: {e}")
            print("💡 Make sure secure Flask server is running with: python secure_app.py")
            return False
    
    def simulate_scam_call(self, scam_type: str):
        """Simulate a scammer call based on real data"""
        print(f"\n📞 Simulating {scam_type} call...")
        
        # Find matching scam data
        matching_calls = []
        for row in self.analytics_data:
            if scam_type.lower() in row.get('scammer_input', '').lower():
                matching_calls.append(row)
        
        if not matching_calls:
            matching_calls = self.analytics_data[:3]
        
        call_data = random.choice(matching_calls)
        
        # Generate call ID
        self.active_call_id = f"demo_call_{int(time.time())}"
        
        print(f"📱 Incoming call from: +1-555-SCAM-{random.randint(1000, 9999)}")
        print(f"🎭 Scammer says: \"{call_data.get('scammer_input', 'Unknown')}\"")
        print(f"🤖 Bot strategy: {call_data.get('strategy', 'confused_grandpa')}")
        print(f"💬 Bot response: \"{call_data.get('response_preview', 'Huh? What was that dearie?')}\"")
        
        # Show analytics scores
        print(f"\n📊 Real-time Analysis:")
        print(f"   Urgency Score: {call_data.get('urgency_score', 0)}/10")
        print(f"   Authority Score: {call_data.get('authority_score', 0)}/10") 
        print(f"   Payment Score: {call_data.get('payment_score', 0)}/10")
        print(f"   Scammer Frustration: {float(call_data.get('scammer_frustration', 0)):.1%}")
        print(f"   Estimated Time Waste: {call_data.get('estimated_time_waste', 0)} seconds")
        
        print(f"\n✅ Call {self.active_call_id} is now being tracked")
        return call_data
    
    def get_dashboard_stats(self):
        """Get and display dashboard stats using API key"""
        if not self.api_key:
            print("❌ No API key available")
            return
            
        try:
            headers = {'X-API-Key': self.api_key}
            response = requests.get(f"{self.backend_url}/api/stats", headers=headers)
            
            if response.status_code == 200:
                stats = response.json()
                
                print("\n📊 SECURE DASHBOARD STATS:")
                print("="*40)
                print(f"Total Time Wasted: {stats.get('totalTimeWasted', '0h 0m')}")
                print(f"Total Calls: {stats.get('totalCalls', 0)}")
                print(f"Active Now: {stats.get('activeNow', 0)}")
                print(f"Success Rate: {stats.get('successRate', '0%')}")
                print(f"Money Saved: {stats.get('totalSaved', '$0')}")
                print(f"This Week: {stats.get('thisWeek', '0%')}")
                print(f"Last Updated: {stats.get('lastUpdated', 'Unknown')}")
                print(f"System Status: {stats.get('systemStatus', 'Unknown')}")
                
                # Show recent calls
                recent_calls = stats.get('recentCalls', [])
                if recent_calls:
                    print(f"\n📋 Recent Calls ({len(recent_calls)}):")
                    for i, call in enumerate(recent_calls[:3], 1):
                        print(f"   {i}. {call.get('phoneNumber', 'Unknown')} - {call.get('scamType', 'Unknown')} - {call.get('duration', 0)}s")
                
                # Show current call
                current_call = stats.get('currentCall')
                if current_call:
                    print(f"\n🔴 ACTIVE CALL:")
                    print(f"   📱 Number: {current_call.get('phoneNumber', 'Unknown')}")
                    print(f"   ⏱️  Duration: {current_call.get('duration', 0)} seconds")
                    print(f"   🎭 Scam Type: {current_call.get('scamType', 'Unknown')}")
                    
            elif response.status_code == 401:
                print("❌ API key required")
            elif response.status_code == 403:
                print("❌ Invalid API key")
            elif response.status_code == 429:
                print("❌ Rate limit exceeded - too many requests")
            else:
                print(f"❌ Failed to get stats: HTTP {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to connect to backend: {e}")
    
    def end_active_call(self):
        """End the current active call using admin token"""
        if not self.active_call_id:
            print("❌ No active call to end")
            return
            
        if not self.admin_token:
            print("❌ No admin token available")
            return
            
        try:
            headers = {'Authorization': f'Bearer {self.admin_token}'}
            response = requests.post(f"{self.backend_url}/api/calls/{self.active_call_id}/end", headers=headers)
            
            if response.status_code == 200:
                print(f"✅ Successfully ended call {self.active_call_id}")
                self.active_call_id = None
            elif response.status_code == 403:
                print("❌ Admin token required or invalid")
            elif response.status_code == 404:
                print("❌ Call not found")
            elif response.status_code == 429:
                print("❌ Rate limit exceeded")
            else:
                print(f"❌ Failed to end call: HTTP {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to connect to backend: {e}")
    
    def test_security_features(self):
        """Test various security features"""
        print("\n🔒 TESTING SECURITY FEATURES:")
        print("="*40)
        
        # Test 1: API without key
        print("1. Testing API access without key...")
        try:
            response = requests.get(f"{self.backend_url}/api/stats")
            if response.status_code == 401:
                print("   ✅ Correctly blocked - API key required")
            else:
                print("   ❌ Security issue - should require API key")
        except:
            print("   ❌ Connection error")
        
        # Test 2: Invalid API key
        print("\n2. Testing with invalid API key...")
        try:
            headers = {'X-API-Key': 'invalid-key-123'}
            response = requests.get(f"{self.backend_url}/api/stats", headers=headers)
            if response.status_code == 403:
                print("   ✅ Correctly blocked - invalid API key")
            else:
                print("   ❌ Security issue - should reject invalid key")
        except:
            print("   ❌ Connection error")
        
        # Test 3: Admin endpoint without token
        print("\n3. Testing admin endpoint without token...")
        try:
            response = requests.post(f"{self.backend_url}/api/calls/test123/end")
            if response.status_code == 403:
                print("   ✅ Correctly blocked - admin token required")
            else:
                print("   ❌ Security issue - should require admin token")
        except:
            print("   ❌ Connection error")
        
        # Test 4: Rate limiting (multiple requests)
        print("\n4. Testing rate limiting...")
        try:
            requests.get(f"{self.backend_url}/")  # Warm up
            start_time = time.time()
            for i in range(12):  # Exceed 10 per minute limit
                response = requests.get(f"{self.backend_url}/")
                if response.status_code == 429:
                    print("   ✅ Rate limiting active - request blocked")
                    break
            else:
                print("   ⚠️  Rate limiting may not be active")
        except:
            print("   ❌ Connection error")
        
        print("\n🛡️ Security test complete!")
    
    def show_analytics_summary(self):
        """Show summary of loaded analytics data"""
        print("\n📈 ANALYTICS DATA SUMMARY:")
        print("="*50)
        
        if not self.analytics_data:
            print("❌ No analytics data loaded")
            return
        
        # Calculate summary stats
        total_calls = len(self.analytics_data)
        total_time = sum(float(row.get('estimated_time_waste', 0)) for row in self.analytics_data)
        avg_frustration = sum(float(row.get('scammer_frustration', 0)) for row in self.analytics_data) / total_calls
        
        print(f"📊 Total Interactions: {total_calls}")
        print(f"⏱️  Total Time Wasted: {total_time:.0f} seconds ({total_time/60:.1f} minutes)")
        print(f"😤 Average Scammer Frustration: {avg_frustration:.1%}")
        
        # Show some sample interactions
        print(f"\n💬 Sample Interactions:")
        for i, row in enumerate(self.analytics_data[:3], 1):
            print(f"   {i}. Scammer: \"{row.get('scammer_input', '')}\"")
            print(f"      Bot: \"{row.get('response_preview', '')}\"")
            print()
    
    def run(self):
        """Run the secure interactive demo"""
        self.print_header()
        
        if not self.check_backend_status():
            print("❌ Cannot continue without backend connection")
            return
        
        while True:
            self.print_menu()
            
            try:
                choice = input("Select option (0-8): ").strip().lower()
                print(f"You selected: {choice}")
                
                if choice == '0' or choice == 'exit' or choice == 'quit':
                    print("\n👋 Thanks for testing the Secure Scammer Waste Bot!")
                    print("🎯 Keep wasting those scammers' time securely!")
                    break
                    
                elif choice == '1':
                    print("Starting Gift Card Scam simulation...")
                    self.simulate_scam_call("gift card")
                    
                elif choice == '2':
                    print("Starting Tech Support Scam simulation...")
                    self.simulate_scam_call("microsoft computer")
                    
                elif choice == '3':
                    print("Starting IRS/Tax Scam simulation...")
                    self.simulate_scam_call("IRS arrest")
                    
                elif choice == '4':
                    print("Fetching secure dashboard stats...")
                    self.get_dashboard_stats()
                    
                elif choice == '5':
                    print("Simulating call progress...")
                    if not self.active_call_id:
                        print("❌ No active call. Start a scam call first (options 1-3)")
                    else:
                        print(f"🔴 Simulating progress for {self.active_call_id}...")
                        for i in range(3):
                            time.sleep(1)
                            print(f"   ⏱️  {(i+1)*30}s - Scammer getting frustrated...")
                    
                elif choice == '6':
                    print("Ending active call with admin privileges...")
                    self.end_active_call()
                    
                elif choice == '7':
                    print("Loading analytics summary...")
                    self.show_analytics_summary()
                    
                elif choice == '8':
                    print("Testing security features...")
                    self.test_security_features()
                    
                else:
                    print(f"❌ Invalid option '{choice}'. Please choose 0-8.")
                
                print("\n" + "-"*50)
                input("Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Demo interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                print("Please try again...")
                input("Press Enter to continue...")

if __name__ == "__main__":
    demo = SecureScammerDemo()
    demo.run()
