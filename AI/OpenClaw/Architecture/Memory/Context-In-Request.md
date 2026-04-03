# What OpenClaw sends to LLM on every request?

- Current active [session transcript]() (usually today's conversation). Older sessions are not automatically included. Past sessions are only accessible via tools (`sessions_history`, `memory_search`,etc)
- [System prompt](), e.g, AGENTS.md, SOUL.md, USER.md, TOOLS.md, etc.
- **Long-term memory** (MEMORY.md) is loaded every session by default
- **Short-term daily context** (`memory/today.md`, `memory/yesterday.md`) is automatically injected at the start of the session. Older daily files is only retrieved **on-demand** via `memory_search` tool
- [Tools]() & [Skills]() descriptions are re-sent every time
