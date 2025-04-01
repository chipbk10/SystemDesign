I.**Why introduce the term `session` together with `access-token`**?
- with JWT token, the server can only validate it, but cannot track it.
- the server cannot invalidate an access token:
  - either wait until the token is expired itself
  - or the server changes the signing key (which revokes all tokens)
  - with session data, we can invalidate an access token instantly (e.g., change the status to `revoked`)
- the server cannot track the user's activities (like `last-used-at`, `device-info`, etc.)
  - it enables security monitoring (e.g., detecting unusual activity, or ensure that one active device per user at a time)

II.**Trade-off**
- **pros**:
  - the session added a layer of control and flexibility (revocation, tracking user activities) that a stateless token alone can't provide
- **cons**:
  - it seems we move back to the traditional way (e.g., session-id in cookie)
  - waste resources for storing the session data which is shared across microservices
  - for every request, we have to validate the access-token, and then look up a session associated with this access token
 
III.**Hybrid approach**:
- only do the look-up (for session data) for high-security requests or endpoints (e.g., payment service). Ortherwise, fall back to stateless token validation everywhere

IV. **Example**:
```
{
  "session_id": "sess_123456789",
  "user_id": "user_98765",
  "access_token_hash": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
  "status": "active",
  "created_at": "2025-04-01T10:00:00Z",
  "expires_at": "2025-04-01T11:00:00Z",
  "last_used_at": "2025-04-01T10:30:00Z",
  "device_info": "iPhone 14, iOS 18.1"
}
```

IV.**Takeaways**:
- The cost (storage, lookups) is a trade-off for control (e.g., tracking) and security (e.g., invocation).If these features aren't needed, sticking to pure stateless tokens make more sense (less overhead, and better scalability)


  
