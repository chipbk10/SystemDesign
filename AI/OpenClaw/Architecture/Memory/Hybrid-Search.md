# Hybrid Search

## memory_search

- The agent (via its system prompt and tool descriptions) is trained/instructed to call `memory_search` whenever it thinks it needs past information that isn't in the current context. For example:
  - Any question about past decisions, preferences, events
  - What did we decide about X?
  - Recall my setup for Y
  - Anything involving **remember**, **last time**, **previously**, specific facts from old notes
- For example, we provide strong instructions in `AGENTS.md`:
```
Before answering any question about past events, decisions, or preferences, always use the memory_search tool first.
```

## Indexing
- OpenClaw splits all **Markdown files** (`MEMORY.md` + `memory/YYYY-MM-DD.md` + other workspace files) into small **chunks** (~400 tokens each with overlap).
- Each chunk is stored in SQLite with:
  - Full text (for `keyword search`)
  - Vector embedding (for `semantic search`)

### Search
- When the agent uses `memory_search`, OpenClaw performs **hybrid search** by default:
  - **Vector / Semantic Search** (meaning-based): Good for concepts, similar idea, paraphrasing
  - **BM25 / Keyword Search** (exact or near-exact matches): Good for proper nouns, IDs, code snippets, config keys, dates, error codes, etc.
  - OpenClaw runs **both queries in parallel**, then **merges and ranks** the results using a weighted score (typically ~70% semantic + 30% keyword)
    
- **Important**: Hybrid search works **only on Markdown files**.  
  Old conversation history (`.jsonl` session files) is **not indexed** by default.

### Old Session Files (`sessionId.jsonl`)
These are **not used** for normal search. They are kept on disk for:
- Full conversation recovery
- Backup
- Debugging
- Manual inspection
- Optional future indexing

**In short**:  
Markdown files = Clean, curated, searchable long-term memory (hybrid search).  
Session files = Raw history archive (not searchable by default).

This design keeps the agent's working memory clean and efficient while preserving complete history.


