'''
Problem 1 — Tight Coupling  

Tight coupling happens when a client depends directly on another system’s internal structure.

Example:

Weather company database table:

weather_data
- city_name
- temp_celsius
- humidity_percent
- wind_speed_kmh

Your app directly queries:

SELECT temp_celsius FROM weather_data

Now the company renames the column to:

temperature_celsius

Your app immediately breaks.

Why?
Because your app was tightly coupled to the internal database schema.

---

With an API:

Your app calls:

GET /weather?city=Delhi

The API handles database access internally.
Even if the database column changes, the API can still return:

{
  "temperature": 32
}

Your app continues to work.

---

Core Insight:

Direct database access creates tight coupling.
APIs introduce an abstraction layer.

👉 The API protects clients from internal schema changes and allows backend systems to evolve independently.
'''

# ===

'''
Problem 2 — No Security  

Imagine if applications were allowed to directly access a company’s database.

A malicious user (or hacker) could run queries like:

SELECT * FROM users  
SELECT * FROM internal_models  
DELETE FROM weather_data  

This would expose sensitive data or even destroy the system.

Direct database access = no control layer.

---

With an API:

Your app can only call:

GET /weather

The API decides:
• What data is allowed  
• Who can access it (authentication)  
• What actions are permitted (authorization)  

The client never sees internal tables.
It only receives controlled responses.

---

Core Insight:

Direct database access creates a massive security risk.

APIs act as a protective gate:
• They filter requests  
• Enforce permissions  
• Hide internal systems  

👉 APIs ensure controlled and secure access to data.
'''

# ===

'''
Problem 3 — No Authentication / No Rate Limiting  

Imagine 10 million apps directly calling a company’s database at the same time.

The database would overload.
The system would crash.

There would be:
• No identity check  
• No request limits  
• No abuse control  

This is dangerous and unsustainable.

---

With an API:

The company can enforce rules like:

• API key required  
• 1000 requests per minute limit  
• Block suspicious users  

Example request:

GET /weather?city=Delhi  
Header: API_KEY = 12345

The API checks:
1. Is the API key valid? (Authentication)
2. Has the user exceeded request limit? (Rate limiting)

If someone abuses the system:

❌ The API blocks them.

The database remains protected.

---

Core Insight:

Without an API → No control.  
With an API → Controlled access, identity verification, and traffic management.

APIs protect systems from overload and misuse while ensuring fair usage for legitimate users.
'''

# ===

'''
Problem 4 — Increased Attack Surface  

If a database is directly exposed to the internet, it becomes an easy target.

Attackers can attempt:

• SQL Injection  
• Data deletion  
• Schema discovery (finding table structures)  
• Large-scale data scraping  

Since the database understands SQL, any vulnerability can directly damage or expose the system.

This massively increases the attack surface — meaning more entry points for attackers.

---

With an API:

The database is never exposed publicly.

Clients can only perform predefined operations like:

GET /weather  
POST /login  

They cannot run raw SQL queries.
They cannot inspect tables.
They cannot modify schema.

The API acts as a security filter between the internet and the database.

---

Core Insight:

Direct database exposure = high security risk.  
API layer = reduced attack surface.

👉 APIs hide internal systems and only allow controlled, validated operations.
'''

# ===

'''
Problem 5 — No Control Over Data Exposure  

A company’s database may contain highly sensitive information:

• sensor_locations  
• internal ML models  
• satellite calibration data  
• employee records  

If applications directly access the database, they could potentially see everything.

This creates serious privacy and security risks.

---

With an API:

The API decides what data is safe to share.

Example response:

{
  "temperature": 30,
  "humidity": 60,
  "forecast": "Cloudy"
}

Users only receive public, approved information.

Internal systems remain hidden.

---

Core Insight:

Databases store both public and private data.
APIs control what gets exposed.

👉 APIs enforce data boundaries, ensuring users only see what they are allowed to see — nothing more.
'''