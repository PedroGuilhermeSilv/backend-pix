from pydantic import BaseModel


class InputServiceCreateUserStripe(BaseModel):
    name: str
    email: str

class OutputServiceCreateUserStripe(BaseModel):
    name: str
    email: str
    id: str