from typing import Dict, Optional

from pydantic import BaseModel


class Product(BaseModel):
    id: str
    object: str
    active: bool
    created: int
    default_price: Optional[str]
    description: Optional[str]
    images: list[str]
    marketing_features: list[str]
    livemode: bool
    metadata: Dict
    name: str
    package_dimensions: Optional[Dict]
    shippable: Optional[str]
    statement_descriptor: Optional[str]
    tax_code: Optional[str]
    unit_label: Optional[str]
    updated: int
    url: Optional[str]

class ListProducts(BaseModel):
    object: str
    url: str
    has_more: bool
    data: list[Product]