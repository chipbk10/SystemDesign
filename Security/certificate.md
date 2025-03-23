I.**What is the problem? A [digital signature]() is not good enough?**
- You can a private key to sign a document, then send this document together with your signature and public key to someone. Then someone can use your public key to decrypt the signature, recompute the hash and check if 2 hashes match.
- However, anyone could generate a key pair, sign a document, and send it along with a public key, and **claiming to be you**.
- Note that the public key is just to verify that the signature is made by the person who owns the public key
- The recipient has no way to confirm that **the person who owns the public key is really you**, unless the recipient relies on a trusted third party (**CA**) who confirms that this public key belongs to you.

II. **Certificate Authority (CA)**
- You have to contact with CA, providing your identity (e.g., official documents or other means), and your public key
- CA creates **a digital certificate** that contains your public key, your identity (e.g., name, email) and other metadata (expiry date, etc.). CA signs this certificate with its own private key
- Now, you send the document along with your signature, and your certificate to the recipient
- The recipient will verify the certificate by trying all public keys from a list of trusted CA he knows to decrypt the certificate.
- After decrypting the certificate, the recipient can see your public key, and he can believe that this public key really belongs to you (because it's recognized by a trusted CA)

