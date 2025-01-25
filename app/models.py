from pydantic import BaseModel

class ProductInput(BaseModel):
    code: str
    quantity: int

class CartResponse(BaseModel):
    message: str