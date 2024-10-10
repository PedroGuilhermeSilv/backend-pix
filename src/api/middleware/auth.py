from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.core.security.utils.hash_jwt import decode_jwt

security = HTTPBearer()


def validation_jwt(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> dict | None:
    return decode_jwt(credentials.credentials)
