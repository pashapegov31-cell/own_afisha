from app.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Places(Base):
    __tableename__ = "places"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    seats_count: Mapped[int] = mapped_column(Integer)
