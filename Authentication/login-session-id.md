I. **Session ID**:
- Login with credential (e.g., username & hashed password), the server returns a session-id (a random, unique identifier tied to a session)
- The client stores this session-id in broswer cookie for subsequent requests.
- Pros:
  - low bandwidth (just a 16 bytes string)
  - easy logout or revoke (just delete session associated with session-id in the session store)
  - no need to encrypt or sign
- Cons:
  - costs more resources from server-side
  - **stateful**, maintaining a shared session store across services can be cubersome
  - each requests requires a lookup, update expiration date. That adds latency.

II. **Extend a session**:
- Receiving a session-id, the server looks up in the session store, and updates the expiration time (e.g, reset it to 30 minutes from now)
- Pros: simple logic to keep sessions alive
- Cons: requires a write operation for each request, increasing server load slightly

III. **Applications**:
- **legacy**: many web-app started in mid-2000s when session-ids were dominant approach
- **simplicity for web**: cookies are native to browsers, automatically sent with requests, pair well with server-side session management for monolithic or server-rendered architectures
- **control**: easily invalidate a session without relying on client-side token expiration


