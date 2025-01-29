from beanie import Document
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List
import re

class User(Document):
    full_name: str
    email: EmailStr
    hashed_password: str
    roles: List[str] = Field(default=["user"])

    class Settings:
        name = "users"

    @field_validator("full_name")
    def validate_full_name(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Full name cannot be empty")
        return v

    @field_validator("email")
    def validate_email_format(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError("Invalid email format")
        return v
