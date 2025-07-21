#!/usr/bin/env python3
"""
Simple Interactive Demo - Fixed Input Handling
"""

import requests
import json
import time
import random
import csv
import os
from datetime import datetime

def main():
    print("=" * 60)
    print("  SCAMMER WASTE BOT DEMO")
    print("=" * 60)
    
    # Load CSV data
    csv_path = "analytics_data/scammer_analysis_20250720.csv"
    data = []
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    
    print(f"Loaded {len(data)} scammer interactions")
    
    # Check backend
    try:
        resp = requests.get("http://localhost:5001/api/stats", timeout=3)
        print("Backend connected")
    except:
        print("❌ Backend not running")
        return
    
    while True:
        print("\n" + "=" * 40)
        print("OPTIONS:")
        print("1 - Gift Card Scam")
        print("2 - Tech Support Scam") 
        print("3 - IRS Scam")
        print("4 - Dashboard Stats")
        print("7 - Analytics Summary")
        print("0 - Exit")
        print("=" * 40)
        
        try:
            choice = input("Choose (0-7): ").strip()
            print(f"Processing choice: {choice}")
            
            if choice == '0':
                print("Goodbye!")
                break
                
            elif choice == '1':
                if data:
                    call = data[0]  # Gift card scam
                    print(f"\n📞 GIFT CARD SCAM SIMULATION")
                    print(f"Scammer: {call.get('scammer_input')}")
                    print(f"Bot: {call.get('response_preview')}")
                    print(f"Frustration: {call.get('scammer_frustration')}")
                
            elif choice == '2':
                if len(data) > 1:
                    call = data[1]  # Tech support
                    print(f"\n💻 TECH SUPPORT SCAM SIMULATION")
                    print(f"Scammer: {call.get('scammer_input')}")
                    print(f"Bot: {call.get('response_preview')}")
                    print(f"Frustration: {call.get('scammer_frustration')}")
                
            elif choice == '3':
                if len(data) > 2:
                    call = data[2]  # IRS scam
                    print(f"\n🏛️ IRS SCAM SIMULATION")
                    print(f"Scammer: {call.get('scammer_input')}")
                    print(f"Bot: {call.get('response_preview')}")
                    print(f"Frustration: {call.get('scammer_frustration')}")
                
            elif choice == '4':
                try:
                    resp = requests.get("http://localhost:5001/api/stats")
                    stats = resp.json()
                    print(f"\n📊 DASHBOARD STATS:")
                    print(f"Total Calls: {stats.get('totalCalls', 0)}")
                    print(f"Time Wasted: {stats.get('totalTimeWasted', '0h 0m')}")
                    print(f"Success Rate: {stats.get('successRate', '0%')}")
                    print(f"Money Saved: {stats.get('totalSaved', '$0')}")
                except Exception as e:
                    print(f"Error getting stats: {e}")
                
            elif choice == '7':
                print(f"\n📈 ANALYTICS SUMMARY:")
                print(f"Total interactions: {len(data)}")
                total_time = sum(float(row.get('estimated_time_waste', 0)) for row in data)
                print(f"Total time wasted: {total_time} seconds")
                avg_frustration = sum(float(row.get('scammer_frustration', 0)) for row in data) / len(data) if data else 0
                print(f"Average frustration: {avg_frustration:.1%}")
                
            else:
                print("Invalid choice. Try again.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
