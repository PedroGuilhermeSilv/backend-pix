from fastapi import APIRouter, HTTPException

from src.externals.stripe.application.routers.dto.checkout import OutputSession
from src.externals.stripe.application.services.create_session import CreateCheckout
from src.externals.stripe.application.services.dto.session import ListItems
from src.externals.stripe.config import stripe

router = APIRouter()


@router.post("/session")
def create_session(request: ListItems)-> OutputSession:
    try:
        checkout = CreateCheckout(itens=request)
        session_id = checkout.create()
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return OutputSession(session_id=session_id)
    
@router.get("/session/{session_id}")
def get_session(session_id: str):
    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return session