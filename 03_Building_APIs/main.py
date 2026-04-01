"""
Create an app using FastAPI to implement CRUD operations on an Employees database.

Implement endpoints to:
- Show all employees
- Show a particular employee
- Add a new employee
- Update an existing employee
- Delete an existing employee
"""

from fastapi import FastAPI, HTTPException
from model import Employee
from typing import List

app = FastAPI()

# In-memory database
employees_db: List[Employee] = [
    Employee(id=1, name="Rahul", department="HR"),
    Employee(id=2, name="Ganguly", department="Engineering"),
]


# Show all employees
@app.get("/employees", response_model=List[Employee])
def get_all_employees():
    return employees_db


# Show a particular employee
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for emp in employees_db:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")


# 3. Add an employee
@app.post("/add_employee", response_model=Employee)
def add_employee(new_emp: Employee):

    # Check if employee already exists
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(
                status_code=400,
                detail="Employee already exists"
            )

    # Add employee
    employees_db.append(new_emp)

    return new_emp


# Update an existing employee
@app.put("/employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees_db):
        if emp.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")


# Delete an existing employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for index, emp in enumerate(employees_db):
        if emp.id == emp_id:
            employees_db.pop(index)
            return {"message": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")


"""
FastAPI CRUD App (Employees)
============================

Purpose
-------
Simple REST API to manage employees using an in-memory database.

Tech
----
- FastAPI for API endpoints
- Pydantic for data validation


------------------------------------------------------------
1️⃣ Data Model (Pydantic)
------------------------------------------------------------

Defined in model.py :

Employee:
- id (int, >0)
- name (3–30 chars)
- department (3–30 chars)
- age (optional, 18–70)

Ensures all incoming data is validated.


------------------------------------------------------------
2️⃣ In-Memory Database
------------------------------------------------------------

employees_db: List[Employee]

Stores employee records as a Python list.
(No persistent storage; resets on restart)


------------------------------------------------------------
3️⃣ API Endpoints
------------------------------------------------------------

1. GET /employees
   → Returns all employees

2. GET /employees/{emp_id}
   → Returns employee by ID
   → 404 if not found

3. POST /add_employee
   → Adds new employee
   → Prevents duplicate IDs

4. PUT /employees/{emp_id}
   → Updates existing employee
   → Replaces full object
   → 404 if not found

5. DELETE /employees/{emp_id}
   → Deletes employee
   → 404 if not found


------------------------------------------------------------
4️⃣ Error Handling
------------------------------------------------------------

Uses HTTPException:

- 400 → Duplicate employee
- 404 → Employee not found


------------------------------------------------------------
5️⃣ Key Design Notes
------------------------------------------------------------

- Linear search used for lookup (O(n))
- No database (only list-based storage)
- Full object replacement in update (not partial)
- Clean separation of model and API logic


------------------------------------------------------------
6️⃣ Entry Point
------------------------------------------------------------

Defined in main.py :

Run with:

uvicorn main:app --reload


------------------------------------------------------------
Result
------
A minimal CRUD API demonstrating:

- Request validation
- REST endpoints
- Basic error handling
- Clean backend structure
"""