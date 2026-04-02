# =========================
# 🎯 INTERVIEW Q&A: SQLAlchemy
# =========================

# Q1: What is SQLAlchemy?

answer_1 = """
SQLAlchemy is a Python SQL toolkit and ORM (Object Relational Mapper).

It allows developers to interact with relational databases
like PostgreSQL, MySQL, and SQLite using Python code instead of raw SQL.
"""


# Q2: What problem does SQLAlchemy solve?

answer_2 = """
It removes the need to write raw SQL queries.

Instead of writing SQL manually,
we can use Python objects and classes to interact with the database.

This makes code cleaner, safer, and easier to maintain.
"""


# Q3: What are the two main components of SQLAlchemy?

answer_3 = """
SQLAlchemy has two main parts:

1. SQLAlchemy Core:
   - low-level
   - used to write SQL queries using Python

2. SQLAlchemy ORM:
   - high-level
   - maps Python classes to database tables
"""


# Q4: What is ORM?

answer_4 = """
ORM stands for Object Relational Mapping.

It maps:
- Python class → database table
- object → table row
- attribute → column

So we can work with database data as Python objects.
"""


# Q5: Explain the mapping with an example

answer_5 = """
Example:

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

Here:
- User class → users table
- id, name → columns
- each object → one row
"""


# Q6: What are benefits of SQLAlchemy?

answer_6 = """
- reduces need for raw SQL
- improves code readability
- safer (prevents SQL injection)
- database-independent (can switch DB easily)
- Pythonic way of working with data
"""


# Q7: SQLAlchemy Core vs ORM?

answer_7 = """
Core:
- closer to SQL
- more control
- used for complex queries

ORM:
- easier to use
- works with Python objects
- faster development

Use ORM for most cases,
Core when you need fine control.
"""


# Q8: When would you NOT use ORM?

answer_8 = """
Avoid ORM when:

- performance is critical
- very complex queries are needed
- need full control over SQL

In such cases, SQLAlchemy Core or raw SQL is better.
"""


# Q9: How does SQLAlchemy integrate with FastAPI?

answer_9 = """
In FastAPI:

- SQLAlchemy is used for database operations
- Pydantic handles request/response validation
- FastAPI handles routing

So:
FastAPI → API layer
Pydantic → validation
SQLAlchemy → database
"""


# Q10: Short interview answer

answer_short = """
SQLAlchemy is a Python ORM that allows interaction with databases using Python objects,
providing both high-level ORM and low-level SQL control.
"""