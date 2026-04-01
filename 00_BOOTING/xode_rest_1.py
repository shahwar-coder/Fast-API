'''
Rest Api 1
-----------
Usage: Create User
Rest API URL: http://127.0.0:8000/user/create
Method Type: GET
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="Home Page-Application root request")
def home():
    return {"message" : "This is home page"}

@app.post("/user/create", description="Create a user")
def create_user():
    pass