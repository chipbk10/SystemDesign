I.**Why not OAuth & access Profile?**
- because OAuth is to grant access to a resource, not to identify
- OAuth access-token is not standardized, is up to implementation from authorization server (e.g., Google uses an opaque token, Facebook uses jwt token)

II.**OIDC**
- is built on top of OAuth.
- the difference is authorization server returns an jwt id-token (together with access-token) which contains user info in the claims

III.**Flow**
1. `client-app` registers with `authorization-server`
```
client-id = todoapp-123
redirect-uri = https://todoapp.com/callback
```
2. `client-app` redirects user to `login-web-page`
- nonce: client generate a random string (to prevent token replay)
- code_challenge = hashed(pkce)
```
https://accounts.google.com/o/oauth2/v2/auth?
  client_id=todoapp-12345&
  response_type=code&
  scope=openid%20profile%20email%20https://www.googleapis.com/auth/calendar&
  redirect_uri=https://todoapp.com/callback&
  nonce=xyz789& 
  code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM&
  code_challenge_method=S256
```   
3. user authenticates and approves
4. `authorization-server` returns a `temporary-code` to `client-app`
```
https://todoapp.com/callback?code=4/P7q7W91a-oMsCeLvIaQm6bTrgtp7
```
5. `client-app` exchanges `temporary-code` (together with other info) to `authorization-server` for `id-token`
```
POST https://oauth2.googleapis.com/token
  Content-Type: application/x-www-form-urlencoded

  client_id=todoapp-12345&
  code=4/P7q7W91a-oMsCeLvIaQm6bTrgtp7&
  redirect_uri=https://todoapp.com/callback&
  grant_type=authorization_code&
  code_verifier=aVeryLongRandomString123
```
6. `authorization-server` verifies and return `id-token`
```
{
  "access_token": "ya29.a0AfH6SMD...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "1//xEoDL4iW3cXl...",
  "id_token": "eyJhbGciOiJSUzI1NiIs..."
}
```
- `id-token` looks like:
```
{
  "iss": "https://accounts.google.com",
  "sub": "123456789012345678901",
  "aud": "todoapp-12345",
  "exp": 1711033200,
  "iat": 1711029600,
  "nonce": "xyz789",
  "name": "Alice Smith",
  "email": "alice@gmail.com"
}
```
7. `client-app` exchanges `id-token` for `access-token` (& `refresh-token`) with `server-app`

8. from now on, `client-app` uses `access-token` (together with `refresh-token`) to keeps the user logged in.
