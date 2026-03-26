# Gateway

- OpenClaw uses a clean **hub-and-spoke** design. The **Gateway** is the single long-lived “control plane” (a Node.js daemon) that sits in the middle of everything. Everything else (chat apps, your control clients, mobile nodes, the AI runtime) connects to it like spokes.

- **Only one Gateway per machine** → This is deliberate. It owns all messaging sessions (WhatsApp can only have one active session per device, for example), so there are never conflicts.

- **Protocol**: Typed **WebSocket** JSON (requests/responses + server-push events). First frame must be a connect handshake; everything is validated against JSON Schema. Idempotency keys prevent duplicate actions.

- Gateway does the **heavy lifting**:
  - Validates the message, checks allowlists, DM pairing rules, group mention requirements, etc.
  - Resolves the session (main session = full power; DM/Group = sandboxed by default).
  - Looks up device pairing / auth (crypto challenge-response for remote devices; auto-approve for local/Tailscale).
  - Pushes the event to the Agent Runtime.
 


