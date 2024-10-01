
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.pix.application.routers.create_pix_qrcode import router as pix_router
from src.core.user.application.routers.create_user import router as user_router
from src.core.security.application.routers.auth import router as auth_router
from src.db.generate import *  # noqa

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





