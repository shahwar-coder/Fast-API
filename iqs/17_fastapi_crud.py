# =========================
# 🎯 INTERVIEW Q&A: FastAPI CRUD (Your Project)
# =========================

# Q1: Can you explain your FastAPI project?

answer_1 = """
I built a CRUD API using FastAPI to manage employee data.

It supports:
- creating employees
- reading employees
- updating employees
- deleting employees

The data is stored in an in-memory list,
and I used Pydantic models for validation.
"""  


# Q2: What is your data model?

answer_2 = """
I used a Pydantic model called Employee.

It includes:
- id (must be > 0)
- name (3–30 characters)
- department (3–30 characters)
- age (optional, between 18–70)

Pydantic automatically validates all incoming data.
"""  # :contentReference[oaicite:1]{index=1}


# Q3: What endpoints did you implement?

answer_3 = """
I implemented the following endpoints:

- GET /employees → get all employees
- GET /employees/{emp_id} → get one employee
- POST /add_employee → add new employee
- PUT /employees/{emp_id} → update employee
- DELETE /employees/{emp_id} → delete employee

These cover full CRUD operations.
"""  # :contentReference[oaicite:2]{index=2}


# Q4: How is data stored?

answer_4 = """
Data is stored in an in-memory list:

employees_db: List[Employee]

This means:
- data is temporary
- it resets when the server restarts

It’s good for learning but not for production.
""" 


# Q5: How do you handle errors?

answer_5 = """
I used HTTPException for error handling.

Examples:
- 400 → duplicate employee ID
- 404 → employee not found

This ensures proper API responses.
"""  # :contentReference[oaicite:4]{index=4}


# Q6: How does validation work?

answer_6 = """
Validation is handled by Pydantic.

For example:
- id must be > 0
- name must be between 3–30 characters
- age must be between 18–70

If invalid data is sent, FastAPI automatically returns an error.
"""  # :contentReference[oaicite:5]{index=5}


# Q7: What is the time complexity of your search?

answer_7 = """
Currently, I use linear search (O(n)) to find employees.

This is fine for small data,
but not efficient for large datasets.

In production, I would use a database with indexing.
"""  # :contentReference[oaicite:6]{index=6}


# Q8: How would you improve this project?

answer_8 = """
I would improve it by:

- using a database (PostgreSQL, MongoDB)
- adding async endpoints
- implementing authentication and authorization
- adding pagination
- using partial updates (PATCH instead of PUT)
- adding logging and monitoring
"""


# Q9: What is PUT vs POST?

answer_9 = """
POST:
- used to create new resources

PUT:
- used to update existing resources
- usually replaces the entire object

In my project, PUT replaces the full employee record.
"""


# Q10: Short interview answer

answer_short = """
I built a FastAPI CRUD API with Pydantic validation,
in-memory storage, and proper error handling,
supporting all basic operations like create, read, update, and delete.
"""