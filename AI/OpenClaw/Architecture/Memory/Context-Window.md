**Short Summary**

### 1. **Context Window**
The maximum number of tokens (roughly words) the AI model can process at once.  
Everything sent to the model (history + memory + system prompt + tools) counts toward this limit. When it gets full, performance drops.

### 2. **Memory Flush** (Pre-Compaction Flush)
A safety step that happens **before** compaction.  
The agent is quietly asked to write important facts, decisions, and context into `MEMORY.md` and `memory/YYYY-MM-DD.md` so nothing critical is lost when old history is summarized.

### 3. **Compaction**
When the context window is nearly full, OpenClaw automatically:
- Summarizes the **oldest** parts of the current conversation (**the current session**).
- Replaces the long detailed history with a short summary in the session transcript.
- Keeps recent messages untouched.

This allows very long conversations without hitting the model’s token limit.

---

**Simple Analogy**:  
Context Window = limited desk space  
Memory Flush = copy important notes to permanent notebook before cleanup  
Compaction = replace old papers with a single sticky-note summary
