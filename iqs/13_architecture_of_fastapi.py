# =========================
# 🎯 INTERVIEW Q&A: FastAPI Architecture
# =========================

# Q1: What is FastAPI architecture?

answer_1 = """
FastAPI architecture is based on three main components:

1. Starlette → handles web framework features like routing and requests
2. Uvicorn / Gunicorn → runs the application as an ASGI server
3. Pydantic → handles data validation and parsing

Together, they make FastAPI fast and reliable.
"""


# Q2: What is the role of Starlette?

answer_2 = """
Starlette is the web framework layer.

It handles:
- routing (URL handling)
- request and response processing
- middleware
- WebSockets

FastAPI is built on top of Starlette.
"""


# Q3: What is the role of Uvicorn or Gunicorn?

answer_3 = """
Uvicorn and Gunicorn are ASGI web servers.

They:
- run the FastAPI application
- handle incoming HTTP requests
- manage connections between client and app

Uvicorn is commonly used for development,
while Gunicorn + Uvicorn workers are used in production.
"""


# Q4: What is the role of Pydantic?

answer_4 = """
Pydantic handles data validation.

It:
- validates request data (body, query, headers)
- enforces correct data types
- automatically parses input into Python objects

This ensures clean and safe data handling.
"""


# Q5: Explain the request flow in FastAPI

answer_5 = """
Request flow:

1. User sends request
2. Uvicorn (server) receives it
3. FastAPI/Starlette processes routing
4. Pydantic validates input data
5. Application logic runs
6. Response is returned to the user
"""


# Q6: Why is this architecture powerful?

answer_6 = """
This architecture is powerful because:

- Starlette provides high-performance async handling
- Uvicorn efficiently serves requests
- Pydantic ensures strong data validation

Together, they create a fast, scalable, and reliable API system.
"""


# Q7: Short interview answer

answer_short = """
FastAPI is built on Starlette (web framework), Uvicorn (ASGI server),
and Pydantic (data validation), working together to handle requests efficiently.
"""


# =========================
# 🧠 MEMORY TRICK
# =========================

memory_tip = """
SUP Model:

S → Starlette (framework)
U → Uvicorn (server)
P → Pydantic (validation)
"""