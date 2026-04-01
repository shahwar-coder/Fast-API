'''
1) In the weather API example, why is direct database access a bad architectural decision?

Answer:
Direct database access breaks abstraction and security boundaries.

Problems:
- Tight coupling between client and internal schema.
- Any schema change breaks clients.
- No centralized authentication or rate limiting.
- Increased attack surface.
- No control over what data is exposed.

Senior insight:
APIs enforce a contract layer that protects internal systems and enables independent evolution.


2) You described API as a “contract-based gateway.” What exactly is the contract?

Answer:
The contract includes:
- Endpoint URL
- HTTP method
- Request schema
- Response schema
- Status codes
- Authentication mechanism

In production:
This contract is documented using OpenAPI/Swagger.

Breaking the contract = breaking clients.


3) Suppose the weather provider changes their internal database structure. 
Why does your app still work?

Answer:
Because of abstraction.

The API layer isolates internal implementation from external consumers.
As long as the response contract remains unchanged,
clients are unaffected.

This is a core principle of clean architecture.


4) In a production SaaS system, how would you protect the weather API from abuse?

Answer:
- API keys or JWT authentication
- Rate limiting (per user/IP)
- Request validation
- Logging and monitoring
- WAF (Web Application Firewall)
- Caching frequent responses
- DDoS protection

Principal-level thinking:
Security must be layered, not single-mechanism.


5) If 1 million users request weather for Bangalore at the same time, 
what architectural components would you add?

Answer:
- Redis caching (cache weather for short TTL)
- Load balancer
- Horizontal scaling (multiple API instances)
- CDN (if responses are cacheable)
- Async I/O for non-blocking performance

Senior signal:
Never hit the database for repeated identical requests.


6) In the mental model “App → API → Internal System,” 
where should business logic live?

Answer:
Business logic belongs in the service layer inside the backend,
not in controllers/routes.

Layered architecture:
Route → Service → Repository → Database

This improves:
- Testability
- Maintainability
- Scalability


7) What is the difference between exposing data and exposing functionality via API?

Answer:
Exposing data:
GET /weather → returns stored information.

Exposing functionality:
POST /predict-weather-risk → runs algorithm and returns result.

AI systems often expose functionality (model inference), not just raw data.

Principal insight:
Modern APIs expose capabilities, not just CRUD resources.


8) Why is standard communication (JSON + HTTP) important?

Answer:
Standardization enables interoperability.

Benefits:
- Language-agnostic
- Tooling support
- Easy debugging
- Observability via logs
- Works across web, mobile, AI systems

Senior insight:
Standards reduce integration cost.


9) What risks arise if the API exposes “too much” data?

Answer:
- Data leakage
- Security vulnerabilities
- Compliance violations
- Increased payload size (performance issue)
- Attack surface expansion

Best practice:
Return only necessary fields (principle of least privilege).


10) How would you version this weather API without breaking clients?

Answer:
Options:
- URL versioning: /v1/weather
- Header versioning
- Query parameter versioning

Best practice:
Maintain old versions until clients migrate.
Deprecate gradually with communication.

Principal-level thinking:
Never force breakage in distributed systems.


11) If the weather API is slow, where could the bottleneck be?

Answer:
Possible layers:
- Network latency
- Load balancer misconfiguration
- API server CPU limits
- Blocking I/O
- Database query inefficiency
- External provider delay

Senior engineers debug across layers, not just code.


12) How does this API concept apply to AI model serving?

Answer:
AI model serving is the same pattern:

Client → API → Model inference engine

The API:
- Validates input schema
- Authenticates user
- Calls model
- Returns structured output

Without APIs:
No scalable AI deployment is possible.

Principal insight:
APIs are the foundation of production AI systems.
'''