'''
[1] Definition  

An API (Application Programming Interface) is like a waiter in a restaurant.

You (client) tell the waiter what you want.
The waiter takes your request to the kitchen (server).
The kitchen prepares it and sends it back through the waiter.

Technically:
An API is a set of rules that allows two software systems to talk to each other.

Why it is required:
- Frontend and backend cannot directly access each other’s code.
- APIs create a safe communication bridge.
- They allow apps, websites, and services to work together.

Example:
GET /users/1
→ Server sends user data in JSON.

---

[2] Key Features  

What makes an API reliable:

• Request → Response model  
• Uses structured data (usually JSON)  
• Uses HTTP status codes (200 = success, 404 = not found)  
• Usually stateless (each request is independent)  
• Supports authentication  

Why required:
- Makes communication predictable.
- Allows scaling across thousands of users.
- Ensures systems remain simple and organized.

Interview Insight:
Stateless APIs scale better because the server doesn’t store client session data.

---

[3] Types of APIs  

Based on who can use them:

• Public API → Anyone can use it (e.g., payment gateway APIs)  
• Private API → Only internal teams use it  
• Partner API → Shared with specific partners  

Why required:
- Controls access.
- Protects business logic and internal systems.

Interview Insight:
Most SaaS companies heavily use private + partner APIs internally.

---

[4] API Protocols  

Protocols define HOW communication happens.

• REST → Most common, simple, HTTP-based  
• GraphQL → Client chooses exactly what data it needs  
• gRPC → High-performance, used in microservices  
• SOAP → Older, XML-based  

Why required:
- Different systems need different performance and flexibility levels.

Simple understanding:
REST = ask for resource  
GraphQL = ask exactly what you want  
gRPC = call a function remotely  

---

[5] Working  

Step-by-step:

1. Client sends request  
2. Server processes logic  
3. Server sends response  

Example:
POST /login  
→ Validate username/password  
→ Return JWT token  

Why required:
- Defines a clear communication pattern.
- Allows distributed systems to function properly.

---

[6] API Components  

Every API request contains:

• Endpoint → Where to send request (/users)  
• Method → What action (GET, POST, PUT, DELETE)  
• Headers → Extra info (auth tokens)  
• Body → Data sent to server  
• Status Code → Result of request  
• Response → Data returned  

Why required:
- Each part has a clear role.
- Makes APIs structured and standard.

Think of it like:
Address + Action + Identity + Data + Result.

---

[7] API Lifecycle  

APIs are not “build once and forget”.

Stages:
• Design  
• Develop  
• Test  
• Deploy  
• Version (v1, v2)  
• Maintain  
• Deprecate  

Why required:
- Clients depend on APIs.
- Breaking an API can break mobile apps, dashboards, AI systems.

Interview Insight:
Versioning (e.g., /v1/users) prevents breaking existing users.

---

[8] Authentication & Authorization  

Authentication = Who are you?  
Authorization = What are you allowed to do?

Example:
User logs in → gets JWT token  
JWT sent in header → server verifies identity  
Server checks role → allows or denies action  

Why required:
- Protects sensitive data.
- Prevents misuse of APIs.
- Essential for production systems.

Interview Insight:
Authentication verifies identity.
Authorization enforces permissions.
They are different but often confused.

---

Final Mental Model:

API = Structured conversation between systems.

Without APIs:
- No microservices
- No SaaS platforms
- No AI model serving
- No mobile apps talking to backend

APIs are the backbone of modern backend engineering.
'''