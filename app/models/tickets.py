from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Tickets(Base):
    __tablename__ = "tickets"

    num: Mapped[int] = mapped_column(primary_key=True)
    concert_id: Mapped[int] = mapped_column(ForeignKey("concerts.id"))
    is_sold: Mapped[bool] = mapped_column(Boolean)
