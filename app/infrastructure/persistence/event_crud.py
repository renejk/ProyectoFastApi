from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.application.contracts.event_repository import EventRepository
from app.domain.schemas.event_schema import EventRequestModel,EventResponseModel
from app.domain.model.event import Event



class EventCRUD(EventRepository):

    @staticmethod
    def create(event: EventRequestModel, db: Session) -> EventResponseModel:
        try:
            _event = Event(**event.model_dump())
            db.add(_event)
            db.commit()         
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
                                , detail=str(e))
        return EventResponseModel(**_event.model_dump())
    
    @staticmethod
    def get_by_id(id: int, db: Session) -> EventResponseModel:
        try:
            _event = db.query(Event).filter(Event.id == id).first()
            if not _event:
                raise ValueError("Event not found")
            return EventResponseModel(**_event.model_dump())
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def find_all(db: Session) -> list[EventResponseModel]:
        try:
            _events = db.query(Event).all()
            return [EventResponseModel(**_event.model_dump()) for _event in _events]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))
        
    @staticmethod
    def get_by_user_id(user_id: int, db: Session) -> list[EventResponseModel]:
        try:
            _events = db.query(Event).filter(Event.user_id == user_id).all()
            return [EventResponseModel(**_event.model_dump()) for _event in _events]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def update(id: int, event: EventRequestModel, db: Session) -> EventResponseModel:
        try:
            _event = db.query(Event).filter(Event.id == id).first()
            if not _event:
                raise ValueError("Event not found")
            _event.name = event.name if event.name else _event.name
            _event.attendees = event.attendees if event.attendees else _event.attendees
            _event.event_date = event.event_date if event.event_date else _event.event_date
            _event.user_id = event.user_id if event.user_id else _event.user_id
            db.commit()
            return EventResponseModel(**_event.model_dump())
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def delete(id: int, db: Session) -> None:
        try:
            _event = db.query(Event).filter(Event.id == id).first()
            if not _event:
                raise ValueError("Event not found")
            db.delete(_event)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))
        

    @staticmethod
    def get_report_users(db: Session) -> list[UserResponseModel]:
        try:
            _users = db.query(User).join(Event).group_by(User.id).all()

            # generacion pdf


            return [UserResponseModel(**_user.model_dump()) for _user in _users]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))