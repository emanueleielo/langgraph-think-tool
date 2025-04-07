"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""
import logging
import os
from typing import Any, Callable, List, Optional, cast, Sequence

import httpx
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg
from tavily import AsyncTavilyClient
from typing_extensions import Annotated

from src.agent.configuration import Configuration
from src.agent.utils import load_chat_model


def search(
    query: str, *, config: Annotated[RunnableConfig, InjectedToolArg]
) -> Optional[list[dict[str, Any]]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    configuration = Configuration.from_runnable_config(config)
    wrapped = TavilySearchResults(max_results=configuration.max_search_results)
    result = wrapped.invoke({"query": query})
    return cast(list[dict[str, Any]], result)

def think(thought: str, config: Annotated[RunnableConfig, InjectedToolArg]) -> str:
    """Use the tool to think about something.
           This is perfect to start your workflow.
           It will not obtain new information or take any actions, but just append the thought to the log and return the result.
           Use it when complex reasoning or some cache memory or a scratchpad is needed.

           :param thought: A thought to think about and log.
           :return: The full log of thoughts and the new thought.
    """
    configuration = Configuration.from_runnable_config(config)
    think_prompt = configuration.think_prompt.format(thought=thought)
    response  = load_chat_model(configuration.model).invoke(think_prompt)
    return response.content


TOOLS: List[Callable[..., Any]] = [search,think]
