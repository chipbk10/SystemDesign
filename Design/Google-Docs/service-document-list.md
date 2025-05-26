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
  - query the database based on the `user_id` to get all documents metadata

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
2. **Tell me more about how you design the Index for Documents table?**
- Index Name: `UserDocumentsIndex`
- Partition Key: `user_id` (e.g., `user123)
- Sort Key: `updated_at` (to sort by recency)
- Projected Attributes: `document_id`, `title`, `updated_at`, `role` (derived from `owner_id` or `collaborators` fields ---> **@Todo: How?**)

3. **How Indexing works?**
- When a document is created or updated (e.g., adding a collaborator), the Application Server writes to the main table (`Documents`) and also updates the index with entries for the owner and all collaborators
- The index allows querying by `user_id` to fetch all documents where the user is an owner or collaborator, including metadata (`title`, `updated_at`) and their role

4. **Can you optimize more?**
- we can store the list of document metadata for frequent users in the cache (e.g., AWS ElastiCache, or Google Cloud Memorystore) with a key `user:documents:user123`, and a short TTL (e.g., 5 minutes)
- on `GET /documents/user123`, we check the cache first, if missed, query the index and update the cache
- we invalidate the cache when a document's metadata or collaborators change (e.g., via NoSQL Streams/Listeners)

5. **What if a user has many documents (e.g., 500 documents)?**
- we can use pagination in the query (e.g., DynamoDB's Limit and `LastEvaluatedKey`, or Google Firestore's Limit and `startAfter`)
- example: `GET /documents/user123?limit=10&after=doc456` return the next 10 documents
