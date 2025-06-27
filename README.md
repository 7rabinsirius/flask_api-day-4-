# flask_api-day-4-

## 🧰 Flask REST API: User Information Manager

This project is a simple yet fully functional **CRUD REST API** built using Flask. It allows clients to manage user information (name and email) with support for creating, reading, updating, and deleting users from an in-memory data store.

### 🚀 Features
- **GET /user_info**
  - Retrieve all users or a specific user using `user_id` as a query parameter.
- **POST /user_info**
  - Create a new user by sending JSON with `name` and `email`.
- **PUT /user_info**
  - Update an existing user's info using `user_id` and a JSON payload.
- **DELETE /user_info**
  - Remove a user by passing `user_id` in the query string.

### 📦 Tech Stack
- **Python 3.x**
- **Flask** – lightweight WSGI web framework

### 🧪 Sample Usage (via Postman or curl)

#### Create a User
```http
POST /user_info
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

#### Update a User
```http
PUT /user_info?user_id=1
Content-Type: application/json

{
  "email": "alice.updated@example.com"
}
```

