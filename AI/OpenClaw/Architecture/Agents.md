# Agents

- Loads session state from disk (history + compacted summary).
- Assembles rich context:
  - **System prompts** from workspace files (AGENTS.md, SOUL.md, TOOLS.md, etc.).
  - **Relevant skills** (playbooks in skills/<name>/SKILL.md – only the ones that match the current turn).
  - **Memory search** (hybrid vector + keyword search over past conversations and curated MEMORY.md facts).
- Calls the LLM
- If the model **decides to use a tool** (bash, browser via Chromium CDP, file ops, canvas, etc.), the runtime executes it:
  - Non-main sessions run in an ephemeral Docker sandbox.
  - **Results stream back to the model so it can continue reasoning**.
- Persists the entire turn (messages + tool results) back to disk as an append-only log.
- Gateway formats and sends the final response (or multiple messages) back to the original chat app.




