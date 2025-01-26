from pydantic import BaseModel
from typing import List


class ProductInput(BaseModel):
    code: str
    quantity: int

class CatalogItem(BaseModel):
    code: str
    name: str
    price: float

class CartItem(BaseModel):
    """
    Represents a single item in the cart with pricing details.
    """
    item: str
    quantity: int
    original_price: float
    discounted_price: float

class ListCatalogResponse(BaseModel):
    """
    Represents the response for the `/catalog/list` endpoint.
    """
    items: List[CatalogItem]

class ListCartResponse(BaseModel):
    """
    Represents the response for the `/cart/list` endpoint.
    """
    items: List[CartItem]

class CartResponse(BaseModel):
    """
    Generic response model for actions like adding or clearing the cart.
    """
    message: str
