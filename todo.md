1. **Authentication**
- oauth [**Done**]
- oidc [**Done**]
- sso
- saml

2. **Handle Failures**

- resilience
- fault tolerance
- failover & retries strategies
- rate limiting
- circuit breaker [**Done**]
- service mesh (a sidecar proxy) [**Done**]

3. **Storage**
- CDN
- caching strategies
- nosql
- read-replicas
- sql-sharding
- sql-partitioning
- sql-vertical-scaling (upgrade CPU, RAM, hardware)
- sql-indexes
- sql-batching (combine multiple write operations into a single transaction where possible)
- sql-schema-design (normalize less and denormalize more to reduce write complexity. E.g., fewer joins or foreign key constraints)
- sql-queue-write (with a message broker like Kafka, RabbitMQ or Redis to buffer write requests. The app sends writes to the queue, and a separate worker process handles the actual database updates asynchronously)
- heavy-write: consider the trade-off between consistency and availability
- heavy-read

3. **Others**
- stikcy session
- CAP theorem
- SQL vs NoSQL
- How to migrate from legacy system to clouding service?
