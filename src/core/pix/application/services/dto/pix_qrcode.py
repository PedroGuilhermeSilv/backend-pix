from pydantic import BaseModel


class InputCreatePixQrCode(BaseModel):
    value: str
    key : str


class OutputCreatePixQrCode(BaseModel):
    image_url: str