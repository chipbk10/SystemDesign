# Search Service

## Functional Requirements:
- allows users search a media by keywords (e.g., "hiking" in `title` or `tags`)
- allows users filter by `media_type` (e.g., video)
- allows users rank by relevance (e.g., title matches > tags), and sorted by recency (e.g., sorted by `upload_time`)
- gives users suggestions when typing

## Non-Functional Requirements:
- must handle millions of uploads and queries daily with low latency (<100ms)

## High-Level Architecture
- we will use a Search Service with Amazon OpenSearch for a `full-text search`, integrated with DynamoDB for metadata storage
- Mobile/Web app sends queries via API Gateway to the Search Service, which queries OpenSearch and returns result linking to S3 media

## Indexing
- we index metadata (media_id, title, tags, media_type, user_id, upload_time) in OpenSearch using an inverted index, which maps terms (e.g., "hiking") to media_ids for fast keyword search
- Mobile/Web app uploads a media via Media Service. When status turns into "processed":
  - DynamoDB Streams (**Event Streams**) triggers a `Lambda` function to index new or updated metadata in OpenSearch
  - or push new/updated metadata to OpenSearch (or ElasticSearch) via a **Message Queue**.
  - @Todo [compare](https://www.geeksforgeeks.org/message-queues-vs-event-streams-in-system-design/) between **Event Streams** and **Message Queue**

## Query Processing
- Mobile/Web app sends `GET /api/search?query=hiking&media_type=video` to the Search Service
- Search Service runs a `multi_match` query on `title` and `tags`, filter by `media_type`
- results are ranked by relevance (e.g., title matches > tags), and sorted by `upload_time` if specified

## Scalability and Performance:
- To **scale up**, OpenSearch shards by `media_id` (e.g., shard_number = hash(media_id) % number_of_shards) across nodes (e.g., 5 primary shards, 5 replica shards) to handle millions of documents. A query searches in all shards in parallel, and then combine the results
- frequent queries are **cached** in OpenSearch (**per shard**)
  - **query cache**: stores filter results (e.g., store all video media: `media_type: video -> [media_id1, media_id2, ...]`)
  - **request cache**: stores full json response for a query (e.g., `query: string -> {"results": [...]`)
  - when indexing a new (or updated or deleted) media, the cached results for queries that might include this media_id could become **stale**. OpenSearch invalidates these relevant cached query results to ensure that subsequent searches fetch the updated data from the index.
  - How do we handle frequent invalidations? we can batch updates (e.g., indexing multiple documents in one operation to reduce invalidation frequency)
- we can **cache** the query results in **Redis** to avoid OpenSearch hits. It's good for top queries (e.g., trending, hashtag searches)
  - cacheKey = md5("query=hiking&media_type=video")
  - cacheValue = {"results": [{"media_id": "550...", ...}, ...]}
  - when indexing a new media (e.g., a new media that title contains "hiking"), **the cache query results in Redis become stale**. Tracking which queries are impacted is tricky and adding complexity. In practice, we'd prefer to set a short TTL (e.g., 5 minutes) to naturally expire stale results.

- to reduce latency, we **denormalize** key metadata (e.g., `thumnail_s3_url`). When OpenSearch returns search results, it includes all needed fields (e.g., `media_id`, `title`, `thumbnail_s3_url`), so we don't need to look up in DynamoDB.
  - the trade-off is we increase the index size.
  - another cons ischanges to `thumbnail_s3_url` in DynamoDB require re-indexing in OpenSearch, adding complexity & latency. We have to accept eventual consistency between DynamoDB & OpenSearch. The fast sync via Dynamo Streams < 1s). It means it might take 1 second for a new media to appear in search results.
  - note that we only denormalize only fields needed for search results (e.g., thumbnail_s3_url for UI previews) to minimize index size and costs. Fields like `processed_s3_url` (for video playback) are fetched from DynamoDB later (e.g., via `GET /api/media/download`) when the user selects a video, as they're not needed in search results

- we use `search_after` for **pagination** to avoid **deep scrolling issue** (**@TODO**)
- OpenSearch Dynamic Queries: (**@TODO**)

