I.**Why does this matter?**
- SQL databases are traditionally designed to run on a single server, so as data grows, reads and writes can bottleneck (makes the db server overloaded)

II.**Sharding**
- it's all about splitting data across multiple instances to improve scalability and performance. The approach can be applied to any database type (sql, no-sql)
- we can shard based on a key (e.g., user-id, region, or time)

III.**Challenges**
- **joins**: cross-shard queries (e.g., joining data from different shards) are hard or impossible without extra logic
- **transactions**: maintaining [acid]() compliance across shards is tricky, or impossible
