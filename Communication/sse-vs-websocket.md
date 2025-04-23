- communication
  - in a stock app, a user might tap to add `TSLA` to their watchlist.
  - with WebSocket, the app can send this request over existing connection.
  - with SSE, you'd need a REST API call to update the subscription, then rely on the SSE stream for updates.

- latency:
  -@Todo 
