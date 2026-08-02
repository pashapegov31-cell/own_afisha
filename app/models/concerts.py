from datetime import datetime, time

from sqlalchemy import DateTime, ForeignKey, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Concerts(Base):
    __tablename__ = "concerts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    tickets_costs: Mapped[int] = mapped_column(Integer)
    tickets_count: Mapped[int] = mapped_column(Integer)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    lasts: Mapped[time] = mapped_column(Time)
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"))
