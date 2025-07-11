## What is Indexing in a Search Engine?

- Indexing is a process of organizing and storing data (e.g., media metadata) in a specialized data structure optimized for **fast, flexible, and relevant search queries**
  
- Indexing creates a structure (called an **inverted index**) that allows efficient searching across multiple fields (e.g., `title`, `description`, `tags`) using keywords, partial matches, filter, and ranking based on different criterias (e.g., frequency, proximity, relevance, recency, etc.)

- Indexing supports complex queries like "find videos with `hiking` in the title or tags"

## Analyzer Processing before indexing

- **character filters**: preprocess the text (e.g., remove HTML tags or special characters)
- **tokenizer**: splits the text into tokens based on rules (e.g., splitting on whitespace or punctuation)
- **token filters**: modify tokens (e.g., lowercase them, remove stopwords like `a`, `to`, or stem words like `running` to `run`)

## Inverted index

- these tokens are added to the inverted index, mapping each token to the document containing it.
  - `hiking` -> `[media_id: 550, media_id: 123, ....]`
  - `mountain` -> `[media_id: 550, ...]`

- we might have separate inverted indices for each field (e.g., title, description, etc.) within a shard
