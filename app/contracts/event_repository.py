from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.domain.schemas.event_schema import EventRequestModel, EventResponseModel

class EventRepository(ABC):

    @abstractmethod
    def create(self, event: EventRequestModel, db: Session) -> EventResponseModel:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int, db: Session) -> EventResponseModel:
        pass

    @abstractmethod
    def get_by_name(self, name: str, db: Session) -> EventResponseModel:
        pass

    @abstractmethod
    def find_all(self, db: Session) -> list[EventResponseModel]:
        pass        

    @abstractmethod
    def update(self, id: int, event: EventRequestModel, db: Session) -> EventResponseModel:
        pass

    @abstractmethod
    def delete(self, id: int, db: Session) -> None:
        pass