# app/tests/test_cart_class.py
import unittest
from app.cart import Cart

class TestCartClass(unittest.TestCase):
    def setUp(self):
        """
        Create a fresh Cart instance before each test to ensure isolation.
        """
        self.cart = Cart()

    def test_add_valid_product(self):
        """
        Ensure adding a valid product with positive quantity updates the cart.
        """
        self.cart.add_product("GR1", 2)
        items = self.cart.list_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["item"], "GR1")
        self.assertEqual(items[0]["quantity"], 2)

    def test_add_multiple_different_products(self):
        """
        Ensure adding different valid products accumulates properly.
        """
        self.cart.add_product("GR1", 1)
        self.cart.add_product("SR1", 3)
        items = sorted(self.cart.list_items(), key=lambda x: x["item"])
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0], {"item": "GR1", "quantity": 1})
        self.assertEqual(items[1], {"item": "SR1", "quantity": 3})

    def test_add_same_product_multiple_times(self):
        """
        Ensure adding the same product multiple times increments the quantity.
        """
        self.cart.add_product("CF1", 1)
        self.cart.add_product("CF1", 2)
        items = self.cart.list_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], {"item": "CF1", "quantity": 3})

    def test_add_invalid_format_product_code(self):
        """
        Adding a product with an invalid code should raise ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.cart.add_product("INVALID", 1)
        self.assertIn("Invalid product code", str(context.exception))

    def test_add_empty_code(self):
        """
        Adding a product with an empty code should raise ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.cart.add_product("", 1)
        self.assertIn("Product code cannot be empty", str(context.exception))

    def test_add_zero_quantity(self):
        """
        Adding a product with zero quantity should raise ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.cart.add_product("GR1", 0)
        self.assertIn("Quantity must be positive", str(context.exception))

    def test_add_negative_quantity(self):
        """
        Adding a product with a negative quantity should raise ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.cart.add_product("GR1", -2)
        self.assertIn("Quantity must be positive", str(context.exception))

    def test_clear_cart(self):
        """
        Clearing the cart should remove all items.
        """
        self.cart.add_product("GR1", 2)
        self.cart.add_product("SR1", 3)
        self.cart.clear()
        items = self.cart.list_items()
        self.assertEqual(len(items), 0)

if __name__ == "__main__":
    unittest.main()
