- **network partitions**: occur when communication between some nodes fails due to network issues (e.g., dropped messages, latency, or hardware failure).
- in a distributed system, under the **CAP theorem**, when a **network partition** happens, you choose:
  - **AP**: System stays available (responds to all requests) but data might be stale (not always consistent across nodes).
  - **CP**: Data is consistent (same across all nodes) but system might be unavailable at some points (when partitions occur, some requests might fail).
- You can’t have both full **consistency** and full **availability** during a partition.

