class Cart:
    """
    A simple in-memory cart system.
    Stores items as a dictionary {product_code: quantity}.
    """

    def __init__(self):
        self._items = {}

    def add_product(self, code: str, quantity: int):
        """
        Add a product with the given code and quantity to the cart.
        Raises ValueError if the code is invalid or the quantity is non-positive.
        """
        if not code.strip():
            raise ValueError("Product code cannot be empty")
        if code.isnumeric() or len(code) != 3:
            raise ValueError("Invalid product code")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        current_qty = self._items.get(code, 0)
        self._items[code] = current_qty + quantity

    def list_items(self):
        """
        Return a list of items in the cart.
        Format: [ {"item": code, "quantity": quantity}, ... ]
        """
        return [
            {"code": code, "quantity": qty} for code, qty in self._items.items()
        ]

    def clear(self):
        """
        Empty the cart.
        """
        self._items.clear()
