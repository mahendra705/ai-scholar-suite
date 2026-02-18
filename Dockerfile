# Stage 1: Builder - install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy dependency definition first for better layer caching
COPY pyproject.toml ./

# Install project dependencies into a virtual environment
RUN python -m venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
RUN pip install --no-cache-dir .

# Copy source code and install the project itself
COPY src/ ./src/
RUN pip install --no-cache-dir .

# Stage 2: Final - minimal runtime image
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application source
COPY src/ ./src/

# Copy startup scripts
COPY start.sh ./start.sh
COPY start_server.py ./start_server.py
RUN chmod +x ./start.sh ./start_server.py

# Expose the API port (Railway will set PORT env var)
# Railway automatically sets PORT environment variable
EXPOSE 8000

# Use Python startup script which properly handles PORT environment variable
# Railway will use startCommand from railway.json, but this is a fallback
CMD ["python", "start_server.py"]
