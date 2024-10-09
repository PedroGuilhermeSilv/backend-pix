from pydantic import BaseModel


class OutputAuthUserDto(BaseModel):
    token: str
    exp: int


class InputAuthUserDto(BaseModel):
    email: str
    password: str


class InputVerifyToken(BaseModel):
    token: str


class OutputVerifyToken(BaseModel):
    email: str
    exp: int
