### Skills

**Skills** are reusable instruction manuals written in Markdown (`SKILL.md`) that teach the agent how to perform specific tasks or workflows.

They act as "playbooks" that guide the agent step-by-step without requiring the user to specify which tools to use. The agent itself decides which tools to call based on the skill’s instructions and the available tools in its context.

#### Key Features

- Skills are stored in the `skills/` folder (either in the workspace or managed globally).
- Each skill contains a short `description` in its YAML frontmatter so the agent can quickly determine relevance.
- The agent only loads the full `SKILL.md` when it determines the skill is needed, keeping the prompt efficient.
- Skills can describe complex multi-step processes, best practices, and reasoning patterns.

#### Purpose

Skills allow users to extend the agent’s capabilities easily and consistently. Examples include “github-pr-review”, “trip-planning”, “daily-journal”, or “email-summarization”. 

You do **not need to mention specific tool names** in a skill — the agent intelligently selects the appropriate tools on its own.
