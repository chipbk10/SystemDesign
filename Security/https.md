I. **What is https?**
- `https` is a secured version of http that ensures data exchanged between a client (e.g., browser, mobile app) and a server is encrypted and protected

II. **How does https work?**
1. **Handshake Initiation**
- When we visit an https webiste, our browser sends a request to the server to start a secure connection
2. **SSL/TLS Certificate**
- The server responds by sending its SSL/TLS [certificate](), which include its public key and proof of its identity (verified by a trusted Certificate Authority - CA)
3. **Verification**
- Our browser checks the [certificate]() to ensure it's valid, not expired, and issued by a trusted CA. 
4. **Key Exchange**
- The client generates a session key, then uses the server's public key to encrypt and send back to server
5. **Secure Communication**
- The server uses its private key to decrypt, and retrieve the session key
- From now on, this session key will be used to secure the rest of the communication (encrypt & decrypt data)

III. **Other questions**
1. **What happens with 2 consecutive api calls?**
- via http `keep-alive`, both calls can reuse the same tcp connection, and share the same session key
  
2. **Where is the symmetric session key stored?**
- from client-side, the session key is stored in memory (e.g., in iOS app, the session key is stored in URLSession instance, in web-app, stored in browser memory)
- from server-side, the session key might be stored in persistent storage (e.g., relational db) or in distributed cache (e.g., reddis, memcache)





