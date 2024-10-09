from pydantic import BaseModel


class OutputSession(BaseModel):
    session_id: str

class OutputStatusPayment(BaseModel):
    payment_status: str