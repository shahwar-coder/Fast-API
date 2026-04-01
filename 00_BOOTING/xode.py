from fastapi import FastAPI
 
app = FastAPI()

'''
Usage: Application Root Request 
Rest API URL: http://localhost:8000/
Required Fields: None
Access Type: Public
'''

@app.get("/", description="This isAppplication Root Request")
def home_page():
    return {"message" : "Hello from homepage"}

@app.get("/about", description="About page of the application")
def about_page():
    return {"message" : "This is the about page"}

