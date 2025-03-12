I. **What is ssl-pinning?**
- ssl-pinning or certificate pinning, is a security technique used in applications (especially mobile apps) to ensure that they only communicate with a server using a specific, trusted SSL/TLS certificate or public key.
- without ssl-pinning, the tls handshake only proves that **the certificate (associates with a sepcific domain)** comes from a trusted CA, but might not from the server we want to contact with.

II. **Why is ssl-pinning needed in mobile app?**
- CA can be compromised (rarely, but might happen), or out of date in a specific mobile OS 
- Hacker can install a fake certificate on a device. Pinning prevents this by rejecting any certificate that doesn't match the pinned one.

III. **How to do ssl-pinning?**
- store a public key of a server in mobile app code
- at handshake, check if the public key in the certificate is the same as the pinned public key in code

IV. **The cons**
- if the server's certificate expires or changes, the mobile app must be updated to pin the new certificate

V. **Why isn't ssl-pinning used for web-app?**
1. **TLS layer**:
- web-app (e.g., java-script) cannot access low-level TLS details (like the server's certificate or public key). The handshake are handled at the browser level.
- mobile-app has a control over the handshake process

2. **CA list**
- web-app: CA list is **tied to browser's version**, not OS version. Updating browser (normally is automatically without user intervention) is lightweight (tens of MB)
- mobile-app: CA list is **tied to OS version**. Updates are heavier (GBs). Users are less likely to update mobile OS, due to the size, battery concerns, or lack of support for older devices
  
