from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.pix.application.routers.create_pix_qrcode import router as pix_router
from src.core.qrcode.application.routers.get_qr_code import router as qrcode_router
from src.core.security.application.routers.auth import router as auth_router
from src.core.user.application.routers.create_user import router as user_router
from src.db.generate import *  # noqa
from src.externals.stripe.application.routers.checkout import router as checkout_router
from src.externals.stripe.application.routers.products import router as products_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")
app.include_router(pix_router, prefix="/pix")
app.include_router(auth_router, prefix="/auth")
app.include_router(products_router, prefix="/stripe")
app.include_router(checkout_router, prefix="/stripe")
app.include_router(qrcode_router, prefix="/qrcode")
