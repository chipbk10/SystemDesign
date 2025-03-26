I.**Polling**:
- Polling is a technique where a client repeatedly sends requests to a server at regular intervals to check for updates, new data, or the status of an operation. 

II.**Polling vs Retries**:
- **Retries**: Handle transient failures (e.g., network timeouts, 503 errors) by reattempting the same operation until it succeeds or fails permanently. Triggered by a failure (e.g., an HTTP 500 or timeout).
- **Polling**: Monitor state changes or wait for an async process to complete, not necessarily tied to failures. Triggered by a schedule or need to check progress, regardless of success or failure.

III.**Short Polling**:
- The client repeatedly sends http requests to the server at fixed intervals (e.g., every 5 seconds) to check for updates, and the server responds immediately, whether there’s new data or not.

IV.**Long Polling**:
- The client sends **a http request** to the server, and the server holds the connection open until either new data is available or a timeout occurs. Once the server responds, the client immediately sends a new request to keep the “listening” cycle going.
- Headers like Connection: keep-alive or timeouts can be set to manage how long the server waits.
- pros: simple setup
- cons: server connections overhead

V.**Long Polling vs WebSocket**
- [WebSockets]() offer a persistent, bidirectional connection over a single TCP socket, upgraded from HTTP. Better than Long Polling in terms of efficiency, latency, scalability, simplicity for real-time (e.g., chat, gaming, live updates)
- However, Long Polling wins in terms of
  - working with legacy system or constraints (only work with http, no protocol upgrade),
  - simple setup (no need to upgrade server to WebSocket server),
  - a fallback mechanism when WebSocket connection fails, unavailable or unreliable




