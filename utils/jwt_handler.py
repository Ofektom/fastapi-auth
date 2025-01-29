import jwt
from datetime import datetime, timedelta, timezone
from decouple import config
import logging

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = "HS256"
logger = logging.getLogger(__name__)

def create_access_token(data: dict, expires_delta: int = 60):
    try:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        logger.error(f"Error creating JWT token: {e}")
        raise ValueError("Error creating JWT token")
