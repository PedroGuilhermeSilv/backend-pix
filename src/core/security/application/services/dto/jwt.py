from pydantic import BaseModel


class OutputAuthUserDto(BaseModel):
    token: str
    exp: int


class InputAuthUserDto(BaseModel):
    email: str
    password: str
