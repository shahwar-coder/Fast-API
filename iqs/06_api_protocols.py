'''
1) When would REST become a bottleneck in a high-scale microservices architecture?

Answer:
REST can become a bottleneck when:
- High request volume between internal services.
- Large JSON payload overhead.
- High latency sensitivity.
- Need for streaming.
- Heavy serialization/deserialization cost.

Because REST uses:
- Text-based JSON
- HTTP/1.1 (often)
- Repeated headers

In such cases:
gRPC with Protocol Buffers (binary + HTTP/2) is more efficient.

Principal insight:
REST is excellent for external APIs, not always optimal for internal service mesh.


2) Why is SOAP still used in enterprise systems despite being older?

Answer:
Because SOAP provides:
- Strict contracts (WSDL)
- Built-in security standards (WS-Security)
- Formal message structure
- Strong compliance alignment
- Transaction support

In banking, healthcare, government:
Predictability and compliance > flexibility.

Senior signal:
Technology choice depends on domain constraints.


3) GraphQL prevents over-fetching. What new complexity does it introduce?

Answer:
GraphQL introduces:
- Complex resolver logic
- Harder caching
- Query depth abuse risks
- Performance unpredictability
- N+1 query problems
- Security concerns (deep nested queries)

Mitigation:
- Query depth limits
- Cost analysis
- DataLoader pattern
- Monitoring heavy queries

Principal mindset:
Flexibility increases backend responsibility.


4) Why is gRPC often preferred for internal microservices?

Answer:
Because it provides:
- Binary serialization (smaller payloads)
- Strong typing via .proto
- Auto-generated client/server code
- Streaming support
- HTTP/2 multiplexing
- Low latency

Senior-level thinking:
In internal systems, performance and type safety matter more than browser compatibility.


5) If you had to design an AI inference service for real-time trading, 
which protocol would you choose and why?

Answer:
Likely gRPC.

Reasons:
- Low latency requirement
- High throughput
- Binary efficiency
- Strong schema enforcement
- Streaming support for live updates

REST may introduce unnecessary overhead.

Principal insight:
Protocol selection must align with latency budget.


6) Why are WebSockets fundamentally different from REST?

Answer:
REST:
- Stateless
- Request-response
- Short-lived connections

WebSocket:
- Persistent connection
- Bidirectional communication
- Event-driven
- Real-time streaming

Use case difference:
REST = retrieve/update resource.
WebSocket = continuous data flow.

Senior signal:
Choose communication model based on interaction pattern.


7) What security concerns arise with WebSockets?

Answer:
- Long-lived connection abuse
- DoS via open connections
- Authentication persistence
- Message injection
- Lack of rate limiting

Mitigation:
- Authenticate during handshake
- Token validation per message (if needed)
- Connection limits
- Timeout policies
- Monitoring open connection count

Principal mindset:
Persistent connections increase attack surface.


8) Why is REST considered resource-oriented while gRPC is function-oriented?

Answer:
REST:
- Based on resources (/users/10)
- Uses HTTP verbs (GET, POST)

gRPC:
- Based on remote procedure calls
- Calls named methods (GetUser)

REST models nouns.
gRPC models actions/functions.

Senior insight:
Architectural style influences API modeling philosophy.


9) If you expose a public API for millions of developers, 
which protocol is safest and easiest to adopt?

Answer:
REST.

Reasons:
- Universal HTTP support
- Easy debugging (browser/curl)
- Language-agnostic
- Wide tooling ecosystem
- Human-readable JSON

Principal insight:
Adoption friction matters in public platforms.


10) When does GraphQL outperform REST significantly?

Answer:
When:
- Frontend needs flexible nested data.
- Multiple round trips would otherwise be required.
- Mobile apps with bandwidth constraints.
- Rapidly evolving UI requirements.

GraphQL reduces:
- Over-fetching
- Under-fetching
- Multiple endpoint calls

Senior signal:
GraphQL shines in frontend-heavy ecosystems.


11) How does protocol choice impact observability and monitoring?

Answer:
REST:
- Easy logging (JSON readable)
- HTTP status codes standardized
- Tooling support mature

gRPC:
- Requires specialized monitoring tools
- Binary payload not human-readable
- Metrics need structured instrumentation

WebSocket:
- Harder to monitor request-level metrics
- Need connection-level observability

Principal insight:
Operational complexity increases with protocol sophistication.


12) In AI systems, how might multiple protocols coexist?

Answer:
Example architecture:
- REST → Public inference API.
- gRPC → Internal microservices communication.
- WebSocket → Real-time streaming responses.
- GraphQL → Flexible dashboard queries.
- Hardware API → CUDA for GPU inference.

Senior-level thinking:
Production systems often combine protocols strategically.


13) If performance is not an issue, should you default to gRPC over REST?

Answer:
No.

Consider:
- Browser support limitations.
- Developer familiarity.
- Tooling maturity.
- Public adoption ease.
- Debugging complexity.

Principal mindset:
Choose the simplest solution that meets requirements.
Complexity must be justified.
'''

'''
14) What is statelessness in Web APIs, and why is it important?

Answer:
Statelessness means:
The server does not store client session state between requests.
Each request must contain all the information needed to process it.

Example:
Client sends JWT token in every request:
GET /profile
Header: Authorization: Bearer <token>

The server:
- Verifies token
- Processes request
- Sends response
- Does not remember previous interaction

Why it is important:

1) Horizontal Scalability  
   Any request can go to any server instance.
   No need for sticky sessions.

2) Simpler Infrastructure  
   No in-memory session tracking.
   Easier load balancing.

3) Fault Tolerance  
   If one server crashes,
   another can handle the next request without issue.

Trade-offs:
- Slightly larger requests (token sent each time).
- If session-like behavior is needed, external store (Redis/DB) must be used.

Senior Insight:
Stateless APIs + externalized state (Redis, DB) 
= foundation of scalable cloud-native architecture.
'''