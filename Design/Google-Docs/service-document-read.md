# Document Service

## Read

**1.Request:**
- client sends a REST GET request to the API gateway: `GET /documents/doc123`

**2.Process:**
- **Authentication**
- **Authorization**
- **Fetch Data:**
  - query the `Document` table by `document_id` to retrieve `title`, `content`, and other metadata
- **Real-Time Sync**:
  - client establishes a WebSocket connection to the Real-Time Sync Service to receive updates (e.g., updated text, added media by other collaborators)

**3.Response:**
- returns the document's content and metadata to the client
