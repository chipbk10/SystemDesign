# Hybrid Search

- The agent calls the `memory_search` tool (the main way it recalls old information), OpenClaw automatically runs a hybrid search behind the scenes:
  - **Vector / Semantic Search** (meaning-based): Good for concepts, similar idea, paraphrasing
  - **BM25 / Keyword Search** (exact or near-exact matches): Good for proper nouns, IDs, code snippets, config keys, dates, error codes, etc.

- OpenClaw runs **both queries in parallel**, then **merges and ranks** the results using a weighted score (typically ~70% semantic + 30% keyword)

## Memory Search

- The agent (via its system prompt and tool descriptions) is trained/instructed to call `memory_search` whenever it thinks it needs past information that isn't in the current context. For example:
  - Any question about past decisions, preferences, events
  - What did we decide about X?
  - Recall my setup for Y
  - Anything involving **remember**, **last time**, **previously**, specific facts from old notes
