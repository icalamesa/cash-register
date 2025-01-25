from fastapi import FastAPI, HTTPException
from app.catalog import Catalog
from app.cart import Cart
from app.models import ProductInput
from app.pricing_engine import PricingEngine

def create_app() -> FastAPI:
    """
    Create and return a new FastAPI app with a fresh Cart.
    """
    app = FastAPI()
    catalog = Catalog()
    cart = Cart() 

    @app.post("/cart/add")
    def add_to_cart(product: ProductInput):
        if not product.item or not product.item.strip():
            raise HTTPException(status_code=400, detail="Product item cannot be empty")
        if product.quantity is None:
            raise HTTPException(status_code=400, detail="Product quantity cannot be empty")
        if product.quantity < 0:
            raise HTTPException(status_code=400, detail="Product quantity cannot be negative")

        if not catalog.get_product(product.item):
            raise HTTPException(status_code=400, detail="Product not found")

        try:
            cart.add_product(product.item, product.quantity)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        return {"message": f"Added {product.quantity} of {product.item} to the cart"}

    @app.get("/cart/list")
    def list_cart():
        return cart.list_items()

    @app.post("/cart/clear")
    def clear_cart():
        cart.clear()
        return {"message": "Cart cleared"}

    return app
