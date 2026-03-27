### Cron Jobs

- Cron Jobs allow OpenClaw to run scheduled, automated tasks at specific times or intervals without user input.

- They are managed globally by the Gateway and stored in `~/.openclaw/cron/jobs.json`. Each cron job can trigger a message or task to a specific agent (or the default agent).

- Cron jobs support two main session types:
  - **Isolated session**: Runs in a fresh, clean context (recommended for most background tasks).
  - **Main session**: Runs within the main conversation history.

- They are ideal for proactive behaviors such as daily briefings, system checks, backups, or sending scheduled reports. Cron jobs can be created, edited, and managed using the CLI command `openclaw cron`
