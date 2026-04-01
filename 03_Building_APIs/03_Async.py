"""
Simple demonstration of asynchronous programming in Python.

Goal:
Start multiple tasks that simulate slow I/O operations
(such as API calls or database queries) and run them
concurrently using async and await.
"""

import asyncio


# Simulated I/O task
async def fetch_data(task_name, delay):
    print(f"{task_name} started")

    # Simulate waiting for an external resource
    await asyncio.sleep(delay)

    print(f"{task_name} finished")
    return f"{task_name} result"


async def main():
    # Start multiple async tasks concurrently
    task1 = fetch_data("Task 1", 2)
    task2 = fetch_data("Task 2", 3)
    task3 = fetch_data("Task 3", 1)

    # Run all tasks concurrently
    results = await asyncio.gather(task1, task2, task3)

    print("\nResults:")
    for r in results:
        print(r)


# Run the async program
asyncio.run(main())


# ======= X =======

"""
Async Programming Demo (asyncio)

Purpose
-------
Demonstrates running multiple I/O-bound tasks concurrently using async/await.

Key Concepts
------------
- async def → defines a coroutine
- await → pauses execution until result is ready
- asyncio.sleep() → simulates non-blocking I/O delay
- asyncio.gather() → runs multiple coroutines concurrently

Flow
----
1. Three async tasks are created (fetch_data).
2. Each task simulates a delay using await.
3. asyncio.gather() runs all tasks in parallel.
4. Results are collected and printed after all tasks complete.

Result
------
Tasks run concurrently instead of sequentially,
reducing total execution time.
"""