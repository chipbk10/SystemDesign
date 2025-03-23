I.**Service Mesh**:
- A service mesh is a dedicated infrastructure layer designed to manage, monitor and secure communication between services in a distributed system

II.**Implementation**
- The key idea here is the service mesh manages service-to-service communication transparently, without requiring changes to the application code.

1. Data Plane:
  - made up of proxies (e.g., Envoy, Linkerd Proxy) deployed as sidecars next to each service instance (e.g., in a Kubernetes pod)
  - these proxies intercept all inbound and outbound traffic, handling tasks like routing, load balancing, retries, and encryption
  - the application doesn't need to know about the proxy - it just sends requests as usual, and the proxy takes care of the rest
  
2. Control Plane:
  - a centralized system that configures and manages the proxies in the data plane
  - define policies (e.g., rate limiting, circuit breaker policies), and **pushes them to the proxies** (via gRPC or http protocols)
  - provide a dashboard or api for operators to monitor and control the mesh

III.**Flow**
- a request from service A to service B through service A's sidecar proxy, which routes it to service B's sidecar proxy, applying any configured rules along the way.

IV.**Features**
1. Traffic management:
  - Routing: direct traffic based on rules (e.g., version-based routing, A/B testing, canary releases)
  - Load Balancing: distribute requests across services
  - Retries & Timeouts: automatically retry failed requests or enforce timeouts
  
2. Resilience:
  - Circuit breaking
  - Rate limiting
  - Fault injection: simulate failures (e.g., delays, errors) to test resilience

3. Security:
  - Encrypt traffic between services
  - Access control: enforce policies like "service A can only call service B"

4. Observability:
  - Metrics: track latency, error rates, and request volume across all services
  - Tracing: follow a request's path through multiple service (e.g., using Jaeger or Zipkin) --> to debug
  - Logging: capture detailed communication logs

V.**Solutions in market**
  - Open-source: Linkerd, Istio
  - Cloud: AWS Mesh Controller
