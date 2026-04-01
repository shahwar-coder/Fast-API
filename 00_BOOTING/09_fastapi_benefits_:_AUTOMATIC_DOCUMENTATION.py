'''
Q1. What does “automatic documentation” mean in FastAPI?
Ans. It means FastAPI creates API docs for you just by reading your code — no extra setup.
'''
# Example
from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def hello():
    return {"msg": "Hi"}  
# → This endpoint automatically appears in /docs and /redoc
# without writing any doc code.


'''
Q2. What is available at /docs in FastAPI?
Ans. /docs shows Swagger UI, where you can test your API with buttons and live requests.
'''
# Example
# Open browser → http://127.0.0.1:8000/docs
# You can click GET/POST buttons and send real requests.
# Note : Swagger UI is basically an interactive API explorer. 
# It lets you see all your endpoints, their parameters, and try them out directly from the browser.


'''
Q3. What is available at /redoc?
Ans. /redoc shows clean, professional API documentation that is easy for teams to read.
'''
# Example
# Open browser → http://127.0.0.1:8000/redoc
# It shows all endpoints with descriptions and data models in a nice format.
# It is different from Swagger UI as it focuses more on 
# - readability and structure rather than interactivity.


'''
Q4. How does FastAPI generate documentation automatically?
Ans. It reads your path operations, type hints, and Pydantic models, 
then builds the docs from them.
'''
# Example
@app.post("/users")
def create_user(name: str, age: int):
    return {"ok": True}
# Both parameters appear in the auto docs!


'''
Q5. Why does this save time for developers?
Ans. Because you don’t need to manually write API docs 
— FastAPI updates them whenever the code changes.
'''
# Example
# Add a new endpoint → instantly appears in docs, no copy-paste needed.


'''
Q6. Why is automatic documentation great for teams?
Ans. Everyone can understand and test the API quickly, even new team members.
'''
# Example
# A teammate opens /docs → they can try the API without reading all the code.
# ------------
# Swagger UI can be thought of as a "live playground" for your API,
# while ReDoc serves as a "well-organized manual" for understanding it.
# ------------
# Swagger UI is like Postman but built into your API docs.
# ReDoc is like a nicely formatted PDF manual that you can read through.
