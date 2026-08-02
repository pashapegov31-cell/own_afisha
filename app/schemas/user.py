from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    pasword: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    password: str
    tickets_ids: list[int]
    is_admin: bool = False
    concerts_ids: list[int]
