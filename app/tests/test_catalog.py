import unittest
from app.catalog import Catalog

class TestCatalog(unittest.TestCase):
    def setUp(self):
        """
        Create a new instance of the Catalog class before each test.
        """
        self.catalog = Catalog()

    def test_get_existing_product(self):
        """
        Test retrieving an existing product by its code.
        """
        product = self.catalog.get_product("GR1")
        self.assertIsNotNone(product)
        self.assertEqual(product["name"], "Green Tea")
        self.assertEqual(product["price"], 3.11)

    def test_get_non_existing_product(self):
        """
        Test retrieving a non-existing product by its code.
        """
        product = self.catalog.get_product("INVALID")
        self.assertIsNone(product)

    def test_get_all_products(self):
        """
        Test retrieving the entire catalog with all product codes and prices.
        """
        all_products = self.catalog.get_all_products()

        self.assertIsInstance(all_products, dict)

        expected_catalog = {
            "GR1": {"name": "Green Tea", "price": 3.11},
            "SR1": {"name": "Strawberries", "price": 5.00},
            "CF1": {"name": "Coffee", "price": 11.23}
        }
        self.assertEqual(all_products, expected_catalog)

        self.assertIn("GR1", all_products)
        self.assertEqual(all_products["GR1"]["price"], 3.11)

        self.assertIn("SR1", all_products)
        self.assertEqual(all_products["SR1"]["price"], 5.00)

        self.assertIn("CF1", all_products)
        self.assertEqual(all_products["CF1"]["price"], 11.23)

if __name__ == "__main__":
    unittest.main()
