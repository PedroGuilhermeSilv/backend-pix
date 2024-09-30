from fastapi import APIRouter, HTTPException

from src.core.user.application.services.create_user import (
    CreateUser,
    InputServiceCreateUser,
    OutputCreateUser,
)
from src.core.user.infra.ponyorm.repository.user_repository import PonyORMUserRepository

router = APIRouter()


@router.post("/")
async def create_user(request: InputServiceCreateUser) -> OutputCreateUser:
    try:
        service = CreateUser(repository=PonyORMUserRepository())
        response = await service.execute(request)
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return response
    