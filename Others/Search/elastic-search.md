# Elastic Search

## API
- RESTful API

## Indexing
- send a document for indexing:
```json
POST /posts/_doc/1
{
  "title": "A good holiday",
  "description": "Flying to California beach in the morning, so good weather, feel relaxed with our family",
  "created_time": "2025-07-11T15:47:00+07:00"
}
```
- Elastic search hashes the document ID (`1`) to determine which primary shard to handle it.
  - Example, shard 0 is on Node A, so the document goes to Node A
- Lucene on shard 0 will handle the fields
  - analyze + tokenize + filter + inverted indexing (`store in Memory` to reduce disk I/O, will batch updates in refresh process)
  - stores full json document in the `_source` field for retrieval
  - the operation is logged in the transaction log for durability
  - the document is synchronously copied to replica shards (e.g., a replica of shard 0 on Node B) for fault tolerance and load balancing
  - uses a refresh process (every 1 second) to updates the shard's inverted index to include newly indexed document (still in memory), making it searchable
  


## Searching
- submit a search query
```json
GET /posts/_search
{
  "query": {
    "match": { "description": "California beach" }
  }
}
```
- the query is sent to a coordinating node, which identifies which shards need to be queried (all primary or replicas)
- at each shard, the same process happens:
  - analyze + tokenize (e.g., to `["california", "beach"]`)
  - check the relevant field's (e.g., in this case is `description`) inverted index
  - Lucene calculates a relevance score for matches
- each shard processes the query independently (in parallel), and then returns its top matching to the coordinating node
- the coordinating node merges result, sort them by relevance score, and removes duplicates
- the coordinating node fetches the full document for the matching IDs (e.g., Doc1) from the `_source` field
- @Todo

# Questions
1. Why don't we call as a `coordinating shard`?
2. How to mitigate the coordinating node overwhelming?
3. Can you tell me other cloud-solutions (AWS Open Search, or Elastic Cloud)?
