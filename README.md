# System Design

1. How does https work? [https](https://github.com/chipbk10/SystemDesign/blob/master/https.md), [handshake](https://github.com/chipbk10/SystemDesign/blob/master/handshake.md)
2. Where is a shared session key stored? [https](https://github.com/chipbk10/SystemDesign/blob/master/https.md)
3. How to avoid handshake overhead for subsequent https requests? [keep-alive](https://github.com/chipbk10/SystemDesign/blob/master/keep-alive.md)
4. How to resume previous https session without doing a full handshake? [partial handshake](https://github.com/chipbk10/SystemDesign/blob/master/partial-handshake.md)
5. How to route the subsequent https request to the same server? [sticky session](https://github.com/chipbk10/SystemDesign/blob/master/sticky-session.md)
6. How does login work? [session_token](https://github.com/chipbk10/SystemDesign/blob/master/authenticate.md), [access_token](https://github.com/chipbk10/SystemDesign/blob/master/authenticate.md), [jwt](https://github.com/chipbk10/SystemDesign/blob/master/jwt.md), [authenticate](https://github.com/chipbk10/SystemDesign/blob/master/authenticate.md)

## Cryptographic

1. How to ensure that a message received over https is not altered and comes from a trusted source? [signature](https://github.com/chipbk10/SystemDesign/blob/master/Cryptographic/signature.md), [certificate](https://github.com/chipbk10/SystemDesign/blob/master/Cryptographic/certificate.md)
2. How does ssl-pinning enhance mobile app security? [ssl-pinning](https://github.com/chipbk10/SystemDesign/blob/master/Cryptographic/ssl-pinning.md)
3. Why isn't ssl-pinning used in web app? [ssl-pinning](https://github.com/chipbk10/SystemDesign/blob/master/Cryptographic/ssl-pinning.md)
