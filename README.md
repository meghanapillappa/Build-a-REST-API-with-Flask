# Build-a-REST-API-with-Flask
Build a CRUD API to manage user data (in-memory dictionary)
This project is a simple REST API built with Flask . The API provides full CRUD (Create, Read, Update, Delete) functionality to manage user data stored in an in-memory dictionary. It demonstrates the fundamentals of API development, HTTP methods, and JSON handling in Python.

The API has the following routes:

GET /users → Fetch all users

GET /users/<user_id> → Fetch a specific user by ID

POST /users → Add a new user (requires JSON with id and name)

PUT /users/<user_id> → Update an existing user’s data

DELETE /users/<user_id> → Remove a user from storage

Each route returns a JSON response along with appropriate HTTP status codes like 200 OK, 201 Created, 400 Bad Request, and 404 Not Found.

Since this project uses in-memory storage, the data will reset when the application restarts. In a real-world application, a database such as SQLite, MySQL, or MongoDB could be integrated instead.

This project highlights REST principles, Flask routing, request handling, and API testing using tools like Postman or curl. It serves as a foundational project for anyone learning backend development with Python and Flask
