**Short Summary: System Prompts in OpenClaw**

### What are System Prompts?

In OpenClaw, the **System Prompt** is the complete set of instructions given to the LLM at the start of every session. It defines the agent's personality, rules, knowledge, and behavior.

### How OpenClaw Builds the System Prompt

OpenClaw automatically combines specific Markdown files (called **bootstrap files**) from your workspace folder:

| File              | Purpose |
|-------------------|--------|
| **AGENTS.md**     | Core operating rules, workflows, memory policy, tool usage, safety |
| **SOUL.md**       | Personality, tone, values, style, and boundaries |
| **USER.md**       | Information about you (preferences, background, habits) |
| **IDENTITY.md**   | How the agent should refer to itself |
| **TOOLS.md**      | Notes and guidelines about available tools |
| **MEMORY.md**     | Long-term memory and important facts |
| **HEARTBEAT.md**  | Optional recurring instructions |
| **BOOTSTRAP.md**  | One-time setup instructions (only on first run) |

These files are concatenated in a specific order and sent as the **System Prompt**.

### Key Points
- Only the above files are automatically included.
- Other `.md` files in the workspace are **not** part of the system prompt unless the agent manually reads them.
- You can heavily customize the agent’s behavior by editing `AGENTS.md` and `SOUL.md`.

This design makes the system prompt transparent, human-readable, and easy to modify.
