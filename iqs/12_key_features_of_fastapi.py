# =========================
# 🎯 INTERVIEW Q&A: Key Features of FastAPI
# =========================

# Q1: What are the key features of FastAPI?

answer_1 = """
FastAPI has several important features that make it powerful and easy to use:

1. Fast
FastAPI is very high-performance and comparable to Node.js and Go.

2. Async Support
It supports async/await, which allows handling many requests at the same time efficiently.

3. Fast to Develop
Using Python type hints, developers can write code faster with fewer bugs.

4. Automatic Validation
FastAPI uses Pydantic to validate request data automatically.

5. Automatic Documentation
It generates interactive API documentation (Swagger and OpenAPI) automatically.
"""


# Q2: Why is FastAPI considered fast?

answer_2 = """
FastAPI is fast because:

- it uses async programming (async/await)
- it is built on Starlette (high-performance framework)
- it uses Pydantic for efficient data handling

This makes it suitable for high-load systems.
"""


# Q3: What is async support in FastAPI?

answer_3 = """
Async support means FastAPI can handle multiple requests at the same time
without blocking the system.

This improves performance and scalability, especially for I/O operations like APIs and databases.
"""


# Q4: How does automatic validation work?

answer_4 = """
FastAPI uses Pydantic models.

When a request comes in:
- it checks data types
- validates required fields
- returns errors automatically if data is incorrect

This reduces manual validation code.
"""


# Q5: What is automatic documentation?

answer_5 = """
FastAPI automatically generates API documentation.

You can access:
- /docs → Swagger UI (interactive testing)
- /redoc → clean documentation view

This helps developers understand and test APIs easily.
"""


# Q6: Why is FastAPI fast to develop?

answer_6 = """
FastAPI is fast to develop because:

- type hints reduce errors
- built-in validation saves time
- automatic docs remove extra work

So developers can focus on logic instead of boilerplate code.
"""


# Q7: Short interview answer

answer_short = """
FastAPI is fast, supports async programming, provides automatic validation,
and generates API documentation, making it efficient and easy to develop APIs.
"""


# =========================
# 🧠 MEMORY TRICK
# =========================

memory_tip = """
FAST:

F → Fast performance
A → Async support
S → Simple development
T → Type-safe validation
"""