# Components

- All following markdown files are automatically injected into the **System Prompt** under the **Project Context** section every time the agent processes a turn

## Identity & Personality
- `SOUL.md` - defines tone, personality, boundaries, and communication style
- `IDENTITY.md` - Agent's name, role and self-concept
- `USER.md` - user info (e.g., preferences, background, habit, timezone, important facts, etc)

## Rules & Behavior
- `Agents.md` - operational rules, workflows, safety policies, memory management, and decision-making guidelines

## Memory
- `MEMORY.md` - curated long-term knowledge, facts, preferences, and learned information
- `memory/YYYY-MM-DD.md` - daily logs 

## Periodic Checking
- `HEARTBEAT.md` - checklist and instructions for **proactive** behavior during heartbeat/cron runs

## Tools
- `TOOLS.md` - notes about available tools, usage instructions, environment details, local configuration, and API hints

## Inital Setup
- `BOOTSTRAP.md` - initial setup instructions (only used for new agents)
