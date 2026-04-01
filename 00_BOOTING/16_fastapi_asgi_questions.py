'''
Q1. What problem does ASGI solve in simple terms?
A.
ASGI solves the problem of handling many requests at the same time.
Old Python apps could handle only one request at a time and would block
if something was slow (like a database or network call).
ASGI allows apps to wait without blocking other requests.
'''
# Example:
# User A makes a slow request (DB call)
# User B makes a fast request
# With ASGI → User B does NOT have to wait for User A


'''
Q2. How is ASGI different from older Python web systems (WSGI)?
A.
WSGI handles requests one-by-one and blocks while waiting.
ASGI handles multiple requests concurrently and can pause/resume work.
This makes apps faster and more scalable.
'''
# Example:
# WSGI → one worker, one request at a time
# ASGI  → one worker, many requests in progress


'''
Q3. What is the simple mental model of FastAPI, ASGI, and Uvicorn?
A.
FastAPI is the brain (defines routes and logic).
ASGI is the communication rulebook.
Uvicorn is the engine that runs the app and follows ASGI rules.
All three work together.
'''
# Example:
# FastAPI → decides what to do
# ASGI    → defines how messages flow
# Uvicorn → listens on the network and runs the app


'''
Q4. Why must FastAPI be run with an ASGI server like Uvicorn?
A.
FastAPI is ASGI-compatible, not a server itself.
It cannot listen to network requests on its own.
Uvicorn is needed to start the server and handle incoming traffic.
'''
# Example:
# uvicorn main:app   ✅ works
# python main.py     ❌ does not start a server


'''
Q5. What does the command "uvicorn main:app" actually mean?
A.
It tells Uvicorn:
- main → the Python file
- app  → the FastAPI object inside that file
Uvicorn loads the app and starts listening for HTTP requests.
'''
# Example:
# File: main.py
# app = FastAPI()
# Command: uvicorn main:app


'''
Q6. Why can’t we just run FastAPI apps like normal Python scripts?
A.
Running a script only executes code once.
Web apps must stay alive and listen continuously for requests.
Only a server like Uvicorn can do that.
'''
# Example:
# python main.py → program runs and exits
# uvicorn main:app → program runs and keeps listening
