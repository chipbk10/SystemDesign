I.**VPN encryption: why it's needed?**
- vpn adds its own encryption layer (e.g., via OpenVPN, WireGuard) to wrap all your network traffic (not just https) into a secure tunnel between your device and the vpn server.
- https reveals the destination **server's IP**
  - cannot bypass through the ISP or Government firewall
  - or on public Wi-fi (e.g., at a coffee shop), a malicious network can redirect your request to a different endpoint
- vpn encrypts these info, so your ISP only sees you talking to the VPN server
- https reveals **packet sizes** or **timing**, which can reveal activity (e.g., streaming vs browsing). VPN encrypt these info

II.**Communication**
- a VPN client (installed on the user's device) encrypts the https request (along with all other traffic)
- VPN client sends the encrypted content to VPN server via VPN protocol (e.g., OpenVPN, WireGuard, IPsec)
- VPN server decrypts and forward the request to the destination server
