I. **Root Certificate**:
- top-level certificate issued by a trusted CA (e.g., DigiCert, Let's Encrypt, Sectigo). It's self-signed, meaning the CA signs its (root) certificate with its own private key
- CA certificates are installed in Browser, OS, and has a very long validity period (e.g., 10-20 years)

II. **Intermediate Certificate**:
- is issued by a root CA (or another intermediate CA). It means the certificate is signed by the root certificate or another intermediate certificate.
- Validity period is shorter than root certificates (e.g., 5-10 years)
- Must be included in your server configuration, and will be sent together with leaf certificate during the TLS handshake
- Represents different types of certificates. For example:
  - single domain (`example.com`), wildcard - secures a domain and all its subdomains (`*.example.com`), multi-domain: secures multiple distinct doamins (example.com, shop.com)
  - DV (domain validation), OV (organization validation), etc.

III. **Leaf Certificate**:
- directly secures your website, proving its identity, and enabling https encryption
- shortest validity period (e.g., 90 days for Let's Encrypt, 1-2 years for paid CAs)
- not used to sign other certificates
- Root Certificate (e.g., ISRG Root X1)
    └── Intermediate Certificate (e.g., Let’s Encrypt R3)
           └── Leaf Certificate (e.g., yourdomain.com)

IV. **How to request certificates from CA?**
- creat a CSR (Certificate Signing Request) on your server, in which specify all info (e.g., domain name, your organization identity, CA etc.)
- it will generate a private key (store it locally on your server), a request form (contains all infos above, and a public key details)
- submit this CSR to a CA, you will receive a leaf certificate & some intermediate certificates
- send all these certificates during the TLS handshake
