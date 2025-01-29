# exception_handlers.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .exceptions import UserAlreadyExistsException, InvalidCredentialsException, PasswordValidationException, NotFoundException
import logging

logger = logging.getLogger(__name__)

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(UserAlreadyExistsException)
    async def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
        logger.error(f"User already exists: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail}
        )

    @app.exception_handler(InvalidCredentialsException)
    async def invalid_credentials_exception_handler(request: Request, exc: InvalidCredentialsException):
        logger.error(f"Invalid credentials: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail}
        )
    
    @app.exception_handler(PasswordValidationException)
    async def password_validation_exception_handler(request: Request, exc: PasswordValidationException):
        logger.error(f"Password validation failed: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail}
        )

    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(request: Request, exc: NotFoundException):
        logger.error(f"Resource not found: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail}
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unexpected error: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"message": "An unexpected error occurred"}
        )
