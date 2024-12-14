from sqlalchemy import DateTime, Float, Integer, String, ForeignKey
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
    event_date: Mapped[str] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    duration: Mapped[float] = mapped_column(Float)

    user: Mapped["User"] = relationship()

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "attendees": self.attendees,
            "duration": self.duration,
            "event_date": self.event_date.__str__(),
            "user_id": self.user.id
        }