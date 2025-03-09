I. **ClientHello**
- Client sends a message that includes:
1. ssl/tls versions the client supports
2. cipher suites (encryption algorithms, key exchange method, etc.)
3. a client random nonce

II. **ServerHello**
- Server respond a message that includes:
1. ssl/tls version for both side to work on
2. cipher suite for both side to work on
3. a server randome nonce which is combined with the client random nonce to create the symmetric session's key
4. session ID (optional), to avoid a full handshake (< TLS 1.2)

III. **Verify Server Certificate**
IV. **Exchange Symmetric Session Key**
V.**Finished**
