from src.core.security.application.services.dto.jwt import (
    InputAuthUserDto,
    OutputAuthUserDto,
)
from src.core.user.domain.repository.user_repository import UserRepository
from src.core.utils.hash_jwt import create_jwt
from src.core.utils.exceptions.erros import InvalidPasswordError, UserNotFoundError
from src.core.utils.hash import verify_password


class JWTCreator:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, input: InputAuthUserDto) -> OutputAuthUserDto:
        user = await self.repository.get_by_email(input.email)
        if not user:
            raise UserNotFoundError

        try:
            if not verify_password(input.password, user.password):
                raise InvalidPasswordError
            payload = {"email": user.email}
            token = create_jwt(payload, expires_in=60)

        except Exception as error:
            raise error
        return OutputAuthUserDto(token=token, exp=60)
