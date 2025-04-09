I.**Representational State Transfer - REST**:
- is a set of principles
1. **Client-Server**
- client & server are separate entities - no tight coupling
2. **Stateless**
- each request from client must contain all information needed to process it.
- the server doesn't store client state between requests
3. **Cacheable**
- server must indicate if the response can be cached (e.g., via [cache-control]() or [etag]())
4. **Uniform interface**:
- each resource has a unique URI
- client interacts with resources using representations (e.g., json, xml), not directly with server's database
- requests and responses include enough info (e.g., http methods, status code) to describe the action
5. **Layered system**:
- the client doesn't need to know if it's talking directly to the server or an intermediary (e.g., a CDN or load balancer)

II.**RESTful**:
- is a REST uses http methods (GET, PUT, etc.) as verbs to act on resources, and it avoids verbs in the URL
- For example:
  - non-RESTful: `GET /fetchOrderDetails/123`
  - RESTful: `GET /orders/123`

III. **HTTP methods**:
- **GET**: retrieve a resource
- **POST**: create a resource
- **PUT**: update (or replace) a resource
  - `**PUT** /orders/123` -> Replace the entire order 123 
- **PATCH**: partially update a resource
  - `**PATCH** /orders/123` -> partially update order 123 (e.g., change status)
- **DELETE**: remove a resource
