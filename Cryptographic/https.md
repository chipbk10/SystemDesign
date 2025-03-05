I. **What is https?**
- `https` is a secured version of http that ensures data exchanged between a client (e.g., browser, mobile app) and a server is encrypted and protected
II. **How does https work?**
1. **Handshake Initiation**
- When we visit an https webiste (e.g., https://example.com), our browser sends a request to the server to start a secure connection
2. **SSL/TLS Certificate**
- The server responds by sending its SSL/TLS [certificate](), which include its public key and proof of its identity (verified by a trusted Certificate Authority - CA)
3. **Verification**
- Our browser checks the [certificate]() to ensure it's valid, not expired, and issued by a trusted CA. 
4. **Key Exchange**
- The client generates a session key, then uses the server's public key to encrypt and send back to server
5. **Secure Communication**
- The server uses its private key to decrypt, and retrieve the session key
- From now on, this session key will be used to secure the rest of the communication (encrypt & decrypt data)

@Todo: how 2 consecutive api calls work? api-gateway, load balancing
