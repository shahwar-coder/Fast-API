'''
[1] Definition of an API  

An API (Application Programming Interface) is a controlled gateway that allows one software system to access data or functionality from another system.

Think of it like this:

You are building a Weather App.
You need real-time weather data.
But you do NOT own satellites.
You do NOT own weather servers.
You cannot directly enter their internal system.

There is a gate.

That gate is the API.

Instead of directly accessing the weather company’s database (which is not allowed),
your app sends a request to their API.

The API:
• Receives your request  
• Checks if you are allowed (authentication)  
• Fetches data from internal systems  
• Returns only the required response  

Your app never touches their internal code or database.

---

Simple Example:

Your Weather App sends:

GET /weather?city=Bangalore

The weather service API responds:

{
  "city": "Bangalore",
  "temperature": "28°C",
  "condition": "Cloudy"
}

---

Why APIs Are Required:

1. Security  
   Systems do not expose their databases directly.

2. Abstraction  
   Clients don’t need to know how data is stored internally.

3. Standard Communication  
   Everyone follows the same request–response format.

4. Scalability  
   Multiple apps (mobile, web, AI systems) can use the same API.

---

Mental Model:

App → API (Gate) → Internal System  
App ← API ← Internal System  

The API is a safe bridge.
It allows access, but under rules.

---

Interview-Ready Line:

“An API is a contract-based gateway that enables secure and structured communication between independent software systems without exposing internal implementation details.”
'''