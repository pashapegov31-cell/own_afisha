from datetime import datetime, time

from pydantic import BaseModel


class Concert(BaseModel):
    id: int
    name: str
    tickets_count: int
    tickets_costs: int
    start_time: datetime
    lasts: time
    place_id: int
