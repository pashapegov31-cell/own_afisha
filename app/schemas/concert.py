from datetime import datetime, time

from pydantic import BaseModel


class ConcertCreate(BaseModel):
    name: str
    start_time: datetime
    lasts: time


class ConcertResponse(BaseModel):
    id: int
    name: str
    tickets_count: int
    tickets_costs: int
    start_time: datetime
    lasts: time
    place_id: int

    model_config = {"from_attributes": True}
