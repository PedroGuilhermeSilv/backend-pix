from pydantic import BaseModel


class Item(BaseModel):
    price: str
    quantity: int

class ListItems(BaseModel):
    data: list[Item]

class StatusSession(BaseModel):
    payment_status: str