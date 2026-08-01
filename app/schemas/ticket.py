from pydantic import BaseModel


class Ticket(BaseModel):
    num: int
    concert_id: int
    place_id: int
    is_sold: bool = False
