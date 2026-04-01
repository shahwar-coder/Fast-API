'''
Working of an API  

An API follows a simple Request → Process → Response cycle.

---

1. Request Initiation  

A client (web app, mobile app, browser) sends a request to the API.

The request includes:
• HTTP method (GET, POST, PUT, DELETE)
• URL (endpoint)
• Headers (authentication, metadata)
• Optional body (data)

Example:
GET /users/10

---

2. API Endpoint  

The request is sent to a specific URL called an endpoint.

Think of it as a door:
Each door handles a specific task.

Example:
/users/10 → Fetch user data  
/orders → Create new order  

---

3. Request Processing  

The server receives the request and:

• Validates input parameters  
• Checks authentication & authorization  
• Executes business logic  
• Accesses database or other services  

Example:
Fetch user from database where id = 10.

---

4. Response Generation  

After processing, the server prepares a response.

The response includes:
• Status code (200, 404, 500)
• Data (usually JSON)

Example:
{
  "id": 10,
  "name": "Shahwar"
}

---

5. Response Delivery  

The server sends the response back to the client.

The client:
• Displays the data
• Or performs another action

---

Simple Flow (Mental Model):

App → Request → API Endpoint → Server Logic → Database  
Database → Server → Response → App  

---

Core Insight:

An API acts as a controlled communication bridge.
It receives structured requests, processes them securely, and returns structured responses.
'''