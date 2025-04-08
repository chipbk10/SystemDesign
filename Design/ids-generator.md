I.**Design IDs generator**
- IDs must be unique in our distributed system (despite nodes, data center, regions, etc.)
- IDs must be numerical values only
- IDs fit into 64 bits
- IDs are ordered by date
- Abilities to generate over 10K unique IDs per second

II.**Twitter snowflake**
- 1 bit: 0/1 is reserved for later use
- 41 bits: is for `timestamp`, which is converted to [UTC]() with default epoch 01/01/2020.
  - the generator can last for 2^41 / 1000 / 3600 / 24 / 365 = 69 years (counting from the default epoch)
- 5 bits for datacenter id
- 5 bits for a machine id (a node)
- 12 bits for sequence number
  - it can generate 2^12 = 4096 ids per milli-second within a node
- `ID = (timestamp << 22) | (datacenter-id << 17) | (node-id << 12) | (sequence-number)`

III.**Measures**
1.**Throughput**
- 4096 IDs per milli-second per node
- 4096 million per second, far exceeding 10K IDs per second

2.**Scalability**
- adding more nodes (up to 2^5 data centers, 2^5 nodes per data center), it is still fine

3.**Node ID assignment**
- nodes need unique IDs.
- we can assign IDs via config files for each node. Simple but not scalable or dynamic
- we can use a `coordination service` (like [Zookeeper]() or etcd to assign node IDs dynamically). This ensures no duplicates even if nodes restart or new ones join

4.**Clock synchronization**
- use [NTP (network time protocol)]() to keep clocks in sync across nodes
- each node syncs with NTP before starting ID generation to ensure its clock is accurate.
