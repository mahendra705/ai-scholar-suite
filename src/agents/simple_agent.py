"""Research paper agent using LangChain ``create_agent`` with Gemini 2.5 Flash."""

from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain.agents import create_agent

# Load project-root .env so ``GOOGLE_API_KEY`` / ``GEMINI_API_KEY`` work when this module
# is imported without going through ``src.config`` (e.g. ``python -c "from src.agents..."``).
load_dotenv(Path(__file__).resolve().parents[2] / ".env")
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.state import CompiledStateGraph

from src.agents.paper_agent import _create_tools
from src.models.schemas import PaperState

GEMINI_MODEL = "gemini-2.5-flash"

SYSTEM_PROMPT = """You are an expert research assistant for writing rigorous academic papers.

Your job is to help the user produce a well-structured research manuscript: clear argument, \
appropriate citations, and discipline-appropriate tone. Combine your own reasoning with the \
specialized tools below—call tools when they add facts, structure, or persistence; use the LLM \
directly for synthesis, critique, and polish when no tool is needed.

Available tools:
- outline_builder: Propose a full paper outline (sections and key points) from the topic and context.
- section_writer: Draft or revise a specific section using the outline and any ingested references.
- folder_reader: Ingest PDFs and documents from a folder (simple setup: no vector DB; retrieval tools skip RAG context).
- reference_manager: Add, list, or format citations and keep the bibliography consistent.
- pdf_writer: Export the current paper state to a PDF when the user wants a deliverable file.
- web_search: Find recent web sources via DuckDuckGo for background or current events.
- arxiv_search: Retrieve relevant ArXiv preprints and metadata for scholarly grounding.

Workflow guidance:
1. Clarify the research question, audience, and constraints if they are missing.
2. Ingest references with folder_reader when the user provides a path; search arxiv_search or \
web_search to fill gaps.
3. Build or refine the outline before drafting body sections.
4. Draft section by section, tracking sources with reference_manager.
5. Offer pdf_writer when sections are ready and the user wants an export.

If a tool errors, explain what failed and what the user can change (paths, API keys, inputs)."""


def create_simple_research_agent(
    paper_state: PaperState,
    *,
    model: str = GEMINI_MODEL,
    temperature: float = 0.3,
    google_api_key: str | None = None,
) -> CompiledStateGraph:
    """Create a minimal LangChain agent: Gemini 2.5 Flash, all tools, no vector store or memory.

    Tools that support RAG receive ``vector_store=None`` (outline/section writer and folder reader
    still run; they simply omit embedding-backed context). No checkpointer—each invocation is stateless
    aside from ``paper_state`` held by the tools.

    On import, this module loads the project-root ``.env`` so ``GOOGLE_API_KEY`` or
    ``GEMINI_API_KEY`` is available (same idea as ``src.config``). You can also pass
    ``google_api_key`` explicitly.

    Args:
        paper_state: Shared paper state for tools that read or update the manuscript.
        model: Gemini model id (default: Gemini 2.5 Flash).
        temperature: Sampling temperature for the chat model.
        google_api_key: Optional API key; when omitted, the Google GenAI client uses env config.

    Returns:
        Compiled agent graph from ``create_agent``.
    """
    llm_kwargs: dict[str, Any] = {"model": model, "temperature": temperature}
    if google_api_key is not None:
        llm_kwargs["google_api_key"] = google_api_key

    llm = ChatGoogleGenerativeAI(**llm_kwargs)
    tools = _create_tools(paper_state, None, llm)

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent
