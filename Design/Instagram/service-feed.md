# Feed Service

## Functional Requirements
- **Generates personalized feeds**
  - fetches media from users, a given user follows (e.g., User A's feed shows User B's videos if A follows B)
  - orders media by recency (in chronological order - e.g., `upload_time`) or relevance (e.g., `view_count`, `number_of_likes`)
- **Handles feed updates**
  - adds new media to followers' feeds when a user uploads content
  - updates feeds when a user follows/unfollows another user (e.g., add/remove their media)
- **Incorporates Trending/Recommended content**
  - includes media from celebrity users or trending posts (e.g., viral videos)

## Non-Functional Requirements
- **Scalability and Performance**
  - serves 100 millions of feed requests/day with low latency (<100ms)
  - serves millions of feed updates/day

## APIs
- **Serving Feeds**
  - responds to API requests for a user's feed  
- **Update Feeds**
  - processes events (follow/unfollow, media uploads) to keep feeds updated

## Serving Feeds
- `GET /api/feed?user_id=12345&limit=20&after=2025-05-14T23:44:00Z`.
- we use [pagination cursor]() (timestamp of last seen item) to avoid returning excessive data at once, and convenient for user navigation or scrolling.
- we check if user's feed in Redi cache before hiting DynamoDB Feed table
- a feed looks like as follows. In which **the metadata refers to the person the user's follow**
  ```json
  {
    "user_id": "12345",
    "timestamp": "2025-05-14T23:44:00Z",
    "media_id": "550e8400-e29b-41d4-a716-446655440000",
    "posted_by": "67890",
    "media_type": "video",
    "title": "Mountain Adventure",
    "thumbnail_s3_url": "s3://processed-bucket/550e8400_thumbnail.jpg"
  }
  ```
- without **generated & convenient Feed data**, you have to query for all the followees (from `followee` table), then for each followee, you have to query for recent uploaded/updated media (from `media` table), and then create a news feed by sorting and merging (e.g., 1000 media items) by `upload_time` to return the 20 newest. This approach, known as **fan-out-on-read**, increases the latency, not scalable (with a large reading volumn)

## Update Feeds (media uploads)
- User B (`user_id: 67890`) uploads a video
- Media Service writes metadata to media table (status: "processed")
- DynamoDB Streams triggers SQS **fan-out-on-write** to followers' feeds

## Update Feeds (follow action)
- User A (`user_id: 12345`) follows User B (`user_id: 67890`)
- Follow Service update Follow Relationship tables
- Feed Service adds User B's recent media (e.g., 10 items) to User A's feed

## Update Feeds (unfollow action)
- User A (`user_id: 12345`) follows User B (`user_id: 67890`)
- Follow Service update Follow Relationship tables (by deleting the relationship)
- Feed Service remove all User B's recent media from User A's feed

## Redis Cache
- the feeds in Redis cache: the key is `feed:user-id` (e.g., `feed:12345`), the value is a list of feeds, **which is ordered chronologically**. Each feed (in the list) is a **JSON** string representing media metadata (e.g., `[JSON(item1), JSON(item2), ...]`)
- during the **fan-out-on-write** operations, we **invalidate (by deleting)** the Redis cache for affected users' feeds rather than updating it accordingly.
  - it means the next feed request will miss the cache, we have to query DynamoDB, rebuild the feed and re-cache it in Redis for subsequent requests.
  - we don't update the affected feeds in Redis accordingly, because parsing and updating then filtering again the existing list of feeds is complex and error-prone rather than a single invalidation (DELETE) operation
- TTL (time-to-live) of a feed is short (e.g., 5 minutes) to avoid the cache staleness

## DynamoDB
- to scale up, we can shard the DynamoDB by user-id
- all metadata of the same user-id should be hosted on the same partition to avoid the merge after a query

# Edge cases
## Celebrity (upload a video)
- a celebrity (`user_id: 67890`) with 1 million followers uploads a new video
- this triggers **fan-out-on-write**:
  - query for 1 million followers (from Follows table) might happens on several partitions. We can query all shards in parallel, then merge
  - 1 million writes to the Feed table (that leads to DynamoDB throttling **@TODO**). The solution is we can use **SQL fan-out with batching**. For example, each Lambda processes ~ a batch of around ~ 1000 followers. **@TODO**
  - invalidate 1 million feeds in Redis is potentially slow for a single Lambda. We can batch invalidation in SQS workers
  - **Eventual Consistency**: most followers see the video within seconds (<1s) for small batches, up to 15 minutes for all 1 million due to SQS processing

## Trending/Recommended Content
- the Search Service may index the celebrity's video as trending (e.g., because of high `view_count`)

## Sparse Feeds
- happens when user has very few followers, and the news feed doesn't have much content
- the Feed Service may add the trending/recommended (the celebrity's) media to the non-followers' feeds **via periodic jobs**, enhancing visibility.

# Questions
1. **How do you handle cache staleness?**
- set a short TTL (e.g., 5 minutes)
- invalidate on writes
   
2. **How do you handle when a celebrity (with millions follower) uploads a new media?**
- query in parallel
- fan-out-on-write with batching
- accept eventual consistency
  
3. **How do you handle with a user who has very few followers?**
- index the celebrity's media as trending/recommended content in Search Service
- via periodic jobs & Search Service, add trending/recommended media to the user's feed
