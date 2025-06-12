# Conflict-free Replicated Data Types - CRDTs
- basically, CRDTs is a special kind of data structure that allows multiple users to edit shared data concurrently, and their changes **merge automatically without conflicts**
- CRDTs use mathematical rules to ensure all updates eventually converge to the same state, **no matter the order they're applied** 

## Operation-based CRDTs (CmRDT)
- rely on operations (e.g., insert, delete, update) to define the state
- each operation includes metadata (e.g., unique IDs, timestamps) to ensure conflict-free merging
- CmRDTs don't always store all operations indefinitely. To save space, they may periodically create snapshot of the current state and compact (e.g., combine many operations into a single operation) or prune (e.g., delete obsolete operations that no longer affect the current state) operations
- CmRDTs ensure `eventual consistency` because operations are **commutative** and **idempotent**

## State-based CRDTs

- Conflict-Free Replicated Data Types - CRDT
  - pros: decentralized (no central server), support offline edit
  - cons: Complex implementation, higher storage for metadata

- Merge Logic
  - The merge logic (union of IDs) is simple in theory, but preparing the meta-data (unique IDs, tombstones, causality) and applying it (rich text, scalability) is complex.
- Unique IDs:
  - Each character or edit needs a globally unique identifier (e.g., !12) to track its position and state across clients.
  - Generating unique IDs without collisions is non-trivial, especially in distributed systems (e.g., A and B offline, no server coordination).
  - Example: CRDTs like Logoot use timestamped IDs or Lamport clocks, requiring complex logic to ensure uniqueness and ordering.

- CRDT vs OT
  - OT fits our 10-editor limit and centralized architecture, while CRDTs are overkill unless we need offline support, or support to 50 users editing at the same time

 
