'''
API Components (Revised & Production-Oriented)

An API works through clearly defined components.
Each component has a specific responsibility in the request–response cycle.

---

1. Endpoint  

An endpoint is the full URL where a client sends a request.

Production Example:

GET https://api.company.com/v1/users/10?include=posts

Breakdown:

https://              → Protocol (secure communication)
api.company.com       → API host (server)
v1                    → API version
/users                → Resource
/10                   → Path parameter (specific user ID)
?include=posts        → Query parameter (modifies response)
GET                   → Operation (retrieve data)

Endpoints precisely define:
WHAT resource,
WHICH version,
WHICH specific item,
AND WHAT action to perform.

Endpoints are the entry doors to the API.

---

2. HTTP Method  

Defines the type of operation on the resource.

GET    → Retrieve data  
POST   → Create new data  
PUT    → Update existing data  
DELETE → Remove data  

Example:
POST https://api.company.com/v1/users  
→ Create a new user.

The same endpoint can behave differently based on the method.

---

3. Request  

A message sent by the client to the API.

It includes:

• Endpoint  
• HTTP Method  
• Headers (metadata like authentication)  
• Optional Body (data for create/update)

Example Request:

POST https://api.company.com/v1/users

Headers:
Authorization: Bearer token123  
Content-Type: application/json  

Body:
{
  "name": "John",
  "email": "john@example.com"
}

The request tells the server:
Who you are, what you want, and what data you are sending.

---

4. Response  

Message returned by the API after processing.

It includes:

• Status Code  
• Headers  
• Body (data)

Example Response:

Status: 201 Created  

{
  "id": 10,
  "name": "John",
  "email": "john@example.com"
}

The response confirms what happened and returns data if needed.

---

5. Status Codes  

Indicate the outcome of the request.

200 → Success  
201 → Created  
400 → Bad Request  
401 → Unauthorized  
404 → Not Found  
500 → Server Error  

Status codes allow clients to programmatically handle outcomes.

---

6. Headers  

Metadata attached to request or response.

Common examples:

Authorization → Identifies client  
Content-Type → Format of data (JSON)  
X-RateLimit-Limit → Max requests allowed  
Retry-After → Time before retry  

Headers influence behavior without altering core data.

---

7. Body  

The actual data being transmitted.

Request Body → Data sent to server  
Response Body → Data returned to client  

Usually structured as JSON.

---

8. Rate Limiting & Quotas  

Controls how many requests a client can make within a time window.

Prevents abuse and ensures system stability.

Example Response Headers:

X-RateLimit-Limit: 1000  
X-RateLimit-Remaining: 245  
Retry-After: 60  

This protects backend infrastructure.

---

Core Insight:

API Communication = Endpoint + Method + Request + Processing + Response

Each component has a distinct role.
Together, they create secure, predictable, and scalable system interaction.
'''