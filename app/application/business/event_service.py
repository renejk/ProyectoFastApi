from fpdf import FPDF
from sqlalchemy.orm import Session
from app.domain.schemas.event_schema import EventRequestModel, EventResponseModel, EventToUpdateModel
from app.infrastructure.persistence import EventCRUD


class EventService:

    event_repository = EventCRUD()

    @classmethod
    def create(self, event: EventRequestModel, db: Session) -> EventResponseModel:
        event_response = self.event_repository.create(event, db)
        return event_response
    
    @classmethod
    def find_all(self, db: Session) -> list[EventResponseModel]:
        events = self.event_repository.find_all(db)
        return events
    
    @classmethod
    def get_by_id(self, id: int, db: Session) -> EventResponseModel:
        event = self.event_repository.get_by_id(id, db)
        return event
    
    @classmethod
    def get_by_user_id(self, user_id: int, db: Session) -> list[EventResponseModel]:
        events = self.event_repository.get_by_user_id(user_id, db)
        return events
    
    @classmethod
    def update(self, id: int, event: EventToUpdateModel, db: Session) -> EventResponseModel:
        event = self.event_repository.update(id, event, db)
        return event
    
    @classmethod
    def delete_by_id(self, id: int, db: Session) -> str:
        self.event_repository.delete(id, db)
        return "Event deleted"
    
    @classmethod
    def get_report_events(self, user_id: int, db: Session) -> FPDF:
        pdf = self.event_repository.get_report_events(user_id, db)
        return pdf
    
