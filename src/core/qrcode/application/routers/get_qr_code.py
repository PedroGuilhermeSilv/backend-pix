from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from src.core.qrcode.application.service.get_qr_code import GetQrCode

router = APIRouter()


@router.get("/{file_name}")
def read_item(file_name: str):
    service = GetQrCode(file_name=file_name)
    local_file_path = service.download_from_s3(file_name)

    try:
        file = open(local_file_path, mode="rb")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(
        file,
        media_type="image/png",
        headers={"Content-Disposition": f"attachment; filename={file_name}"},
    )
