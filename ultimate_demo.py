#!/usr/bin/env python3
"""
Ultimate Grandpa Bot Demo
Showcases the massive response collection with hundreds of variations
"""

import random
import time
from massive_responses import *
from gift_card_numbers import *

def ultimate_gift_card_scam_demo():
    """The ultimate gift card scam scenario with maximum time wasting"""
    
    print("💳 ULTIMATE GIFT CARD SCAM SCENARIO 💳")
    print("=" * 45)
    print()
    print("This scenario shows how Grandpa can waste 30+ minutes of a scammer's time...")
    print()
    
    # Progressive scammer desperation
    scammer_script = [
        "Hello sir, you owe $500 in back taxes to the IRS",
        "You need to pay immediately with Target gift cards", 
        "Go to the store and buy $500 worth of gift cards",
        "Are you at the store yet? This is urgent!",
        "Okay, now scratch off the back of the cards",
        "I need you to read me the numbers on the cards",
        "Sir, can you please read the activation codes?",
        "The numbers! Just give me the numbers!",
        "Why is this taking so long?!",
        "Sir, are you still there?!"
    ]
    
    grandpa_tactics = [
        "general_confusion",
        "gift_card_confusion", 
        "physical_limitations",
        "hold_music",
        "number_reading_disaster",
        "maximum_time_waste",
        "suspicious_questions",
        "complete_derailment",
        "final_confusion",
        "victory"
    ]
    
    for i, (scammer_line, tactic) in enumerate(zip(scammer_script, grandpa_tactics)):
        print(f"📞 Scammer: {scammer_line}")
        
        # Generate response based on tactic
        if tactic == "general_confusion":
            response = get_response_by_category('irs_authority')
        elif tactic == "gift_card_confusion":
            response = get_response_by_category('gift_cards')
        elif tactic == "physical_limitations":
            response = "I can't drive to the store, my license expired in 1987..."
        elif tactic == "hold_music":
            response = get_response_by_category('hold_music')
        elif tactic == "number_reading_disaster":
            response = get_gift_card_number_response()
        elif tactic == "maximum_time_waste":
            response = get_maximum_time_waster()
        elif tactic == "suspicious_questions":
            response = "What's your badge number? I need to verify you're really from the IRS..."
        elif tactic == "complete_derailment":
            response = "That reminds me of my prize-winning tomatoes from 1962..."
        elif tactic == "final_confusion":
            response = "Numbers? I thought we were talking about gift cards..."
        else:  # victory
            response = "Oh, you hung up. That was rude! *goes back to watching TV*"
            
        print(f"👴 Grandpa: {response}")
        print()
        
        # Add realistic timing
        if "hold" in response.lower() or "🎵" in response:
            print("   *Scammer waits on hold, getting increasingly frustrated*")
            time.sleep(2)
        else:
            time.sleep(1)
        
        # Scammer gives up at some point
        if i >= 7 and random.random() < 0.3:
            print("📱 *Scammer hangs up in rage* 📱")
            print("🎉 GRANDPA WINS! Time wasted: 30+ minutes! 🎉")
            return
    
    print("📱 *Scammer finally gives up* 📱")
    print("🎉 GRANDPA WINS! Mission accomplished! 🎉")

def show_response_statistics():
    """Show statistics about the response collection"""
    
    print("📊 RESPONSE COLLECTION STATISTICS 📊")
    print("=" * 40)
    print()
    
    stats = {
        "Gift Card Responses": len(GIFT_CARD_RESPONSES),
        "Hold Music Responses": len(HOLD_MUSIC_RESPONSES), 
        "Tech Support Responses": len(TECH_SUPPORT_DEEP),
        "IRS/Authority Responses": len(IRS_AUTHORITY_DEEP),
        "Romance/Inheritance": len(ROMANCE_INHERITANCE_DEEP),
        "Gift Card Number Responses": len(GIFT_CARD_NUMBER_RESPONSES),
        "Number Reading Holds": len(NUMBER_READING_HOLDS),
        "Max Time Waste": len(MAX_TIME_WASTE_NUMBERS),
        "Combo Responses": len(COMBO_RESPONSES)
    }
    
    total_responses = sum(stats.values())
    
    for category, count in stats.items():
        percentage = (count / total_responses) * 100
        print(f"• {category:<25}: {count:3d} responses ({percentage:4.1f}%)")
    
    print()
    print(f"🎯 TOTAL UNIQUE RESPONSES: {total_responses}")
    print(f"💪 SCAMMER FRUSTRATION LEVEL: MAXIMUM")

