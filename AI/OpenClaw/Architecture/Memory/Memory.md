## 1. `MEMORY.md`
- **Purpose**: Long-term, permanent memory.
- Stores important facts, user preferences, key decisions, personal details, project knowledge, and anything that should persist forever.
- **Always loaded** into the system prompt on every session.
- This is the agent’s main “knowledge base”.

## 2. `memory/YYYY-MM-DD.md` (Daily Files)
- **Purpose**: Short-term / episodic memory.
- Used for daily notes, observations, events, action items, and temporary context of that specific day.
- Only **today’s** and **yesterday’s** files are automatically loaded into context.
- Older daily files are kept on disk but must be retrieved manually via `memory_search`.

### Important Note on Writing to Memory

OpenClaw **does not** automatically save notes, observations, or events into these files.  

The agent only writes reliably when:
- You explicitly instruct it (e.g. “Remember that…”, “This is important…”)
- During the automatic **Memory Flush** before compaction

**Recommendation**:  
Define a clear **Memory Protocol** in your **`AGENTS.md`** to teach the agent *when* and *how* to write important information into `MEMORY.md` and daily files.

```markdown
## Memory Protocol

- Always decide what is worth remembering.
- Use `MEMORY.md` for permanent, important facts, preferences, decisions, and user details.
- Use `memory/YYYY-MM-DD.md` for daily notes, events, observations, and temporary context.
- Proactively write important information without being asked when:
  - User states a clear preference or decision
  - A key event, plan, or conclusion happens
  - Something might be needed in future sessions
- During Memory Flush (pre-compaction), summarize and save all relevant context.

When in doubt, write it down.
```

