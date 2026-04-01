'''
Q1. What are type hints in Python?
A.
Type hints describe what kind of data a variable, function argument,
or return value is expected to have.
They do not strictly enforce types at runtime,
but tools use them for validation, safety, and clarity.
'''
# Example:
# age: int = 15
# name: str = "Shahwar"


'''
Q2. Do type hints change how Python executes code?
A.
No. Python does not enforce type hints at runtime.
The code will still run even if types are wrong,
but external tools and frameworks rely on them.
'''
# Example:
# age: int = "fifteen"   # Python allows this
# But tools like FastAPI will complain


'''
Q3. How are type hints used in function definitions?
A.
Type hints specify what type of arguments a function expects
and what type it returns.
This improves readability and tooling support.
'''
# Example:
# def add(a: int, b: int) -> int:
#     return a + b


'''
Q4. Why are type hints important in FastAPI?
A.
FastAPI uses type hints to:
- validate incoming request data
- reject invalid inputs automatically
- generate Swagger documentation
- prevent bugs without extra code
'''
# Example:
# @app.get("/add")
# def add(a: int, b: int):
#     return {"result": a + b}


'''
Q5. How does FastAPI handle wrong input using type hints?
A.
If incoming data does not match the type hints,
FastAPI automatically returns a validation error response.
You do not need to write manual checks.
'''
# Example:
# Valid request:
# /add?a=10&b=5
#
# Invalid request:
# /add?a=ten&b=five
# → FastAPI returns 422 error automatically


'''
Q6. What problem do type hints solve in API development?
A.
They eliminate repetitive validation code,
make APIs safer by default,
and clearly communicate expected data formats.
'''
# Example:
# Without type hints → manual if/else checks
# With type hints → FastAPI validates for you
