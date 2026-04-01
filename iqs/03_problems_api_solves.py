'''
1) In a large SaaS system, how do you detect tight coupling before it causes production failures?

Answer:
Indicators of tight coupling:
- Clients depend on raw database schema.
- Frequent breaking changes after backend refactors.
- Multiple clients tightly bound to internal column names.
- No API contract documentation.

Detection methods:
- Schema change impact analysis.
- Contract tests between services.
- Observing high client breakage after minor backend changes.

Senior insight:
If a small backend refactor breaks multiple clients, you have coupling debt.


2) Suppose you must migrate a database schema in production without downtime.
How would the API layer help?

Answer:
Safe migration pattern:
1. Add new column (temperature_celsius).
2. Keep old column temporarily.
3. API maps both internally.
4. Gradually update backend logic.
5. Remove old column after validation.

Because clients only talk to API:
The migration is invisible externally.

Principal-level thinking:
APIs enable zero-downtime schema evolution.


3) If APIs reduce attack surface, why do API breaches still happen?

Answer:
Because:
- Poor authentication implementation.
- Misconfigured CORS.
- Broken object-level authorization (IDOR).
- Weak rate limiting.
- Insufficient input validation.
- Token leakage.

APIs reduce attack surface — but only if properly implemented.

Security is architectural, not automatic.


4) How would you design rate limiting for a weather API serving 5 million users?

Answer:
Approach:
- Use Redis for distributed rate limiting.
- Token bucket or leaky bucket algorithm.
- Limit per API key + per IP.
- Different tiers (free vs paid users).
- Burst allowance with sustained cap.

Senior signal:
Rate limiting must be distributed and horizontally scalable.


5) Why is exposing raw SQL capability more dangerous than exposing controlled endpoints?

Answer:
Raw SQL:
- Allows arbitrary queries.
- Enables schema discovery.
- Enables data exfiltration.
- Enables destructive operations.

Controlled endpoints:
- Restrict operations to predefined actions.
- Validate inputs.
- Apply authorization checks.
- Sanitize parameters.

Principal insight:
Security = reducing degrees of freedom for attackers.


6) In the “No Control Over Data Exposure” problem, what principle is being applied?

Answer:
Principle of Least Privilege.

Users should only access:
- The minimum data required.
- The minimum permissions required.

APIs enforce this by:
- Filtering fields.
- Enforcing role-based access.
- Restricting endpoints.

Senior-level understanding:
Data minimization reduces legal and compliance risks (GDPR, etc.).


7) If the database is hidden behind an API, is it fully secure?

Answer:
No.

Additional risks:
- Insider threats.
- API vulnerabilities.
- Misconfigured infrastructure.
- Credential leaks.
- Supply chain attacks.

Security must include:
- Network isolation (VPC).
- IAM controls.
- Secrets management.
- Monitoring & alerting.

APIs are one layer in a defense-in-depth strategy.


8) How does tight coupling affect microservices architecture?

Answer:
If microservices directly access each other's databases:
- Service boundaries collapse.
- Independent deployment becomes impossible.
- Cascading failures increase.
- Schema changes ripple across services.

Best practice:
Each service owns its database.
Other services communicate via APIs or events.

Principal mindset:
Service autonomy is critical for scalability.


9) In the absence of an API, how would scaling failures manifest?

Answer:
Symptoms:
- Database connection pool exhaustion.
- Increased query latency.
- Deadlocks.
- CPU spikes.
- System crashes.

Without rate limiting:
Abusive clients monopolize resources.

Senior insight:
APIs act as traffic regulators before load reaches critical infrastructure.


10) How would you design an API to prevent data scraping attacks?

Answer:
Mitigations:
- Rate limiting.
- CAPTCHA (if public-facing).
- Behavioral anomaly detection.
- API key enforcement.
- Pagination limits.
- Monitoring unusual access patterns.
- Rotating tokens.

Principal-level thinking:
Security must consider economic incentives of attackers.


11) If internal ML models are stored in the database, how should they be exposed safely?

Answer:
Never expose raw model files via API.

Instead:
- Expose inference endpoints only.
- Validate inputs strictly.
- Control output schema.
- Log inference usage.
- Apply authorization checks.

AI systems should expose capability, not assets.


12) What monitoring metrics would indicate API abuse?

Answer:
- Sudden spike in 4xx or 5xx errors.
- Unusual traffic from single IP/API key.
- High request burst patterns.
- Increased DB read/write load.
- Repeated authentication failures.

Senior signal:
Security monitoring must be real-time, not reactive.


13) How does abstraction through APIs improve long-term system evolution?

Answer:
Abstraction allows:
- Refactoring internal architecture.
- Changing database vendors.
- Migrating to microservices.
- Adding caching layers.
- Introducing async processing.

All without breaking clients.

Principal insight:
APIs are stability layers in evolving systems.
'''