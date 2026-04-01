# =========================
# 🎯 INTERVIEW Q&A: FastAPI vs Flask vs Django
# =========================

# Q1: How is FastAPI different from Flask?

answer_1 = """
FastAPI and Flask are both Python web frameworks, but FastAPI is more modern and feature-rich.

Key differences:

1. Built-in Validation
- FastAPI → automatic validation using Pydantic
- Flask → requires manual validation or extra libraries

2. API Documentation
- FastAPI → auto-generates Swagger/OpenAPI docs
- Flask → needs third-party tools

3. Async Support
- FastAPI → supports async/await
- Flask → mainly synchronous

So FastAPI reduces boilerplate and is more suitable for modern APIs.
"""


# Q2: How is FastAPI different from Django (DRF)?

answer_2 = """
FastAPI and Django serve different purposes.

Key differences:

1. Performance
- FastAPI → async, high performance (ASGI)
- Django → traditionally synchronous (WSGI)

2. Use Case
- FastAPI → lightweight, API-focused
- Django → full-stack framework (includes ORM, admin panel, templates)

3. Complexity
- FastAPI → simple and minimal
- Django → heavier but feature-rich

So FastAPI is better for APIs, while Django is better for full web applications.
"""


# Q3: When would you choose FastAPI over Flask?

answer_3 = """
Choose FastAPI when:

- you want automatic validation
- you need built-in documentation
- you want async support
- you are building scalable APIs

It helps reduce development time and errors.
"""


# Q4: When would you choose FastAPI over Django?

answer_4 = """
Choose FastAPI when:

- building microservices or APIs
- performance is important
- you don’t need full-stack features like admin panel

Django is better when you need a complete web application.
"""


# Q5: Short interview answer

answer_short = """
FastAPI provides built-in validation, async support, and automatic docs,
making it faster and more API-focused than Flask and Django.
"""


# =========================
# 🧠 MEMORY TRICK
# =========================

memory_tip = """
FastAPI vs Flask:
- FastAPI = modern + automatic
- Flask = manual + flexible

FastAPI vs Django:
- FastAPI = API-focused
- Django = full-stack
"""