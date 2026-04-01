"""Authentication vs Authorization

Authentication
Verifies the identity of a user or system.

Answers:
“Who are you?”

Examples:
• Username + Password  
• API Key  
• JWT Token  
• OAuth login  

Result → User identity is confirmed.

---

Authorization
Determines what an authenticated user is allowed to do.

Answers:
“What can you do?”

Examples:
• Admin → can delete users  
• User → can only view data  

Result → Access is allowed or denied.

---

Core Difference

Authentication → Identity verification  
Authorization → Permission control

Order:

Authentication → Authorization

Example:

Login to system → Authentication  
Access admin dashboard → Authorization"""