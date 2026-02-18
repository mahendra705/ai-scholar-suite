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

# Expose the API port (Railway will set PORT env var)
# Railway automatically sets PORT environment variable
EXPOSE 8000

# Railway will use the startCommand from railway.json instead of CMD
# This CMD is a fallback for local Docker runs
# Use main.py app which includes full setup (ChromaDB, SessionManager, CORS)
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
