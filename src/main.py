"""Application entry point.

Initializes the FastAPI app with SessionManager, ChromaDB, and CORS middleware.
"""

import logging
import os
import chromadb
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.api.server import create_app
from src.config import get_settings
from src.core.session_manager import SessionManager

logger = logging.getLogger(__name__)


def build_app():
    """Build and configure the full application stack.

    Creates a ChromaDB client/collection, a SessionManager, and the FastAPI app
    with CORS middleware enabled for development.
    """
    try:
        settings = get_settings()
        logger.info(f"Starting application with settings: host={settings.api_host}, port={settings.get_port()}")
        logger.info(f"ChromaDB path: {settings.chromadb_path}")
        logger.info(f"Output dir: {settings.output_dir}")

        # Ensure ChromaDB directory exists
        os.makedirs(settings.chromadb_path, exist_ok=True)
        logger.info(f"ChromaDB directory created/verified: {settings.chromadb_path}")

        # Ensure output directory exists
        os.makedirs(settings.output_dir, exist_ok=True)
        logger.info(f"Output directory created/verified: {settings.output_dir}")

        # ChromaDB persistent client and collection
        chroma_client = chromadb.PersistentClient(path=settings.chromadb_path)
        chroma_collection = chroma_client.get_or_create_collection(name="reference_materials")
        logger.info("ChromaDB client and collection initialized")

        # Session manager
        session_manager = SessionManager()
        logger.info("SessionManager initialized")

        # FastAPI app
        app = create_app(session_manager=session_manager)

        # CORS middleware – allow all origins for development
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Attach shared resources to app state for access in endpoints
        app.state.chroma_client = chroma_client
        app.state.chroma_collection = chroma_collection
        app.state.settings = settings

        logger.info("Application initialized successfully")
        return app
    except Exception as e:
        logger.exception(f"Failed to initialize application: {e}")
        raise


app = build_app()


def main():
    """Run the application with uvicorn."""
    settings = get_settings()
    uvicorn.run(
        "src.main:app",
        host=settings.api_host,
        port=settings.get_port(),
        reload=True,
    )


if __name__ == "__main__":
    main()
