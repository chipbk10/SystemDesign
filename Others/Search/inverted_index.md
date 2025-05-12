## What is Indexing in a Search Engine?
- Indexing is a process of organizing and storing data (e.g., media metadata) in a specialized data structure optimized for **fast, flexible, and relevant search queries**
- Indexing creates a structure (called an **inverted index**) that allows efficient searching across multiple fields (e.g., `title`, `tags`) using keywords, partial matches, filter, and ranking supporting complex queries like "find videos with `hiking` in the title or tags"


## Inverted index
- maps **terms** (words or tokens) to the **documents** (e.g., media records) containing them
  - Term `hiking` -> `[media_id: 550, media_id: 123, ....]`
  - Term `mountain` -> `[media_id: 550, ...]`

- **@TODO**
