from app.database import Base
from sqlalchemy import Boolean, String, Text


from sqlalchemy.orm import Mapped, mapped_column


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(Text)
    tickets_ids: Mapped[list[int]] = mapped_column()  #! ForeignKey to Tickets
    is_admin: Mapped[bool] = mapped_column(Boolean)
    concerts_ids: Mapped[list[int]] = mapped_column()  #! ForeignKey to Concerts
