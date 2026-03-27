### Internal Hooks
- are automated scripts that run when specific events occur inside the OpenClaw Gateway or Agent runtime.
- They allow custom logic to execute automatically at key moments, such as when a new session is created (/new), a session is compacted, a message is received, or the gateway starts up.
- Each internal hook consists of a HOOK.md metadata file and a handler.ts script.
- They are useful for tasks like logging, auto-backup, injecting messages, or modifying behavior without involving the LLM.

Here's a detailed explanation of how an **Internal Hook** looks like in OpenClaw:

### Structure

An internal hook is a small folder that contains exactly two main files:

#### 1. `HOOK.md` (Metadata File)

This file defines what the hook does and which events it listens to.

```markdown
---
name: session-greeter
description: Sends a friendly welcome message when a new session is created with /new or /reset
metadata:
  openclaw:
    emoji: "👋"
    events:
      - command:new
      - command:reset
---

# Session Greeter Hook

This hook automatically greets the user whenever a new session starts.
It demonstrates how to inject a message directly from a hook.
```

#### 2. `handler.ts` (The Actual Logic)

This is the executable TypeScript code that runs when the subscribed event fires.

```typescript
import type { HookHandler } from '@openclaw/types';

const handler: HookHandler = async (event) => {
  // Only run for the events we care about
  if (event.type !== "command" || 
      (event.action !== "new" && event.action !== "reset")) {
    return;
  }

  console.log(`[session-greeter] New session started: ${event.sessionKey}`);

  // Inject a message that will be sent to the user
  if (Array.isArray(event.messages)) {
    event.messages.push({
      role: "assistant",
      content: "👋 Hello! A fresh session has been started. How can I help you today?"
    });
  }
};

export default handler;
```

### Folder Structure

```
~/.openclaw/hooks/session-greeter/
├── HOOK.md          ← Metadata + events to listen to
└── handler.ts       ← The actual code (required)
```

### How It Works

- When you run `openclaw hooks enable session-greeter`, OpenClaw discovers and registers the hook.
- When a matching event occurs (e.g., user types `/new`), the Gateway fires the event.
- The `handler.ts` is executed automatically.
- The hook can read the event data, modify it (e.g., add messages), perform file operations, log things, or call external APIs.

