I.**HTTP Caching**:
- allows web browsers and other clients (mobile apps) to store copies of web resources locally, this improves performance, reduces latency, and decreases server load.
- it's server driven

II.**How HTTP Caching works?**:
- When a client sends an [idempotent]() request, the server can include caching instructions in the HTTP response headers.
- These instructions tell the client whether, how, and for how long it can cache the resource.
- The next time, the client needs the same resource, it can use the cached version instead of making a new request to the server (assuming the cache is still valid)

III.**HTTP Headers**:

1. Cache-Control:
- `max-age`: how long the resouce is considered fresh
- `no-cache`: forces validation with the server before using the cached version
- `no-store`: caching is not allowed (e.g., for sensitive data)
- `public`: can be cached by any cache (e.g., browsers or proxies - CDN)
- `private`: can only be cached by the end client (e.g., browser, mobile app)

2. Expires:
- specifies an exact date/time when the resouce expires (e.g., Expires: Mon, 31 Mar 2025 12:00:00 GMT)

3. ETag:
- a unique identifier for a specific version of a resource. The client can send this back to the server to check if the resource has changed

4. Last-Modified:
- indicates when the resource was last updated.

IV.**Cache Validation**:
- when a cached resource's freshness expires, the client sends `If-None-Match` (with the ETag) or `If-Modified-Since` (with the Last-Modified date)
- if the resource hasn't changed, the server responds with `304 Not Modified`, and the client uses the cached version
- if it has changed, the server sends the updated resource
