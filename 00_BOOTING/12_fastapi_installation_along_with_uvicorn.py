'''
intall command : pip install fastapi uvicorn
---
pip -> Python's package manager
    -> Downloads libraries written by other developers
    -> And FastAPI is one of the Python libraries
---
but, why install both `fastapi` & `uvicorn` ?
-> fastapi -> let's you define apis
-> uvicorn -> actually runs the apis
note: FastAPI does not run by itself, you need uvicorn to listen to requests
---
This is how Fast API project folder looks like:
fastapi_project/
│
├── main.py
That's it.
---
'''

# QA-SET-1

'''
Q1. Why do we need to install FastAPI to build an API?
A.
FastAPI is a Python library that lets us WRITE API logic:
routes, request handling, and validation.
Without installing it, Python does not know what FastAPI is.
'''
# Example:
# pip install fastapi
# → Makes FastAPI available to import in Python code


'''
Q2. Why is Uvicorn needed along with FastAPI?
A.
FastAPI does NOT run by itself.
Uvicorn is the server that actually RUNS the app
and LISTENS for incoming HTTP requests.
'''
# Example:
# FastAPI = brain (logic)
# Uvicorn  = runner (server)
# Without Uvicorn → API code exists but nothing listens


'''
Q3. What does the command `pip install fastapi uvicorn` do?
A.
It downloads FastAPI and Uvicorn from PyPI
and installs them into your Python environment
so they can be imported and used.
'''
# Example:
# pip install fastapi uvicorn
# → installs both API framework + server in one step


'''
Q4. Why is pip used for installing FastAPI?
A.
pip is Python’s package manager.
It is designed to download and manage external Python libraries
written by other developers.
'''
# Example:
# pip install requests
# pip install fastapi
# Both are third-party Python libraries


'''
Q5. Why is the initial project structure kept so simple?
A.
A simple structure avoids confusion.
At the beginning, the goal is to understand concepts,
not manage many files or folders.
'''
# Example:
# fastapi_project/
# └── main.py
# One file → clear starting point


'''
Q6. Why is the file usually named main.py?
A.
There is no magic in the name.
It is a convention that indicates:
“This is where the application starts.”
'''
# Example:
# main.py → entry point
# Later projects may add more files,
# but main.py usually stays as the starting file



# QA-SET-2


'''
Q1. How does FastAPI + Uvicorn map to real backend systems?
A.
FastAPI handles WHAT should happen when a request arrives
(routing, validation, responses),
while Uvicorn handles HOW requests arrive
(network, ports, concurrency).
This separation mirrors real production systems.
'''
# Example:
# Client → HTTP request
# Uvicorn → receives request on port 8000
# FastAPI → processes logic and returns response


'''
Q2. Why is FastAPI called a “brain” and not a server?
A.
FastAPI does not open ports or listen on the network.
It only defines rules:
“If request looks like this, respond like that.”
The server (Uvicorn) is responsible for I/O.
'''
# Example:
# FastAPI alone = Python file with functions
# Uvicorn + FastAPI = running web service


'''
Q3. How does this setup relate to ML / GenAI services?
A.
Most ML/GenAI systems expose models through APIs.
FastAPI defines endpoints like /predict or /chat,
while Uvicorn keeps the model service alive and reachable.
'''
# Example:
# POST /embed → FastAPI validates input
# → calls embedding model
# → returns vectors as JSON


'''
Q4. Why is a single-file (main.py) approach ideal for beginners?
A.
It reduces cognitive load.
You learn request → response flow
before learning architecture patterns like routers or services.
This mirrors how prototypes are built in ML and GenAI.
'''
# Example:
# main.py:
# app = FastAPI()
# @app.get("/")
# def root(): return {"status": "ok"}


'''
Q5. How does Uvicorn relate to scalability and performance?
A.
Uvicorn is an ASGI server designed for async workloads.
This makes it suitable for:
- high concurrency
- I/O-heavy tasks
- model inference endpoints
'''
# Example:
# uvicorn main:app --workers 4
# → multiple worker processes handling requests


'''
Q6. Why is this separation critical in production systems?
A.
Separating framework (FastAPI) from server (Uvicorn)
allows independent scaling, replacement, and tuning.
This is how serious backend and GenAI systems are built.
'''
# Example:
# FastAPI app stays same
# Swap Uvicorn → Gunicorn + Uvicorn workers
# Deploy behind load balancer
