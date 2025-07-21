#!/bin/bash

# startup script to run both backend and frontend together

echo "🤖 starting scammer waste bot dashboard..."

# build react frontend first
echo "building react frontend..."
cd /workspaces/waste-time/interface-imagine-integrate-main
npm install
npm run build

# copy built files to flask static directory
echo "copying frontend files to flask static directory..."
cd /workspaces/waste-time
cp -r interface-imagine-integrate-main/dist/* static/

# start flask backend on port 5001
echo "starting flask backend on port 5001..."
python app.py &
BACKEND_PID=$!

# wait a bit for backend to start
sleep 3

echo "✅ dashboard started!"
echo "   - integrated dashboard: http://localhost:5001"
echo "   - backend API: http://localhost:5001/api/stats"
echo "   - twilio webhook: http://localhost:5001/voice"
echo ""
echo "🎯 ready to waste some scammer time! 🤖👴"
echo ""
echo "press ctrl+c to stop service"

# wait for user to stop process
trap "echo 'stopping service...'; kill $BACKEND_PID; exit" INT
wait
