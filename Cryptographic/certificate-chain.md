I. **Certificate Chain**:
- When a web server (e.g., Apache, Nginx) serves a leaf certificate over https, it typically sends the [leaf certificate](), and the [intermediate certificates]() in the chain (but not the root, as that's assumed to be in the client's trust store).
- For example:
  - Leaf Certificate: `example.com`
  - Intermediate Certificate: `DigiCert SHA2 Secure Server CA`
  - Root Certificate: `DigiCert Global Root CA` (not sent, trusted by the client)

II. **Validation Process**:
1. The client verifies the leaf certificate's signature using the intermediate CA's public key (from the intermediate certificate)
2. The client then verifies the intermediate certificate's signature using the root CA's public key (from its trust store: e.g., browser or OS)
