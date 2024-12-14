from pydantic import BaseModel, ConfigDict

class EventRequestModel(BaseModel):
    name: str
    attendees: int
    event_date: str
    duration: float
    user_id: int

    @classmethod
    def validate_name(cls, name: str) -> str:
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name
    
    @classmethod
    def validate_attendees(cls, user_id: int) -> int:
        if user_id < 1:
            raise ValueError("User id must be greater than 0")
        return user_id

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "name": "John",
            "attendees": 10,
            "duration": 10.0,
            "event_date": "2022-01-01T00:00:00",
            "user_id": 1
        }
    })


class EventToUpdateModel(BaseModel):
    name: str|None = None
    attendees: int|None = None
    event_date: str|None = None
    duration: float|None = None
    user_id: int|None = None    


    model_config = ConfigDict(json_schema_extra={
        "example": {
            "name": None,
            "attendees": None,
            "event_date": None,
            "duration": None,
            "user_id": None
        }
    })

class EventResponseModel(BaseModel):
    id: int
    name: str
    attendees: int
    event_date: str
    duration: float
    user_id: int
    model_config = ConfigDict(from_attributes=True)