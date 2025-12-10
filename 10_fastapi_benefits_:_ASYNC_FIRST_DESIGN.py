'''
Q1. What does “async-first design” mean in FastAPI?
Ans. It means FastAPI was built to use async/await from the beginning, not added later.
'''
# Example
@app.get("/data")
async def get_data():
    return {"msg": "Async makes this faster!"}


'''
Q2. How does async help FastAPI handle more users?
Ans. Async lets the server work on other tasks while waiting, so it doesn’t get stuck on one request.
'''
# Example
# While waiting for a slow database call, the server can serve other users.
# Other tasks means handling new requests, processing data, etc.


'''
Q3. What happens when an API call is slow?
Ans. With async, FastAPI doesn’t freeze — it keeps serving new requests until the slow task finishes.
'''
# Example
import asyncio

@app.get("/slow")
async def slow_task():
    await asyncio.sleep(3)  # simulates a slow API call
    return {"done": True}
# Here, other requests can be handled during the 3-second wait.
# Processing other requests won't cause any issues as the event loop manages them efficiently.
# An event loop is like a manager that keeps track of all tasks and switches between them as needed.
# Event loop is a core part of async programming that allows multiple tasks to run seemingly at the same time.
# Where is event loop present? It is part of the Python runtime when using async/await.


'''
Q4. Why is async important for high-traffic APIs?
Ans. It helps the system stay responsive even when thousands of users hit it at once.
'''
# Example
# A busy API with many GET calls stays fast because each call doesn’t block others.


'''
Q5. When is async especially useful?
Ans. When your API calls external services like databases, APIs, or file systems that take time.
'''
# Example
# Calling a payment API → async waits without blocking the server.


'''
Q6. What is the main scalability benefit?
Ans. FastAPI handles many tasks at the same time, making it perfect for big, real-time, or high-load apps.
'''
# Example
# Chat apps, analytics dashboards, or microservices with heavy traffic.
