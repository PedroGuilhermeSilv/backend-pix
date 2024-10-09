from fastapi import APIRouter, HTTPException

from src.core.security.application.services.auth_jwt import (
    JWTCreator,
)
from src.core.security.application.services.dto.jwt import (
    InputAuthUserDto,
    InputVerifyToken,
    OutputAuthUserDto,
    OutputVerifyToken,
)
from src.core.security.application.services.verify_jwt import VerifyJWT
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


@router.post("/verify")
async def verify_jwt(request: InputVerifyToken) -> OutputVerifyToken:
    try:
        service = VerifyJWT(repository=PonyORMUserRepository())
        response = await service.execute(request)
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return response
