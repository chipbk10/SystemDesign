I. **Why bother?**
- each handshake is expensive (e.g., 300ms delay). It might cause latency, and not good user experience.
- if the web/mobile app switches networks (e.g., wifi to 4g), a new handshake is required. It costs CPU and battery resources on both client and server

II. **How to resume previous session without key exchange and certificate validation?**

- without key exchange and certificate validation, this reduces the latency (e.g., from 300ms down to 100ms)

1. **Session ID** (< TLS 1.2)
- During the initial full handshake, the server assigns a unique SessionID, and associates it with Session State (e.g., session key, other parameters)
- Both client & server store this SessionID and Session State in their memory
- On a new TCP connection, the client includes the SessionID in its `ClientHello`
- If the server recognizes the ID, and has the session cached, it replies with the same ID in `ServerHello`, and both reuse the prior session key without a new key exchange and certificate validation.
- The cons is the server has to maintain the SessionIDs and assoicated SessionStates in cache. If the server flushes its cache (due to timeout, memory pressure, or reboot), the SessionID became invalid. Eviction is as simple as removing the ID from the cache. No extra infrastructure needed.

2. **Session Ticket** (TLS 1.2, 1.3)
   
  - Full Handshake:
    - Client and server use ECDHE → **master secret** which is used to generate session key & psk
    - **Both derive the same resumption PSK from the master secret**.
    - Server encrypts PSK into a session ticket and sends it to the client.
    - Client stores the ticket and the PSK it calculated.

  - Resumption:
    - Client sends the ticket and a **binder** (made with its stored PSK).
    - Server decrypts the ticket, gets the PSK, checks the binder.
    - Both use the PSK (client from memory, server from ticket) to resume.

- The pros is the server becomes stateless. We can still resume the previous session despite server reboots.
- The cons is more bandwidth (SessionTicket > SessionID), more delay (to encrypt & decrypt SessionTicket). Eviction requires maintaining a blacklist of unwanted sessions, which must be stored persistently and checked during resumption.

