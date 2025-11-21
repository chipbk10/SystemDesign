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
