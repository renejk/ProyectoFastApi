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