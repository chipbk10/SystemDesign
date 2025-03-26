I.**Idempotency issue**
- **idempotent operation**: doesn't change the state with each execution (e.g., GET request - read data, PUT request - update data, DELETE request)
- **non-idempotent operation**: change the state differently with each execution (e.g., POST request - create data, appending data, etc.)
- The **idempotency issue** refers to the problem where retrying a `non-idempotent operation` after a failure can lead to unintended side effects, like duplicate actions or inconsistent data, because the original request might have succeeded without the client knowing.
- For example:
  - Client sends: “Create order for 1 laptop, $1000.”
  - Server processes it, assigns order ID #123, but the response times out.
  - Client retries the same request.
  - Without idempotency, the server creates a second order, ID #124, charging the customer $2000 total.

II.**Solution**:
- To solve the idempotency issue: the client generates a unique idempotency_key, includes it in the HTTP header, and sends it with the initial request and all retries. The server processes the request, stores the outcome with the idempotency_key in a database or cache, and checks each request’s key.
- If it’s already processed, the server returns the stored outcome instead of reprocessing.

III.**Key Takeaways**:
- **Retries + Idempotency = Safe Resilience**



