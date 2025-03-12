I. **How does login work in distributed computing world?**
- front-end sends a credential (e.g., username + hashed-password) to server
- server check if the credential valids, then returns a token (session token or access token) to represent the authenticated user
- front-end puts this token in the browser cookie for later use

II. **Session Token**:
- A random, unique identifier tied to a server-side **session store**. Based on this session token (or session id), the server can look up in the session store for user-id for example.
- note that: no need to encrypt or sign as the session token doesn't contain sensitive data, just a random meaningless string
- Pros: @Todo
- Cons: @Todo

III. **Access Token**:
- [jwt token]() = encoded(header).encoded(payload).signature
- payload contains info about user (e.g., user-id, expiration date)
- Pros: @Todo
- Cons: @Todo


