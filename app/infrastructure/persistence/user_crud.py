from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.application.contracts.user_repository import UserRepository
from app.domain.model.user import User
from app.domain.schemas.user_schema import UserRequestModel, UserResponseModel, UserToUpdateModel


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
        try:
            _user = db.query(User).filter(User.id == id).first()
            if not _user:
                raise ValueError("User not found")
            return UserResponseModel(**_user.model_dump())
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def get_by_email(email: str, db: Session) -> UserResponseModel:
        try:
            _user = db.query(User).filter(User.email == email).first()
            if not _user:
                raise ValueError("User not found")
            return UserResponseModel(**_user.model_dump())
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def find_all(db: Session) -> list[UserResponseModel]:
        try:
            _users = db.query(User).all()
            return [UserResponseModel(**_user.model_dump()) for _user in _users]
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))

    @staticmethod
    def update(id: int, user: UserToUpdateModel, db: Session) -> UserResponseModel:
        try:
            _user = db.query(User).filter(User.id == id).first()
            if not _user:
                raise ValueError("User not found")
            _user.email = user.email if user.email else _user.email
            _user.name = user.name if user.name else _user.name
            _user.password = user.password if user.password else _user.password
            _user.last_name = user.last_name if user.last_name else _user.last_name
            _user.role = user.role if user.role else _user.role
            _user.phone = user.phone if user.phone else _user.phone
            _user.status = user.status if user.status else _user.status
            db.commit()
            return UserResponseModel(**_user.model_dump())
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                                , detail=str(e))
            

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