from fastapi import APIRouter, status, Depends
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session
from app.domain.schemas.user_schema import UserRequestModel, UserResponseModel
from app.application.business.user_service import UserService


user_router = APIRouter(
    prefix="/users",
    tags=["userS"]
)


@user_router.post("", response_model= UserResponseModel,  status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequestModel, db: Session = Depends(get_db)):
    user_response = UserService.create(user, db)
    return user_response