# Follow Service
- manages social relationships, enabling users to follow/unfollow others

## Functional Requirements
- following a person to see their recent media in user's news feed
- unfollowing a person, user shouldn't see their recent media in news feed

## Non-functional Requirements
- **Scalability**: storing and querying millions of relationships (e.g., 1 million users, each following 100 others -> 100 million edges) requires a specialized database, not DynamoDB alone, which is optimized for key-value queries
- **Performance**: Fast writes (follow/unfollow) and reads (feed generation) are critical for a responsive UX
- **Integration**: the Follow Service feeds into the Feed Service (for generating news feed), and Search Service (e.g., prioritizing media from followed users)

## High-Level Architecture

- **Database**:
  - DynamoDB (for simplicity and AWS integration): we stores the follow relationships as adjacency lists (e.g., `user_id` -> list of followed `user_id`s)
  - Neptune (for complex graph queries - e.g., find mutual followers)
  - Redis for in-memory performance to cache frequent queries (e.g., follower lists for popular users) to reduce database load
    
- **Follow Service API**:
  - `POST /api/follow`
  - `POST /api/unfollow`
  - `GET /api/followers` - the user follows whom?
  - `GET /api/following` - who follows the user?

- **Event System**:
  - publish follow/unfollow to a **Message Queue** (e.g., AWS Simple Queue Service) or a **Notification System** (e.g., AWS Simple Notification Service) to notify the Feed Service and update news feed asynchronously

## Flow
- what happens when a user follows/unfollows another user?
- `POST /api/follow(unfollow)`, request body: `{"follower_id": "12345", "followee_id": "789021"}`
- checks userB exists (query `User` table), and ensures userA isn't already following (or unfollowing) userB (query `FollowRelationships` table)
- checks userB's privacy settings (e.g., allow other to follow, or requires approval)
- insert a record in both `FollowRelationships`, and `FolloweeRelationships` (with status = "active" or "pending" if requires approval) in an atomic transaction
- publish an event asynchronously (via SQS queue or SNS topic or via DynamoDB Streams) to notify other services.
  - Feed Service consumes the event, adding/removing User B's recent media to/from User A's feed (e.g., update in Feed table or cache)
  - Search Service: update relevance scores to prioritize User B's media in User A's searches (**@Todo**)
  ```javascript
    await opensearch.search({
      index: "media",
      body: {
        query: {
          bool: {
            should: [
              { multi_match: { query: "hiking", fields: ["title", "tags"] } },
              { terms: { user_id: ["67890"] } } // **Boost followed users**
            ]
          }
        }
      }
    });
  ``` 
  - Caching: update Redis cache for User B's follower list or User A's following list

## Questions
1. **How do you handle a celebrity with 10 million followers?**
- we cache follower lists of the celebrity in Redis to reduce DynamoDB reads
- in DynamoDB, we shard writes (**@Todo**): choose a shard randomly or based on a rule (e.g., `followee_id % num_shards`). To retrieve all follow relationships, we query all shard keys and merge results
  ```json
    {"celebrity_id": "12345_shard1", "followee_id": "67890"}
    {"celebrity_id": "12345_shard2", "followee_id": "99999"}
  ```
2. **What if feed updates lag?**
- Monitor SQS backlog, prioritize critical users (**@Todo**)
3. **Why not use a graph database?**
- DynamoDB is sufficient for simple follow queries (we don't need complex queries like finding mutual friends), lower ops cost (**@Todo**)
- **@Todo**: compare between key-value NoSQL and Graph database
4. **How do you know an user is/becomes a celebrity?**
- we mark `celebrity_status = true` in `User` table
- **@Todo**
