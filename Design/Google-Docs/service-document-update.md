# Document Service

## Update

**1.Request:**
- client sends a WebSocket message (for real-time text edits)

**2.Process:**
- **Authentication**
- **Authorization**
- **Content Edits:**
  - client sends a delta (a collection of operations) via WebSocket to the Real-Time Sync Service
  - the Application Server applies OT/CRDT to resolve conflicts from concurrent edits
  - the Application Server updates the content and append a new entry to the `revision` list in the `Document` table
  - Streams/Listeners (AWS DynamoDB Streams, or Google Cloud Firestore Listeners) trigger the Real-Time Sync Service to broadcast updates to all connected clients

**3.Response:**
- returns the confirmation for the update
- **@Todo**
