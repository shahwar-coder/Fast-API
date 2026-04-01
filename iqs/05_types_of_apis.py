'''
1) What architectural differences exist between a Web API and a Library API?

Answer:
Web API:
- Runs over network (HTTP/HTTPS).
- Introduces latency.
- Requires authentication and rate limiting.
- Must handle distributed failures.
- Language-agnostic (JSON-based communication).

Library API:
- Runs in-process.
- No network overhead.
- Faster execution.
- Tight version dependency.
- Language-specific.

Senior insight:
Web APIs solve distributed communication.
Library APIs solve code reuse.


2) Why are remote APIs fundamentally more complex than local/library APIs?

Answer:
Because distributed systems introduce:
- Network latency
- Partial failures
- Timeouts
- Retries
- Serialization/deserialization overhead
- Security risks

Golden rule:
In distributed systems, the network is unreliable.

Principal mindset:
Remote API design must assume failure.


3) All Web APIs are Remote APIs. Why is this distinction important?

Answer:
Because some remote APIs use:
- gRPC
- Message queues
- TCP protocols
- Internal service mesh communication

Not all remote APIs are HTTP-based.

Senior signal:
Protocol choice impacts performance, security, and scalability.


4) When would you choose gRPC over REST for a Remote API?

Answer:
Choose gRPC when:
- Low latency is critical.
- High throughput required.
- Strong schema contracts needed.
- Internal microservice communication.
- Streaming support required.

Choose REST when:
- Public-facing APIs.
- Browser compatibility.
- Simplicity preferred.

Principal insight:
Use REST externally, gRPC internally.


5) What risks arise from tight coupling to a Library API?

Answer:
- Breaking changes during upgrades.
- Dependency conflicts.
- Version mismatch issues.
- Vendor lock-in.
- Hidden performance overhead.

Mitigation:
- Pin versions.
- Abstraction wrappers.
- Regular dependency audits.

Senior mindset:
Library APIs are powerful but create dependency risk.


6) How does a Database API improve safety compared to raw database access?

Answer:
Database APIs:
- Abstract connection management.
- Provide query parameterization.
- Prevent SQL injection (when used correctly).
- Manage transactions safely.
- Enforce schema constraints.

Raw database access:
- Risk of injection.
- Manual connection handling.
- No abstraction boundary.

Principal insight:
Database APIs standardize safe data access patterns.


7) In large-scale systems, why should services avoid directly exposing Database APIs?

Answer:
Because:
- It breaks service boundaries.
- Enables tight coupling.
- Exposes internal schema.
- Reduces independent scalability.

Best practice:
Expose Web API or RPC layer instead.
Each service owns its database.

Senior-level understanding:
Data ownership defines service autonomy.


8) What unique challenges exist when designing Hardware APIs?

Answer:
- Real-time constraints.
- Resource limitations.
- Concurrency handling.
- Hardware failures.
- Low-level memory management.
- Driver compatibility.

Example:
GPU APIs must manage memory transfer between CPU and GPU efficiently.

Principal insight:
Hardware APIs must balance abstraction with performance.


9) Why are GUI APIs event-driven instead of request-response like Web APIs?

Answer:
GUI APIs respond to:
- User actions (clicks, typing).
- System events.
- Rendering cycles.

They use event loops instead of stateless requests.

Senior insight:
Different API types follow different interaction paradigms.


10) How does API type influence testing strategy?

Answer:
Web APIs:
- Integration testing
- Contract testing
- Load testing
- Security testing

Library APIs:
- Unit testing
- Mocking dependencies

Hardware APIs:
- Simulation environments
- Hardware-in-the-loop testing

Principal mindset:
Testing strategy depends on API context.


11) In AI systems, which API types commonly interact together?

Answer:
Example architecture:
- Library API → TensorFlow/PyTorch for model training.
- Hardware API → CUDA for GPU acceleration.
- Database API → Store embeddings or metadata.
- Web API → Expose model inference.
- Remote API → Call third-party LLM services.

Senior insight:
AI systems are layered API compositions.


12) If a Remote API call fails intermittently, how should a senior engineer handle it?

Answer:
Techniques:
- Retry with exponential backoff.
- Circuit breaker pattern.
- Timeout enforcement.
- Fallback response.
- Caching previous result.
- Observability metrics.

Principal insight:
Failure handling defines production maturity.


13) How does understanding API types influence system design decisions?

Answer:
Because:
- Network APIs introduce latency.
- Library APIs introduce version dependencies.
- Database APIs impact data consistency.
- Hardware APIs impact performance limits.
- GUI APIs impact UX responsiveness.

Senior-level thinking:
Choosing the wrong API type can create architectural bottlenecks.

Understanding API types helps design systems that scale, remain secure, and evolve safely.
'''