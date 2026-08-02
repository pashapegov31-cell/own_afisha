from pydantic import BaseModel


class TicketCreate(BaseModel):
    concert_id: int


class TicketResponse(BaseModel):
    num: int
    concert_id: int
    is_sold: bool = False
