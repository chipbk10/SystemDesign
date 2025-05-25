# Questions
1. **Do you immediately send every typing or small changes (e.g., adding a space, comma, changing a color, font size, etc.) via WebSocket to sync with others?**
- Yes, for real-time collaboration like Google Docs, the front-end (web/mobile app) sends most typing and small changes (e.g., adding a space, comma, formatting) immediately via WebSocket to the Real-Time Sync Service to sync with other collaborators
- However, to optimize performance and reduce network overhead, changes are typically batched or debounced, balancing responsiveness and efficiency
  - batching: we will batch all changes within a short time window (e.g., 50-100ms) into a single WebSocket request to reduce network overhead
  - debouncing: it then wait for a debouncing period (e.g., 100ms-200ms) before sending the next batch of changes, ensuring efficient real-time sync while maintaining responsiveness

2. **Do you send the whole content of the document in every WebSocket request?**
- No, we send only the incremental changes (e.g., an operation, a collection of operations - a delta)
- This way minimizes data transfer and ensures efficient real-time sync
- For example:
  - an operation: for insert the text "Hello" at position 0 with bold formatting
    ```json
      {
        "op": "insert",
        "value": "Hello",
        "offset": 0,
        "attributes": {
          "bold": true
        }
      }
    ``` 
  - a deltas: contains 2 operations for a single document - inserting a space at position 5 and then inserting "World" after that
    ```json
    {
      "document_id": "doc123",
      "delta": [
        {"op": "insert", "value": "Hello", "offset": 0},
        {"op": "insert", "value": " ", "offset": 5}
      ]
    }
    ```
3. **How do you handle editing in the offline mode?**
- we can queue the offline changes in local storage

4. **Tell me about the local storage from the web/mobie app**
- for web app, we can use IndexDB **@Todo**
- for native mobile app, we can use  SQLite
- for cross-platform: we can a lightweight NoSQL database (e.g., Hive or Sembast)
