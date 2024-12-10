from sqlalchemy import DateTime, Integer, String, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.infrastructure.database import Base
from app.domain.model.user import User


class Event(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    name: Mapped[str] = mapped_column(String(256))
    attendees: Mapped[int] = mapped_column(Integer)
    even_date: Mapped[str] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    user: Mapped["User"] = relationship()