from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index_page():
    return {'message': "Hello from index page"}

# http://127.0.0.1:8000/docs (to check APIs)