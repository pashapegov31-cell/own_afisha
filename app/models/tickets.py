from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Tickets(Base):
    __tablename__ = "tickets"

    num: Mapped[int] = mapped_column(Integer)
    concert_id: Mapped[int] = mapped_column(ForeignKey("concerts.id"))
    is_sold: Mapped[bool] = mapped_column(Boolean)
