#!/usr/bin/env python3
"""
Live Demo of Advanced Scammer Waste Bot
Interactive demonstration of all features
"""
import requests
import time
import json
from datetime import datetime

class BotDemo:
    def __init__(self):
        self.base_url = "http://localhost:5000"
        self.api_key = "scammer-waste-api-key-2025"
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }
        
    def run_demo(self):
        """Run comprehensive demonstration"""
        print("🤖 ADVANCED SCAMMER WASTE BOT - LIVE DEMO")
        print("=" * 60)
        
        # Check system health
        self.check_health()
        
        # Demonstrate AI conversation
        self.demo_conversation()
        
        # Show analytics
        self.show_analytics()
        
        # Display dashboard data
        self.show_dashboard()
        
        print("\n✨ Demo completed successfully!")
    
    def check_health(self):
        """Check system health"""
        print("\n🔍 SYSTEM HEALTH CHECK")
        print("-" * 30)
        
        try:
            response = requests.get(f"{self.base_url}/api/health")
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Status: {data['status']}")
                print(f"📅 Timestamp: {data['timestamp']}")
                print(f"🔢 Version: {data['version']}")
                print("🔧 Components:")
                for component, status in data['components'].items():
                    print(f"   • {component}: {status}")
            else:
                print(f"❌ Health check failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Health check error: {e}")
    
    def demo_conversation(self):
        """Demonstrate AI conversation capabilities"""
        print("\n🗣️ AI CONVERSATION DEMO")
        print("-" * 30)
        
        # Simulate a realistic scammer conversation
        scammer_messages = [
            "Hello, this is Microsoft Technical Support. Your computer has been infected with a dangerous virus.",
            "We detected malicious activity from your IP address. You need to give us remote access immediately.",
            "This is very urgent! Your computer will crash and all your files will be lost if you don't act now!",
            "Why are you asking so many questions? Just follow my instructions!",
            "Sir, you need to download TeamViewer right now so we can fix your computer!"
        ]
        
        conversation_id = f"demo_{int(time.time())}"
        
        for i, message in enumerate(scammer_messages, 1):
            print(f"\n👤 Scammer (Turn {i}): {message}")
            
            try:
                response = requests.post(
                    f"{self.base_url}/api/chat",
                    headers=self.headers,
                    json={
                        "message": message,
                        "conversation_id": conversation_id
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"🧓 Bot Response: {data['response']}")
                    
                    # Show analysis
                    analysis = data['analysis']
                    print(f"📊 Analysis:")
                    print(f"   • Technique: {analysis['technique_detected']}")
                    print(f"   • Frustration Level: {analysis['frustration_level']}/10")
                    print(f"   • Urgency Score: {analysis['urgency_score']}")
                    
                    # Show conversation stats
                    stats = data['conversation_stats']
                    print(f"📈 Stats: {stats['total_turns']} turns, {stats['time_wasted_minutes']:.1f} min wasted")
                    
                elif response.status_code == 429:
                    print("⏱️ Rate limited - waiting...")
                    time.sleep(2)
                    continue
                else:
                    print(f"❌ Error: {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Request failed: {e}")
            
            # Natural delay between messages
            time.sleep(1.5)
    
    def show_analytics(self):
        """Display analytics data"""
        print("\n📊 REAL-TIME ANALYTICS")
        print("-" * 30)
        
        try:
            response = requests.get(f"{self.base_url}/api/stats", headers=self.headers)
            if response.status_code == 200:
                stats = response.json()
                
                overview = stats['overview']
                print(f"📞 Total Conversations: {overview['total_conversations']}")
                print(f"⏰ Time Wasted: {overview['total_time_wasted_hours']:.2f} hours")
                print(f"🎯 Success Rate: {overview['success_rate_percentage']:.1f}%")
                print(f"💰 Cost to Scammers: ${overview['estimated_cost_to_scammers']:.2f}")
                
                print(f"\n📈 Today's Performance:")
                today = stats['today']
                print(f"   • Conversations: {today['conversations']}")
                print(f"   • Time Wasted: {today['time_wasted_minutes']} minutes")
                print(f"   • Top Technique: {today['top_technique']}")
                
                if stats['techniques']:
                    print(f"\n🎭 Scammer Techniques Encountered:")
                    for technique, count in stats['techniques'].items():
                        print(f"   • {technique}: {count} times")
                        
            else:
                print(f"❌ Analytics error: {response.status_code}")
        except Exception as e:
            print(f"❌ Analytics failed: {e}")
    
    def show_dashboard(self):
        """Display dashboard information"""
        print("\n📋 DASHBOARD OVERVIEW")
        print("-" * 30)
        
        try:
            response = requests.get(f"{self.base_url}/api/dashboard", headers=self.headers)
            if response.status_code == 200:
                dashboard = response.json()
                
                daily_report = dashboard['daily_report']
                summary = daily_report['summary']
                
                print(f"📅 Daily Report ({daily_report['report_date']}):")
                print(f"   • Conversations Handled: {summary['conversations_handled']}")
                print(f"   • Total Time Wasted: {summary['total_time_wasted_minutes']} minutes")
                print(f"   • Estimated Cost Impact: ${summary['estimated_cost_impact']}")
                print(f"   • Primary Technique: {summary['primary_technique_encountered']}")
                
                if daily_report['recommendations']:
                    print(f"\n💡 Recommendations:")
                    for i, rec in enumerate(daily_report['recommendations'], 1):
                        print(f"   {i}. {rec}")
                
                forecast = daily_report['next_day_forecast']
                print(f"\n🔮 Tomorrow's Forecast:")
                print(f"   • Predicted Conversations: {forecast['predicted_conversations']}")
                print(f"   • Confidence: {forecast['confidence']}")
                
            else:
                print(f"❌ Dashboard error: {response.status_code}")
        except Exception as e:
            print(f"❌ Dashboard failed: {e}")
    
    def test_technique_analysis(self):
        """Test technique analysis endpoint"""
        print("\n🔍 TECHNIQUE ANALYSIS")
        print("-" * 30)
        
        try:
            response = requests.get(f"{self.base_url}/api/techniques", headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                
                print(f"🎭 Technique Analysis Summary:")
                print(f"   • Total Techniques Detected: {data['total_techniques']}")
                print(f"   • Most Common: {data['most_common']}")
                
                if data['technique_analysis']:
                    print(f"\n📊 Detailed Breakdown:")
                    for technique in data['technique_analysis'][:3]:  # Top 3
                        print(f"   • {technique['technique']}: {technique['encounters']} encounters ({technique['percentage']}%)")
                        
            else:
                print(f"❌ Technique analysis error: {response.status_code}")
        except Exception as e:
            print(f"❌ Technique analysis failed: {e}")


if __name__ == "__main__":
    print("🚀 Starting Live Demo...")
    print("Make sure the server is running at http://localhost:5000")
    print()
    
    demo = BotDemo()
    demo.run_demo()
    
    print("\n" + "=" * 60)
    print("🎉 DEMO COMPLETE!")
    print("🌐 View the web dashboard at: http://localhost:5000")
    print("📚 API Documentation available at the same URL")
    print("🔧 Use the API key: scammer-waste-api-key-2025")
    print("=" * 60)
