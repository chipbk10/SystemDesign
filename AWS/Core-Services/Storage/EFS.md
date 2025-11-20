## ✅ Amazon EFS (Elastic File System)

- **What it is**: A fully managed, scalable shared file storage service for AWS.
- **Access**: Multiple EC2 instances (or containers) can access the same EFS file system concurrently.
- **Scope**: Multi-AZ within a region → high availability and durability.
- **Protocol**: Uses NFS (Network File System).
- **Scaling**: Automatically grows and shrinks as you add/remove files.
- **Use cases**: Web servers, content management, big data, container storage.
- **Pricing**: Pay for the amount of data stored (not provisioned size).
- **Difference** from EBS:
  - EBS = block storage, single EC2 only (per AZ).
  - EFS = shared file storage, many EC2s (multi-AZ).
  - EFS is for shared files, **not for transactional DB storage**. If you need multi-instance access: use a **managed database service like Amazon RDS or Aurora**.
  - EBS or RDS is for databases.

## ✅ Why not replace EBS with EFS?

- EC2 needs a root volume to boot → EBS provides that.
- EFS is network-attached storage, not a boot disk.
- EFS is better for shared data, not for OS or low-latency block storage.

## Analogy
- **EBS** = your computer’s internal SSD (fast, local).
- **EFS** = a network file share (accessible by many machines).
