"""
SQLAlchemy

SQLAlchemy is a Python SQL toolkit and Object Relational Mapper (ORM) that
allows Python applications to interact with relational databases such as
PostgreSQL, MySQL, and SQLite.

It provides an abstraction layer so developers can work with databases using
Python code instead of writing raw SQL queries directly.

SQLAlchemy has two main components:

1. SQLAlchemy Core
   - A lower-level SQL expression toolkit.
   - Allows developers to construct SQL queries using Python syntax.
   - Close to raw SQL but more programmatic.

2. SQLAlchemy ORM (Object Relational Mapper)
   - A higher-level abstraction.
   - Maps Python classes to database tables.
   - Developers interact with Python objects instead of SQL queries.

Conceptual Mapping:

Python Class      -> Database Table
Object Instance   -> Table Row
Class Attribute   -> Table Column

Example:

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

This class represents a "users" table in the database.

Benefit:
SQLAlchemy simplifies database interactions, improves code readability,
and enables developers to work with databases in a more Pythonic way.
"""