#!/usr/bin/env python3
"""Startup script for Railway deployment.
Reads PORT from environment variable and starts uvicorn server.
"""
import os
import sys

def main():
    # Get port from environment variable, default to 8000 if not set
    port = int(os.getenv("PORT", "8000"))
    host = "0.0.0.0"
    
    print(f"Starting application on {host}:{port}")
    print(f"Python: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")
    
    # Import uvicorn and run the server
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=host,
        port=port,
        log_level="info"
    )

if __name__ == "__main__":
    main()

