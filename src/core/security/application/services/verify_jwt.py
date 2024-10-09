from src.core.security.application.services.dto.jwt import (
    InputVerifyToken,
    OutputVerifyToken,
)
from src.core.security.utils.hash_jwt import decode_jwt
from src.core.user.domain.exceptions.user_exceptions import (
    UserNotFoundError,
)
from src.core.user.domain.repository.user_repository import UserRepository


class VerifyJWT:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, input: InputVerifyToken) -> OutputVerifyToken:

        try:
            user_decode = decode_jwt(input.token)
            user = await self.repository.get_by_email(user_decode["email"])
            if not user:
                raise UserNotFoundError

        except Exception as error:
            raise error
        return OutputVerifyToken(email=user_decode["email"], exp=user_decode["exp"])
