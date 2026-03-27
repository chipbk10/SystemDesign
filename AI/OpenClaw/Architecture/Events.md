### Events in OpenClaw

- Events are internal notifications that occur within the OpenClaw Gateway and Agent runtime.

- They represent important moments in the system lifecycle, such as receiving a message, executing a command (`/new`, `/reset`), starting a session, compaction, or gateway startup.

- Events are primarily used by [Hooks]() — small scripts that automatically react when specific events occur. 

- Currently, most events are related to commands, messages, sessions, and lifecycle stages. The event system is relatively limited and cannot be easily extended with custom event types.
