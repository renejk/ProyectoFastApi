from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.application.contracts.user_repository import UserRepository
from app.domain.model.user import User
from app.domain.schemas.user_schema import UserRequestModel, UserResponseModel


class UserCRUD(UserRepository):

       

    @staticmethod
    def create(user: UserRequestModel, db: Session) -> UserResponseModel:

        try:
            _user_find = db.query(User).filter(User.email == user.email).first()
            if _user_find:
                raise ValueError("Email already exists")
            _user = User(**user.model_dump())
            db.add(_user)
            db.commit()         

        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
                                , detail=str(e))
        
        return UserResponseModel(**_user.model_dump())
    
    @staticmethod
    def get_by_id(id: int, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def get_by_email(email: str, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def find_all(db: Session) -> list[UserResponseModel]:
        try:
            _users = db.query(User).all()
            return [UserResponseModel(**_user.model_dump()) for _user in _users]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def update(id: int, user: UserRequestModel, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def delete(id: int, db: Session) -> None:
        try:
            _user = db.query(User).filter(User.id == id).first()
            if not _user:
                raise ValueError("User not found")
            db.delete(_user)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))