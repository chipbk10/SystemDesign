I.**Why OAuth?**:
- OAuth allows a third-party application to access a user's resources on a server without sharing the user's credentials (e.g., username & password).

II.**How OAuth works?**
- Third-party app (**client**) redirects you to the authorization server (e.g, Google) with a request (includes the **client-id**, scope, **PKCE**) to access a user's resource
- The authorization server asks the user to approve the request and login
- The authorization server sends a short-lived (10 minutes) `temporary authorization code` back to the third-party app via the redirected URL
- The third-party app takes this code and sends it back (together with client-id, client-secret, pkce) to the authorization server
- The authorization server verifies everything and issues an access-token, and refresh-token back to third-party app
- From now on, the third-party app can access the user's resource

III.**PKCE**:
- The mobile app can't securely store a client secret, instead OAuth uses PKCE (pronounced `pixy`)
- The third-part app generates a random `code verifier`, and a hashed version (called a `code challenge`)
- It sends the challenge with the initial request
- Later, when exchanging the code for an access-token, it must provide the original verifier.
- The authorization server checks if it matches the challenge

IV.**Middle-man-attack**:
- A middle-man with the temporary code can't have the access-token, because he doesn't have the PKCE or client-secret
