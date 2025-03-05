I. **What is a digital signature?**
A digital signature is used to ensure that:
- the content (digital message, documents, or software) is not altered during the delivery
- confirms the identity of the sender
- confirms the sender did send that content. The sender cannot refuse that.

II. **How it works?**
1. **Hashing**:
- The sender passes the content to a hash function (e.g., SHA-256) to generate a unique hash. This hash acts as a fingerprint of the data.
2. **Signing**:
- The sender encrypts this hash by using his private key to create a digital signature. This steps binds the signature to the sender's identity.
3. **Transmission**:
- The sender sends the original content, together with his digital signature to the recipient.
4. **Verification**:
- The recipient uses the sender's public key (from the sender's [certificate]()) to decrypt the signature, and gets the original hash (if decryption succeeds, the content has been signed by this sender)
- The recipient independently compute the hash of the content (also using the same hash function)
- If the two hashes match, the content is not altered during the delivery.
   
III. **Application**
- Ensure security of communication (via web protocol https, email protocol s/mime, etc.)
- Validate transactions (in blockchain)
- Sign a software