def trap_queen_hold_music_showcase():
    """Showcase the Trap Queen inspired hold music responses"""
    
    print("🎵 TRAP QUEEN INSPIRED HOLD MUSIC SHOWCASE 🎵")
    print("=" * 50)
    print()
    print("When Grandpa puts scammers on hold with style...")
    print()
    
    # Show different types of hold music
    hold_scenarios = [
        "Looking for gift cards",
        "Finding reading glasses", 
        "Getting tax papers",
        "Calling neighbor Harold",
        "Making tea for 20 minutes"
    ]
    
    for scenario in hold_scenarios:
        print(f"👴 Grandpa: 'Hold on, I'm {scenario}...'")
        hold_response = get_response_by_category('hold_music')
        print(f"🎼 {hold_response}")
        print()
        time.sleep(1.5)
    
    print("🎶 Result: Scammer listens to off-key humming for 30 minutes! 🎶")

def scammer_frustration_meter():
    """Show how different responses affect scammer frustration"""
    
    print("😤 SCAMMER FRUSTRATION METER 😤")
    print("=" * 35)
    print()
    
    frustration_levels = [
        ("Basic confusion", "😐", "Low - scammer still hopeful"),
        ("Gift card confusion", "😕", "Medium - scammer getting annoyed"),
        ("Hold music", "😠", "High - scammer waiting impatiently"), 
        ("Number reading disaster", "😡", "Very High - scammer losing patience"),
        ("Maximum time waster", "🤬", "EXTREME - scammer about to hang up"),
        ("Combo response", "💀", "NUCLEAR - scammer hangs up in rage")
    ]
    
    for response_type, emoji, description in frustration_levels:
        print(f"{emoji} {response_type:<25}: {description}")
        time.sleep(0.5)
    
    print()
    print("🎯 GOAL: Reach maximum frustration as quickly as possible!")

def interactive_response_generator():
    """Interactive tool to generate responses for specific scammer lines"""
    
    print("🎮 INTERACTIVE RESPONSE GENERATOR 🎮")
    print("=" * 40)
    print()
    print("Enter scammer lines and get contextually appropriate responses!")
    print("Type 'quit' to exit.")
    print()
    
    while True:
        scammer_line = input("📞 Enter scammer line: ").strip()
        
        if scammer_line.lower() in ['quit', 'exit']:
            break
            
        if not scammer_line:
            continue
        
        # Show multiple response options
        print("\n👴 Grandpa's response options:")
        print()
        
        for i in range(3):
            response = get_contextual_response(scammer_line)
            frustration = random.choice(["😐", "😕", "😠", "😡", "🤬"])
            print(f"{i+1}. {response} {frustration}")
        
        print()

def main():
    """Ultimate demo menu"""
    
    print("🤖👴 ULTIMATE GRANDPA SCAM-WASTING BOT DEMO 👴🤖")
    print("=" * 60)
    print()
    print("💯 FEATURING HUNDREDS OF UNIQUE RESPONSES! 💯")
    print()
    
    while True:
        print("Choose a demo:")
        print("1. 💳 Ultimate Gift Card Scam Scenario")
        print("2. 📊 Response Collection Statistics")
        print("3. 🎵 Trap Queen Hold Music Showcase") 
        print("4. 😤 Scammer Frustration Meter")
        print("5. 🎮 Interactive Response Generator")
        print("6. 🎯 Run All Demos")
        print("7. 🚪 Exit")
        print()
        
        choice = input("Enter choice (1-7): ").strip()
        print()
        
        if choice == "1":
            ultimate_gift_card_scam_demo()
        elif choice == "2":
            show_response_statistics()
        elif choice == "3":
            trap_queen_hold_music_showcase()
        elif choice == "4":
            scammer_frustration_meter()
        elif choice == "5":
            interactive_response_generator()
        elif choice == "6":
            # Run all demos
            demos = [
                ultimate_gift_card_scam_demo,
                show_response_statistics, 
                trap_queen_hold_music_showcase,
                scammer_frustration_meter
            ]
            for demo in demos:
                demo()
                print("\n" + "="*60 + "\n")
        elif choice == "7":
            print("👋 Thanks for testing the Ultimate Grandpa Bot!")
            print("🎉 Now go waste some scammers' time! 🎉")
            break
        else:
            print("❌ Invalid choice. Please try again.")
            print()
        
        input("\nPress Enter to continue...")
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
