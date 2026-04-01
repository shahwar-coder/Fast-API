from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


'''what are we doing????
from fastapi import FastAPI
- Imports the FastAPI class from the fastapi package
- This class is used to create a FastAPI application

app = FastAPI()
- Creates the FastAPI application object
- This object stores all routes and configurations
- Uvicorn runs this object to start the web server

@app.get("/")
- A decorator that registers a route
- Tells FastAPI to respond to a GET request
- '/' represents the root (home) endpoint of the API

def read_root():
- Defines the function executed when the '/' endpoint is accessed
- The function name does not matter to FastAPI

return {"message": "Hello FastAPI!"}
- Returns a Python dictionary
- FastAPI automatically converts it into a JSON response
- This JSON is sent back to the client
'''

# ========================


"""
To run FastAPI app:
-> uvicorn <filename_without_.py>:<FastAPI_variable> --reload

Example:
-> uvicorn 13_fastapi_create_your_first_fastapi_app:app --reload


NOTE ABOUT YELLOW UNDERLINE ON `fastapi` IMPORT:

- Even if the FastAPI app runs correctly using uvicorn,
  you may still see a yellow underline under `fastapi` in the import line.

- This does NOT mean FastAPI is broken.

- This happens because VS Code is using the WRONG Python interpreter.
  It is looking for FastAPI in a different environment than the one
  where FastAPI is actually installed.


QUICK FIX (VS Code):

1. Open Command Palette
   -> Ctrl + Shift + P (Windows/Linux)
   -> Cmd + Shift + P (Mac)

2. Search and select:
   -> Python: Select Interpreter

3. Choose the interpreter that belongs to your virtual environment:
   -> fast-api-env (recommended)

4. DO NOT choose generic system Python paths like:
   - /usr/bin/python
   - /usr/local/bin/python

5. Restart / Reload VS Code window if needed.


IMPORTANT CONCEPT:

- Terminal Python and VS Code Python can be DIFFERENT.
- Your app may run fine in terminal,
  but VS Code editor warnings depend on the selected interpreter.

Once the correct interpreter is selected:
- Yellow underline disappears
- Auto-complete works correctly
- Pylance warnings become accurate
"""

