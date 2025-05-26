# Document Service

## Delete

**1.Request:**
- client sends a REST DELETE request (e.g., `DELETE /documents/doc123`)

**2.Process:**
- **Authentication**
- **Authorization**
- **Soft Delete**
  - Mark the document as deleted in the NoSQL database (e.g., add is_deleted: true) to **preserve revision history** (**@Todo Why?**) and allow recovery (**@Todo why needed?**)
  - **@Todo**: so the user can undo the deletion??
- **Media Cleanup**
  - delete associated images/videos from the Storage Service to reclaim space
- **Notification**
  - notify collaborators of deletion via the Messaging Service

**3.Response:**
- returns the deletion confirmation to the client
