I.**Server-Sent Events**
- **unidirectional communication** where the server push data to the client as a stream of events
- **simple setup**: use standard HTTP
- **connection**: a long-lived HTTP connection, automatic reconnection (via `EventSource` and `retry`)
- **data type**: only text UTF-8
- **use cases**: to be used in cases where the client only needs to receive data
  - live stock tickers
  - sport scores
  - news feeds

 
  
