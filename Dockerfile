# Production Flask backend for scammer waste bot
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

# Copy application code
COPY src/ ./src/
COPY run_secure.py .
COPY config/ ./config/

# Create data directories
RUN mkdir -p data/analytics data/logs data/static

# Expose ports
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Default command - Use Gunicorn for production
# Default command - Use Gunicorn for production
CMD ["python", "run_secure.py"]
