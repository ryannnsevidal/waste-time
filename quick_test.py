#!/usr/bin/env python3
"""
Simple test script to verify demo functionality
"""

import sys
import os

# Add current directory to path
sys.path.append('/workspaces/waste-time')

try:
    from demo_backend import ScammerDemo
    
    print("🧪 Testing Demo Backend...")
    demo = ScammerDemo()
    
    print(f"✅ Demo loaded with {len(demo.analytics_data)} data points")
    
    # Test backend connection
    if demo.check_backend_status():
        print("✅ Backend connection works")
    else:
        print("❌ Backend connection failed")
    
    print("\n🎯 Demo is ready to run!")
    print("Run: python demo_backend.py")
    
except Exception as e:
    print(f"❌ Error testing demo: {e}")
    import traceback
    traceback.print_exc()
