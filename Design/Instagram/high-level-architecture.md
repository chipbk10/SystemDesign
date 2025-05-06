# Client Layer
- mobile apps (iOS/Android)
- web browsers

# API Gateway
- routes requests to backend services

# Core Services
- **Media Service**: handles upload/download/view of photos/videos.
- **Search Service**: indexes and searches media by title.
- **Follow Service**: manages follow/unfollow relationships.
- **Feed Service**: generates news feeds with top (recent) media.

# Store Layer
- **Object Storage**: stores photos/videos (e.g., AWS S3)
- **NoSQL Key-Value Database**: stores media metadata, and follow relationships (e.g., DynamoDB)
- **Caching**: speeds up feed generation, recent posts of celebrities (e.g., Redis)
- **Search Index**: indexes titles for fast search (e.g., Elasticsearch)

# CDN
- delivers photos/videos with low latency

# Message Queue
- handle asynchronous tasks (e.g., media processing)
- @Todo: push media-id to Feed Service
