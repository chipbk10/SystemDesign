- eTag is designed to identify a specific version of a resource, mainly for caching.
  1. server receives a HTTP request for a particular resource
  2. server generates an eTag for the resource (e.g., "resource_version1"), and attaches this eTag in HTTP header of the response with status code 200
  3. client represents and caches the resource, together with eTag in HTTP header (for later use)
  4. client sends another request for the same resource together with the eTag (e.g., conditional request header: `If-None-Match: resource_version1`)
  5. server compares current value of eTag with the eTag client sent
  6. if they're the same, server returns status code `304 (Not Modified)` with an empty http body, and client will use its cached resource
  7. if they're not the same, server returns status code `200` with an updated resource and a new eTag (e.g., "resource_version2")
 
- eTag vs idempotency key
  - eTag is tied to a resource's state, mainly for caching
  - idempotency key is tied to a request to avoid duplicate operations
