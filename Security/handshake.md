***

# 🔒 **Short Explanation of the HTTPS Handshake**

When your browser connects to a website using HTTPS, it performs a **TLS handshake** to create a secure, encrypted channel.

### **1. Client → Server: “Hello”**

Your browser sends:

*   supported TLS versions
*   supported cipher suites
*   a random number
*   (optional) client info like SNI = domain name

This is called **ClientHello**.

***

### **2. Server → Client: Certificate + Key Info**

The server responds with:

*   its **TLS certificate** (contains server's *public key*)
*   the chosen cipher suite
*   another random number

This is **ServerHello**.

Your browser **verifies** the certificate:

*   signed by a trusted CA
*   matches the domain
*   not expired/revoked

If valid → continue. If not → security warning.

***

### **3. Client creates a session key**

The client generates a **random symmetric key** (session key) that will be used for encryption.

Then the client encrypts this session key using the server’s **public key** (from the certificate) and sends it to the server.

Server decrypts it using its **private key**.

Now **both sides share the same symmetric session key**.

***

### **4. Secure channel established**

Both sides send a “finished” message encrypted with the newly agreed symmetric key.

At this point:

### ✔ Identity is verified

### ✔ Encryption keys are shared

### ✔ All future data is encrypted symmetrically (fast)

***
