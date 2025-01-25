from fastapi import FastAPI, HTTPException
from app.models import ProductInput
from app.catalog import Catalog


app = FastAPI()
catalog = Catalog()

@app.post("/cart/add")
def add_to_cart(product: ProductInput):
    """
    Add a product to the cart.
    Input: { "item": "GR1", "quantity": 1 }
    Output: { "message": "Added 1 of GR1 to the cart" }
    """
    if not product.item.strip() or product.item==None:
        raise HTTPException(status_code=400, detail="Product item cannot be empty")
    if not product.quantity or product.quantity==None:
        raise HTTPException(status_code=400, detail="Product quantity cannot be empty")
    if product.quantity < 0:
        raise HTTPException(status_code=400, detail="Product quantity cannot be negative")
    if not catalog.get_product(product.item):
        raise HTTPException(status_code=400, detail="Product not found")

    return {"message": f"Added {product.quantity} of {product.item} to the cart"}