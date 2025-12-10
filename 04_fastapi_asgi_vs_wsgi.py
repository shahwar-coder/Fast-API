'''
Q1. What is WSGI in simple words?
Ans. WSGI is an older way for Python web apps to run. It only supports sync code.
Example: One request must finish before the next one starts.

Q2. Why is WSGI called a "single-lane road"?
Ans. Because it handles one request at a time, like cars moving slowly in one lane.

Q3. What is ASGI?
Ans. ASGI is a newer system that supports async code and many connections at once.

Q4. Why is ASGI like a "multi-lane highway"?
Ans. Because multiple requests can move at the same time without blocking each other.

Q5. Which one does FastAPI use: WSGI or ASGI?
Ans. FastAPI uses ASGI because it needs async support to be fast and efficient.

Q6. Why does FastAPI perform better with ASGI?
Ans. ASGI lets FastAPI handle many users at the same time, making it great for real-time or high-traffic apps.
Example: Chat apps or APIs with lots of requests.
'''
