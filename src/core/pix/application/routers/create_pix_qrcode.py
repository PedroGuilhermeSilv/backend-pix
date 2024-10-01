from fastapi import APIRouter

from src.core.pix.application.services.dto.pix_qrcode import (
    InputCreatePixQrCode,
    OutputCreatePixQrCode,
)
from src.core.pix.application.services.generate_pix_qrcode import CreatePixQrCodeService

router = APIRouter()


@router.post("/", response_model=OutputCreatePixQrCode)
def create(request: InputCreatePixQrCode):
    service = CreatePixQrCodeService()
    response = service.execute(request)

    return response