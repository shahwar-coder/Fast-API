'''
Q1. What does “writing your first API” actually mean?
A.
Writing your first API means:
- defining a URL
- choosing an HTTP method (GET, POST, etc.)
- returning structured data (usually JSON)

If a program can receive an HTTP request and send a response,
it is already a real API.
'''
# Example:
# URL: /
# Method: GET
# Response: {"message": "Hello FastAPI!"}
# This satisfies the definition of an API


'''
Q2. Why is this FastAPI app considered a REAL API and not a demo?
A.
Because it:
- listens on a route (/)
- responds to real HTTP requests
- returns machine-readable JSON
- can be accessed by browsers, curl, Postman, or other services

There is no such thing as a “fake API” once HTTP is involved.
'''
# Example:
# GET http://localhost:8000/
# Response → {"message": "Hello FastAPI!"}
# Any client can consume this response


'''
Q3. What role does the @app.get("/") decorator play?
A.
The decorator:
- registers a URL path
- binds it to an HTTP method (GET)
- connects it to a Python function

It tells FastAPI:
“When someone calls this URL with GET, run this function.”
'''
# Example:
# @app.get("/health")
# def health():
#     return {"status": "ok"}


'''
Q4. Why don’t we write socket, HTTP, or JSON-handling code ourselves?
A.
FastAPI abstracts:
- socket handling
- HTTP parsing
- header management
- JSON serialization

This lets developers focus on:
- business logic
- data
- models
'''
# Example:
# return {"user": "Rahul"}
# FastAPI handles:
# - converting dict → JSON
# - setting headers
# - sending HTTP response


'''
Q5. Why is returning a Python dict enough to create an API response?
A.
FastAPI automatically:
- detects the return type
- converts dicts into JSON
- sets Content-Type: application/json

This is why FastAPI feels “simple but powerful.”
'''
# Example:
# return {"id": 1, "active": True}
# Client receives valid JSON without extra code


'''
Q6. What does main.py represent in a FastAPI project?
A.
main.py is the entry point:
- where the FastAPI app is created
- where routes are registered
- what Uvicorn runs to start the server

As projects grow, main.py stays the starting door.
'''
# Example:
# uvicorn main:app
# main  → filename
# app   → FastAPI instance
