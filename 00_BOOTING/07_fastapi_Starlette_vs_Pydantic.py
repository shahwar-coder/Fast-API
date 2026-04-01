'''
Q1. What does Starlette do inside FastAPI?
Ans. Starlette handles 
routing, requests, responses, middleware, and WebSockets.
'''
# Starlette = Web framework layer (lower-level).
# FastAPI is built on top of Starlette.

# Example
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Hello"}   # Starlette sends this response


'''
Q2. What does Pydantic do inside FastAPI?
Ans. Pydantic validates and converts data using models and type hints.
'''
# Example
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int


'''
Q3. How do Starlette and Pydantic work together for a request?
Ans. Starlette routes the request, Pydantic validates the body, then FastAPI sends clean data to your function.
'''
# Example
@app.post("/users")
def create_user(user: User):  # Pydantic validates this
    return user


'''
Q4. Why is Starlette important for performance?
Ans. Because it runs on ASGI, allowing async and super fast request handling.
'''
# Example
@app.get("/async")
async def hello():
    return {"msg": "Fast!"}
# This async function benefits from Starlette's ASGI support.


'''
Q5. Why is Pydantic important for correctness?
Ans. It checks data types and shows clear errors for wrong input.
'''
# Example (invalid input)
# {"name": "John", "age": "abc"}
# Pydantic error: "age must be an integer"


'''
Q6. What is the simple interview line to explain both?
Ans. Starlette powers the web layer, Pydantic powers data validation, FastAPI combines both.
'''
# Example (conceptual)
# Request → Starlette handles it
# JSON body → Pydantic validates it
# Your function → receives clean Python object
