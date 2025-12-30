### General Summary: Home Networking, Modems, Routers, Wi-Fi Extension, and IP Addresses

#### 1. **Modem vs. Router**
- **Modem**: Converts the signal from your ISP (e.g., fiber optic, cable, DSL) into a digital signal your devices can use. A pure modem does **not** provide Wi-Fi and usually has only one Ethernet port.
- **Router**: Manages your local network (LAN), assigns private IP addresses to devices, provides Wi-Fi, and connects multiple devices to the internet via the modem.
- **Modern reality**: Most ISPs provide an **all-in-one device** (gateway) that combines both modem and router functions, with built-in Wi-Fi and multiple LAN ports.

#### 2. **Extending Wi-Fi in Multi-Story Homes**
- Common setup: One main gateway connected via Ethernet cables to multiple **Access Points (APs)** or secondary routers configured in **AP mode** on different floors (star topology).
- In AP mode, secondary devices only extend Wi-Fi coverage — they do **not** create a separate network.
- Best practice: Use the **same SSID (network name)** and **password** on all access points for seamless roaming (devices automatically switch between APs without disconnecting).
- Connection options:
  - **Ideal**: Run Ethernet cables directly from the main gateway to each AP (star topology) → maximum speed and stability.
  - **Alternative**: Daisy-chain APs (connect one AP to another via LAN port) → works but can reduce performance due to bottleneck.
- Important: When connecting secondary devices, use **LAN-to-LAN** ports (avoid the WAN port) and set them to **Access Point mode** to prevent creating a separate subnet or double NAT.

#### 3. **IP Addresses in Home Networks**
- **Public IP (WAN IP)**: The single address assigned by your ISP to your gateway for internet access.
  - Usually **dynamic** (changes over time).
  - Due to IPv4 shortage, many ISPs use **CG-NAT (Carrier-Grade NAT)** → multiple customers share the same public IP, distinguished by ports.
- **Private IP (LAN IP)**: Internal addresses used inside your home network.
  - Common ranges: 192.168.0.0/16, 192.168.1.0/24 (most common), 10.0.0.0/8, etc.
  - The gateway’s private IP (e.g., 192.168.1.1 or 192.168.0.1) is used to access its admin interface for changing Wi-Fi name/password, viewing connected devices, etc.
  - Devices in AP mode do not assign their own private IPs — all devices get IPs from the main gateway.

#### 4. **Key Tips for Strong Whole-Home Wi-Fi**
- Use the same SSID and password across all access points.
- Choose different wireless channels on nearby APs to avoid interference.
- Prefer wired backhaul (Ethernet) over wireless repeaters for better speed and reliability.
- For seamless coverage without running cables, consider mesh Wi-Fi systems.
