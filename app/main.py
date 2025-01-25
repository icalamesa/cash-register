from fastapi import FastAPI, HTTPException
from app.models import ProductInput

app = FastAPI()

@app.post("/cart/add")
def add_to_cart(product: ProductInput):
    """
    Add a product to the cart.
    Input: { "item": "GR1", "quantity": 1 }
    Output: { "message": "Added 1 of GR1 to the cart" }
    """
    if not product.item.strip():
        raise HTTPException(status_code=400, detail="Product item cannot be empty")
    return {"message": f"Added {product.quantity} of {product.item} to the cart"}