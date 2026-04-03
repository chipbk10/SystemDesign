# Sessions

### What is a Session?

A **Session** in OpenClaw is a single continuous conversation transcript. It represents the live back-and-forth chat history between you and the agent.

### Key Details

- Each session is stored as a separate file: `<sessionId>.jsonl`  
  (Location: `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl`)

- **Only the current (active) session** is loaded into the context window.

- OpenClaw creates a **new session** automatically in these cases:
  - Every new day (daily reset at 4:00 AM by default)
  - When you use `/new` or `/reset` command
  - After long idle periods (configurable)

### Important Characteristics

- Sessions are **raw and complete** — they contain every message, tool call, and result.
- Old sessions are **not** automatically sent to the model (to save tokens).
- They are **not indexed** for hybrid search by default.
- Old sessions are kept on disk for:
  - Full history recovery
  - Debugging
  - Manual inspection
  - Backup

### Summary

| Item                    | Description |
|-------------------------|-----------|
| Current Session         | Actively used in context window |
| Old Sessions            | Archived on disk, not auto-loaded |
| Purpose                 | Live conversation + complete history archive |
| Searchability           | Not searchable by default (can be enabled) |

This separation keeps the agent fast and token-efficient while preserving your full conversation history.
