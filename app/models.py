from pydantic import BaseModel

class ProductInput(BaseModel):
    item: str
    quantity: int
