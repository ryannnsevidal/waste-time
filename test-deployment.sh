#!/bin/bash

# test script to validate the docker deployment

echo "🧪 Testing Scammer Waste Bot Docker Deployment"
echo "=============================================="

# wait for service to be ready
echo "⏳ Waiting for service to start..."
sleep 10

# test basic endpoint
echo "🔍 Testing basic endpoint..."
if curl -s http://localhost:5001/ > /dev/null; then
    echo "✅ Basic endpoint responding"
else
    echo "❌ Basic endpoint failed"
    exit 1
fi

# test API endpoint
echo "🔍 Testing API endpoint..."
response=$(curl -s -w "%{http_code}" http://localhost:5001/api/stats)
http_code="${response: -3}"

if [ "$http_code" = "200" ]; then
    echo "✅ API endpoint responding with 200"
else
    echo "❌ API endpoint failed with code: $http_code"
    exit 1
fi

# test API response structure
echo "🔍 Testing API response structure..."
api_response=$(curl -s http://localhost:5001/api/stats)

# check if response contains required fields
if echo "$api_response" | grep -q "totalTimeWasted" && \
   echo "$api_response" | grep -q "totalCalls" && \
   echo "$api_response" | grep -q "successRate"; then
    echo "✅ API response structure correct"
    echo "📊 Sample response: $api_response"
else
    echo "❌ API response structure invalid"
    echo "🔍 Actual response: $api_response"
    exit 1
fi

# test webhook endpoint
echo "🔍 Testing webhook endpoint..."
webhook_response=$(curl -s -X POST http://localhost:5001/voice -d "From=%2B15551234567&SpeechResult=Hello")

if echo "$webhook_response" | grep -q "<Response>"; then
    echo "✅ Webhook endpoint responding with TwiML"
else
    echo "❌ Webhook endpoint failed"
    echo "🔍 Response: $webhook_response"
    exit 1
fi

echo ""
echo "🎉 All tests passed! Scammer Waste Bot is ready to waste some time! 🤖👴"
echo ""
echo "📊 Dashboard: http://localhost:5001"
echo "🔗 API Docs: http://localhost:5001/api/stats"
echo "📞 Twilio Webhook: http://localhost:5001/voice"
