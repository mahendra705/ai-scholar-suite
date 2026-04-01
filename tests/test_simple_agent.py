"""Tests for the Gemini-based simple research agent."""

from unittest.mock import MagicMock, patch

import pytest

from src.agents.simple_agent import (
    GEMINI_MODEL,
    SYSTEM_PROMPT,
    create_simple_research_agent,
)
from src.models.schemas import PaperState


@pytest.fixture
def paper_state():
    return PaperState(
        title="Test Paper",
        author="Test Author",
        topic="Machine Learning",
    )


class TestCreateSimpleResearchAgent:
    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_returns_compiled_graph(self, mock_gemini, mock_create_agent, paper_state):
        mock_gemini.return_value = MagicMock()
        mock_graph = MagicMock()
        mock_create_agent.return_value = mock_graph

        result = create_simple_research_agent(paper_state)

        assert result is mock_graph

    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_agent_created_with_all_tools(self, mock_gemini, mock_create_agent, paper_state):
        mock_gemini.return_value = MagicMock()
        mock_create_agent.return_value = MagicMock()

        create_simple_research_agent(paper_state)

        call_kwargs = mock_create_agent.call_args
        tools = call_kwargs.kwargs.get("tools") or call_kwargs[1].get("tools")
        tool_names = {t.name for t in tools}
        expected = {
            "outline_builder",
            "section_writer",
            "folder_reader",
            "reference_manager",
            "pdf_writer",
            "web_search",
            "arxiv_search",
        }
        assert tool_names == expected

    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_no_checkpointer_passed(self, mock_gemini, mock_create_agent, paper_state):
        mock_gemini.return_value = MagicMock()
        mock_create_agent.return_value = MagicMock()

        create_simple_research_agent(paper_state)

        call_kwargs = mock_create_agent.call_args.kwargs
        assert call_kwargs.get("checkpointer") is None

    @patch("src.agents.simple_agent._create_tools")
    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_tools_built_with_no_vector_store(
        self, mock_gemini, mock_create_agent, mock_create_tools, paper_state
    ):
        mock_llm = MagicMock()
        mock_gemini.return_value = mock_llm
        mock_create_agent.return_value = MagicMock()
        mock_create_tools.return_value = []

        create_simple_research_agent(paper_state)

        mock_create_tools.assert_called_once_with(paper_state, None, mock_llm)

    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_system_prompt_configured(self, mock_gemini, mock_create_agent, paper_state):
        mock_gemini.return_value = MagicMock()
        mock_create_agent.return_value = MagicMock()

        create_simple_research_agent(paper_state)

        call_kwargs = mock_create_agent.call_args
        system_prompt = call_kwargs.kwargs.get("system_prompt") or call_kwargs[1].get(
            "system_prompt"
        )
        assert system_prompt == SYSTEM_PROMPT
        assert "research" in system_prompt.lower()
        assert "outline_builder" in system_prompt

    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_llm_created_with_gemini_flash(self, mock_gemini, mock_create_agent, paper_state):
        mock_gemini.return_value = MagicMock()
        mock_create_agent.return_value = MagicMock()

        create_simple_research_agent(paper_state)

        mock_gemini.assert_called_once_with(model=GEMINI_MODEL, temperature=0.3)

    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_google_api_key_passed_when_provided(
        self, mock_gemini, mock_create_agent, paper_state
    ):
        mock_gemini.return_value = MagicMock()
        mock_create_agent.return_value = MagicMock()

        create_simple_research_agent(paper_state, google_api_key="test-key")

        mock_gemini.assert_called_once_with(
            model=GEMINI_MODEL, temperature=0.3, google_api_key="test-key"
        )

    @patch("src.agents.simple_agent.create_agent")
    @patch("src.agents.simple_agent.ChatGoogleGenerativeAI")
    def test_llm_passed_as_model(self, mock_gemini, mock_create_agent, paper_state):
        mock_llm_instance = MagicMock()
        mock_gemini.return_value = mock_llm_instance
        mock_create_agent.return_value = MagicMock()

        create_simple_research_agent(paper_state)

        call_kwargs = mock_create_agent.call_args
        model = call_kwargs.kwargs.get("model") or call_kwargs[1].get("model")
        assert model is mock_llm_instance
