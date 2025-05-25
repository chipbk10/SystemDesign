# Communication
- we will use WebSocket for real-time updates (e.g., sending/receiving document changes)
- we will use REST APIs for operations like creating/deleting/sharing documents

# Client Layer
- mobile apps (iOS/Android)
- web browsers

## API Gateway
- enforce authentication, and rate-limit traffic
- routes REST and WebSocket requests to backend services

# Application Layer
- handle CRUD (create/read/update/delete) on documents
- resolve the conflicts for real-time collaboration
- handle sharing a document

## Authentication/Authorization Service
- identify user
- check the user's access control

## Real-Time Sync Service
- use WebSocket to push updates to the client layer

# Store Layer

## Real-Time Database
  - we will use a NoSQL database service (e.g., AWS DynamoDB, or GCF) for storing document content and metadata
  - it supports low-latency, scalable reads/writes and **real-time updates via streams or listeners**. 

## Object Storage Service
  - we will use an object storage service (e.g., AWS S3, or GCS) for storing large documents (e.g., very big size like few GBs), or blobs (e.g., images, videos, pdfs attachment)
  - it will offload our real-time database

## Revision History
  - we will use a NoSQL database service (e.g., AWS DynamoDB or GCF) to store document revisions
  - it enables rollback and conflict resolution
  - each edit is timestamped and linked to a user **@Todo: why?**

## Caching Service
  - we will use an in-memory cache (w.g., AWS ElastiCache - Redis, or GCM) for caching frequently accessed document metadata or session data
  - it will reduce latency and database load
  - **@Todo: be more specific**

# Infrastructure Layer

## Load Balancer
- distributes traffic across regions/zones **@Todo**
- AWS ELB, Google Cloud Load Balancing

## Global CDN
- caches static assets for low latency **@Todo: what are static assets in this case?**
- AWS CloudFront, Google Cloud CDN

## Monitoring Service
- tracks latency (including tail latency) and system health **@Todo: how does it work?**
- AWS CloudWatch, Google Cloud Monitoring

## Security
- we use TLS for transit (encrypt data when transferring)
- we encrypt documents when storing on physical storages (default support by AWS DynamoDB, S3, or Google Cloud services)

## Questions
1. **How do you support offline mode?**
- we will cache document state locally (e.g., in browser storage, etc.) to allow editing offline
- we will sync changes when reconnected

2. abcd



## Notes
- **GCF**: Google Cloud Firestore
- **GCS**: Google Cloud Storage
- **GCM**: Google Cloud Memorystore
