# auth_route.py

from fastapi import APIRouter, HTTPException, status, Depends
from models.user_model import User
from schemas.auth_schema import UserRegisterSchema, UserLoginSchema, TokenResponse
from utils.hashing import hash_password, verify_password
from utils.jwt_handler import create_access_token
import re
from exceptions.exceptions import PasswordValidationException, UserAlreadyExistsException, NotFoundException, InvalidCredentialsException

auth_router = APIRouter()

# Password validation function
def validate_password(password: str):
    regex_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}$"
    
    if not re.match(regex_pattern, password):
        raise PasswordValidationException()
    
    return password

@auth_router.post("/register", response_model=dict)
async def register_user(user: UserRegisterSchema):
    try:
        existing_user = await User.find_one(User.email == user.email)
        if existing_user:
            raise UserAlreadyExistsException()

        validate_password(user.password)

        hashed_password = hash_password(user.password)
        
        new_user = User(
            full_name=user.full_name,
            email=user.email,
            hashed_password=hashed_password,
            roles=user.roles
        )
        await new_user.insert()
        return {"message": "User registered successfully"}

    except Exception as e:
        raise e 

@auth_router.post("/login", response_model=TokenResponse)
async def login_user(user: UserLoginSchema):
    try:
        existing_user = await User.find_one(User.email == user.email)
        if not existing_user:
            raise NotFoundException(detail="User not found")

        if not verify_password(user.password, existing_user.hashed_password):
            raise InvalidCredentialsException()

        access_token = create_access_token({"sub": str(existing_user.id), "roles": existing_user.roles})
        return {"access_token": access_token}

    except Exception as e:
        raise e 
