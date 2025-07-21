#!/usr/bin/env python3
"""
Interactive Demo for Scammer Waste Bot Backend
Uses real analytics data to simulate scammer interactions
"""

import requests
import json
import time
import random
import csv
import os
from datetime import datetime
from typing import List, Dict

class ScammerDemo:
    def __init__(self, backend_url="http://localhost:5001"):
        self.backend_url = backend_url
        self.analytics_data = self.load_real_data()
        self.active_call_id = None
        self.api_key = os.getenv("SCAMMER_WASTE_API_KEY", "scammer-waste-api-key-2025")  # Production API key from environment
        
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
        print("    SCAMMER WASTE BOT - INTERACTIVE BACKEND DEMO")
        print("="*64)
        print("📊 Loaded {} real scammer interactions".format(len(self.analytics_data)))
        print("🎯 Ready to waste some scammer time!")
        print()
    
    def print_menu(self):
        """Print interactive menu"""
        print("\n" + "="*50)
        print("📞 DEMO OPTIONS:")
        print("="*50)
        print("[1]  Start Gift Card Scam Call")
        print("[2]  Start Tech Support Scam Call") 
        print("[3]  Start IRS/Tax Scam Call")
        print("[4]  View Real-Time Dashboard Stats")
        print("[5]  Simulate Active Call Progress")
        print("[6]  End Current Active Call")
        print("[7]  View Analytics Data Summary")
        print("[0]  Exit Demo")
        print("="*50)
    
    def check_backend_status(self):
        """Check if backend is running"""
        try:
            headers = {"X-API-Key": self.api_key}
            response = requests.get(f"{self.backend_url}/api/stats", headers=headers, timeout=5)
            if response.status_code == 200:
                print("✅ Backend is running at", self.backend_url)
                return True
            else:
                print(f"❌ Backend responded with status {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Backend connection failed: {e}")
            print("💡 Make sure Flask server is running with: python secure_app.py")
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
            # Use any data if no exact match
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
        
        # Simulate adding to backend tracking
        print(f"\n✅ Call {self.active_call_id} is now being tracked by backend")
        return call_data
    
    def get_dashboard_stats(self):
        """Get and display dashboard stats"""
        try:
            headers = {"X-API-Key": self.api_key}
            response = requests.get(f"{self.backend_url}/api/stats", headers=headers)
            if response.status_code == 200:
                stats = response.json()
                
                print("\n📊 LIVE DASHBOARD STATS:")
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
                    
            else:
                print(f"❌ Failed to get stats: HTTP {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to connect to backend: {e}")
    
    def simulate_call_progress(self):
        """Simulate an ongoing call with live updates"""
        if not self.active_call_id:
            print("❌ No active call. Start a scam call first (options 1-3)")
            return
            
        print(f"\n🔴 Simulating live call progress for {self.active_call_id}...")
        print("📊 Watch the dashboard stats update in real-time!")
        
        for i in range(5):
            time.sleep(2)
            duration = (i + 1) * 30
            frustration = min(0.9, (i + 1) * 0.15)
            
            print(f"⏱️  {duration}s - Scammer frustration: {frustration:.1%}")
            
            # Simulate different responses
            responses = [
                "What? I can't hear you dearie, hold on...",
                "Is this about my Medicare? Let me find my glasses...",
                "Gift cards? Do they have pictures of gifts on them?",
                "Microsoft? I thought you were the IRS...",
                "Hold on, my cat is in the computer again..."
            ]
            
            if i < len(responses):
                print(f"🤖 Bot: \"{responses[i]}\"")
        
        print("✅ Call simulation complete! Check dashboard stats (option 4)")
    
    def end_active_call(self):
        """End the current active call"""
        if not self.active_call_id:
            print("❌ No active call to end")
            return
            
        try:
            headers = {"X-API-Key": self.api_key}
            response = requests.post(f"{self.backend_url}/api/calls/{self.active_call_id}/end", headers=headers)
            if response.status_code == 200:
                print(f"✅ Successfully ended call {self.active_call_id}")
                self.active_call_id = None
            else:
                print(f"❌ Failed to end call: HTTP {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to connect to backend: {e}")
    
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
        
        # Count scam types
        scam_types = {}
        strategies = {}
        
        for row in self.analytics_data:
            scam_input = row.get('scammer_input', '')
            strategy = row.get('strategy', 'unknown')
            
            # Categorize scam types
            if 'gift card' in scam_input.lower():
                scam_types['Gift Card'] = scam_types.get('Gift Card', 0) + 1
            elif 'microsoft' in scam_input.lower() or 'computer' in scam_input.lower():
                scam_types['Tech Support'] = scam_types.get('Tech Support', 0) + 1
            elif 'irs' in scam_input.lower() or 'tax' in scam_input.lower():
                scam_types['IRS/Tax'] = scam_types.get('IRS/Tax', 0) + 1
            else:
                scam_types['Other'] = scam_types.get('Other', 0) + 1
                
            strategies[strategy] = strategies.get(strategy, 0) + 1
        
        print(f"📊 Total Interactions: {total_calls}")
        print(f"⏱️  Total Time Wasted: {total_time:.0f} seconds ({total_time/60:.1f} minutes)")
        print(f"😤 Average Scammer Frustration: {avg_frustration:.1%}")
        
        print(f"\n🎭 Scam Types:")
        for scam_type, count in scam_types.items():
            print(f"   {scam_type}: {count} calls")
            
        print(f"\n🤖 Bot Strategies:")
        for strategy, count in strategies.items():
            print(f"   {strategy}: {count} uses")
        
        # Show some sample interactions
        print(f"\n💬 Sample Interactions:")
        for i, row in enumerate(self.analytics_data[:3], 1):
            print(f"   {i}. Scammer: \"{row.get('scammer_input', '')}\"")
            print(f"      Bot: \"{row.get('response_preview', '')}\"")
            print()
    
    def run(self):
        """Run the interactive demo"""
        self.print_header()
        
        if not self.check_backend_status():
            print("❌ Cannot continue without backend connection")
            return
        
        while True:
            self.print_menu()
            
            try:
                choice = input("Select option (0-7): ").strip().lower()
                print(f"You selected: {choice}")  # Immediate feedback
                
                if choice == '0' or choice == 'exit' or choice == 'quit':
                    print("\n👋 Thanks for testing the Scammer Waste Bot!")
                    print("🎯 Keep wasting those scammers' time!")
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
                    print("Fetching dashboard stats...")
                    self.get_dashboard_stats()
                    
                elif choice == '5':
                    print("Starting call progress simulation...")
                    self.simulate_call_progress()
                    
                elif choice == '6':
                    print("Ending active call...")
                    self.end_active_call()
                    
                elif choice == '7':
                    print("Loading analytics summary...")
                    self.show_analytics_summary()
                    
                else:
                    print(f"❌ Invalid option '{choice}'. Please choose 0-7.")
                
                # Add a pause and prompt to continue
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
    demo = ScammerDemo()
    demo.run()
