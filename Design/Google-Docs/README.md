# Question
- Let's design an real-time text editor like Google Docs

# Clarify Requirements

## Functional Requirements
- Users can create, view, delete, and edit a text document
- Users can share with others to view, edit a text document
- Multiple users can edit simultaneously on the same document

## Non-Functional Requirements
- **High Availability**: the system remains working/accessible even when some components fails (e.g., regional outages)
- **High Reliability**: no data loss during editing
- **Consistency**: all users must eventually see the same state of the document
- **Low Latency**: changes made by one user should be visible to others with low latency (e.g., 100-500ms)
- **Scalability**: the system should handle many users editing concurrently, up to thousands of simultaneously edits on a single document (as Google Docs does)
- **Security**: ensure secure access control, encryption in transit and **at rest** and protection against unauthorized access
- **Offline Support**: allow users to edit documents offline and sync changes when reconnected

## Questions
1. **How do you ensure your system highly available during regional outages?**
- we can use redundant servers across multiple regions or zones to handle failures gracefully.
- failure in one zone are mitigated by automatic failover to other zones, ensuring minimal downtime
- we can implement metrics for latency, error rates, and availability to diagnose issues. Our teams gets notified by the issues and fix them as soon as possible
  
2. **How do you ensure no data loss happens during editing?**
- our system should implement automatic saving, version control and redundant storage
- **@Todo**

3. **How do you ensure all users eventually see the same state of the document?**:
- multiple users can edit the document simultaneously.
- we can achieve eventual consistency using OT (operational transformation) or CRDT (conflict-free replicated data types) to resolve conflicts in real-time, and then synchronize document states across users

4. **How to ensure a low latency?**:
- we aim for low latency in the range of 100-500ms for updates to propagate
- of course, the latency depends on the network condition. However, we should ensure a fast and efficient conflict-resolution algorithm
- beside, we should use a **global CDN**, and can monitor and optimize for **tail latency**
  - **@Todo**

5. **How do you ensure the security in our system?**
- encryption in transit: we can use TLS for data transfer
- encryption data at rest: we should encrypt all data in physical storage, ensuring that documents remain secure even if physical storage is compromised.
  - normally, the cloud storage services (e.g., AWS S3, or GCS) encrypt data by default
- protection against unauthorized access:
  - we can use authentication systems (e.g., OAuth to check with identity providers like Google Accounts) to verify user identities
  - require authentication tokens (e.g., JWTs) for all API requests to prevent unauthorized access to endpoints
  - we can implement RBAC (role-based access control) or use ACLs (access control lists) to check the permissions
