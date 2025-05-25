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
- **@Todo**
  
2. **Why don't we implement our own Identity Service?**
- An Identity Service handles:
  - user authentication (e.g., issuing, validating and managing JWT tokens)
  - user management (e.g., sign-up, login, password reset, password policies, and multi-factor authentication)
  - security
  - scalability (e.g., millions JWT validation at once)
  - standard authentication mechanism (e.g., OAuth, Open ID Connect)
  - low latency (10-50ms). Moreover, API Gateway can cache public keys or local validation for subsequent requests (**@Todo**)
- We can implement our own Identity Service, but this increases development and maintenance overhead. And it might introduce security risks if not implemented carefully

3. **So, we don't store User data in our database?**
- We don't store comprehensive user data (e.g., email, password, profile details) in our database
- We store only minimal user-related data (e.g., user_id, roles) necessary for document operations.
- In case, user metadata is needed (e.g., display name for UI), we can fetch it from the Identity Service on-demand (e.g., our Application Server calls API Gateway at user profile endpoint) and cache it in the caching service (e.g., AWS Redis, Google Cloud Memorystore)

4. **What happens if a user is blacklisted?**
- If a user is blacklisted (e.g., their account is revoked or marked for revocation in the Identity Service), their ability to access our system is blocked, but their presence in the `Collaborators` list is still there.
- The application server can periodically run a batch job to remove blacklisted users from `Collaborators` list. Then we notify the document owner or other collaborators via Messaging Service if needed
- if the blacklisted user is the owner of a document, we can:
  - either ignore the ownership, the other collaborators remain the edit/view access
  - or transfer the ownership to the admin or other collaborators (e.g., the first edit collaborator)
  - or archive document if now suitable owner is available. It can be recovered when the ownership is resolved.
