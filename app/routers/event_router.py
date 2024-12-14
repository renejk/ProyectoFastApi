from io import BytesIO
from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session
from app.domain.schemas.event_schema import EventRequestModel, EventResponseModel, EventToUpdateModel
from app.application.business.event_service import EventService


event_router = APIRouter(
    prefix="/events",
    tags=["events"]
)


@event_router.post("", response_model= EventResponseModel,  status_code=status.HTTP_201_CREATED)
async def create_event(event: EventRequestModel, db: Session = Depends(get_db)):
    event_response = EventService.create(event, db)
    return event_response

@event_router.get("", response_model=list[EventResponseModel], status_code=status.HTTP_200_OK)
async def get_events(db: Session = Depends(get_db)):
    events = EventService.find_all(db)
    return events

@event_router.get("/{id}", response_model=EventResponseModel, status_code=status.HTTP_200_OK)
async def get_event(id: int, db: Session = Depends(get_db)):
    event = EventService.get_by_id(id, db)
    return event

@event_router.get("/user/{user_id}", response_model=list[EventResponseModel], status_code=status.HTTP_200_OK)
async def get_events_by_user_id(user_id: int, db: Session = Depends(get_db)):
    events = EventService.get_by_user_id(user_id, db)
    return events

@event_router.put("/{id}", response_model=EventResponseModel, status_code=status.HTTP_200_OK)
async def update_event(id: int, event: EventToUpdateModel, db: Session = Depends(get_db)):
    event_response = EventService.update(id, event, db)
    return event_response

@event_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(id: int, db: Session = Depends(get_db)):
    response = EventService.delete_by_id(id, db)
    return response

@event_router.get("/pdf/user/{user_id}",status_code=status.HTTP_200_OK)
async def get_events_pdf(user_id: int, db: Session = Depends(get_db)):
    response = EventService.get_report_events(user_id, db)
    pdf_buffer = BytesIO()
    pdf_buffer.write(response.output(dest='S'))
    pdf_buffer.seek(0)
    return StreamingResponse(response, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=events.pdf"})


