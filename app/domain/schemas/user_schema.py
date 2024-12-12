from pydantic import BaseModel, EmailStr, ConfigDict


class UserRequestModel(BaseModel):
    name: str
    last_name: str
    role: str
    email: EmailStr
    phone: str
    status: str
    password: str

    @classmethod
    def validate_name(cls, name: str) -> str:
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters")
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        return name

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "name": "John",
            "last_name": "Doe",
            "role": "admin",
            "email": "john@example.com",
            "phone": "123456789",
            "status": "active",
            "password": "123456789"
        }
    })

class UserToUpdateModel(BaseModel):
    name: str|None = None
    last_name: str|None = None
    role: str|None = None
    email: EmailStr|None = None
    phone: str|None = None
    status: str | None = None
    password: str|None = None

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "name":None,
            "last_name": None,
            "role": None,
            "email": None,
            "phone": None,
            "status": None,
            "password": None
        }
    })


class UserResponseModel(BaseModel):
    id: int
    name: str
    last_name: str
    role: str
    email: EmailStr
    phone: str
    status: str
    created_at: str
    model_config = ConfigDict(from_attributes=True)