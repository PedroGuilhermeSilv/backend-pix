from fastapi import APIRouter, HTTPException

from src.externals.stripe.application.routers.dto.list_products import ListProducts
from src.externals.stripe.config import stripe

router = APIRouter()


@router.get("/products")
def list_products() -> ListProducts:
    try:
        products = stripe.Product.list()
        products = ListProducts(**products)
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return products
    