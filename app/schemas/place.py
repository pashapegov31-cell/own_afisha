from pydantic import BaseModel


class Place(BaseModel):
    id: int
    name: str
    seats_count: int
