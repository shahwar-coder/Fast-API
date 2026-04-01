# =========================
# 🎯 INTERVIEW Q&A: Authentication vs Authorization
# =========================

# Q1: What is Authentication?

answer_1 = """
Authentication is the process of verifying identity.

It answers the question:
"Who are you?"

Examples:
- username and password
- API keys
- JWT tokens
- OAuth login (Google, GitHub)

Result:
The system confirms that the user is valid.
"""


# Q2: What is Authorization?

answer_2 = """
Authorization is the process of deciding what a user is allowed to do.

It answers the question:
"What can you do?"

Examples:
- admin can delete users
- normal user can only view data

Result:
The system allows or denies access to resources.
"""


# Q3: What is the main difference?

answer_3 = """
Authentication checks identity.

Authorization checks permissions.

So:

Authentication → who you are
Authorization → what you can do
"""


# Q4: What is the correct order?

answer_4 = """
The correct order is:

1. Authentication
2. Authorization

First, the system verifies who you are.
Then it decides what you are allowed to access.
"""


# Q5: Can you give a real-world example?

answer_5 = """
Example:

- Logging into a website → Authentication
- Accessing admin dashboard → Authorization

Another example:

- Swipe ID card to enter office → Authentication
- Access restricted room → Authorization
"""


# Q6: What happens if authentication fails?

answer_6 = """
If authentication fails, the user is not recognized,
so authorization does not even happen.

Access is denied immediately.
"""


# Q7: What happens if authorization fails?

answer_7 = """
If authentication succeeds but authorization fails,
the user is valid but does not have permission.

Example:
You are logged in, but cannot access admin features.
"""


# Q8: Short interview answer

answer_short = """
Authentication verifies identity (who you are),
while authorization determines permissions (what you can do).
Authentication happens first, followed by authorization.
"""


# =========================
# 🧠 MEMORY TRICK
# =========================

memory_tip = """
AuthN → Name (who are you)
AuthZ → Access (what can you do)
"""