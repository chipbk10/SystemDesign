
| Type            | Data Model            | Strengths                          | Weaknesses                       | Use Cases                        | Examples                        |
|-----------------|-----------------------|------------------------------------|----------------------------------|----------------------------------|---------------------------------|
| Key-Value       | Key-value pairs       | Simplicity, speed, scalability     | Limited query flexibility        | Caching, session management      | MemCached, Redis, DynamoDB      |
| Document        | JSON/BSON documents   | Flexible schema, rich queries      | Less efficient for joins         | CMS, e-commerce catalogs         | MongoDB, CouchDB, Firestore     |
| Column-Family   | Column-based tables   | High write throughput, analytics   | Complex reads, learning curve    | Time-series, event logging       | Cassandra, HBase, ScyllaDB      |
| Graph           | Nodes and edges       | Relationship traversal             | Less suited for simple data      | Social networks, fraud detection | Neo4j, Neptune, ArangoDB        |
