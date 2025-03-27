I.**Partitioning**
- a broader term for dividing data into subsets (partitions), which **may or may not** be distributed across multiple servers
- [sharding]() is just a specific type of partitioning
- partitioning might happen within a single server. For example:
  - In PostgreSQL, you partition a sales table by year (2023 on Partition 1, 2024 on Partition 2) on a single server. No distribution, just better organization.
