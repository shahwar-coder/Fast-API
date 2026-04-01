# =========================
# 🎯 ADVANCED / TRICKY PYDANTIC INTERVIEW QUESTIONS
# =========================

# Q1: What is the difference between validation and parsing in Pydantic?

q1 = """
Pydantic is said to do both validation and parsing. What’s the difference?
"""

a1 = """
Validation checks if data is correct.

Parsing converts data into the expected type.

Example:
"35" → 35 (parsing)
Check if > 18 → validation
"""


# Q2: Why does Pydantic accept "35" as int?

q2 = """
Why does Pydantic accept string "35" as an integer?
"""

a2 = """
Because Pydantic performs type coercion.

It tries to convert compatible types automatically.
To prevent this, we use strict types like StrictInt.
"""


# Q3: What is the difference between default=None and Optional?

q3 = """
Is Optional[int] enough to make a field optional?
"""

a3 = """
No.

Optional[int] means the value can be None,
but the field is still required unless you provide a default.

To make it optional:
age: Optional[int] = None
"""


# Q4: What is the difference between None and missing field?

q4 = """
What’s the difference between a field being None vs missing?
"""

a4 = """
Missing → field not provided at all
None → field provided but value is null

Pydantic treats them differently in validation.
"""


# Q5: What is alias in Pydantic?

q5 = """
What is field aliasing in Pydantic?
"""

a5 = """
Alias allows using a different name for input/output.

Example:
name: str = Field(..., alias="full_name")

Input JSON can use "full_name" instead of "name".
"""


# Q6: What is orm_mode?

q6 = """
What is orm_mode in Pydantic?
"""

a6 = """
orm_mode allows Pydantic to read data from ORM objects
(like SQLAlchemy models) instead of dictionaries.

It is required when returning database objects in FastAPI.
"""


# Q7: What are validators in Pydantic?

q7 = """
How do you add custom validation in Pydantic?
"""

a7 = """
Using validators.

Example:
@validator("age")
def check_age(cls, v):
    if v < 18:
        raise ValueError("Too young")
    return v
"""


# Q8: What is root_validator?

q8 = """
What is root_validator used for?
"""

a8 = """
It validates multiple fields together.

Useful when validation depends on more than one field.
"""


# Q9: What is difference between Field() and validator?

q9 = """
When would you use Field vs validator?
"""

a9 = """
Field → simple rules (gt, length, etc.)
Validator → complex/custom logic

Use Field for basic constraints,
validator for business logic.
"""


# Q10: What is model_config / Config class?

q10 = """
What is Config class in Pydantic?
"""

a10 = """
Config (or model_config in v2) is used to control model behavior.

Examples:
- orm_mode = True
- allow_population_by_field_name
- extra = "forbid"
"""


# Q11: What happens with extra fields?

q11 = """
What happens if extra fields are passed?
"""

a11 = """
By default, Pydantic ignores extra fields.

But we can control it using:

extra = "forbid" → error
extra = "allow" → accept
"""


# Q12: Mutable default trap (IMPORTANT)

q12 = """
What happens if you use a list as a default value?
"""

a12 = """
Using mutable defaults like [] is dangerous.

It can be shared across instances.

Correct way:
use default_factory=list
"""


# Q13: Difference between .dict() and .json()

q13 = """
What is difference between .dict() and .json()?
"""

a13 = """
.dict() → returns Python dictionary
.json() → returns JSON string
"""


# Q14: What is schema() in Pydantic?

q14 = """
What does .schema() do?
"""

a14 = """
It generates a JSON schema of the model.

Used for documentation (like OpenAPI in FastAPI).
"""


# Q15: Performance question (VERY IMPORTANT)

q15 = """
Is Pydantic fast? Any limitations?
"""

a15 = """
Pydantic is fast but adds overhead due to validation.

For very high-performance systems,
validation cost should be considered.

Pydantic v2 improves performance significantly.
"""


# =========================
# 🎯 SUPER SHORT ANSWER (ADVANCED)
# =========================

answer_short = """
Pydantic provides type-safe validation and parsing with support for strict types,
custom validators, ORM integration, and configurable behavior,
making it essential for reliable API design in FastAPI.
"""