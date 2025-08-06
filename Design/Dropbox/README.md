# Question
- Let's design a distributed file storage system like Dropbox or GoogleDrive

# Clarify Requirements

## Functional Requirements
- Users can upload/download a file (from 1KB to 1000GB) with resumable function
- Users can synchronize across devices (web, mobile, desktop)
- Users can share files with other users
- Users can create, rename, move, or delete files and folders
- Nice to have:
  - versioning: maintain a history of file versions to allow users to revert to previous versions.
  - search: users can search for files by name, or other metadata

## Non-Functional Requirements
- **Availability**: should be highly available (e.g., 99.9% uptime) to ensure users can access files anytime
- **Reliability**: data should not be lost, even in the case of hardware failures or network issues
- **Latency**: low latency for file uploads, downloads, and synchronization
- **Scalability**: the system must handle millions of users and petabytes of data, scaling seamlessly as usage grows
- **Security**: files must be encrypted both at rest (in DB) and in transit (SSL/Authorization) to protect user data
- **Consistency**: availability >> consistency. Eventual consistency is preferred. Example: a user edits a document on their laptop, and it's automatically updated on their phone within seconds.
