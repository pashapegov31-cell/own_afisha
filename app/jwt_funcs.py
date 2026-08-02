import hashlib
from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None) -> str:
    to_encode = data.copy()
    expires = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update(
        {"exp": expires, "iat": datetime.now(timezone.utc), "typ": "access"}
    )
    encoded_access_token = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITM
    )
    return encoded_access_token


def create_refresh_token(data: dict, expires_delta: timedelta | None) -> str:
    to_encode = data.copy()
    expires = datetime.now(timezone.utc) + (
        expires_delta or timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    to_encode.update(
        {
            "exp": expires,
            "iat": datetime.now(timezone.utc),
            "typ": "refresh",
        }
    )
    encoded_refresh_token = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITM
    )
    return encoded_refresh_token


def decode_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITM])
        return payload
    except JWTError:
        raise


def hashed_token(token: str):
    return hashlib.sha256(token.encode()).hexdigest()
