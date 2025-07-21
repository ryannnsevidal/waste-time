#!/bin/bash

# comprehensive deployment script for scammer waste bot

set -e  # exit on any error

echo "🤖 Scammer Waste Bot Deployment Script"
echo "======================================="

# check if docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# check if docker-compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

# function to use either docker-compose or docker compose
docker_compose_cmd() {
    if command -v docker-compose &> /dev/null; then
        docker-compose "$@"
    else
        docker compose "$@"
    fi
}

echo ""
echo "📋 Pre-deployment checklist:"
echo "   ✅ Docker installed"
echo "   ✅ Docker Compose available"

# check if frontend needs to be built
if [ ! -d "interface-imagine-integrate-main/dist" ]; then
    echo "   ⚠️  Frontend not built - will be built in Docker"
else
    echo "   ✅ Frontend already built"
fi

# check if analytics directory exists
if [ ! -d "analytics_data" ]; then
    echo "   📁 Creating analytics_data directory..."
    mkdir -p analytics_data
fi

echo ""
echo "🔧 Deployment Options:"
echo "1) Development (Flask only, port 5001)"
echo "2) Production (Flask + Nginx, ports 80/443)"
echo "3) Development with frontend rebuild"
echo "4) Stop all services"
echo "5) View logs"
echo ""

read -p "Select option (1-5): " choice

case $choice in
    1)
        echo "🚀 Starting development deployment..."
        docker_compose_cmd up --build -d scammer-waste-bot
        echo ""
        echo "✅ Development deployment complete!"
        echo "   📊 Dashboard: http://localhost:5001"
        echo "   🔗 API: http://localhost:5001/api/stats"
        echo "   📞 Webhook: http://localhost:5001/voice"
        ;;
    
    2)
        echo "🚀 Starting production deployment..."
        docker_compose_cmd --profile production up --build -d
        echo ""
        echo "✅ Production deployment complete!"
        echo "   📊 Dashboard: http://localhost"
        echo "   🔗 API: http://localhost/api/stats"
        echo "   📞 Webhook: http://localhost/voice"
        echo "   🔧 Direct backend: http://localhost:5001"
        ;;
    
    3)
        echo "🔄 Rebuilding with fresh frontend..."
        # force rebuild without cache
        docker_compose_cmd build --no-cache scammer-waste-bot
        docker_compose_cmd up -d scammer-waste-bot
        echo ""
        echo "✅ Rebuild complete!"
        echo "   📊 Dashboard: http://localhost:5001"
        ;;
    
    4)
        echo "🛑 Stopping all services..."
        docker_compose_cmd down
        echo "✅ All services stopped!"
        ;;
    
    5)
        echo "📋 Service logs:"
        docker_compose_cmd logs -f
        ;;
    
    *)
        echo "❌ Invalid option selected."
        exit 1
        ;;
esac

if [ "$choice" -le 3 ]; then
    echo ""
    echo "📊 Service Status:"
    docker_compose_cmd ps
    
    echo ""
    echo "🔍 Useful Commands:"
    echo "   View logs: docker-compose logs -f"
    echo "   Stop services: docker-compose down"
    echo "   Restart: docker-compose restart"
    echo "   Shell access: docker-compose exec scammer-waste-bot bash"
    echo ""
    echo "🎯 Ready to waste some scammer time! 🤖👴"
fi
