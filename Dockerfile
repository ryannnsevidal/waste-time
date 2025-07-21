# Multi-stage build for scammer waste bot with React frontend + Flask backend

# Stage 1: Build React frontend
FROM node:18-alpine as frontend-build

WORKDIR /app/frontend

# Copy frontend package files
COPY interface-imagine-integrate-main/package*.json ./
COPY interface-imagine-integrate-main/bun.lockb ./

# Install dependencies
RUN npm install

# Copy frontend source
COPY interface-imagine-integrate-main/ ./

# Build frontend for production
RUN npm run build

# Stage 2: Python backend with frontend serving
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY . .

# Copy built frontend from previous stage
COPY --from=frontend-build /app/frontend/dist ./static

# Create analytics data directory
RUN mkdir -p analytics_data

# Expose ports
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5001/ || exit 1

# Default command
CMD ["python", "app.py"]
