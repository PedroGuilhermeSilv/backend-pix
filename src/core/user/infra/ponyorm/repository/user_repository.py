from pony.orm import db_session, select

from src.core.user.domain.repository.user_repository import (
    UserInput,
    UserOutput,
    UserRepository,
)
from src.core.user.infra.ponyorm.models.user import User as PonyORMUser


class PonyORMUserRepository(UserRepository):
    def __init__(self):
        self.model_user = PonyORMUser

    async def save(self, user: UserInput) -> UserOutput:
        with db_session:
            user_ = self.model_user(
                id=user.id,
                email=user.email,
                password=user.password
            )

            return UserOutput(email=user_.email, id=user_.id, password=user_.password)


    async def get_by_email(self, email: str) -> UserOutput | None:
        with db_session:
            user_ = select(u for u in self.model_user if u.email == email).first()
            if user_:
                return UserOutput(email=user_.email, id=user_.id, password=user_.password)
            return None


    async def clear(self):
        with db_session:
            self.model_user.select().delete(bulk=True)
 