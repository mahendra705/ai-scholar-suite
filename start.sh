#!/bin/sh
# Startup script for Railway deployment
# Reads PORT from environment variable (set by Railway)

set -e

# Get port from environment variable, default to 8000 if not set
PORT=${PORT:-8000}

echo "Starting application on port $PORT"
echo "PATH: $PATH"

# Ensure we're using the virtual environment's uvicorn
# The PATH should already include /app/.venv/bin from Dockerfile
exec uvicorn src.main:app --host 0.0.0.0 --port "$PORT"

