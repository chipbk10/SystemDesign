I.**2xx**:
- **200**: ok - success
- **201**: created - data is created
- **202**: accepted - it’s in progress but not guaranteed
  
II.**3xx**:
- **301**: redirect - permanently (cached from front-end)
- **302**: redirect - temporarily (no cache)

III.**4xx**:
- **400**: bad request
- **401**: unauthorized - authentication is required
- **403**: forbidden - has no permission to access the resource
- **404**: not found - temporary unavailable resource
- **429**: too many requests
- **409**: conflict

IV.**5xx**:
- **500**: internal server error
- **502**: **@Todo**
- **503**: service unavailable - The server cannot handle the request (because it is overloaded or down for maintenance)
