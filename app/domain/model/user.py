from sqlalchemy import DateTime, Integer, String
from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column, Mapped
from app.infrastructure.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    password: Mapped[str] = mapped_column(String(256))
    name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(256))
    phone: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "role": self.role,
            "email": self.email,
            "phone": self.phone,
            "status": self.status,
            "created_at": self.created_at.__str__()
        }