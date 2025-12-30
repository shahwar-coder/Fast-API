'''
Q1. What is FastAPI in simple words?
Ans. FastAPI is a modern Python framework for building quick and simple web APIs. 
It helps you create endpoints that return data, usually as JSON.

Q2. Why is FastAPI known for being fast?
Ans. FastAPI uses async features and efficient tools underneath, so it can handle many users at once.
Example: Multiple people can request data without slowing each other down.

Q3. What type of data does FastAPI usually return?
Ans. It normally returns JSON.
Example: {"msg": "Hello"}

Q4. How does FastAPI use Python type hints?
Ans. FastAPI reads the type hints you write to auto-validate data and make the API clearer.
Example: age: int means the input must be a number.

Q5. Why is FastAPI friendly with async functions?
Ans. It supports async/await, letting your app work on other tasks while waiting for slow operations like database queries.
Example: async def get_user(): ...

Q6. What are FastAPI’s auto-generated docs?
Ans. FastAPI creates interactive API docs at /docs or /redoc where you can test endpoints easily.
'''
