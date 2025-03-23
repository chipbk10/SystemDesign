I.**Login**:
- Login with credential (username & password), server returns:
  - an [jwt]() access token (user info, short expiration time, signature)
  - an [refresh token]() (just a random unique string that is linked to server user data)
- Pros:
  - stateless, scalable, working in distributed system (microservices)
  - costs less resources from server-side
- Cons:
  - not easy to invalidate a token (blacklist, refresh token list)
  
II.**Extend a session**:
- Client sends the access token in http header (e.g., Authorization: Bearer <access_token>)
- If the access token is expired, the server returns a 401 Unauthorized error
- Client receives 401:
  - sends a separate request to the `token-refresh-endpoint` (e.g., POST /oauth/token) to refresh token
  - server validates the refresh token and returns a new access token, and new refresh token
  - client retries the original request with the new access token

III.**Revoke a token**:
- logout:
  - from client-side: delete the access & refresh tokens 
  - **blacklist**: from server-side: add access token into black-list. The downside is for each request, we have to look up to see if the token is in the black-list. Maintaining a blacklist across different services is cubersome, not scalable.
  - **revoke refresh token**: use short-lived access token (e.g., 15 mins). From server-side, revoke the refresh token (delete or invalide from DB). When the access token is expired, a session cannot extend as the refresh token has been revoked from server. (**best practice**)
 
IV.**Applications**
- Access tokens are used mostly in mobile apps (as cookie is not native in mobile) and apis (as it's stateless)

