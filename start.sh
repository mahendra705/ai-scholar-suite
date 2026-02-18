#!/bin/bash
# Startup script for Railway deployment
# Reads PORT from environment variable (set by Railway)

set -e

# Get port from environment variable, default to 8000 if not set
PORT=${PORT:-8000}

echo "Starting application on port $PORT"

# Start uvicorn with the port
exec uvicorn src.main:app --host 0.0.0.0 --port "$PORT"

