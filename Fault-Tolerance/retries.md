I.**Retries**
- for many reasons (packet loss, connection loss, temporarily locked access, overloaded, etc.), an API is not stable

II.**Exponential Backoff**
- Increase the delay between retries exponentially (e.g., 1s, 2s, 4s, 8s). Often paired with a max delay (cap).
- with Jitter: add randomness to delay to avoid `synchronized retries`

III.**Should not use retries**
- 400 bad request
- 404 unavailable
- [idempotency]() issue
