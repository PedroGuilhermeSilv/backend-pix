from fastapi import APIRouter, HTTPException

from src.core.security.application.services.auth_jwt import (
    InputAuthUserDto,
    JWTCreator,
    OutputAuthUserDto,
)
from src.core.user.infra.ponyorm.repository.user_repository import PonyORMUserRepository

router = APIRouter()


@router.post("/")
async def auth_jwt(request: InputAuthUserDto) -> OutputAuthUserDto:
    try:
        service = JWTCreator(repository=PonyORMUserRepository())
        response = await service.execute(request)
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return response
    