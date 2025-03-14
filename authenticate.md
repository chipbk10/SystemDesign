I. **How does login work in distributed computing world?**
- front-end sends a credential (e.g., username + hashed-password) to server
- server check if the credential valids, then returns a `session id` or a `session token` (or `access token`) to represent the authenticated user
- front-end puts this token in the browser cookie for later use

II. **Session ID**:
- A random, unique identifier tied to a server-side **session store**. Based on this `session token` (or session id), the server can look up in the session store for user-id for example.
  - Pros:
    - low bandwidth (just a string) in comparison with `session token` (contains user info, signature)
    - easy logout or invalidate a session, just deleting this session from session-store of server-side
    - no need to encrypt or sign as the session token doesn't contain sensitive data, just a random meaningless string  
  - Cons:
    - Storing session data for many users can consume significant memory or database resources
    - Maintaining a shared session store across services can be cumbersome
    - Each request requires a lookup, update expiration date, adding latency
      
- **Refresh a session**: for each request, the server updates the expiration time (e.g., resets it to 30 minutes from now).
  - Pros: Seamless for users; keeps active sessions alive.
  - Cons: Requires a write operation per request, increasing server load slightly.

III. **Access Token**:
- [jwt token]() = encoded(header).encoded(payload).signature
- payload contains info about user (e.g., user-id, expiration date)
- logout:
  - just delete the token from client-side
  - or put this token in a blacklist.
- Pros: @Todo
- Cons: @Todo
- **Refresh a session**:

IV. **In Reality**
- In reality, modern app (FB, Twitter, Google, etc.) use a hibrid approach
  - web: use `session-id` (leverage web-cookie) with Redis (session-store)
  - mobile: use `session-token` (jwt, oauth token)

V. **Solutions in Market**
- Authentication services: Auth0, Firebase, Clerk
- Open source: Lucia, Passport, Keycloak


