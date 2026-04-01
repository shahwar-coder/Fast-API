'''
1) You said APIs are usually stateless. Why does statelessness improve scalability? 
   What trade-offs does it introduce?

Answer:
Statelessness means the server does not store client session data between requests.
Each request contains everything needed (like JWT in headers).

Why it improves scalability:
- Any request can go to any server instance (horizontal scaling becomes easy).
- No need for sticky sessions.
- Load balancers distribute traffic freely.

Trade-offs:
- Slightly larger request size (because auth/token is sent every time).
- If you need session-like behavior, you must use external stores (Redis, DB).

In production:
Stateless APIs + external state store (Redis) = scalable architecture.
This is how large SaaS systems operate.


2) In a high-traffic SaaS system, when would REST be a bad choice compared to gRPC?

Answer:
REST is text-based (JSON over HTTP) and slightly heavier.
gRPC uses binary protocol (Protocol Buffers) and HTTP/2.

gRPC is better when:
- Internal microservices communicate heavily.
- Low latency is critical.
- High throughput is required.
- Strong schema contracts are needed.

REST is better when:
- Public APIs are exposed.
- Browser compatibility is needed.
- Simplicity is preferred.

Senior insight:
Use REST externally, gRPC internally.


3) A mobile app calls GET /users/1 and receives 200 but wrong data. 
   Is this an API failure? Why?

Answer:
Yes, logically it is a failure.

HTTP status codes indicate transport-level success.
But business logic correctness is different.

If:
- Response structure is correct (transport success)
- But data is incorrect (logic failure)

Then:
It is an application-level bug, not protocol-level failure.

Senior thinking:
Differentiate transport errors vs domain/business logic errors.


4) Why is versioning (/v1, /v2) critical in production systems?

Answer:
Clients depend on API contracts.
If you change response structure without versioning:
- Mobile apps break.
- Integrations fail.
- External partners lose trust.

Versioning allows:
- Backward compatibility.
- Safe migrations.
- Gradual deprecation.

Principal-level thinking:
Never break contracts. Evolve them.


5) Explain the difference between authentication and authorization 
   using a real SaaS example.

Answer:
Authentication = verifying identity.
Example: JWT verifies user is Shahwar.

Authorization = checking permissions.
Example: Shahwar can read invoices but not delete them.

Common mistake:
Developers check only authentication but forget role checks.

Production best practice:
AuthN (identity) → AuthZ (role/permission) → Business logic.


6) Why are HTTP status codes important beyond just 200 and 404?

Answer:
They standardize error communication.

Examples:
- 201 → Resource created
- 400 → Bad request
- 401 → Unauthorized
- 403 → Forbidden
- 409 → Conflict
- 500 → Internal error

Why important:
Frontend and other services rely on consistent codes.
Monitoring systems rely on status codes for alerting.
SRE teams use 5xx spikes to detect incidents.

Senior signal:
Correct status codes improve observability.


7) What are potential security risks in public APIs?

Answer:
- Unauthorized access
- Token theft
- Rate abuse
- Injection attacks
- Data overexposure
- Replay attacks

Mitigations:
- HTTPS
- JWT expiration
- Rate limiting
- Input validation
- Proper role checks
- Logging and monitoring

Principal insight:
Security must be layered, not single-point protection.


8) If APIs are “just communication bridges”, where does business logic live?

Answer:
Business logic should live in the backend service layer,
not in controllers/routes.

Why:
- Separation of concerns
- Easier testing
- Reusability
- Clean architecture

In FastAPI terms:
Routes → call service layer → call repository/DB layer

Senior engineers avoid putting logic inside route handlers.


9) When would GraphQL be better than REST?

Answer:
GraphQL is better when:
- Frontend needs flexible data fetching.
- Multiple nested resources are required.
- Over-fetching or under-fetching is a problem.

Example:
Mobile app wants only user name + email.
REST may return entire object.
GraphQL returns only requested fields.

Trade-off:
- More complex caching.
- More complex backend logic.


10) In distributed systems, what happens if one API call depends on another?

Answer:
This creates tight coupling.

Risks:
- Cascading failures
- Increased latency
- Retry storms

Solutions:
- Circuit breakers
- Timeouts
- Retry policies
- Async event-driven communication
- Caching

Senior thinking:
Design APIs to be loosely coupled.


11) Why is API lifecycle management important for AI systems?

Answer:
AI systems often expose model inference APIs.

If API changes:
- Client apps break.
- Prompt formats mismatch.
- Output schema changes cause downstream errors.

Lifecycle ensures:
- Stable contracts
- Gradual model upgrades
- Backward compatibility

Principal-level insight:
API stability is more important than rapid feature changes.


12) What makes an API “production-ready”?

Answer:
- Authentication & Authorization
- Proper status codes
- Input validation
- Logging
- Monitoring
- Rate limiting
- Versioning
- Documentation (OpenAPI)
- Error handling

Not production-ready:
Just returning JSON from a route.

Senior mindset:
APIs are infrastructure, not just endpoints.
'''