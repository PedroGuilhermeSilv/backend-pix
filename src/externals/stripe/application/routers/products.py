from fastapi import APIRouter, HTTPException

from src.externals.stripe.application.routers.dto.products import ListProducts
from src.externals.stripe.config import stripe

router = APIRouter()


@router.get("/products", response_model=ListProducts)
def list_products() -> ListProducts:
    try:
        products = stripe.Product.list()
        prices = stripe.Price.list()
        
        product_list = []
        for product in products['data']:
            product_dict = product.to_dict()
            price = next((price for price in prices['data'] if price['id'] == product['default_price']), None)
            if price:
                product_dict['unit_amount'] = price['unit_amount']
            product_list.append(product_dict)
        
        return ListProducts(object=products['object'], url=products['url'], has_more=products['has_more'], data=product_list)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
@router.get("/products/{price_id}")
def get_price(price_id: str):
    try:
        price = stripe.Price.retrieve(price_id)
    except Exception as error:
        raise HTTPException(status_code=error.status_code, detail=error.msg)
    return price
    