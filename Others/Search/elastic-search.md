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
- @Todo
