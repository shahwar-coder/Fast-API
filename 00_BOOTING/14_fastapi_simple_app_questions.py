# QA-SET-1

'''
Q1. What does `from fastapi import FastAPI` do?
A.
It imports the FastAPI class, which is used to create a web application.
This class provides all the tools needed to define routes, handle requests,
and return responses.
'''
# Example:
# from fastapi import FastAPI
# app = FastAPI()  # creates an API application


'''
Q2. What is `app = FastAPI()` actually creating?
A.
It creates the FastAPI application object.
This object is the central registry that stores:
- all routes
- request/response logic
- configuration
Uvicorn runs THIS object to start the server.
'''
# Example:
# app = FastAPI()
# uvicorn main:app  # Uvicorn runs the app object


'''
Q3. What does `@app.get("/")` mean?
A.
It is a decorator that tells FastAPI:
“When a GET request comes to '/', run the function below.”
It maps a URL path + HTTP method to a Python function.
'''
# Example:
# @app.get("/users")
# def get_users():
#     return {"users": []}


'''
Q4. Why is the function name (`root` or `read_root`) not important?
A.
FastAPI does NOT care about the function name.
It only cares about:
- the decorator (@app.get)
- the path ("/")
- the HTTP method (GET)
The function name is for humans, debugging, and readability.
'''
# Example:
# @app.get("/")
# def anything_here():
#     return {"ok": True}


'''
Q5. What happens when the function returns a dictionary?
A.
FastAPI automatically:
- converts the Python dict to JSON
- sets correct HTTP headers
- sends the JSON as the response body
You don’t manually serialize anything.
'''
# Example:
# return {"message": "Hello FastAPI"}
# Client receives:
# {"message": "Hello FastAPI"}


'''
Q6. What is the full request–response flow here?
A.
1. Client sends GET request to "/"
2. Uvicorn receives the request
3. FastAPI matches "/" + GET
4. The function is executed
5. Return value is converted to JSON
6. Response is sent back to client
'''
# Example:
# Browser → http://localhost:8000/
# Response → {"message": "Hello FastAPI"}


# QA-SET-2

'''
Q1. Why is FastAPI considered just the “brain” and not the server?
A.
FastAPI only defines:
- routes
- request validation
- response logic

It does NOT:
- open ports
- listen to HTTP traffic
- manage event loops

That job is handled by an ASGI server like Uvicorn.
'''
# Example:
# FastAPI = decision maker
# Uvicorn = listener + traffic handler
# Without Uvicorn → API code exists but nothing runs


'''
Q2. How does this basic FastAPI app fit into real backend or GenAI systems?
A.
This app is the entry point for:
- ML inference APIs
- RAG pipelines
- prompt orchestration services
- agent endpoints

Every serious GenAI system starts with:
“Expose logic through an HTTP endpoint.”
'''
# Example:
# @app.post("/embed")
# def create_embedding(text: str):
#     return embedding_model(text)


'''
Q3. Why does FastAPI automatically return JSON from a dict?
A.
FastAPI is built for APIs, not HTML pages.
So it assumes:
- Python dict → structured data
- structured data → JSON (API standard)

This makes it perfect for ML/GenAI pipelines that speak JSON.
'''
# Example:
# return {"vector": [0.12, 0.98, 0.44]}
# Used directly by:
# - frontend
# - another microservice
# - an agent


'''
Q4. Why is the decorator-based routing powerful for AI services?
A.
Each decorator cleanly maps:
- one endpoint
- one responsibility

This matches AI system design:
- /predict
- /retrieve
- /generate
- /rank
'''
# Example:
# @app.post("/generate")
# def generate(prompt: str):
#     return llm(prompt)


'''
Q5. How does this simple app scale into production architecture?
A.
This single-file app later grows into:
- routers (modular endpoints)
- dependency injection
- middleware (auth, logging)
- background tasks
- async ML inference

But the CORE idea stays the same.
'''
# Example:
# main.py still contains:
# app = FastAPI()
# Everything else plugs into it


'''
Q6. Why is FastAPI a favorite for ML / GenAI backends specifically?
A.
Because it offers:
- automatic request validation (Pydantic)
- high performance (ASGI + async)
- clean JSON APIs
- easy integration with Python ML stack

It removes boilerplate so you focus on models and logic.
'''
# Example:
# FastAPI + PyTorch + Vector DB + LLM
# = production-grade GenAI backend


# QA-SET-2


'''
Q1. Why is FastAPI considered just the “brain” and not the server?
A.
FastAPI only defines:
- routes
- request validation
- response logic

It does NOT:
- open ports
- listen to HTTP traffic
- manage event loops

That job is handled by an ASGI server like Uvicorn.
'''
# Example:
# FastAPI = decision maker
# Uvicorn = listener + traffic handler
# Without Uvicorn → API code exists but nothing runs


'''
Q2. How does this basic FastAPI app fit into real backend or GenAI systems?
A.
This app is the entry point for:
- ML inference APIs
- RAG pipelines
- prompt orchestration services
- agent endpoints

Every serious GenAI system starts with:
“Expose logic through an HTTP endpoint.”
'''
# Example:
# @app.post("/embed")
# def create_embedding(text: str):
#     return embedding_model(text)


'''
Q3. Why does FastAPI automatically return JSON from a dict?
A.
FastAPI is built for APIs, not HTML pages.
So it assumes:
- Python dict → structured data
- structured data → JSON (API standard)

This makes it perfect for ML/GenAI pipelines that speak JSON.
'''
# Example:
# return {"vector": [0.12, 0.98, 0.44]}
# Used directly by:
# - frontend
# - another microservice
# - an agent


'''
Q4. Why is the decorator-based routing powerful for AI services?
A.
Each decorator cleanly maps:
- one endpoint
- one responsibility

This matches AI system design:
- /predict
- /retrieve
- /generate
- /rank
'''
# Example:
# @app.post("/generate")
# def generate(prompt: str):
#     return llm(prompt)


'''
Q5. How does this simple app scale into production architecture?
A.
This single-file app later grows into:
- routers (modular endpoints)
- dependency injection
- middleware (auth, logging)
- background tasks
- async ML inference

But the CORE idea stays the same.
'''
# Example:
# main.py still contains:
# app = FastAPI()
# Everything else plugs into it


'''
Q6. Why is FastAPI a favorite for ML / GenAI backends specifically?
A.
Because it offers:
- automatic request validation (Pydantic)
- high performance (ASGI + async)
- clean JSON APIs
- easy integration with Python ML stack

It removes boilerplate so you focus on models and logic.
'''
# Example:
# FastAPI + PyTorch + Vector DB + LLM
# = production-grade GenAI backend
