I. **Why we send plain text password over https?**
- any message over https is encrypted by a (symmetric) session key, so the plain text password is encrypted also

II.**How server stores password in DB?**
- hash(password + salt)
- DB might look like:
  - username: john
  - salt: 7x9kP2mQ
  - hash: e2fc714c9467e2f2b177e7d66f6872f9
- if DB is compromised, the actual passwords are not revealed (because we don't store password, but a hash)

III.**How to verify password?**
- server received a plain-text password. Server adds the salt, hash the password, and check if it matches the stored hash.

IV.**Why not hash the password from client-side?**
- if we hash the password from client-side, the hash becomes the "password" the server checks, which even makes the security weaker
  
