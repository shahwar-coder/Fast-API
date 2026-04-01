'''
Q1. What does the --reload flag do in Uvicorn?
A.
The --reload flag makes Uvicorn watch your Python files.
Whenever you change the code, the server automatically restarts.
This means your changes take effect immediately.
'''
# Example:
# Command:
# uvicorn main:app --reload
# Change return message in main.py
# Refresh browser → new response appears automatically


'''
Q2. Why is --reload especially useful for beginners?
A.
Because beginners change code very frequently.
Without --reload, you must stop and restart the server every time.
With --reload, you only refresh the browser.
'''
# Example:
# Without reload:
# Edit code → Ctrl+C → run uvicorn again → refresh browser
# With reload:
# Edit code → refresh browser


'''
Q3. What problem does --reload actually solve?
A.
It removes the manual restart loop during development.
This makes learning faster, smoother, and less frustrating.
'''
# Example:
# Learning APIs → many small experiments
# --reload removes repeated server restarts


'''
Q4. How does --reload work internally (conceptual)?
A.
Uvicorn monitors your project files for changes.
When it detects a change, it shuts down the server
and starts it again automatically.
'''
# Example:
# main.py saved → Uvicorn detects change → restarts server


'''
Q5. Why should --reload NEVER be used in production?
A.
Because file watching costs resources and reduces performance.
In production, code does not change live.
Stability and speed matter more than convenience.
'''
# Example:
# Development → uvicorn main:app --reload
# Production  → uvicorn main:app   (no reload)


'''
Q6. What is the correct mental model for --reload?
A.
--reload is a development helper, not a server feature.
It exists only to improve developer experience.
'''
# Example:
# --reload = training wheels
# Remove training wheels before production
