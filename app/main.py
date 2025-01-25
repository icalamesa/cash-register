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
        if not product.code or not product.code.strip():
            raise HTTPException(status_code=400, detail="Product code cannot be empty")
        if product.quantity is None:
            raise HTTPException(status_code=400, detail="Product quantity cannot be empty")
        if product.quantity < 0:
            raise HTTPException(status_code=400, detail="Product quantity cannot be negative")

        if not catalog.get_product(product.code):
            raise HTTPException(status_code=400, detail="Product not found")

        try:
            cart.add_product(product.code, product.quantity)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        return {"message": f"Added {product.quantity} of {product.code} to the cart"}

    @app.get("/cart/list")
    def list_cart():
        """
        Get all the products in the cart, query the catalog for the latest prices,
        and calculate the pricing details including original and discounted prices.
        """
        cart_items = cart.list_items()

        product_data = {}
        for item in cart_items:
            product = catalog.get_product(item["code"])
            product_data[item["code"]] = product["price"]

        result = PricingEngine.calculate_total(cart_items, product_data)

        expected_cart = [
            {
                "code": entry["code"],
                "quantity": entry["quantity"],
                "original_price": entry["original_price"],
                "discounted_price": entry["discounted_price"],
            }
            for entry in result["breakdown"]
        ]

        return expected_cart

    @app.post("/cart/clear")
    def clear_cart():
        cart.clear()
        return {"message": "Cart cleared"}

    return app
