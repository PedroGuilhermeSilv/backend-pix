from pydantic import BaseModel


class OutputSession(BaseModel):
    session_id: str