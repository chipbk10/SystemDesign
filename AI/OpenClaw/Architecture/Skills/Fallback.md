When the LLM reasons and **cannot find any appropriate skill or tool** to do the job, here’s exactly what happens in OpenClaw:

### Normal Behavior

1. The agent will **not** force itself to use a skill or tool.
2. It will rely only on its **general knowledge** (what the base LLM knows) + the context provided in the prompt (AGENTS.md, SOUL.md, USER.md, recent history, etc.).
3. It will attempt to answer or solve the task using normal reasoning, without calling any tool.

This is the default and safest behavior.

### What the Agent Usually Does

In such cases, a well-written `AGENTS.md` usually instructs the agent to:

- Be honest and say it doesn’t have a specialized skill for this task.
- Ask the user for clarification.
- Offer to solve it with general knowledge if possible.
- Suggest creating a new skill if the task is recurring.

**Typical response pattern:**
- “I don’t have a specific skill for this task, but I can help you with my general knowledge...”
- Or: “This seems like something that would benefit from a dedicated skill. Would you like me to create one?”

### How to Improve This Situation

You can reduce these cases by:
- Writing better, more general descriptions in your existing skills.
- Adding a **meta-skill** or general instruction in `AGENTS.md` like:
  > “If no skill clearly matches the request, use your best general reasoning and tools. Be transparent if you’re unsure.”

- Creating a broad “fallback” skill for common uncategorized tasks.
