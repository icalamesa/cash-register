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

if __name__ == "__main__":
    unittest.main()