'''
Q1. What is the big-picture idea of FastAPI?
Ans. FastAPI is a modern Python framework that makes APIs fast, safe, scalable, and easy to build.
'''
# Example
# A simple API endpoint:
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"msg": "FastAPI = modern + fast + safe"}


'''
Q2. Why is FastAPI considered “fast”?
Ans. Because it uses async + Starlette + Pydantic to handle requests very quickly.
'''
# Example
@app.get("/async-demo")
async def demo():
    return {"speed": "async-powered"}


'''
Q3. Why is FastAPI considered “safe”?
Ans. Pydantic automatically validates input, preventing wrong or harmful data.
'''
# Example
# If age must be an integer, FastAPI rejects strings automatically.


'''
Q4. What makes FastAPI scalable?
Ans. Its async-first design lets it handle many users and slow tasks without blocking.
'''
# Example
# While one task waits for a database, other users still get responses.


'''
Q5. How does FastAPI save developer time?
Ans. It auto-generates documentation and handles validation, so you write less code.
'''
# Example
# Visiting /docs instantly shows interactive API docs — no extra work.


'''
Q6. What is the single-line interview answer for FastAPI?
Ans. FastAPI is chosen for high-performance async APIs with built-in validation and automatic docs.
'''
# Example
# Interview flashcard:
# "FastAPI = fast async APIs + strong validation + auto docs"
