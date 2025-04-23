- **communication**
  - in a stock app, a user might tap to add `TSLA` to their watchlist.
  - with WebSocket, the app can send this request over existing connection.
  - with SSE, you'd need a REST API call to update the subscription, then rely on the SSE stream for updates.

- **latency**:
  - SSE has overhead due to http headers

- **data type**:
  - WebSocket supports both text (json, xml) and binary data, allowing you to send complex payloads (e.g., compressed price data, chart updates or multimedia)
  - SSE is limited to UTF-8 text only
    - SSE can encode binary data (e.g., using base64) then put it in a json
    - however, it's not efficient for a large data, and we have to encode/decode

- **reconnection**:
  - when a user's phone switches networks
  - WebSocket can quickly re-establish the connection with less data loss compared to SSE
  - SSE reconnect via `last-event-id` and `retry` fields, but you must implement logic to handle network interruptions manually

- **scalability**
  - Websockets: is better if your app expands to include interactive feature like chat, trade execution, or collaborative watchlists, where bidirectional communication is essential
  - SSE: is best for simple, read-only streams. Adding interactive features requires separate APIs
  - for example: if you later add a feature for users to place trades directly in the app, WebSockets can handle both price updates and trade requests over one connection

- **setup**:
  - SSE uses standard HTTP and is easier to set up than WebSocket servers (e.g., just send `text/event-stream` responses)
  - WebSocket requires:
    - libraries or framework supporting WebSockets
    - implement the first HTTP handshake (to upgrade from HTTP to WebSocket protocol, compute hash-key)
    - after handshake, manage connection (handle open, close, ping/pong, error events, state for each client, implement hearbeats ping/pong to detect inactive clients), handle message frame (that contains data, meta-data, etc.)



