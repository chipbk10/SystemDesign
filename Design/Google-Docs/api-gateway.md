# API GateWay
- handle authentication
- handle rate-limiting
- handle routing requests to application services

## Authentication
- intercepts all incoming REST and WebSockets client request
- extracts the JWT token from the `Authorization` header
- validates it agains Identity Service (e.g., AWS Cognito, Google Identity Platform)
- forwards the request to the application server

# Questions
1. **How does Identity Service work?**
- The Identity Service provides a public key or endpoint (e.g., JWKS endpoint) for the API Gateway to verify JWT signatures, ensuring the token is authentic and untampered
- 
2. **Why don't we implement our own Identity Service?**
- An Identity Service handles:
  - user authentication (e.g., issuing, validating and managing JWT tokens)
  - user management (e.g., sign-up, login, password reset, password policies, and multi-factor authentication)
  - security
  - scalability (e.g., millions JWT validation at once)
  - standard authentication mechanism (e.g., OAuth, Open ID Connect)
  - low latency (10-50ms). Moreover, API Gateway can cache public keys or local validation for subsequent requests (**@Todo**)
- We can implement our own Identity Service, but this increases development and maintenance overhead. And it might introduce security risks if not implemented carefully

3. 
