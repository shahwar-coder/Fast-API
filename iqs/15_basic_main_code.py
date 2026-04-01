# =========================
# 🎯 INTERVIEW Q&A: Basic FastAPI App
# =========================

# Q1: Can you explain this FastAPI code?

answer_1 = """
This code creates a simple FastAPI application.

- FastAPI() initializes the app
- @app.get('/') defines a GET API endpoint
- index_page() is the function that runs when the endpoint is called
- It returns a JSON response

So when a user hits '/', they get a simple message.
"""


# Q2: What is FastAPI()?

answer_2 = """
FastAPI() creates an instance of the FastAPI application.

It is the main entry point where we define routes and configurations.
"""


# Q3: What does @app.get('/') mean?

answer_3 = """
@app.get('/') is a decorator.

It means:
- this function will handle HTTP GET requests
- for the '/' (root) URL

So when someone visits '/', this function is executed.
"""


# Q4: What does the function return?

answer_4 = """
The function returns a dictionary:

{'message': "Hello from index page"}

FastAPI automatically converts it into JSON response:

{
  "message": "Hello from index page"
}
"""


# Q5: How do you run this application?

answer_5 = """
We run it using Uvicorn:

uvicorn main:app --reload

- main → filename
- app → FastAPI instance
- --reload → auto-reload on changes
"""


# Q6: How can you test the API?

answer_6 = """
FastAPI provides automatic documentation.

You can open:

http://127.0.0.1:8000/docs

This gives Swagger UI where you can test APIs directly.
"""


# Q7: What is the response type?

answer_7 = """
The response is JSON.

FastAPI automatically converts Python dictionaries into JSON responses.
"""


# Q8: Short interview answer

answer_short = """
This is a basic FastAPI app where a GET endpoint is defined at '/',
which returns a JSON response, and can be tested via Swagger UI at /docs.
"""