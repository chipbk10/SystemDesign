## SDK
- an SDK is typically a language‑specific wrapper around an API.

## SDK vs API
- While the API defines the core contract and capabilities of the system, the SDK focuses on developer experience by handling repetitive concerns like request construction, authentication, serialization, error handling, and retries.

| Aspect | API | SDK |
|------|-----|-----|
| Purpose | Exposes system capabilities | Simplifies API usage |
| Language | Language-agnostic | Language-specific |
| Level | Low-level | Higher-level |
| Usage style | HTTP requests and payloads | Native methods and objects |
| Responsibility | Defines behavior and data | Improves developer experience |
| Business logic | Implemented on the server | None |
| Required to use system | Yes | No (optional) |

## Example

```python3
from example_sdk import Client

client = Client(api_key="ACCESS_TOKEN")

video = client.videos.create(
    title="My first video",
    description="Demo upload"
)
```

- Under the hood, the SDK:

  - calls POST /videos
  - adds authentication headers
  - serializes the request
  - parses the response into objects
  - translates HTTP errors into exceptions

✅ Same API call, less boilerplate
