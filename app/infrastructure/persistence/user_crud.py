from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.application.contracts.user_repository import UserRepository
from app.domain.model.user import User
from app.domain.schemas.user_schema import UserRequestModel, UserResponseModel


class UserCRUD(UserRepository):

    @staticmethod
    def validate_email(email: str, db: Session) -> None:
        _user = db.query(User).filter(User.email == email).first()
        if _user:
            raise ValueError("Email already exists")
       

    @staticmethod
    def create(self, user: UserRequestModel, db: Session) -> UserResponseModel:

        try:
            self.validate_email(user.email, db)
            _user = User(**user.model_dump())
            db.add(_user)
            db.commit()         

        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
                                , detail=str(e))
        
        return UserResponseModel(**_user.model_dump())
    
    @staticmethod
    def get_by_id(self, id: int, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def get_by_email(self, email: str, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def find_all(self, db: Session) -> list[UserResponseModel]:
        pass

    @staticmethod
    def update(self, id: int, user: UserRequestModel, db: Session) -> UserResponseModel:
        pass

    @staticmethod
    def delete(self, id: int, db: Session) -> None:
        pass