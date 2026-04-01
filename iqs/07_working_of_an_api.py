'''
1) In the Request → Process → Response cycle, where should input validation happen and why?

Answer:
Input validation should happen at the API boundary (controller/route layer)
before business logic is executed.

Why:
- Prevent invalid data from entering system.
- Reduce unnecessary DB calls.
- Block malicious payloads early.
- Enforce schema contract.

Senior insight:
Validate at the edge. Trust nothing from the client.


2) What is the difference between an endpoint and business logic?

Answer:
Endpoint:
- Defines URL and HTTP method.
- Handles request parsing.
- Calls service layer.

Business logic:
- Contains domain rules.
- Performs calculations.
- Enforces constraints.

Clean architecture:
Route → Service → Repository → DB

Principal mindset:
Endpoints are transport adapters, not logic containers.


3) During request processing, where should authentication and authorization occur?

Answer:
Authentication:
- Early in the request lifecycle (middleware or dependency layer).

Authorization:
- After identity is verified, before executing business logic.

Flow:
Request → AuthN → AuthZ → Business Logic → DB

Senior insight:
Fail fast on security checks to reduce attack surface.


4) If an API endpoint calls multiple downstream services, what risks arise?

Answer:
- Increased latency.
- Cascading failures.
- Partial success scenarios.
- Retry storms.
- Tight service coupling.

Mitigation:
- Timeouts.
- Circuit breakers.
- Async processing.
- Caching.
- Fallback responses.

Principal-level thinking:
Distributed calls multiply failure probability.


5) Why should database access not happen directly inside the endpoint function?

Answer:
Because:
- Violates separation of concerns.
- Harder to test.
- Difficult to reuse logic.
- Encourages tight coupling.

Best practice:
Use repository or data access layer.

Senior signal:
Structured layering improves maintainability.


6) What distinguishes a 400 error from a 422 error?

Answer:
400 Bad Request:
- Malformed request.
- Missing required parameters.

422 Unprocessable Entity:
- Request structure valid,
- But semantic validation failed.

Example:
Age = -5 (valid JSON but invalid business rule).

Principal insight:
Use precise status codes for clarity and observability.


7) If the API returns 200 but incorrect data, where might the issue be?

Answer:
Possible causes:
- Business logic bug.
- Incorrect DB query.
- Caching stale data.
- Serialization mapping error.
- Incorrect authorization filtering.

Senior-level debugging:
Trace across layers, not just endpoint.


8) What happens internally when a GET request is made in a stateless API?

Answer:
- Load balancer routes request.
- Server parses request.
- Auth validated.
- Business logic executed.
- DB queried.
- JSON serialized.
- Response returned.
- No session stored.

Statelessness allows:
Any server instance to handle the next request.


9) How would you optimize the “Response Generation” step for high throughput APIs?

Answer:
- Use efficient serialization (ujson/orjson).
- Avoid heavy object transformations.
- Cache repeated responses.
- Use compression (gzip).
- Reduce payload size.
- Stream large responses.

Principal mindset:
Serialization cost matters at scale.


10) What observability signals should you capture in the Request → Response cycle?

Answer:
- Request latency (p95/p99).
- Error rate (4xx/5xx).
- Request volume.
- DB query time.
- External API latency.
- Authentication failures.
- Rate-limit violations.

Senior insight:
You cannot scale what you cannot measure.


11) How does async programming change the Request → Process → Response model?

Answer:
Async allows:
- Non-blocking I/O.
- Better concurrency.
- Higher throughput per instance.

Instead of waiting for DB/network call,
event loop handles other requests.

Principal insight:
Async improves I/O-bound API performance, not CPU-bound tasks.


12) If the database is slow, how does that affect the entire API cycle?

Answer:
Impact:
- Increased response latency.
- Connection pool exhaustion.
- Thread starvation (if blocking).
- Increased 5xx errors.

Mitigation:
- Query optimization.
- Caching.
- Read replicas.
- Async DB drivers.
- Circuit breakers.

Senior signal:
Database performance directly impacts API reliability.


13) Where should rate limiting be enforced in the API flow?

Answer:
Preferably:
- At API Gateway.
- Or Middleware layer before business logic.

Why:
- Prevents unnecessary resource consumption.
- Protects DB and downstream services.

Principal mindset:
Protect infrastructure as early as possible in request lifecycle.
'''