from src.core.user.application.services.dto.user_dto import (
    InputServiceCreateUser,
    OutputCreateUser,
    OutputServiceCreateUser,
)
from src.core.user.domain.dto.user_dto import UserInput
from src.core.user.domain.entity import User
from src.core.user.domain.exceptions.user_exceptions import UserAlreadyExistError
from src.core.user.domain.repository.user_repository import UserRepository
from src.externals.stripe.application.services.create_customer import (
    CreateCustumer,
    Customer,
)


class CreateUser:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, input: InputServiceCreateUser) -> OutputServiceCreateUser:
        if user := await self.repository.get_by_email(input.email):
            raise UserAlreadyExistError

        try:
            user = User(email=input.email, password=input.password)
            user = await self.repository.save(UserInput(**user.model_dump()))
            username = user.email.split("@")[0]
            service_external = CreateCustumer(customer=Customer(name=username, email=user.email))
            service_external.create()
        except Exception as error:
            raise error
        return OutputCreateUser(email=user.email, id=user.id)
