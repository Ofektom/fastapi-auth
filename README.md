# FastAPI Authentication System

This is a simple FastAPI-based authentication system that allows users to register and log in. It includes features like password validation, token-based authentication using JWT, and user registration with email verification. It uses Beanie and MongoDB as the database, and the application is structured with modern FastAPI best practices.

## Requirements

- Python 3.7+
- MongoDB instance
- Virtual environment (optional, but recommended)

## Setup

Follow these steps to set up the application after cloning the repository:

### 1. Clone the repository

```bash
git clone https://github.com/Ofektom/fastapi-auth.git
cd fastapi-auth

```

### 2. Set up a virtual environment (optional)

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies

`pip install -r requirements.txt`

### 4. Set up environment variables

```plaintext
MONGO_URI=mongodb://localhost:27017/fastapi-auth
SECRET_KEY=your-secret-key
ALGORITHM=HS256
```

### 5. Run the application

`uvicorn main:app --reload`

## Endpoints

### 1. Register User

`Endpoint: POST /auth/register`
Request Body:
json
Copy
Edit

```json
{
  "full_name": "John Doe",
  "email": "johndoe@example.com",
  "password": "Password123!",
  "roles": ["user"]
}
```

Response:
json
Copy
Edit

```json
{
  "message": "User registered successfully"
}
Validation Rules for Password:

Minimum 8 characters
At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character (e.g., !@#$%^&*())
```

### 2. Login User

Endpoint: POST /auth/login
Request Body:
json
Copy
Edit

```json
{
  "email": "johndoe@example.com",
  "password": "Password123!"
}
```

Response:
json
Copy
Edit

```json
{
  "access_token": "your-access-token",
  "token_type": "bearer"
}
```

3. Protected Route Example
   Endpoint: GET /protected
   Authorization: Bearer token required (JWT)
   Response: Any data you want to secure
   json
   Copy
   Edit

```json
{
  "message": "This is a protected route"
}
```

## Exception Handling

The application includes custom exception handling for the following:

**Email Already Registered:** Returns a 400 Bad Request error with the message User with this email already exists if the email is already taken.
Invalid Credentials: Returns a 401 Unauthorized error with the message Invalid email or password for failed login attempts.

**General Error:** If an error occurs, a 500 Internal Server Error will be returned.
Example Error Response:
json
Copy
Edit

```json
{
  "detail": "An error occurred while registering the user"
}
```

Custom Exception Classes
The app uses custom exception classes for specific errors like EmailAlreadyExists, PasswordValidationError, and UserNotFound.

## Notes

The app uses JWT tokens for user authentication.
You can replace the MongoDB connection string with your own database credentials in the .env file.
Make sure to install the required dependencies with pip install -r requirements.txt.
The app runs locally on http://127.0.0.1:8000, but can be deployed to any server.
To test the API, you can use Postman or any API client that supports sending HTTP requests.

**Additional Features**

Password hashing and verification are handled using bcrypt.
JWT tokens are signed using a secret key.

Password validation ensures strong password security.
The app uses pydantic for request validation.

## License

MIT License - see the LICENSE file for details.

### Key Details in the `README.md`:

1. **How to Run the Application:** Instructions to clone the repository, set up a virtual environment, install dependencies, configure environment variables, and run the app.
2. **Endpoints:** Provides the necessary API endpoints with example request and response bodies. This is particularly useful for frontend developers to know how to structure requests to interact with the backend.
3. **Exception Handling:** Describes the exceptions thrown and the responses the API will return when issues occur.
4. **Notes on JWT, Password Validation, etc.:** Gives additional context about important aspects of the app, such as security mechanisms (JWT, password hashing).

This should be a comprehensive `README.md` for anyone using or consuming the API.
