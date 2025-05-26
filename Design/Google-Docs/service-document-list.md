# Document Service

## List

**1.Request:**
- client sends a REST GET request to the API gateway: `GET /documents/user123`

**2.Process:**
- **Authentication**
- **Authorization**
  - the Application Server verifies the `user_id` from the JWT token matches the requested `user123`
  - ensuring users can only query their own documents
- **Fetch Data:**
  - query the `Document` table based `document_id` to retrieve `title`, `content`, and other metadata


**3.Response:**
- returns the list of documents metadata (e.g., title, updated_time)


## Questions
1. **How do you look up for a list of documents that the user participate in?**
- By natural reasoning, we should query the `Collaborators` based on the `user_id` to get all documents. Then we for each `document_id`, we can query the `Documents` table for the document metadata.
- The challenge of NoSQL is not supporting join queries.
- Querying by `user_id` in the `Collaborators` table, or querying `owner_id` in `Documents` table require efficient indexing, as scanning the entire table would be slow and costly
- **Solution:** we will create a **secondary index** (e.g., Global Secondary Index in DynamoDB or Firestore index) to query `Documents` by `user_id` (covering both `owner_id` and `collaborators.user_id`)
  ```json
  {
    "document_id": "doc123",
    "title": "Project Plan",
    "owner_id": "user123",
    "collaborators": [
      {"user_id": "user123", "role": "edit"},
      {"user_id": "user456", "role": "view"}
    ],
    "created_at": "2025-05-25T10:00:00Z",
    "updated_at": "2025-05-25T10:55:00Z",
    "content": {...},
    "revisions": [...]
  }
  ``` 
