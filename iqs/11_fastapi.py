# =========================
# 🎯 INTERVIEW Q&A: FastAPI
# =========================

# Q1: What is FastAPI?

answer_1 = """
FastAPI is a modern and high-performance Python framework used to build APIs.

It is designed to be fast, easy to use, and production-ready.
"""


# Q2: What makes FastAPI different from other frameworks?

answer_2 = """
FastAPI uses Python type hints, which makes code more structured and easier to validate.

It is also very fast because it is built on Starlette (for async handling)
and Pydantic (for data validation).
"""


# Q3: Why is FastAPI fast?

answer_3 = """
FastAPI is fast because:

- it supports asynchronous programming (async/await)
- it is built on Starlette (high-performance ASGI framework)
- it uses efficient data validation with Pydantic

This makes it comparable to Node.js and Go in performance.
"""


# Q4: What are the key features of FastAPI?

answer_4 = """
Key features include:

- automatic request validation
- automatic API documentation (Swagger UI, OpenAPI)
- type-safe code using Python type hints
- async support for high concurrency
- easy integration with databases and ML models
"""


# Q5: What is automatic documentation in FastAPI?

answer_5 = """
FastAPI automatically generates API docs.

You get:
- Swagger UI → /docs
- ReDoc → /redoc

This helps developers test APIs directly from the browser.
"""


# Q6: What are common use cases of FastAPI?

answer_6 = """
FastAPI is commonly used for:

- building REST APIs
- backend services
- microservices
- serving AI/ML models
- building scalable web applications
"""


# Q7: What are the requirements for FastAPI?

answer_7 = """
FastAPI requires:

- Python 3.7 or higher
"""


# Q8: Can FastAPI handle async code?

answer_8 = """
Yes, FastAPI fully supports async/await.

This allows handling multiple requests efficiently,
making it suitable for high-performance applications.
"""


# Q9: Short interview answer

answer_short = """
FastAPI is a fast and modern Python framework for building APIs,
with features like async support, automatic validation,
and auto-generated documentation.
"""


# =========================
# 🧠 MEMORY TRICK
# =========================

memory_tip = """
FastAPI = Fast + Automatic + Pythonic

Fast → high performance
Automatic → validation + docs
Pythonic → type hints
"""