## ✅ Amazon RDS (Relational Database Service)

- What it is: A fully managed service for relational databases.
- Supported engines: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora.
- Key features:
  - Automated backups, patching, and failover.
  - Multi-AZ deployment for high availability. **Tied to a single region**
  - Read replicas for scaling read traffic.
- Benefits: No need to manage hardware, OS, or DB software manually.

## ✅ Common Exam Questions:

1. Is RDS serverless?
→ No (except Aurora Serverless).
→ For RDS, you still have to choose DB engine, CPU, memory, storage type (EBS underhood)
→ does not automatically shard or scale horizontally.
3. Does RDS manage backups automatically?
→ Yes, with configurable retention.
4. Can RDS scale horizontally?
→ Yes, using read replicas (for reads only).
5. Multi-AZ vs Read Replica?
→ Multi-AZ = HA (standby in another AZ), Read Replica = performance (read scaling).
6. Difference between RDS and Aurora?
→ Aurora is AWS’s own DB engine, faster and more scalable.
