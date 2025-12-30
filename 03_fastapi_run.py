'''
Q1. How does FastAPI actually run?
Ans. FastAPI needs an ASGI server (like uvicorn) to run your app and handle requests.
Example: `uvicorn main:app --reload`

Q2. What is uvicorn used for?
Ans. Uvicorn is the server that starts FastAPI and sends your API responses to the browser or client.

Q3. What is the basic structure of a FastAPI app?
Ans. You create a FastAPI object and define routes using decorators.
Example:
    app = FastAPI()

Q4. How do you create a simple GET endpoint in FastAPI?
Ans. Use @app.get("/") above a function to respond to GET requests at the home URL.
Example:
    @app.get("/")

Q5. What does the browser receive when calling a FastAPI endpoint?
Ans. The browser receives JSON data by default.
Example response: {"message": "Hello"}

Q6. Why does FastAPI return JSON automatically?
Ans. FastAPI is designed for APIs, so it automatically converts Python data (like dicts) into JSON for you.
'''
