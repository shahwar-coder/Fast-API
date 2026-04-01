"""
FastAPI Architecture

FastAPI is built on three main components:

1. Starlette
   - The web framework layer.
   - Handles routing, request/response handling, and WebSockets.

2. Uvicorn / Gunicorn
   - The ASGI web server.
   - Runs the FastAPI application and handles client HTTP requests.

3. Pydantic
   - Handles data validation and parsing.
   - Ensures request bodies, query params, and headers match expected types.

Request Flow:

User (Client)
      ↓
Web Server (Uvicorn / Gunicorn)
      ↓
Web Framework (FastAPI / Starlette)
      ↓
Data Validation (Pydantic)
      ↓
Application Logic
      ↓
Response sent back to User
"""