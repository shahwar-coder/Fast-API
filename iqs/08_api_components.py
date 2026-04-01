'''
1) Why should endpoints represent resources (nouns) instead of actions (verbs) in REST design?

Answer:
REST encourages resource-oriented design.

Good:
GET /users/10
POST /orders

Bad:
GET /getUser
POST /createOrder

Why?
- Aligns with HTTP semantics.
- Improves clarity.
- Standardizes API behavior.
- Makes documentation intuitive.

Senior insight:
HTTP method defines action.
Endpoint defines resource.


2) When should you use PUT vs PATCH?

Answer:
PUT:
- Replaces entire resource.
- Idempotent.

PATCH:
- Partially updates resource.
- Modifies specific fields.

Example:
PUT /users/10 → replace full user object.
PATCH /users/10 → update only email.

Principal mindset:
Use semantic correctness for predictability.


3) What makes an HTTP method idempotent and why does it matter?

Answer:
Idempotent means:
Calling it multiple times has the same effect.

GET → idempotent
PUT → idempotent
DELETE → idempotent
POST → not idempotent

Why it matters:
- Safe retries.
- Distributed systems reliability.
- Load balancer retries won't duplicate actions.

Senior signal:
Idempotency prevents accidental data corruption.


4) Why are headers important beyond authentication?

Answer:
Headers control:
- Content negotiation (Accept)
- Caching (Cache-Control, ETag)
- Rate limits
- Correlation IDs for tracing
- Compression (Accept-Encoding)

Principal insight:
Headers influence infrastructure behavior without changing payload.


5) What is the difference between 401 and 403?

Answer:
401 Unauthorized:
- Identity not verified.
- Missing or invalid credentials.

403 Forbidden:
- Identity verified.
- Permission denied.

Senior understanding:
AuthN failure vs AuthZ failure.


6) If your API always returns 200 even on errors, what problems arise?

Answer:
- Clients cannot distinguish failures.
- Monitoring becomes inaccurate.
- Alerting fails.
- Retry logic breaks.
- Violates HTTP standards.

Principal mindset:
Status codes are part of API contract.


7) How should rate limiting be implemented in distributed systems?

Answer:
Use centralized store like Redis.

Approaches:
- Token bucket
- Leaky bucket
- Sliding window

Must be:
- Distributed-aware
- Per API key/IP
- Tier-based (free vs premium)

Senior signal:
Rate limiting must scale horizontally.


8) What security risks exist in request bodies?

Answer:
- Injection attacks
- Over-posting attacks
- Large payload attacks
- Malformed JSON
- Deserialization exploits

Mitigation:
- Schema validation
- Size limits
- Input sanitization
- Strict typing

Principal insight:
Never trust client input.


9) Why should response bodies avoid exposing internal IDs or sensitive fields?

Answer:
Because:
- Internal schema leaks.
- Security vulnerabilities.
- Attack surface increases.
- Enables data scraping.
- Compliance violations.

Best practice:
Use DTOs (Data Transfer Objects).
Expose only necessary fields.

Senior mindset:
Separate internal model from API model.


10) How do correlation IDs improve API observability?

Answer:
Correlation ID:
Unique ID per request.

Flow:
Client → API → DB → External Service

All logs contain same ID.
Enables:
- Distributed tracing.
- Easier debugging.
- Root cause analysis.

Principal insight:
Observability is built into request lifecycle.


11) What happens if rate limiting is enforced only at application layer and not gateway?

Answer:
- Malicious traffic still reaches app servers.
- Wastes compute resources.
- Can overwhelm infrastructure.
- Higher operational cost.

Better:
Enforce at API gateway or edge layer.

Senior signal:
Protect infrastructure as early as possible.


12) Why is Content-Type validation important?

Answer:
Prevents:
- Parsing errors
- Injection vulnerabilities
- Unexpected behavior
- Exploits via alternate encodings

Example:
Expect application/json only.

Principal mindset:
Strict input contracts reduce ambiguity.


13) How do API components support caching mechanisms?

Answer:
Caching depends on:
- HTTP method (GET cacheable).
- Status code (200).
- Headers (Cache-Control, ETag).
- Idempotency.

Correct component usage enables:
- CDN caching.
- Reverse proxy caching.
- Browser caching.

Senior insight:
Well-designed APIs unlock infrastructure optimizations.


14) In AI inference APIs, how should request and response bodies be designed?

Answer:
Request body:
- Strict input schema.
- Size limits.
- Validation rules.

Response body:
- Structured JSON.
- Include metadata (model_version).
- Include inference time.
- Avoid leaking internal details.

Principal-level thinking:
AI APIs must be deterministic, observable, and safe.
'''