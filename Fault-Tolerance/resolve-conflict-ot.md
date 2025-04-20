- **Operational Transformation - OT**:
  - tranforms operations to resolve conflicts. For example, if User A inserts ‘x’ at position 100 and User B deletes position 100, OT adjusts the positions so both operations apply correctly.
  - pros: mature (Google Docs), simpler for centralized systems, low latency for small groups (5-10 users edit at the same time)
  - cons: requires a central server, complex for large-scale (e.g., 50 users edit at the same time) or offline edits

- In OT, a patch or operation is a single user action, like inserting or deleting a character, not a diff between saves. For example, typing “x” generates `{ op: "add", path: "/text/100", value: "x" }`, sent via WebSockets in real-time or queued offline. Our system auto-saves like Google Docs, so each keystroke is a patch, not a batch on save. This fine-grained approach enables OT to transform concurrent edits, ensuring consistency for 10 editors.

- [Operational Transformations as an algorithm for automatic conflict resolution](https://medium.com/coinmonks/operational-transformations-as-an-algorithm-for-automatic-conflict-resolution-3bf8920ea447)
- [Issues and Experiences in Designing Real-time Collaborative Editing Systems](https://www.youtube.com/watch?v=84zqbXUQIHc&ab_channel=GoogleTechTalks)
- **@Todo**

