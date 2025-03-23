I. **Why bother?**
- Each time, we call a https request, the ssl/tls handshake happens. Note that the handshake is expensive, and it causes latency.

II. **How to avoid ssl/tls handshake overhead for subsequent https requests?**
- the client declares [keep-alive](https://http.dev/keep-alive) in https header
- after the handshake, the server maintains an open tcp connection with the client (a short session: 15-30 seconds)
