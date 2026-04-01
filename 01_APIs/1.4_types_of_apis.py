'''
Types of APIs  

APIs can be classified based on where they are used and what they interact with.

---

1. Web API  

APIs that work over the internet using HTTP/HTTPS.

They allow applications (web apps, mobile apps, AI systems) to communicate with servers remotely.

Data is usually exchanged in JSON format.

Example:
Fetching weather data from a weather service API.
Embedding Google Maps in a website.

Interview Insight:
Most modern backend systems expose Web APIs (REST/GraphQL).

---

2. Library API  

APIs provided by software libraries or frameworks.

They expose predefined functions so developers don’t need to implement everything from scratch.

Example:
NumPy API for mathematical operations.
TensorFlow API for building ML models.
Matplotlib API for visualizations.

Interview Insight:
Library APIs improve productivity through reusable abstractions.

---

3. Remote API  

APIs that allow interaction with systems running on another machine or network.

All Web APIs are Remote APIs, but not all Remote APIs use HTTP (some use internal network protocols).

Example:
Using AWS EC2 API to launch virtual machines.
Accessing Google Drive files via its API.

Interview Insight:
Remote APIs enable distributed and cloud-based systems.

---

4. Database API  

APIs that allow applications to interact with databases in a structured way.

They support CRUD operations (Create, Read, Update, Delete).

Example:
MySQL Connector.
MongoDB API.
Firebase Realtime Database API.

Interview Insight:
Database APIs abstract low-level database communication.

---

5. Hardware API  

APIs that allow software to communicate with physical hardware devices.

They provide an abstraction layer over complex hardware operations.

Example:
CUDA API for GPU computations.
APIs for IoT sensors.
Controlling robots or drones programmatically.

Interview Insight:
Hardware APIs hide low-level device complexity.

---

6. GUI API  

APIs used to build and manage graphical user interfaces.

They allow developers to create buttons, windows, layouts, and interactions programmatically.

Example:
Java Swing.
Tkinter.
Android SDK.

Interview Insight:
GUI APIs abstract UI rendering and event handling.

---

Core Summary:

Different types of APIs exist based on:
• Where they operate (local vs remote)
• What they interact with (web, database, hardware, UI)
• Their purpose (communication vs abstraction)

Understanding types helps you choose the right API architecture for the problem you are solving.
'''