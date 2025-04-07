# 🧠 LangGraph ReAct Agent with Claude "Think" Tool

[![CI](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml)
[![Integration Tests](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml)
[![Open in - LangGraph Studio](https://img.shields.io/badge/Open_in-LangGraph_Studio-00324d.svg)](https://langgraph-studio.vercel.app/templates/open?githubUrl=https://github.com/langchain-ai/react-agent)

This template showcases a [ReAct agent](https://arxiv.org/abs/2210.03629) implemented using [LangGraph](https://github.com/langchain-ai/langgraph), extended with a **Claude-style "think" tool** that enables structured internal reasoning before taking any action—ideal for complex multi-step workflows and policy-compliant environments.

> Inspired by Anthropic’s "think" tool for Claude 3.7 and τ-Bench benchmark: [Read the blog post](https://www.anthropic.com/news/the-think-tool)

---

## 🚀 Features

- 🧠 **`think` Tool**: Forces the agent to reflect before acting, logging structured reasoning steps.
- 🔁 **ReAct Agent Loop**: Reason → Act → Observe → Repeat.
- 🔌 **Pluggable Tooling**: Easily integrate new tools (e.g., search, APIs).
- 📚 **Optimized Prompting**: Includes domain-style guidance for better decision-making.
- 🧩 **LangGraph Studio Ready**: Visualize and edit the graph in-browser.

---

## 🔍 What’s New

This fork adds a Claude-inspired `think` tool with the following logic:

```python
def think(thought: str, config: Annotated[RunnableConfig, InjectedToolArg]) -> str:
    """Think tool for structured intermediate reasoning before actions."""
```

Used as a scratchpad to:
- List applicable rules
- Check required information
- Validate planned actions
- Reflect on tool outputs

📌 Prompt template included in `THINK_PROMPT`, used dynamically with `Configuration`.

---

## 📈 Use Cases

- Complex workflows (e.g., booking, support, compliance)
- Long tool-call chains needing internal verification
- Reasoning transparency and debuggability
- Agents operating in policy-heavy domains (e.g., airline, finance, legal)

---

## 🛠️ Getting Started

1. Clone the repo  
2. Create a `.env` file from `.env.example`
3. Install all requirements with `pip install -r requirements.txt`
4. Add your API keys (OpenAI, Tavily)
5. Run in LangGraph Studio

---


## 🧩 File Overview

| File                          | Purpose                                  |
|------------------------------|------------------------------------------|
| `src/agent/tools.py`         | Includes `think` and `search` tools      |
| `src/agent/prompts.py`       | System and think prompt configuration    |
| `src/agent/configuration.py` | Central configuration (e.g. model setup) |

---

## 📚 Resources

- [Anthropic "Think" Tool Post](https://www.anthropic.com/news/the-think-tool)
- [LangGraph Documentation](https://github.com/langchain-ai/langgraph)
- [LangChain Tools Guide](https://python.langchain.com/docs/concepts/#tools)

---

## 🧰 Tools Configuration

You can modify the tool list in `src/agent/tools.py`:

```python
TOOLS: List[Callable[..., Any]] = [search, think]
```

And the system prompt logic in `src/agent/prompts.py`.

---

## ✅ Development Tips

- Use hot reload in LangGraph Studio
- Add custom nodes for internal logging or external validation
- Extend `think()` to support domain-specific policies or memory
