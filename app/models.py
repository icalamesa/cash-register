from pydantic import BaseModel

class ProductInput(BaseModel):
    code: str
    quantity: int
