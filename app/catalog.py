class Catalog:
    """
    A simple catalog class to manage product details like codes, names, and prices.
    """
    def __init__(self):
        self.products = {
            "GR1": {"name": "Green Tea", "price": 3.11},
            "SR1": {"name": "Strawberries", "price": 5.00},
            "CF1": {"name": "Coffee", "price": 11.23},
        }

    def get_product(self, code):
        """
        Retrieve product details by code.
        :param code: Product code to look up.
        :return: Product details dictionary or None if not found.
        """
        return self.products.get(code)

