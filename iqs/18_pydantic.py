# =========================
# 🎯 PYDANTIC INTERVIEW QUESTIONS (BASED ON YOUR CODE)
# =========================

# Q1: What is Pydantic?

q1 = """
What is Pydantic and why is it used in FastAPI?
"""

a1 = """
Pydantic is a data validation and parsing library.

It uses Python type hints to validate input data automatically,
ensuring that incoming data matches the expected schema.
"""


# Q2: What is BaseModel?

q2 = """
What is BaseModel in Pydantic?
"""

a2 = """
BaseModel is the core class in Pydantic.

We inherit from it to define data models,
and it automatically validates and parses input data.
"""


# Q3: What does Field() do?

q3 = """
What is the purpose of Field() in your model?
"""

a3 = """
Field() is used to add validation rules and metadata.

For example:
- gt=0 → value must be greater than 0
- min_length → minimum string length
- max_length → maximum string length
"""


# Q4: What does ... (ellipsis) mean?

q4 = """
What does '...' mean in Field(...)? 
"""

a4 = """
'...' means the field is required.

If the value is not provided, validation will fail.
"""


# Q5: What does Optional[int] mean?

q5 = """
What is Optional[int] in your model?
"""

a5 = """
Optional[int] means the field can be either an integer or None.

In this case, age is not mandatory.
"""


# Q6: What happens if invalid data is passed?

q6 = """
What happens if invalid data is sent to this model?
"""

a6 = """
Pydantic automatically raises a validation error.

FastAPI then returns a 422 Unprocessable Entity response
with details about the error.
"""


# Q7: What is type coercion in Pydantic?

q7 = """
Your comment says it can accept '35' as string.
Why does that happen?
"""

a7 = """
Pydantic performs type coercion.

It tries to convert compatible types automatically,
so "35" (string) becomes 35 (int).
"""


# Q8: How do you enforce strict types?

q8 = """
How would you ensure age only accepts integers (not strings)?
"""

a8 = """
We can use StrictInt instead of int.

Example:
from pydantic import StrictInt

age: Optional[StrictInt]
"""


# Q9: Difference between gt and ge?

q9 = """
What is the difference between gt and ge?
"""

a9 = """
- gt → greater than (>)
- ge → greater than or equal to (>=)
"""


# Q10: What is the difference between PUT and PATCH in this context?

q10 = """
How would Pydantic behave differently in PUT vs PATCH?
"""

a10 = """
PUT:
- expects full object (all required fields)

PATCH:
- allows partial updates (fields can be optional)

For PATCH, we usually make fields optional.
"""


# Q11: What are benefits of using Pydantic?

q11 = """
What are the main advantages of Pydantic?
"""

a11 = """
- automatic validation
- clear schema definition
- reduces manual code
- better error messages
- type safety
"""


# Q12: Short interview answer

answer_short = """
Pydantic is used for data validation using type hints.
It ensures input data is correct, supports automatic parsing,
and integrates seamlessly with FastAPI.
"""