from io import BytesIO
from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session
from app.domain.schemas.user_schema import UserRequestModel, UserResponseModel, UserToUpdateModel
from app.application.business.user_service import UserService


user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@user_router.post("", response_model= UserResponseModel,  status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequestModel, db: Session = Depends(get_db)):
    user_response = UserService.create(user, db)
    return user_response

@user_router.get("/pdf",status_code=status.HTTP_200_OK)
async def get_users_pdf(db: Session = Depends(get_db)):
    response =  UserService.get_users_pdf(db)
    pdf_buffer = BytesIO()
    pdf_buffer.write(response.output(dest='S'))
    pdf_buffer.seek(0)
    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=users.pdf"})


@user_router.get("", response_model=list[UserResponseModel], status_code=status.HTTP_200_OK)
async def get_users(db: Session = Depends(get_db)):
    users = UserService.find_all(db)
    return users

@user_router.get("/{id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = UserService.get_by_id(id, db)
    return user

@user_router.get("/email/{email}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = UserService.get_by_email(email, db)
    return user

@user_router.put("/{id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
async def update_user(id: int, user: UserToUpdateModel, db: Session = Depends(get_db)):
    user_response = UserService.update(id, user, db)
    return user_response

@user_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(get_db)):
    response = UserService.delete_by_id(id, db)
    return response

