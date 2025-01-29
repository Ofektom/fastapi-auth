from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserRegisterSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    roles: List[str] = Field(default=["user"])

    class Config:
        str_min_length = 1
        str_strip_whitespace = True

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
