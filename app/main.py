from fastapi import FastAPI, HTTPException
from app.catalog import Catalog
from app.cart import Cart
from app.models import ProductInput
from app.pricing_engine import PricingEngine

def create_app() -> FastAPI:
    """
    Create and return a new FastAPI app with a fresh Cart.
    """
    app = FastAPI(
        title="Cart Management API",
        description=(
            "A simple API for managing a shopping cart, "
            "handling catalog items, and applying pricing rules dynamically. "
            "Supports adding products, listing cart contents with calculated prices, and clearing the cart."
        ),
        version="1.0.0",
    )
    catalog = Catalog()
    cart = Cart()

    @app.post(
        "/cart/add",
        summary="Add a product to the cart",
        description=(
            "Add a product to the cart by specifying the product code and quantity. "
            "The product code is validated against the catalog to ensure it exists, "
            "and the quantity must be a positive number."
        ),
        tags=["Cart"],
        response_description="Confirmation message indicating the product was successfully added.",
        responses={
            200: {"description": "Product added successfully."},
            400: {"description": "Invalid input or product not found in the catalog."},
        },
    )
    def add_to_cart(product: ProductInput):
        """
        Add a product to the cart.

        - **code**: The product code (e.g., "GR1").
        - **quantity**: The number of items to add.
        """
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

    @app.get(
        "/cart/list",
        summary="List all items in the cart with pricing details",
        description=(
            "Retrieve all products currently in the cart, along with their quantities, "
            "original prices, and discounted prices (if applicable). The catalog is queried for the "
            "latest product prices, and the pricing engine calculates the final discounted totals."
        ),
        tags=["Cart"],
        response_description="A list of items in the cart with their quantities, original prices, and discounted prices.",
    )
    def list_cart():
        """
        Get all items in the cart with pricing details.

        - Queries the catalog for the latest prices.
        - Calculates discounted totals using the pricing engine.
        - Returns a detailed breakdown of the cart contents.
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

    @app.post(
        "/cart/clear",
        summary="Clear the cart",
        description="Removes all products from the cart.",
        tags=["Cart"],
        response_description="Confirmation message indicating the cart has been cleared.",
    )
    def clear_cart():
        """
        Clear all items from the cart.
        """
        cart.clear()
        return {"message": "Cart cleared"}

    return app
