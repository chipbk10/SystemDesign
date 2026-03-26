# Gateway

- OpenClaw uses a clean **hub-and-spoke** design. The **Gateway** is the single long-lived “control plane” (a Node.js daemon) that sits in the middle of everything. Everything else (chat apps, your control clients, mobile nodes, the AI runtime) connects to it like spokes.

- @Todo
