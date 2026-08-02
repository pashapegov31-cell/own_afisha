from pydantic import BaseModel


class PlaceCreate(BaseModel):
    name: str
    seats_count: int

class PlaceResponse(BaseModel):
    id: int
    name: str
    seats_count: int
