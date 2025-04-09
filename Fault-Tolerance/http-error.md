I.**2xx**:
- **201**: created
  
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
- **503**: service unavailable - The server cannot handle the request (because it is overloaded or down for maintenance)
