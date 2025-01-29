from bcrypt import hashpw, gensalt, checkpw
import logging

logger = logging.getLogger(__name__)

def hash_password(password: str) -> str:
    try:
        return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")
    except Exception as e:
        logger.error(f"Error hashing password: {e}")
        raise ValueError("Error hashing password")

def verify_password(password: str, hashed: str) -> bool:
    try:
        return checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception as e:
        logger.error(f"Error verifying password: {e}")
        raise ValueError("Error verifying password")
