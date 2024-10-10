from fastapi import APIRouter, Depends, HTTPException

from src.api.middleware.auth import validation_jwt
from src.externals.stripe.application.routers.dto.checkout import (
    OutputSession,
    OutputStatusPayment,
)
from src.externals.stripe.application.services.create_session import CreateCheckout
from src.externals.stripe.application.services.dto.session import ListItems
from src.externals.stripe.application.services.get_session import GetCheckoutSession

router = APIRouter()


@router.post("/session")
def create_session(
    request: ListItems, token_data: dict = Depends(validation_jwt)
) -> OutputSession:
    try:
        checkout = CreateCheckout(itens=request, user=token_data.get("email"))
        session_id = checkout.create()
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return OutputSession(session_id=session_id)


@router.get("/session/{session_id}")
def get_session(session_id: str) -> OutputStatusPayment:
    try:
        service = GetCheckoutSession(session_id=session_id)
        status = service.execute()
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return OutputStatusPayment(payment_status=status.payment_status)
