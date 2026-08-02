import hashlib
from datetime import datetime, timedelta, timezone

from exceptions import AuthException
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.users import Users
from app.schemas.user import UserCreate, UserLogin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    def hashed_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(user: Users, expires_delta: timedelta | None = None) -> str:

        expires = datetime.now(timezone.utc) + (
            expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        to_encode = {
            "email": user.email,
            "exp": expires,
            "iat": datetime.now(timezone.utc),
            "typ": "access",
        }

        encoded_access_token = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITM
        )
        return encoded_access_token

    @staticmethod
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

    @staticmethod
    def decode_token(token: str):
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITM]
            )
            return payload
        except JWTError:
            raise

    @staticmethod
    def hashed_token(token: str):
        return hashlib.sha256(token.encode()).hexdigest()

    @staticmethod
    async def create_user(db: AsyncSession, new_user: UserCreate) -> Users:
        exists = await db.execute(select(Users).where(Users.email == new_user.email))
        if exists.scalar_one_or_none():
            raise AuthException("Пользователем с таким email уже существует")

        if len(new_user.password) < 8:
            raise AuthException("Пароль должен быть не менее 8 символов")

        valid_user = Users(email=new_user.email, password=new_user.password)
        db.add(valid_user)
        await db.commit()

        return valid_user

    @staticmethod
    async def authentificate(db: AsyncSession, email: str, password: str) -> Users:
        exists = await db.execute(select(Users).where(Users.email == email))
        exists_user = exists.scalar_one_or_none()
        if not exists_user:
            raise AuthException("Неверный логин или пароль")

        valid_password = AuthService.verify_password(
            password, exists_user.hashed_password
        )
        if not valid_password:
            raise AuthException("Неверный логин или пароль")

        return exists_user

    @staticmethod
    async def login_user(db: AsyncSession, log_user: UserLogin):
        user = await AuthService.authentificate(
            db=db, email=log_user.email, password=log_user.password
        )

        access_token = AuthService.create_access_token(user=user)
        return access_token
