from sqlalchemy.orm import Session
from app.domain.schemas.user_schema import UserRequestModel, UserResponseModel
from app.infrastructure.persistence import UserCRUD


class UserService:

    user_repository = UserCRUD()

    @classmethod
    def create(self, user: UserRequestModel, db: Session) -> UserResponseModel:
        user_response = self.user_repository.create(user, db)
        return user_response