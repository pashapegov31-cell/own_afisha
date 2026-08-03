from fastapi import FastAPI

from app.authorization import AuthService
from app.database import async_session, get_by_email, get_by_id, get_db
from app.schemas.user import UserCreate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "own_afisha"}


@app.get("/users")
async def get_all_users():
    return get_db()


@app.get("/users/{user_id}")
async def user_by_id(user_id: int):
    return get_by_id(id=user_id)


@app.get("users/{user_email}")
async def user_by_email(user_email: str):
    return get_by_email(email=user_email)


@app.put("/auth/{email}/{password}")
async def create_new_user(email: str, password: str):
    session = async_session()
    user = UserCreate(email=email, password=password)
    await AuthService.create_user(db=session, new_user=user)
