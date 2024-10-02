from fastapi import APIRouter, HTTPException

from src.externals.stripe.application.routers.dto.checkout import OutputSession
from src.externals.stripe.application.services.create_session import CreateCheckout
from src.externals.stripe.application.services.dto.session import ListItems


router = APIRouter()


@router.post("/session")
def create_session(request: ListItems)-> OutputSession:
    try:
        checkout = CreateCheckout(itens=request)
        session_id = checkout.create()
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return OutputSession(session_id=session_id)
    