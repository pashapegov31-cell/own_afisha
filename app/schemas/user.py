from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    tickets_ids: list[int]
    is_admin: bool = False
    concerts_ids: list[int]
