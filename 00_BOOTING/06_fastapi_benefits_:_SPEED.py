'''
Q1. Why is FastAPI considered very fast?
Ans. Because it is built on tools that are designed for high speed: Starlette for async requests and Pydantic for fast data validation.

Q2. What role does Starlette play in FastAPI’s speed?
Ans. Starlette handles incoming requests using ASGI, which allows many users to be served at the same time.
Example: Hundreds of clients can call your API without blocking each other.

Q3. Why does async make FastAPI faster?
Ans. Async lets the app do other work while waiting for slow tasks, so no single request blocks the system.

Q4. How does Pydantic improve performance?
Ans. Pydantic validates and parses data very quickly using Python type hints.
Example: It checks if "age" is int almost instantly.

Q5. How does FastAPI handle many users efficiently?
Ans. With async + fast validation, it processes lots of requests like a race car engine—quick and smooth.

Q6. When does this speed matter most?
Ans. When your API receives many requests per second or when low latency is important, like live dashboards or microservices.
'''
