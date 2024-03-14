import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

from config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify the plain_password and hashed"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash the password"""
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    """Create a new access token"""
    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             settings.JWT_SECRET_KEY.get_secret_value(),
                             algorithm=settings.ALGORITHM)
    return encoded_jwt
