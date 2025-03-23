I.**What is a Circuit Breaker?**
- A circuit breaker is a design pattern that monitors for failures in external service calls (e.g., APIs, databases). If failures exceed a threshold, it "trips" (ngắt) and stops further requests for a period, allowing the system to recover. It typically has three states:
  - **Closed**: Requests flow normally.
  - **Half-Open**: Limited requests (`threshold`) are allowed to test if the downstream service has recovered.
  - **Open**: Requests are blocked due to repeated failures.

II. **Why do we need circuit breaker?**
- to enhance the resilience of your application by preventing `cascading failures` when a downstream service becomes unavailable or slow.

III.**Circuit breaker implementation**
- Circuit breakers are usually implemented locally with each service
- [Python: circuit breaker implemenation](https://github.com/chipbk10/SystemDesign/blob/master/circuit-breaker.py)

III.**Local breaker vs remote breaker**
- api A has a heavy work on its own
- api A calls api B, C, D concurrently (all at once)
- if any one of the downstream apis (B, C, or D) fails, A will fail entirely

- local breaker: use 3 breakers for B, C and D in api A
- remote breaker: implement breakers at B, C, and D

- local breaker is better
  - **latency**: no need to make a real call (B, C or D), can fail api A faster
  - **resources**: less network resources (opening connections, sending packages, etc.)

IV.**Local breakers implementation**
- [Python: local breakers implemenation](https://github.com/chipbk10/SystemDesign/blob/master/local-circuit-breaker.py)
