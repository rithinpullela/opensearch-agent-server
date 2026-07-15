"""Agentic-search agent: natural-language query -> OpenSearch DSL, via ``/invoke``."""

from __future__ import annotations

from agents.agentic_search.agent import AgenticSearchAgent
from server.config import get_config


def create_agentic_search_agent(opensearch_url: str) -> AgenticSearchAgent:
    """Create the ``agentic_search`` agent (mirrors create_default_agent / create_art_agent)."""
    return AgenticSearchAgent(
        opensearch_url, verify_certs=get_config().opensearch_verify_certs
    )
