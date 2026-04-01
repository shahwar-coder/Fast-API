'''
API Protocols (With Code Examples)

These define HOW systems communicate.

---

1. REST (Representational State Transfer)

Lightweight, HTTP-based, stateless communication.

Example (FastAPI style):

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Shahwar"}

Note:
This defines a REST endpoint.
Client calls GET /users/10 → Server returns JSON.
Each request is independent and resource-based.

---

2. SOAP (Simple Object Access Protocol)

XML-based, structured, enterprise-focused protocol.

Example (SOAP XML Request):

<soap:Envelope>
  <soap:Body>
    <GetUser>
      <UserId>10</UserId>
    </GetUser>
  </soap:Body>
</soap:Envelope>

Note:
Client sends structured XML to request a user.
SOAP defines strict message format and security standards.

---

3. GraphQL

Client requests exactly the fields it needs.

Example (GraphQL Query):

{
  user(id: "10") {
    name
    email
  }
}

Note:
Client asks only for name and email.
Prevents over-fetching unnecessary fields.
Single endpoint handles all queries.

---

4. gRPC (Google Remote Procedure Call)

High-performance RPC using Protocol Buffers.

Example (.proto definition):

service UserService {
  rpc GetUser (UserRequest) returns (UserResponse);
}

message UserRequest {
  int32 user_id = 1;
}

message UserResponse {
  string name = 1;
}

Note:
Client calls GetUser(user_id=10) like a normal function.
Data is serialized in compact binary format.
Used for fast service-to-service communication.

---

5. WebSocket

Persistent, real-time communication channel.

Example (JavaScript):

const socket = new WebSocket("ws://localhost:8000/ws");

socket.onmessage = (event) => {
  console.log("Received:", event.data);
};

socket.send("Hello Server");

Note:
Connection stays open.
Client and server can send messages anytime.
Used for chat apps, gaming, live dashboards.

---

Quick Map — When to Use What?

REST → Standard web/mobile APIs  
SOAP → Enterprise secure integrations  
GraphQL → Flexible frontend data needs  
gRPC → High-performance microservices  
WebSocket → Real-time communication  

Core Insight:

Choose protocol based on:
• Data flexibility needs  
• Performance requirements  
• Security constraints  
• Real-time vs request-response model  
'''

# ====

'''
Top Differences: REST vs SOAP vs GraphQL

| Parameter              | REST                              | SOAP                                | GraphQL                              |
|------------------------|-----------------------------------|--------------------------------------|---------------------------------------|
| 1. Type                | Architectural style               | Strict protocol                     | Query language + runtime             |
| 2. Data Format         | Usually JSON                      | XML only                            | JSON (response), flexible queries    |
| 3. Endpoint Structure  | Multiple endpoints (/users, /orders) | Single endpoint with defined operations | Single endpoint (/graphql)          |
| 4. Data Fetching       | Fixed response structure          | Fixed contract (WSDL-based)         | Client chooses exact fields needed   |
| 5. Typical Use Case    | Web & mobile APIs                 | Enterprise & banking systems        | Frontend-heavy, complex UIs          |

Quick Insight:

REST → Simple, widely used, resource-based  
SOAP → Formal, secure, enterprise-heavy  
GraphQL → Flexible, client-driven data fetching  
'''