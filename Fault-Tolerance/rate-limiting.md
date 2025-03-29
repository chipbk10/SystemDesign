I.**Rate Limiting**:
- caps the number of requests a client (e.g., a user, application, or service) can make to a system within a given time window.
- for example, an API might allow 100 requests per minute per user. If the limit exceeded, additional requests are either delayed, queued, or rejected (e.g., 429 - too many requests)

II.**Algorithms**:
- Token Bucket, Leaky Bucket, Fixed Window, Sliding Window (@Todo)

III.**Purposes**:
- **resource protection & security**: protect the system from overwhelming (too many requests at the same time)
- **faireness**: ensure equitable access for all users of services
- **availability**: maintains system uptime by avoiding overload issue
- **cost control**: limits usage in pay-per-use environments (e.g., cloud APIs)

IV.**Where?**
- Rate limiting is often implemented at multiple layers.
  - **client-side**: might throttle requests before sending them to an API
  - **api gateway / load balancer**: limit requests per IP address, or API key before they reach backend services
  - **application / microservices**:
  - **database / storage layer**: limit the number of write operations per second to a database
  - **middleware / service mesh**: limit inter-service calls to prevent one service from overwhelming another
  - **cdn - dynamic content**: block excessive requests at the CDN level before they hit your infrastructure
