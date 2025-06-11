# Real-Time Sync Service

- @Todo

- OT: Requires server-side history for transformations, complicating offline sync (as discussed previously). Needs careful state management to merge offline deltas.
- CRDTs: Simplifies offline sync, as client-side CRDTs queue mergeable operations, and server-side CRDTs integrate them without history. More robust for mobile apps and intermittent connections.
- Choice: CRDTs are preferred for your editor, aligning with Google Docs’ latest approach, due to their simplicity and offline capabilities.


