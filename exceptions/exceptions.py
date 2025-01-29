# exceptions.py

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

class UserAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "User with this email already exists"):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)

class InvalidCredentialsException(HTTPException):
    def __init__(self, detail: str = "Invalid email or password"):
        super().__init__(status_code=HTTP_401_UNAUTHORIZED, detail=detail)

class PasswordValidationException(HTTPException):
    def __init__(self, detail: str = "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character."):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)

class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)
