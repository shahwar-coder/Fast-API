# =========================
# 🎯 INTERVIEW Q&A: Asynchronous Programming (Python + FastAPI)
# =========================

# Q1: What is asynchronous programming?

answer_1 = """
Asynchronous programming is a way to run tasks without blocking execution.

In simple terms:
a program can start a task (like an API call) and continue doing other work
instead of waiting for it to finish.

This improves performance, especially for I/O operations.
"""  # :contentReference[oaicite:0]{index=0}


# Q2: What problem does async solve?

answer_2 = """
In normal (synchronous) programming:

- task 1 runs → finishes → then task 2 starts

This wastes time when tasks involve waiting (like API or DB calls).

Async solves this by allowing multiple tasks to run concurrently.
"""


# Q3: What are async and await?

answer_3 = """
- async → defines an asynchronous function (coroutine)
- await → pauses execution until the result is ready

Example:
async def fetch():
    await some_task()

This allows non-blocking execution.
"""


# Q4: Explain your example code

answer_4 = """
In the code:

- fetch_data() simulates an I/O task using asyncio.sleep()
- multiple tasks (task1, task2, task3) are created
- asyncio.gather() runs them concurrently

So instead of running one by one, all tasks run together,
reducing total execution time.
"""  # :contentReference[oaicite:1]{index=1}


# Q5: What is asyncio.gather()?

answer_5 = """
asyncio.gather() runs multiple async tasks concurrently.

It waits for all tasks to complete and returns their results.

This is useful when you want to run multiple independent operations together.
"""


# Q6: Why is async important in FastAPI?

answer_6 = """
FastAPI uses async to handle multiple requests efficiently.

Example:
- many users call an API at the same time
- async allows handling all requests without blocking

This makes FastAPI scalable and high-performance.
"""


# Q7: What is I/O-bound vs CPU-bound?

answer_7 = """
I/O-bound:
- waiting for external operations (API, DB, file)
- async helps here

CPU-bound:
- heavy computation (math, ML training)
- async does NOT help much

Async is mainly useful for I/O-bound tasks.
"""


# Q8: What is the benefit of async programming?

answer_8 = """
- better performance
- handles multiple tasks efficiently
- improves scalability
- reduces waiting time
"""


# Q9: Short interview answer

answer_short = """
Asynchronous programming allows a program to run multiple I/O tasks concurrently
using async and await, improving performance and scalability,
especially in web frameworks like FastAPI.
"""