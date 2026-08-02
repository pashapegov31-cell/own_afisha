from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(Text)
    tickets_ids: Mapped[list[int]] = mapped_column(ForeignKey("tickets.num"))
    is_admin: Mapped[bool] = mapped_column(Boolean)
