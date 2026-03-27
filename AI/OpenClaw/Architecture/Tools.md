### Tools

Tools are the executable actions that allow an agent to interact with the user’s machine and external services.

They enable the agent to perform real operations such as reading/writing files, running shell commands, browsing the web, editing documents, or controlling the browser.

#### Key Features

- **Built-in Tools**: Core tools like `read_file`, `write_file`, `edit`, `bash` (shell execution), `browser`, `web_search`, etc.
- **Plugin-Provided Tools**: Additional tools can be added through plugins (e.g., GitHub, Linear, Notion, email tools).
- **Safe Execution**: Tools run through the Gateway’s tool runtime with permission controls and optional sandboxing.

#### How Tools Work

When the agent decides to use a tool, it outputs a structured tool call (with name and parameters). The Gateway executes the tool and returns the result to the agent. This forms the **ReAct loop (Reason → Act → Observe)**.

Tools are one of the most powerful features of OpenClaw, as they allow the agent to go beyond chatting and actually **do work** on your behalf.
