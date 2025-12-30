'''
Q1. What does “automatic validation” mean in FastAPI?
Ans. It means FastAPI checks incoming data for you using Pydantic models, without extra code.
'''
# Example
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int   # must be an integer


'''
Q2. How does Pydantic help make data safer?
Ans. Pydantic makes sure every field has the correct type before your function runs.
'''
# Example (invalid input)
# {"name": "Ali", "age": "abc"}
# Pydantic error: "age must be an integer"


'''
Q3. Why is automatic validation useful?
Ans. It stops bad or dangerous data from reaching your code, making apps more stable.
'''
# Example
# If "email" must be a string, Pydantic blocks numbers or wrong formats.


'''
Q4. Does automatic validation reduce your work?
Ans. Yes! You don’t have to manually check types — FastAPI + Pydantic do it for you.
'''
# Example
# You don't need:
# if not isinstance(age, int): raise error
# Pydantic handles it automatically.


'''
Q5. How does FastAPI use validation while handling requests?
Ans. FastAPI takes the incoming JSON → sends it to Pydantic → gives your code a clean, correct object.
'''
# Example
@app.post("/users")
def create_user(user: User):
    return {"status": "valid", "user": user}
# Here, 'user' is already validated by Pydantic.
# If invalid data is sent, FastAPI returns an error before reaching this function.

'''
Q6. What is the main benefit of automatic validation?
Ans. You get safer, cleaner apps with much less code.
'''
# Example
# Wrong inputs are rejected instantly → cleaner functions for you.
