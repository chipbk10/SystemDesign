# Hybrid Search

```
{
  "agents": {
    "defaults": {
      "memorySearch": {
        "enabled": true,
        "provider": "openai",        // or "local", etc.
        "query": {
          "hybrid": {
            "enabled": true,
            "vectorWeight": 0.7,    // 70% semantic and 30% keyword
            "textWeight": 0.3
          }
        }
      }
    }
  }
}
```
