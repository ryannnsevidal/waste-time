#!/bin/bash

# quick startup script for the dashboard (uses existing build)

echo "🤖 Starting Scammer Waste Bot Dashboard..."

# check if static files exist, if not copy them
if [ ! -d "static" ] || [ -z "$(ls -A static)" ]; then
    echo "📁 Copying frontend files to static directory..."
    mkdir -p static
    cp -r interface-imagine-integrate-main/dist/* static/
fi

# start flask backend
echo "🚀 Starting Flask backend on port 5001..."
python app.py &
BACKEND_PID=$!

# wait for backend to start
sleep 2

echo ""
echo "✅ Dashboard is running!"
echo "   🌐 Dashboard: http://localhost:5001"
echo "   📊 API Stats: http://localhost:5001/api/stats"
echo "   📞 Twilio Webhook: http://localhost:5001/voice"
echo ""
echo "🎯 Ready to waste some scammer time! 🤖👴"
echo ""
echo "Press Ctrl+C to stop..."

# handle shutdown gracefully
trap "echo -e '\n🛑 Stopping service...'; kill $BACKEND_PID 2>/dev/null; exit 0" INT

# keep script running
wait $BACKEND_PID
