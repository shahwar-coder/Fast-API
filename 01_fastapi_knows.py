'''
============================================================
Q1. What is FastAPI in simple words?
Ans:
FastAPI is a Python tool used to build **web APIs** quickly.
It lets computers/apps talk to each other by sending JSON.

# Example:
Your app → sends JSON → FastAPI → returns JSON back.

------------------------------------------------------------

Q2. Why is FastAPI called “fast”?
Ans:
Because:
• It is built on very fast async technology (ASGI)  
• It automatically validates data  
• It creates API docs automatically

So you write less code and get faster results.

# Example:
Just defining a function automatically shows it inside /docs.

------------------------------------------------------------

Q3. What should you know before learning FastAPI?
Ans:
You only need:
• Basic Python  
• How to use functions  
• How to install packages using pip  
• How to run Python files from terminal

No advanced knowledge needed.

------------------------------------------------------------

Q4. How do you install FastAPI?
Ans:
Run this command in terminal:

    pip install "fastapi[standard]"

This installs FastAPI plus the server needed to run APIs.

------------------------------------------------------------

Q5. What is the meaning of /docs and /redoc in FastAPI?
Ans:
FastAPI creates automatic API documentation pages:
• `/docs` → Swagger UI  
• `/redoc` → ReDoc UI  

These pages show all your API routes and let you **test them directly**.

# Example:
After running the app, open:
http://127.0.0.1:8000/docs

============================================================
'''
