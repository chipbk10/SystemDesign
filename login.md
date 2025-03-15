I. **How does login work?**
- front-end sends a credential (e.g., username + **plain text** password) to server
- server check if the credential valids, then returns either a `session id` or a `session token` to represent the authenticated user
- front-end store the `session id` in the browser cookie, or the `session token` in local/session storage for later use

II. **[Session ID](https://github.com/chipbk10/SystemDesign/blob/master/login-session-id.md)**:

III. **[Session Token](https://github.com/chipbk10/SystemDesign/blob/master/login-session-token.md)**:

IV. **In Reality**
- In reality, modern app (FB, Twitter, Google, etc.) use a hibrid approach
  - web: use `session-id` (leverage web-cookie) with Redis (session-store)
  - mobile: use `session-token` (jwt, oauth token)

V. **Solutions in Market**
- Authentication services: Auth0, Firebase, Clerk
- Open source: Lucia, Passport, Keycloak


