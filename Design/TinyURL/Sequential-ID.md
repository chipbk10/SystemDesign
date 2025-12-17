Two key issues with **sequential IDs** for URL shorteners:

***

### ✅ Why Sequential IDs Need a Global Counter

*   If you assign IDs like `1, 2, 3…`, you need a **single source of truth** to keep track of the next number.
*   In a distributed system, this means:
    *   Either **one central server** (bottleneck).
    *   Or a **distributed lock mechanism** (adds complexity and latency). **@Todo**

***

### ✅ Predictability Problem

*   Sequential IDs are easy to guess:
    *   If you see `abc123`, you can try `abc124` and discover other shortened URLs.
*   While not catastrophic (links are public), it **exposes system behavior** and can lead to:
    *   Crawling attacks.
    *   Enumeration of private-but-obscure links.

***

### ✅ Mitigation Strategies

*   **Rate limiting**:
    *   Limit requests per IP or API key.
*   **Access control**:
    *   Require authentication for sensitive links.
*   **Obfuscation**:
    *   Encode the counter in Base62 or Base64 so it looks random.
    *   Add a random prefix or salt.

***

### ✅ Why Many Shorteners Still Use Sequential IDs

*   It’s **fast and simple** for centralized systems.
*   Easy to implement and scale with sharding (e.g., each server gets a range of IDs).

***
