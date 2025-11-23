## ✅ Key Components

- **VPC**: The overall network container.
- **Subnets**: Divide VPC into smaller networks (public or private).
- **Internet Gateway (IGW)**: Enables internet access for public subnets.
- **NAT Gateway**: Allows private subnets to access the internet securely.
- **Route Tables**: Define traffic routing rules.
- **Security Groups**: Instance-level firewall. (e.g, EC2)
- **Network ACLs**: Subnet-level firewall.

## ✅ Scope

- Region-scoped, but spans multiple Availability Zones (AZs).
- You can create **multiple VPCs per Region**.

## ✅ Connections

- **VPC peering connection**:
  - allows you to connect two VPCs privately using AWS’s internal network
  - uses private IP addresses, not the public internet.
  - It enables resources in one VPC to communicate with resources in another VPC as if they were in the same network. 
- **VPC endpoint**:
  - A VPC Endpoint allows resources in your VPC (like EC2 instances) to access AWS services (like S3 or DynamoDB) privately,
  - without going through: Public IP addresses, Internet Gateway, NAT Gateway
- **AWS Site-to-Site VPN**:
  - is a managed service that securely connects your on-premises network (or another cloud provider) to your AWS VPC over the public internet using an **IPsec VPN tunnel**.
  - is a backup connectivity when Direct Connect is unavailable.
- **AWS Direct Connect**:
  - is a networking service that provides a dedicated, private connection between your on-premises data center (or colocation facility) and AWS.
  - Ideal for large data transfers and real-time applications.
  - No public internet is involved for data transfer.
  - Traffic flows through a secure, private connection, reducing latency and improving reliability.
- **PrivateLink**:
  - AWS PrivateLink enables private connectivity between VPCs and supported AWS services without traffic traversing the public internet.
  - It ensures secure communication for applications and services.
- **Transit Gateway**:
  - is a highly scalable service that connects multiple VPCs and on-premises networks through a central hub.
  - It facilitates secure, private connectivity between VPCs and supported services without using the public internet.



