class Cart:
    """
    A simple in-memory cart system.
    Stores items as a dictionary {product_code: quantity}.
    """

    def __init__(self):
        # Dictionary of product_code -> quantity
        self._items = {}

    def add_product(self, code: str, quantity: int):
        """
        Add a product with the given code and quantity to the cart.
        Raises ValueError if the code is invalid or the quantity is non-positive.
        """
        None

    def list_items(self):
        """
        Return a list of items in the cart. 
        Format: [ {"item": code, "quantity": quantity}, ... ]
        """
        None

    def clear(self):
        """
        Empty the cart.
        """
        None
