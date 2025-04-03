- key:value (as a hash)
- redis offer persistence options, like RDB snapshots or AOF (append-only file) logging that can save data to disk periodically or on every write
- native TTL handles the timeout. Redis automatically evicts expired keys
  - `EXPIRE x7Kp9m 2592000` (30 days).
- redis supports a hash data type (like a mini key-value store within a key). This lets us update inner values **without parsing json**.
  - `HSET abc123 originalUrl "https://example.com" count 7`
  - `HINCRBY abc123 count 1`
  - `HGET abc123 originalUrl`
- redis support transaction that allows you to execute a series of commands as a single unit of work (atomic), ensuring the consistency of your data and providing fast performance.
  - however, transactions add overhead and complexity (e.g., handling failures with retries) 



