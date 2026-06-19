## Core Definition & Architecture

* What is MCP? Model Context Protocol (MCP) is an open standard that acts like a universal USB-C port for AI, connecting AI clients/harnesses to external or internal resources.
* The Architecture: It uses a Client-Server model operating over a persistent, stateful connection via JSON-RPC 2.0.
* The Transports: It uses two distinct transport layers depending on where the components live:
  * **Stdio** (Standard Input/Output): The default protocol for local communication. The Harness spawns the local MCP server as a background process on the same machine, piping JSON data directly through OS console streams without using the network or web servers.
  * **SSE** (Server-Sent Events): The protocol used exclusively for remote network communication. It establishes a persistent HTTP connection only when the Harness needs to talk to an MCP server hosted on a different computer, a separate container, or in the cloud.

## Why We Need It vs. Traditional Function Calling

* The **Pre-MCP** Era: AI providers already solved text parsing via native Function Calling, which outputs clean JSON. However, developers still had to hardcode the "glue code" and if/else routing rules for every new tool.
* The **MCP** Solution: It completely decouples the AI client from the tool logic. The Harness uses a dynamic, single-time Registry Map to automatically route requests to independent MCP Servers based on the tool name.
* **Ecosystem Scale**: Instead of N AI frameworks writing custom integrations for M enterprise apps (N × M), everyone writes to 1 universal standard (N + M).

## Internal Tools, Parallelism, and Automation

* **Internal Resources**: MCP is not just for cloud APIs; it is heavily used to package and sandbox local shell commands, private databases, and custom python scripts.
* **Execution Handling**: Modern LLMs are forced via API-level constraints to output structured JSON tool choices. The Harness handles parallel calls concurrently (asynchronously) and sequential calls via a managed state history loop.
* **Automated Generation**: You do not have to write MCP servers manually. Open-source CLI tools (like openapi-mcp-generator or FastMCP) can ingest an OpenAPI/Swagger spec and instantly turn your existing web services into a fully functional MCP server.

## Performance & Scaling Reality

* **Latency**: Running an MCP server in a separate process introduces minor Inter-Process Communication (IPC) overhead (1–5 ms). However, this is negligible compared to the seconds an LLM takes to generate tokens.
* **Connection Scaling**: Massive platforms do not host central, public SSE connections for millions of users because maintaining stateful connections scales poorly. Instead, the industry relies on running MCP servers locally via Stdio, which makes calls to external APIs over standard, short-lived, stateless HTTP requests.
