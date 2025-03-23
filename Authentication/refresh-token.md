I.**Purpose**:
- a refresh token is a long-lived token (e.g., valids for days or weeks) used to obtain new access tokens without requiring the user to re-enter credentials
- a refresh token is just a random and unique string

II. **Steps to Revoke a Refresh Token Server-Side**:
1. **Login**
- credential valids, the server generates access token (jwt) & refresh token (a string)
- server stores refresh token (assoicates with user info and other metadata) in db or cache
2. **Logout**
- during logout, the client sends the refresh token to logout endpoint (alongside deleting access & refresh tokens locally)
- example: 
  - POST /logout
  - Authorization: Bearer <access_token>
  - Body: { "refresh_token": "abc123-def456" }
3. **Revoke**
- server:
  - validates the refresh token (ensures it exists and matches the user)
  - marks it as revoked or deletes it from the store (db or cache)
4. **Refresh**
- when the client uses a refresh token to get a new access token (e.g., POST /oauth/token), the server checks its status:
  - if revoked or missing, reject the request (401 Unauthorized)
  - if valid, issue a new access token and (a new - more secured or the same - simple logic) refresh token 
